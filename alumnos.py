#!/usr/bin/env python
# -*- coding: utf-8 -*-


###########################################################################
## Modulo para Manejo General del Sistema (CONTROLADOR)
## Ultima Revisión: 19-11-2012 11:05 a.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 07 de Noviembre de 2012
#
# +-------------------------------------------------+#
###########################################################################


import wx
import wx.lib.dialogs
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
from wx.lib.wordwrap import wordwrap
import wx.lib.masked as masked
from SimpleCV import Camera

if wx.Platform == '__WXMSW__':
    from wx.lib.pdfwin import PDFWindow
    import win32api

import traceback
import sys
import os
import hashlib
import sqlite3 as lite

from modelo import ModeloBD
from report import Reportes
from alumnos_vista import (WizardConfigInicial, FrameLogin, FramePrincipal,
                           FrameRecuerdaPass, PanelBienvenida,
                           PanelCargaAlumno, PanelEditAlumno, FrameBusqueda,
                           FrameBusquedaReportes,
                           FrameFichasAlumno, FrameReporteGeneral,FrameReporteProf)
from alumnos_vista import (ID_CARGAR_ALUMNOS,
                           ID_EDITAR_ALUMNOS)

from datetime import datetime, date
import time
import string

import xlwt
import xlrd
import wx.lib.agw.xlsgrid as XG
import tempfile
import logging

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

bitmapDir = os.path.relpath(os.path.join(dirName, 'bitmaps'))
iconDir = os.path.relpath(os.path.join(dirName, 'icon'))
licenceDir = os.path.relpath(os.path.join(dirName, 'license'))
tempDir = os.path.relpath(os.path.join(dirName, 'temp'))
profilePicDir = os.path.relpath(os.path.join(dirName, 'fotosAlumnos'))
sys.path.append(os.path.split(dirName)[0])
padding = 5

fotoVacia = os.path.relpath(os.path.join(bitmapDir, 'fondo_FotoALumno.jpg'))

#######################
######DEFINICION DE CLASES
#######################


class DatePickerCtrl(wx.DatePickerCtrl):
    """
    Hace un Override de la Superclase para Cambiar
    el color de fondo del control
    """
    def __init__(self, *args, **kw):
        wx.DatePickerCtrl.__init__(self, *args, **kw)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()


class Choice(wx.Choice):
    """
    Hace un Override de la Superclase para Cambiar
    el color de fondo del control
    """
    def __init__(self, *args, **kw):
        wx.Choice.__init__(self, *args, **kw)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()


class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    """
    Mixin de ListCtrl para presentar un Checkbox en cada fila
    """
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, size=(-1, 165), style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)

        CheckListCtrlMixin.__init__(self)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)

    def OnItemActivated(self, evt):
        self.ToggleItem(evt.m_itemIndex)


class NotEmptyValidator(wx.PyValidator):
    """
    Clase para definir un validador de entrada en los TextCtrl y Choices    """

    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        """
        Note that every validator must implement the Clone() method.
        """
        return NotEmptyValidator()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        tipo = repr(type(textCtrl))
        if tipo == "<class 'wx._controls.TextCtrl'>":  # Si el Control es un TextCtrl
            text = textCtrl.GetValue()
            if len(text) == 0 or text == '(    )    -    ' or text == '        ':
                textCtrl.SetBackgroundColour("red")
                textCtrl.SetFocus()
                textCtrl.Refresh()
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        elif tipo == "<class 'wx._controls.Choice'>":  # Si el Control es un Choice
            text = textCtrl.GetCurrentSelection()
            if text == 0.:
                textCtrl.SetBackgroundColour("red")
                textCtrl.SetFocus()
                textCtrl.Refresh()
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        elif tipo == "<class 'wx._controls.DatePickerCtrl'>":  # Si el Control es un DatePickerCtrl
            text = textCtrl.GetValue()
            hoy = wx.DateTime.Today()
            if text > hoy:
                textCtrl.SetBackgroundColour("red")
                textCtrl.SetFocus()
                textCtrl.Refresh()
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        elif tipo == "<class 'wx.lib.masked.textctrl.TextCtrl'>":  # Si el Control es un Masked TextCtrl
            text = textCtrl.GetValue()
            if text == '        ':
                textCtrl.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
                textCtrl.SetBackgroundColour("red")
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True


    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

class WizardInicio(WizardConfigInicial):
    """
    Clase para presentar el Wizard de Confifuracion inicial
    """

    def choiceEntFedOnChoice( self, event ):
        self.choiceMunicipio.Clear()

        if self.choiceEntFed.GetSelection() == 1:
            #capital
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Libertador (Caracas)")


        if self.choiceEntFed.GetSelection() == 2:
            #amazonas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Alto Orinoco (La Esmeralda)")
            self.choiceMunicipio.Append("Atabapo (San Fernando de Atabapo)")
            self.choiceMunicipio.Append("Atures (Puerto Ayacucho)")
            self.choiceMunicipio.Append(u"Autana (Isla Ratón)")
            self.choiceMunicipio.Append("Manapiare (San Juan de Manapiare)")
            self.choiceMunicipio.Append("Maroa (Maroa)")
            self.choiceMunicipio.Append(u"Río Negro (San Carlos de Río Negro)")


        if self.choiceEntFed.GetSelection() == 3:
            #anzoategui
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Anaco (Anaco)")
            self.choiceMunicipio.Append("Aragua (Aragua de Barcelona)")
            self.choiceMunicipio.Append(u"Bolívar (Barcelona)")
            self.choiceMunicipio.Append("Bruzual (Clarines)")
            self.choiceMunicipio.Append("Cajigal (Onoto)")
            self.choiceMunicipio.Append("Carvajal (Valle de Guanape)")
            self.choiceMunicipio.Append(u"Diego Bautista Urbaneja (Lechería)")
            self.choiceMunicipio.Append("Freites (Cantaura)")
            self.choiceMunicipio.Append(u"Guanipa (San José de Guanipa)")
            self.choiceMunicipio.Append("Guanta (Guanta)")
            self.choiceMunicipio.Append("Independencia (Soledad)")
            self.choiceMunicipio.Append("Libertad (San Mateo)")
            self.choiceMunicipio.Append("McGregor (El Chaparro)")
            self.choiceMunicipio.Append(u"Miranda (Pariaguán)")
            self.choiceMunicipio.Append("Monagas (San Diego de Cabrutica)")
            self.choiceMunicipio.Append(u"Peñalver (Puerto Píritu)")
            self.choiceMunicipio.Append(u"Píritu (Píritu)")
            self.choiceMunicipio.Append("San Juan de Capistrano (Boca de Uchire)")
            self.choiceMunicipio.Append("Santa Ana (Santa Ana)")
            self.choiceMunicipio.Append(u"Simón Rodriguez (El Tigre)")
            self.choiceMunicipio.Append("Sotillo (Puerto La Cruz)")


        if self.choiceEntFed.GetSelection() == 4:
            #apure
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Achaguas (Achaguas)" )
            self.choiceMunicipio.Append("Biruaca (Biruaca)")
            self.choiceMunicipio.Append(u"Muñoz (Bruzual)")
            self.choiceMunicipio.Append(u"Páez (Guasdualito)")
            self.choiceMunicipio.Append("Pedro Camejo (San Juan de Payara)")
            self.choiceMunicipio.Append(u"Rómulo Gallegos (Elorza)")
            self.choiceMunicipio.Append("San Fernando (San Fernando de Apure)")



        if self.choiceEntFed.GetSelection() == 5:
            #aragua
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Bolívar (San Mateo)")
            self.choiceMunicipio.Append("Camatagua (Camatagua)")
            self.choiceMunicipio.Append(u"Francisco Linares Alcántara (Santa Rita)")
            self.choiceMunicipio.Append("Girardot (Maracay)")
            self.choiceMunicipio.Append(u"José Angel Lamas (Santa Cruz de Aragua)")
            self.choiceMunicipio.Append(u"José Félix Ribas (La Victoria)")
            self.choiceMunicipio.Append(u"José Rafael Revenga (El Consejo)")
            self.choiceMunicipio.Append("Libertador (Palo Negro)")
            self.choiceMunicipio.Append(u"Mario Briceño Iragorry (El Limón)")
            self.choiceMunicipio.Append("San Casimiro (San Casimiro)")
            self.choiceMunicipio.Append(u"San Sebastián (San Sebastián de Los Reyes (Venezuela))")
            self.choiceMunicipio.Append(u"Santiago Mariño (Turmero)")
            self.choiceMunicipio.Append(u"Santos Michelena (Las Tejerías)")
            self.choiceMunicipio.Append("Sucre (Cagua)")
            self.choiceMunicipio.Append("Tovar (Colonia Tovar)")
            self.choiceMunicipio.Append("Urdaneta (Barbacoas)")
            self.choiceMunicipio.Append("Zamora (Villa de Cura)")


        if self.choiceEntFed.GetSelection() == 6:
            #barinas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Alberto Arvelo Torrealba (Sabaneta)")
            self.choiceMunicipio.Append(u"Andrés Eloy Blanco (El Cantón)")
            self.choiceMunicipio.Append(u"Antonio José de Sucre (Socopó)")
            self.choiceMunicipio.Append("Arismendi (Arismendi)")
            self.choiceMunicipio.Append("Barinas (Barinas)")
            self.choiceMunicipio.Append("Bolívar (Barinitas)")
            self.choiceMunicipio.Append("Cruz Paredes (Barrancas)")
            self.choiceMunicipio.Append(u"Ezequiel Zamora (Santa Bárbara)")
            self.choiceMunicipio.Append("Obispos (Obispos)")
            self.choiceMunicipio.Append("Pedraza (Ciudad Bolivia)")
            self.choiceMunicipio.Append("Rojas (Libertad)")
            self.choiceMunicipio.Append("Sosa (Ciudad de Nutrias)")


        if self.choiceEntFed.GetSelection() == 7:
            #bolivar
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Caroní (Ciudad Guayana)" )
            self.choiceMunicipio.Append(u"Cedeño (Caicara del Orinoco)")
            self.choiceMunicipio.Append("El Callao (El Callao)" )
            self.choiceMunicipio.Append(u"Gran Sabana (Santa Elena de Uairén)")
            self.choiceMunicipio.Append(u"Heres (Ciudad Bolívar))" )
            self.choiceMunicipio.Append("Piar (Upata)")
            self.choiceMunicipio.Append(u"Raúl Leoni (Ciudad Piar)" )
            self.choiceMunicipio.Append("Roscio (Guasipati)")
            self.choiceMunicipio.Append("Sifontes (El Dorado)" )
            self.choiceMunicipio.Append("Sucre (Maripa)")
            self.choiceMunicipio.Append("Padre Pedro Chien (El Palmar)" )


        if self.choiceEntFed.GetSelection() == 8:
            #carabobo
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Bejuma (Bejuma)")
            self.choiceMunicipio.Append("Carlos Arvelo (G\u00FCig\u00FCe)")
            self.choiceMunicipio.Append("Diego Ibarra (Mariara)")
            self.choiceMunicipio.Append("Guacara (Guacara)")
            self.choiceMunicipio.Append(u"Juan José Mora (Morón)")
            self.choiceMunicipio.Append("Libertador (Tocuyito)")
            self.choiceMunicipio.Append("Los Guayos (Los Guayos)")
            self.choiceMunicipio.Append("Miranda (miranda)")
            self.choiceMunicipio.Append(u"Montalbán (Montalbán)")
            self.choiceMunicipio.Append("Naguanagua (Naguanagua)")
            self.choiceMunicipio.Append("Puerto Cabello (Puerto Cabello)")
            self.choiceMunicipio.Append("San Diego")
            self.choiceMunicipio.Append(u"San Joaquín (San Joaquín)")
            self.choiceMunicipio.Append("Valencia (Valencia)")


        if self.choiceEntFed.GetSelection() == 9:
            #cojedes
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Anzoátegui (cojedes)")
            self.choiceMunicipio.Append(u"Falcón (Tinaquillo)" )
            self.choiceMunicipio.Append("Girardot (El Baúl)")
            self.choiceMunicipio.Append("Lima Blanco (Macapo)")
            self.choiceMunicipio.Append("Pao de San Juan Bautista (El Pao)")
            self.choiceMunicipio.Append("Ricaurte (Libertad)")
            self.choiceMunicipio.Append(u"Rómulo Gallegos (Las Vegas)")
            self.choiceMunicipio.Append("San Carlos (San Carlos)")
            self.choiceMunicipio.Append("Tinaco (Tinaco)")


        if self.choiceEntFed.GetSelection() == 10:
            #delta
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Antonio Díaz (Curiapo)" )
            self.choiceMunicipio.Append("Casacoima (Sierra Imataca)")
            self.choiceMunicipio.Append("Pedernales (Pedernales)")
            self.choiceMunicipio.Append("Tucupita (Tucupita)")


        if self.choiceEntFed.GetSelection() == 11:
            #falcon
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Acosta (San Juan de los Cayos)")
            self.choiceMunicipio.Append(u"Bolívar (San Luis)")
            self.choiceMunicipio.Append("Buchivacoa (Capatárida)")
            self.choiceMunicipio.Append("Cacique Manaure (Yaracal)")
            self.choiceMunicipio.Append("Carirubana (Punto Fijo)")
            self.choiceMunicipio.Append("Colina (La Vela de Coro)")
            self.choiceMunicipio.Append("Dabajuro (Dabajuro)")
            self.choiceMunicipio.Append("Democracia (Pedregal)")
            self.choiceMunicipio.Append(u"Falcón (Pueblo Nuevo)")
            self.choiceMunicipio.Append("Federación (Churuguara)")
            self.choiceMunicipio.Append("Jacura (Jacura)")
            self.choiceMunicipio.Append("Los Taques (Santa Cruz de Los Taques)")
            self.choiceMunicipio.Append("Mauroa (Mene de Mauroa)")
            self.choiceMunicipio.Append("Miranda (Santa Ana de Coro)")
            self.choiceMunicipio.Append("Monseñor Iturriza (Chichiriviche)")
            self.choiceMunicipio.Append("Palmasola (Palmasola)")
            self.choiceMunicipio.Append("Petit (Cabure)")
            self.choiceMunicipio.Append(u"Píritu (Píritu)")
            self.choiceMunicipio.Append("San Francisco (Mirimire)")
            self.choiceMunicipio.Append("Silva (Tucacas)")
            self.choiceMunicipio.Append("Sucre (La Cruz de Taratara)")
            self.choiceMunicipio.Append("Tocópero (Tocópero)")
            self.choiceMunicipio.Append(u"Unión (Santa Cruz de Bucaral)")
            self.choiceMunicipio.Append("Urumaco (Urumaco)")


        if self.choiceEntFed.GetSelection() == 12:
            #guarico
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Camaguán (Camaguán).")
            self.choiceMunicipio.Append("Chaguaramas (Chaguaramas)" )
            self.choiceMunicipio.Append("El Socorro (El Socorro)" )
            self.choiceMunicipio.Append("Sebastian Francisco de Miranda (Calabozo)" )
            self.choiceMunicipio.Append(u"José Félix Ribas (Tucupido)" )
            self.choiceMunicipio.Append(u"José Tadeo Monagas (Altagracia de Orituco)" )
            self.choiceMunicipio.Append(u"Juan Germán Roscio (San Juan de Los Morros)" )
            self.choiceMunicipio.Append(u"Julián Mellado (El Sombrero)" )
            self.choiceMunicipio.Append("Las Mercedes (Las Mercedes)" )
            self.choiceMunicipio.Append("Leonardo Infante (Valle de La Pascua)" )
            self.choiceMunicipio.Append("Pedro Zaraza (Zaraza)" )
            self.choiceMunicipio.Append("Ortiz (Ortiz)" )
            self.choiceMunicipio.Append("San Gerónimo de Guayabal (Guayabal)" )
            self.choiceMunicipio.Append(u"San José de Guaribe (San José de Guaribe)" )
            self.choiceMunicipio.Append("Santa María de Ipire (Santa María de Ipire)" )


        if self.choiceEntFed.GetSelection() == 13:
            #lara
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Eloy Blanco (Sanare)" )
            self.choiceMunicipio.Append("Crespo (Duaca)")
            self.choiceMunicipio.Append("Iribarren (Barquisimeto)")
            self.choiceMunicipio.Append(u"Jiménez (Quibor)")
            self.choiceMunicipio.Append(u"Morán (El Tocuyo)")
            self.choiceMunicipio.Append("Palavecino (Cabudare)")
            self.choiceMunicipio.Append(u"Simón Planas (Sarare)")
            self.choiceMunicipio.Append("Torres (Carora)")


        if self.choiceEntFed.GetSelection() == 14:
            #merida
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Alberto Adriani (El Vigía)")
            self.choiceMunicipio.Append(u"Andrés Bello (La Azulita)")
            self.choiceMunicipio.Append("Antonio Pinto Salinas (Santa Cruz de Mora)")
            self.choiceMunicipio.Append("Aricagua (Aricagua)")
            self.choiceMunicipio.Append(u"Arzobispo Chacón (Canaguá)")
            self.choiceMunicipio.Append(u"Campo Elías (Ejido)")
            self.choiceMunicipio.Append("Caracciolo Parra Olmedo (Tucaní)")
            self.choiceMunicipio.Append("Cardenal Quintero (Santo Domingo)")
            self.choiceMunicipio.Append("Guaraque (Guaraque)")
            self.choiceMunicipio.Append(u"Julio César Salas (Arapuey)")
            self.choiceMunicipio.Append("Justo Briceño (Torondoy)")
            self.choiceMunicipio.Append("Libertador (Mérida)")
            self.choiceMunicipio.Append("Miranda (Timotes)")
            self.choiceMunicipio.Append("Obispo Ramos de Lora (Santa Elena de Arenales)")
            self.choiceMunicipio.Append("Padre Noguera (Santa María de Caparo)")
            self.choiceMunicipio.Append("Pueblo Llano (Pueblo Llano)")
            self.choiceMunicipio.Append("Rangel (Mucuchíes)")
            self.choiceMunicipio.Append("Rivas Dávila (Bailadores)")
            self.choiceMunicipio.Append("Santos Marquina (Tabay)")
            self.choiceMunicipio.Append("Sucre (Lagunillas)")
            self.choiceMunicipio.Append("Tovar (To)")
            self.choiceMunicipio.Append("Tulio Febres Cordero (Nueva bolivarvia)")
            self.choiceMunicipio.Append("Zea (Zea)")


        if self.choiceEntFed.GetSelection() == 15:
            #miranda
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Acevedo (Caucagua)" )
            self.choiceMunicipio.Append(u"Andrés Bello (San José de Barlovento)")
            self.choiceMunicipio.Append("Baruta (Baruta)")
            self.choiceMunicipio.Append(u"Brión (Higuerote)")
            self.choiceMunicipio.Append("Buroz (Mamporal)")
            self.choiceMunicipio.Append("Carrizal (Carrizal)")
            self.choiceMunicipio.Append("Chacao (Chacao)")
            self.choiceMunicipio.Append(u"Cristóbal Rojas (Charallave)")
            self.choiceMunicipio.Append("El Hatillo (Santa Rosalía de Palermo)")
            self.choiceMunicipio.Append("Guaicaipuro (Los Teques)")
            self.choiceMunicipio.Append("Independencia (Santa Teresa del Tuy)")
            self.choiceMunicipio.Append("Lander (Ocumare del Tuy)")
            self.choiceMunicipio.Append("Los Salias (San Antonio de los Altos)a")
            self.choiceMunicipio.Append(u"Páez (Río Chico)")
            self.choiceMunicipio.Append(u"Páez Castillo (Santa Lucía)")
            self.choiceMunicipio.Append(u"Pedro Gual (Cúpira)")
            self.choiceMunicipio.Append("Plaza (Guarenas)")
            self.choiceMunicipio.Append(u"Simón Bolívar (San Francisco de Yare)")
            self.choiceMunicipio.Append("Sucre (Petare)")
            self.choiceMunicipio.Append(u"Urdaneta (Cúa)")
            self.choiceMunicipio.Append("Zamora (Guatire)")


        if self.choiceEntFed.GetSelection() == 16:
            #monagas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Acosta (San Antonio de Capayacuar)" )
            self.choiceMunicipio.Append("Aguasay (Aguasay)")
            self.choiceMunicipio.Append(u"Bolívar (Caripito)")
            self.choiceMunicipio.Append("Caripe (Caripe)")
            self.choiceMunicipio.Append("Cedeño (Caicara)")
            self.choiceMunicipio.Append("Ezequiel Zamora (Punta de Mata)")
            self.choiceMunicipio.Append("Libertador (Temblador)")
            self.choiceMunicipio.Append(u"Maturín (Maturín)")
            self.choiceMunicipio.Append(u"Piar (aragua de Maturín)")
            self.choiceMunicipio.Append("Punceres (Quiriquire)")
            self.choiceMunicipio.Append(u"Santa Bárbara (Santa Bárbara)")
            self.choiceMunicipio.Append("Sotillo (Barrancas del Orinco)")
            self.choiceMunicipio.Append("Uracoa (Uracoa)")


        if self.choiceEntFed.GetSelection() == 17:
            #nuevaEsparta
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Antolín del Campo (La Plaza de Paraguachí)")
            self.choiceMunicipio.Append("Arismendi (La Asunción)")
            self.choiceMunicipio.Append(u"Díaz (San Juan Bautista)")
            self.choiceMunicipio.Append(u"García (El Valle del Espíritu Santo)")
            self.choiceMunicipio.Append(u"Gómez (Santa Ana)")
            self.choiceMunicipio.Append("Maneiro (Pampatar)")
            self.choiceMunicipio.Append("Marcano (Juan Griego)")
            self.choiceMunicipio.Append(u"Mariño (Porlamar)")
            self.choiceMunicipio.Append(u"Península de Macanao (Boca de Río)")
            self.choiceMunicipio.Append("Tubores (Punta de Piedras)")
            self.choiceMunicipio.Append("Villalba (San Pedro de Coche)")


        if self.choiceEntFed.GetSelection() == 18:
            #portuguesa
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Agua Blanca (Agua Blanca)" )
            self.choiceMunicipio.Append("Araure (Araure)")
            self.choiceMunicipio.Append(u"Esteller (Píritu)")
            self.choiceMunicipio.Append("Guanare (Guanare)")
            self.choiceMunicipio.Append("Guanarito (Guanarito)")
            self.choiceMunicipio.Append(u"Monseñor José Vicente de Unda (Chabasquén de Unda)")
            self.choiceMunicipio.Append("Ospino (Ospino)")
            self.choiceMunicipio.Append(u"Páez (Acarigua)")
            self.choiceMunicipio.Append(u"Papelón (Papelón)")
            self.choiceMunicipio.Append(u"San Genaro de Boconoíto (Boconoíto)")
            self.choiceMunicipio.Append("San Rafael de Onoto (San Rafael de Onoto)")
            self.choiceMunicipio.Append(u"Santa Rosalía (El Playón)")
            self.choiceMunicipio.Append("Sucre (Biscucuy)")
            self.choiceMunicipio.Append(u"Turén (Villa Bruzual)")


        if self.choiceEntFed.GetSelection() == 19:
            #sucre
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Eloy Blanco (Casanay)" )
            self.choiceMunicipio.Append(u"Andrés Mata (San José de Aerocuar)")
            self.choiceMunicipio.Append("Arismendi (Río Caribe)")
            self.choiceMunicipio.Append(u"Benítez (El Pilar)")
            self.choiceMunicipio.Append(u"Bermúdez (Carúpano)")
            self.choiceMunicipio.Append(u"Bolívar (Marigï¿½itar)")
            self.choiceMunicipio.Append("Cajigal (Yaguaraparo)")
            self.choiceMunicipio.Append(u"Cruz Salmerón Acosta (Araya)")
            self.choiceMunicipio.Append("Libertador (Tunapuy)")
            self.choiceMunicipio.Append(u"Mariño (Irapa)")
            self.choiceMunicipio.Append(u"Mejía (San Antonio del Golfo)")
            self.choiceMunicipio.Append("Montes (Cumanacoa)")
            self.choiceMunicipio.Append("Ribero (Cariaco)")
            self.choiceMunicipio.Append(u"Sucre (Cumaná)")
            self.choiceMunicipio.Append(u"Valdez (Güiria)")


        if self.choiceEntFed.GetSelection() == 20:
            #tachira
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Bello (Cordero)" )
            self.choiceMunicipio.Append(u"Antonio Rómulo Costa (Las Mesas)")
            self.choiceMunicipio.Append(u"Ayacucho (Colón)")
            self.choiceMunicipio.Append(u"Bolívar (San Antonio del Táchira)")
            self.choiceMunicipio.Append(u"Cárdenas (Táriba)")
            self.choiceMunicipio.Append(u"Córdoba (Santa Ana de Táchira)")
            self.choiceMunicipio.Append(u"Fernández Feo (San Rafael del Piñal)")
            self.choiceMunicipio.Append(u"Francisco de Miranda (San José de Bolívar)")
            self.choiceMunicipio.Append(u"García de Hevia (La Fru00eda)")
            self.choiceMunicipio.Append(u"Guásimos (Palmira)")
            self.choiceMunicipio.Append("Independencia (Capacho Nuevo)")
            self.choiceMunicipio.Append(u"Jáuregui (La Grita)")
            self.choiceMunicipio.Append(u"José María gas (El Cobre)")
            self.choiceMunicipio.Append(u"Junín (Rubio)")
            self.choiceMunicipio.Append("Libertad (Capacho Viejo)")
            self.choiceMunicipio.Append("Libertador (Abejales)")
            self.choiceMunicipio.Append("Lobatera (Lobatera)")
            self.choiceMunicipio.Append("Michelena (Michelena)")
            self.choiceMunicipio.Append("Panamericano (Coloncito)")
            self.choiceMunicipio.Append(u"Pedro María Ureña (Ureña)")
            self.choiceMunicipio.Append("Rafael Urdaneta (Delicias)")
            self.choiceMunicipio.Append("Samuel Daru00edo Maldonado (La Tendida)")
            self.choiceMunicipio.Append(u"San Cristóbal (San Cristóbal)")
            self.choiceMunicipio.Append("Seboruco (Seboruco)")
            self.choiceMunicipio.Append(u"Simón Rodríguez (San Simón)")
            self.choiceMunicipio.Append("Sucre (Queniquea)")
            self.choiceMunicipio.Append("Torbes (San Josecito)")
            self.choiceMunicipio.Append("Uribante (Pregonero)")
            self.choiceMunicipio.Append("San Judas Tadeo (Umuquena)")


        if self.choiceEntFed.GetSelection() == 21:
            #trujillo
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Bello (Santa Isabel)" )
            self.choiceMunicipio.Append(u"Boconó (Boconó)")
            self.choiceMunicipio.Append(u"Bolívar (Sabana Grande)")
            self.choiceMunicipio.Append(u"Candelaria (Chejendé)")
            self.choiceMunicipio.Append("Carache (Carache)")
            self.choiceMunicipio.Append("Escuque (Escuque)")
            self.choiceMunicipio.Append(u"José Felipe Márquez Cañizalez (El Paradero)")
            self.choiceMunicipio.Append(u"Juan Vicente Campos Elías (Campo Elu00edas)")
            self.choiceMunicipio.Append("La Ceiba (Santa Apolonia)")
            self.choiceMunicipio.Append("Miranda (El Dividive)")
            self.choiceMunicipio.Append("Monte Carmelo (Monte Carmelo)")
            self.choiceMunicipio.Append(u"Motatán (Motatán)")
            self.choiceMunicipio.Append(u"Pampán (Pampán)")
            self.choiceMunicipio.Append("Pampanito (Pampanito)")
            self.choiceMunicipio.Append("Rafael Rangel (Betijoque)")
            self.choiceMunicipio.Append("San Rafael de Carvajal (Carvajal)")
            self.choiceMunicipio.Append("Sucre (Sabana de Mendoza)")
            self.choiceMunicipio.Append("Trujillo (Trujillo)")
            self.choiceMunicipio.Append("Urdaneta (La Quebrada)")
            self.choiceMunicipio.Append("Valera (Valera)")


        if self.choiceEntFed.GetSelection() == 22:
            #vargas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Vargas (La Guaira)" )


        if self.choiceEntFed.GetSelection() == 23:
            #yaracuy
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Arístides Bastidas (San Pablo)" )
            self.choiceMunicipio.Append(u"Bolívar (Aroa)")
            self.choiceMunicipio.Append("Bruzual (Chivacoa)")
            self.choiceMunicipio.Append("Cocorote (Cocorote)")
            self.choiceMunicipio.Append("Independencia (Independencia)")
            self.choiceMunicipio.Append(u"José Antonio Páez (Sabana de Parra)")
            self.choiceMunicipio.Append("La Trinidad (Boraure)")
            self.choiceMunicipio.Append("Manuel Monge (Yumare)")
            self.choiceMunicipio.Append("Nirgua (Nirgua)")
            self.choiceMunicipio.Append(u"Peña (Yaritagua)")
            self.choiceMunicipio.Append("San Felipe (San Felipe)")
            self.choiceMunicipio.Append("Sucre (Guama)")
            self.choiceMunicipio.Append("Urachiche (Urachiche)")
            self.choiceMunicipio.Append("Veroes (Farriar)")


        if self.choiceEntFed.GetSelection() == 24:
            #zulia
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Almirante Padilla (El Toro)" )
            self.choiceMunicipio.Append("Baralt (San Timoteo)")
            self.choiceMunicipio.Append("Cabimas (Cabimas)" )
            self.choiceMunicipio.Append("Catatumbo (Encontrados)")
            self.choiceMunicipio.Append(u"Colón (San Carlos del Zulia)" )
            self.choiceMunicipio.Append("Francisco Javier Pulgar (Pueblo Nuevo-El Chivo)")
            self.choiceMunicipio.Append(u"Jesús Enrique Losada (La Concepción)" )
            self.choiceMunicipio.Append(u"Jesús María Semprún (Casigua El Cubo)")
            self.choiceMunicipio.Append("La Cañada de Urdaneta (Concepción)" )
            self.choiceMunicipio.Append("Lagunillas (Ciudad Ojeda)")
            self.choiceMunicipio.Append(u"Machiques de Perijá (Machiques)" )
            self.choiceMunicipio.Append(u"Mara (San Rafael del Moján)")
            self.choiceMunicipio.Append("Maracaibo (Maracaibo)" )
            self.choiceMunicipio.Append("Miranda (Los Puertos de Altagracia)")
            self.choiceMunicipio.Append(u"Páez (Sinamaica)" )
            self.choiceMunicipio.Append(u"Rosario de Perijá (La Villa del Rosario)")
            self.choiceMunicipio.Append("San Francisco (San Francisco)" )
            self.choiceMunicipio.Append("Santa Rita (Santa Rita)")
            self.choiceMunicipio.Append(u"Simón Bolívar (Tu00eda Juana)" )
            self.choiceMunicipio.Append("Sucre (Bobures)")
            self.choiceMunicipio.Append("Valmore Rodríguez (Bachaquero)" )

        self.choiceMunicipio.SetSelection(0)

    def WizardConfigInicialOnWizardPageChanging(self, event):
        page=event.GetPage()
        try:
            if page==self.page1ConfigInicial and event.GetDirection():
                self.nucleo=string.capwords(self.txtNucleo.GetValue())
                self.entfed=self.choiceEntFed.GetStringSelection()
                self.municipio=self.choiceMunicipio.GetStringSelection()
                if self.nucleo=='' or self.choiceEntFed.GetSelection()==0 or self.choiceMunicipio.GetSelection()==0:
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.txtNucleo.Clear()
                    self.choiceEntFed.SetSelection(0)
                    self.choiceMunicipio.SetSelection(0)
                    self.txtNucleo.SetFocus()
                    event.Veto()
            elif page==self.page2ConfigInicial and event.GetDirection():
                #si estamos en la pagina de datos de Usuario administrador
                adminLoginUnicode=string.lower(self.txtUsuarioAdmin.GetValue().encode('utf-8'))
                self.adminLogin=unicode(adminLoginUnicode)
                self.passAdmin=self.txtPassAdmin.GetValue()

                #se encripta la clave con MD5
                self.hashAdmin = hashlib.md5()
                self.hashAdmin.update(self.passAdmin)

                if self.passAdmin=='' or self.adminLogin=='':
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.txtUsuarioAdmin.Clear()
                    self.txtPassAdmin.Clear()
                    self.txtUsuarioAdmin.SetFocus()
                    event.Veto()
            elif self.page3ConfigInicial and event.GetDirection():
                self.preguntaSeg=self.choicePreguntaSeg.GetStringSelection()
                self.respuestaSeg=self.txtRespuestaSeg.GetValue()
                if self.choicePreguntaSeg.GetSelection()==0 or self.respuestaSeg=='':
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.choicePreguntaSeg.SetSelection(0)
                    self.txtRespuestaSeg.Clear()
                    event.Veto()
        except (UnicodeEncodeError, UnicodeDecodeError), e:
            #error, sacamos dialogo y decimos que hagan configuracion -- se crea un LOG del Error
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'El Nombre de Usuario y la Contraseña no deben contener caracteres especiales. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtUsuarioAdmin.Clear()
            self.txtPassAdmin.Clear()
            self.txtPassAdmin.SetFocus()
            event.Veto()

    def WizardConfigInicialOnWizardCancel( self, event ):
        pass

    def WizardConfigInicialOnWizardFinished( self, event ):
        try:
            BD=ModeloBD()
            BD.configuracionInicial(self.nucleo, self.entfed, self.municipio,self.adminLogin, self.passAdmin, self.preguntaSeg, self.respuestaSeg)
            mensaje=wx.MessageDialog(self,u'Datos del Núcleo Agregados al Sistema',u"Agregando Datos del Núcleo", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()
            self.frameInicio = FInicio(None)

            icon = os.path.normpath(os.path.join(iconDir, "favicon.ico"))
            favicon = wx.Icon(icon, wx.BITMAP_TYPE_ICO, 16, 16)
            wx.Frame.SetIcon(self.frameInicio, favicon)

            self.frameInicio.Show()
            self.frameInicio.txtNomUsuario.SetFocus()
        except lite.Error, e:
            #error, sacamos dialogo y decimos que hagan configuracion
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'Error en la conección a la base de Datos. \nIntente de nuevo o haga click en "Cancelar" para salir. \n\n%s'%e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtNucleo.Clear()
            self.choiceEntFed.Clear()
            self.choiceMunicipio.Clear()
            self.txtUsuarioAdmin.Clear()
            self.txtPassAdmin.Clear()
            self.choicePreguntaSeg.Clear()
            self.txtRespuestaSeg.Clear()
            BD.cnn.rollback()
            BD.desconectar()
        except (UnicodeEncodeError, UnicodeDecodeError),e:
            #error, sacamos dialogo y decimos que hagan configuracion
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'La contraseña no debe contener caracteres especiales. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtNucleo.Clear()
            self.choiceEntFed.Clear()
            self.choiceMunicipio.Clear()
            self.txtUsuarioAdmin.Clear()
            self.txtPassAdmin.Clear()
            self.choicePreguntaSeg.Clear()
            self.txtRespuestaSeg.Clear()


class panelBienvenida (PanelBienvenida):

    pass


class Video(wx.Frame):
    """
    Clase que muestra el Stream de una camara para capturar una foto
    """

    fps = 30000

    def __init__(self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Captura de Foto de Alumno", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        app.IconizarFrames(self)

        self.padre=self.GetParent().nombre

        #SE CREAN LOS ELEMENTOS DE INTERFAZ

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize)

        sizerPrincipal = wx.BoxSizer( wx.VERTICAL )

        self.panelPrincipal = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerPrincipal_2 = wx.BoxSizer( wx.VERTICAL )

        self.displayPanel = wx.Panel( self.panelPrincipal, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        sizerVideo = wx.BoxSizer( wx.VERTICAL )

        self.panelVideo = wx.Panel(self.displayPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        sizerVideo.Add(self.panelVideo, 1, wx.ALL | wx.EXPAND, 5)


        self.displayPanel.SetSizer( sizerVideo )
        self.displayPanel.Layout()
        sizerVideo.Fit( self.displayPanel )
        sizerPrincipal_2.Add( self.displayPanel, 1, wx.ALL|wx.EXPAND, 5 )

        self.btnPanel = wx.Panel( self.panelPrincipal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerBtn = wx.BoxSizer( wx.HORIZONTAL )

        self.buttonCaptura = wx.Button( self.btnPanel, wx.ID_ANY, u"Capturar", wx.DefaultPosition, wx.DefaultSize, 0 )
        sizerBtn.Add( self.buttonCaptura, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.buttonSalir = wx.Button( self.btnPanel, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
        sizerBtn.Add( self.buttonSalir, 0, wx.ALL, 5 )


        self.btnPanel.SetSizer( sizerBtn )
        self.btnPanel.Layout()
        sizerBtn.Fit( self.btnPanel )
        sizerPrincipal_2.Add( self.btnPanel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        self.panelPrincipal.SetSizer( sizerPrincipal_2 )
        self.panelPrincipal.Layout()
        sizerPrincipal_2.Fit( self.panelPrincipal )
        sizerPrincipal.Add( self.panelPrincipal, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( sizerPrincipal )
        self.Layout()

        self.Centre( wx.BOTH )

        #DEFINICION DE EVENTOS
        self.Bind(wx.EVT_BUTTON, self.captura,self.buttonCaptura) #Evento: Captura de la foto
        self.Bind( wx.EVT_CLOSE, self.OnClose ) #Evento: Cerrar Frame
        self.buttonSalir.Bind( wx.EVT_BUTTON, self.buttonSalirOnButtonClick ) #Evento: Boton para cerrar frame

    def initVideo(self):

        self.activo=True

        self.cont=0

        self.SetDoubleBuffered(True)
        self.capture = None
        self.imagen = None

        #set up camera init
        self.capture = Camera()
        self.imagen = self.capture.getImage()
        self.imagen = self.imagen.adaptiveScale((320, 240))
        self.imagen.save(os.path.join(profilePicDir, "imagen.jpg"))
        self.SetSize((self.imagen.width,self.imagen.height*1.5))

        self.fpstimer = wx.Timer(self)
        self.fpstimer.Start(10000/self.fps)

        self.Bind(wx.EVT_TIMER, self.onNextFrame, self.fpstimer)
        self.Bind(wx.EVT_PAINT, self.onPaint)

    def onNextFrame(self,evt):
        if self.activo:
            self.updateVideo()
            self.Refresh()
            evt.Skip()

    def updateVideo(self):
        self.imagen = self.capture.getImage()
        self.imagen = self.imagen.adaptiveScale((320, 240))
        self.imagen.save(os.path.join(profilePicDir, "imagen.jpg"))
        self.Refresh()

    def onPaint(self,evt):
        if self.activo:
            wx.BufferedPaintDC(self.panelVideo,wx.Bitmap(os.path.join(profilePicDir, "imagen.jpg"), wx.BITMAP_TYPE_ANY ))
            evt.Skip()


    def captura(self,evt):

        path=None

        if self.padre=='Carga':
            nombreFoto="FotoAlumno-%s-%s.jpg" % (self.GetParent().date_str, os.getpid())
            path=os.path.join(profilePicDir, nombreFoto)
            self.GetParent().foto=path
            self.imagen.adaptiveScale((160, 120)).save(self.GetParent().foto)
        elif self.padre=='Edicion':
            nombreFoto="FotoAlumno-%s-%s.jpg" % (self.GetParent().date_str, os.getpid())
            path=os.path.join(profilePicDir, nombreFoto)
            self.GetParent().fotoEditar=path

            if  not os.path.isfile(self.GetParent().fotoEditar):
                self.GetParent().fotoEditar= path
                self.imagen.adaptiveScale((160, 120)).save(self.GetParent().fotoEditar)
            else:
                self.GetParent().fotoEditar= path
                os.remove(self.GetParent().fotoEditar)
                self.imagen.adaptiveScale((160, 120)).save(self.GetParent().fotoEditar)

        self.GetParent().bitmapFoto.SetBitmap(wx.Bitmap( path, wx.BITMAP_TYPE_ANY ))
        self.GetParent().bitmapFoto.FitInside()
        self.GetParent().bitmapFoto.Refresh()
        self.GetParent().Refresh()
        self.activo=False
        self.Close()

    def buttonSalirOnButtonClick(self,evt):
        self.activo=False
        self.Close()

    def OnClose(self, evt):
        self.activo=False
        os.remove(os.path.join(profilePicDir, "imagen.jpg"))
        self.MakeModal(False)
        self.Destroy()

class panelCarga (PanelCargaAlumno):
    """
    Clase para el manejo de la carga de alumnos al sistema
    """


    def EvtCheckListBox(self, event):
        self.elemento=''
        index = event.GetSelection()
        label = self.checkCatedras_carga.GetString(index)
        if self.checkCatedras_carga.IsChecked(index):
            self.listaCatedras_carga.append(label)
        else:
            self.listaCatedras_carga.remove(label)

        for item in self.listaCatedras_carga:
            self.elemento=self.elemento+','+item

        self.checkCatedras_carga.SetSelection(index)    # so that (un)checking also selects (moves the highlight)


    def btnFoto_CargaOnButtonClick(self, event):
        """
        Abrir Frame para captura de imagen
        """
        self.frameVideo = Video(self)
        self.frameVideo.initVideo()
        self.frameVideo.Show()
        self.frameVideo.MakeModal(True)

    def preCargaRadios(self):
        """
        Inicializaciones Varias del Pnel de Carga de alumnos
        """
        now=datetime.now()
        self.date_str = now.strftime("%Y-%m-%d_%H%M%S")

        self.bitmapFoto.SetBitmap(wx.Bitmap( fotoVacia, wx.BITMAP_TYPE_ANY ))
        self.bitmapFoto.Refresh()
        self.Refresh()

        self.txtNumActFijoInstAlumno_Carga.Enable(False)
        self.datepickerFecAsigInstAlumno_Carga.Enable(False)
        self.txtEdadAlumno_Carga.SetEditable(False)

    def datePickerFechaNacAlumno_CargaOnDateChanged(self, event):
        """
        Calculo automatico de la edad del alumno segun su fecha de Nacimiento
        """
        anio_actual=date.today().year
        anio_nacimiento=self.datePickerFechaNacAlumno_Carga.GetValue().GetYear()
        edad=anio_actual-anio_nacimiento
        if edad >= 5:
            self.txtEdadAlumno_Carga.SetValue(str(anio_actual-anio_nacimiento))
            return True
        else:
            self.txtEdadAlumno_Carga.Clear()
            return False


    def radioEstudiaAlumno_CargaOnRadioBox(self, event):
        """
        Activacion / Desactivacion de diferentes controles segun el alumno estudie o no
        """
        if self.radioEstudiaAlumno_Carga.GetStringSelection()=='No':
            self.txtGradoAlumno_Carga.Clear()
            self.txtAnioAlumno_Carga.Clear()
            self.txtSemestreAlumno_Carga.Clear()
            self.txtInstitAlumno_Carga.Clear()
            self.txtDireccionInstitAlumno_Carga.Clear()
            self.txtTelefonoInstitAlumno_Carga.Clear()

            self.radioEducacionAlumno_Carga.Enable(False)
            self.txtGradoAlumno_Carga.Enable(False)
            self.txtAnioAlumno_Carga.Enable(False)
            self.txtSemestreAlumno_Carga.Enable(False)
            self.txtInstitAlumno_Carga.Enable(False)
            self.txtDireccionInstitAlumno_Carga.Enable(False)
            self.txtTelefonoInstitAlumno_Carga.Enable(False)
            self.radioTipoInstitAlumno_Carga.Enable(False)

        elif self.radioEstudiaAlumno_Carga.GetStringSelection()=='Si':
            self.txtGradoAlumno_Carga.Clear()
            self.txtAnioAlumno_Carga.Clear()
            self.txtSemestreAlumno_Carga.Clear()
            self.txtInstitAlumno_Carga.Clear()
            self.txtDireccionInstitAlumno_Carga.Clear()
            self.txtTelefonoInstitAlumno_Carga.Clear()

            self.radioEducacionAlumno_Carga.Enable(True)
            self.txtGradoAlumno_Carga.Enable(True)
            self.txtAnioAlumno_Carga.Enable(True)
            self.txtSemestreAlumno_Carga.Enable(True)
            self.txtInstitAlumno_Carga.Enable(True)
            self.txtDireccionInstitAlumno_Carga.Enable(True)
            self.txtTelefonoInstitAlumno_Carga.Enable(True)
            self.radioTipoInstitAlumno_Carga.Enable(True)


    def radioInstPropioAlumno_CargaOnRadioBox(self, event):
        """
        Activacion / Desactivacion de diferentes controles segun el alumno estudie tenga instrumento propio o no
        """
        if self.radioInstPropioAlumno_Carga.GetStringSelection()=='No':
            self.datepickerFecAsigInstAlumno_Carga.SetValue(wx.DateTime.Today())
            self.datepickerFecAsigInstAlumno_Carga.Enable(True)
            self.txtNumActFijoInstAlumno_Carga.Clear()
            self.txtNumActFijoInstAlumno_Carga.Enable(True)
        elif self.radioInstPropioAlumno_Carga.GetStringSelection()=='Si':
            self.datepickerFecAsigInstAlumno_Carga.SetValue(wx.DateTime.Today())
            self.datepickerFecAsigInstAlumno_Carga.Enable(False)
            self.txtNumActFijoInstAlumno_Carga.Enable(False)
            self.txtNumActFijoInstAlumno_Carga.Clear()


    def radioOtraAgrupAlumno_CargaOnRadioBox(self, event):
        """
        Activacion / Desactivacion de diferentes controles segun el alumno pertenezca a otra agrupacion  o no
        """
        if self.radioOtraAgrupAlumno_Carga.GetStringSelection()=='No':
            self.txtNombreOtraAgrupAlumno_Carga.Clear()
            self.txtNombreOtraAgrupAlumno_Carga.Enable(False)
            self.datePickerFechaIngOtraAgrupAlumno_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFechaIngOtraAgrupAlumno_Carga.Enable(False)
        elif self.radioOtraAgrupAlumno_Carga.GetStringSelection()=='Si':
            self.txtNombreOtraAgrupAlumno_Carga.Clear()
            self.txtNombreOtraAgrupAlumno_Carga.Enable(True)
            self.datePickerFechaIngOtraAgrupAlumno_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFechaIngOtraAgrupAlumno_Carga.Enable(True)


    #ACTIVACION / DESACTIVACION DE DIFERENTES CONTROLES SEGUN LAS VACUNAS QUE TENGA EL ALUMNO

    def radioFMedVacFA_CargaOnRadioBox( self, event ):
        if self.radioFMedVacFA_Carga.GetStringSelection()=='No':
            self.datePickerFMedVacFA_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacFA_Carga.Enable(False)
        elif self.radioFMedVacFA_Carga.GetStringSelection()=='Si':
            self.datePickerFMedVacFA_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacFA_Carga.Enable(True)


    def radioFMedVacHA_CargaOnRadioBox( self, event ):
        if self.radioFMedVacHA_Carga.GetStringSelection()=='No':
            self.datePickerFMedVacHA_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHA_Carga.Enable(False)
        elif self.radioFMedVacHA_Carga.GetStringSelection()=='Si':
            self.datePickerFMedVacHA_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHA_Carga.Enable(True)


    def radioFMedVacHB_CargaOnRadioBox( self, event ):
        if self.radioFMedVacHB_Carga.GetStringSelection()=='No':
            self.datePickerFMedVacHB_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHB_Carga.Enable(False)
        elif self.radioFMedVacHB_Carga.GetStringSelection()=='Si':
            self.datePickerFMedVacHB_Carga.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHB_Carga.Enable(True)


    def radioFMedTieneSeguro_CargaOnRadioBox( self, event ):
        if self.radioFMedTieneSeguro_Carga.GetStringSelection()=='No':
            self.txtFMedAseg_Carga.Clear()
            self.txtFMedAseg_Carga.Enable(False)
            self.txtFMedTelAseg_Carga.Enable(False)
        elif self.radioFMedTieneSeguro_Carga.GetStringSelection()=='Si':
            self.txtFMedAseg_Carga.Clear()
            self.txtFMedAseg_Carga.Enable(True)
            self.txtFMedTelAseg_Carga.Enable(True)


    def sdbSizerBtnGuardarOnSaveButtonClick( self, event):
        """
        Acciones al Cargar el Alumno en el Sistema
        """

        if self.radioEstudiaAlumno_Carga.GetStringSelection()=='No':
            self.EducacionAlumno_Carga=None
            self.TipoInstitAlumno_Carga=None
            self.txtGradoAlumno_Carga.SetValue('')
            self.txtAnioAlumno_Carga.SetValue('')
            self.txtSemestreAlumno_Carga.SetValue('')
            self.txtInstitAlumno_Carga.SetValue('')
            self.txtDireccionInstitAlumno_Carga.SetValue('')
            self.txtTelefonoInstitAlumno_Carga.SetValue('')
        else:
            self.EducacionAlumno_Carga=self.radioEducacionAlumno_Carga.GetStringSelection()
            self.TipoInstitAlumno_Carga=self.radioTipoInstitAlumno_Carga.GetStringSelection()


        if self.radioInstPropioAlumno_Carga.GetStringSelection()=='Si':
            self.FecAsigInstAlumno_Carga=None
        else:
            self.FecAsigInstAlumno_Carga=self.datepickerFecAsigInstAlumno_Carga.GetValue().Format('%Y-%m-%d')


        if self.radioOtraAgrupAlumno_Carga.GetStringSelection()=='No':
            self.FechaIngOtraAgrupAlumno_Carga=None
        else:
            self.FechaIngOtraAgrupAlumno_Carga=self.datePickerFechaIngOtraAgrupAlumno_Carga.GetValue().Format('%Y-%m-%d')


        if self.radioFMedVacFA_Carga.GetStringSelection()=='No':
            self.FMedVacFA_Carga=None
        elif self.radioFMedVacFA_Carga.GetStringSelection()=='Si':
            self.FMedVacFA_Carga=self.datePickerFMedVacFA_Carga.GetValue().Format('%Y-%m-%d')


        if self.radioFMedVacHA_Carga.GetStringSelection()=='No':
            self.FMedVacHA_Carga=None
        elif self.radioFMedVacHA_Carga.GetStringSelection()=='Si':
            self.FMedVacHA_Carga=self.datePickerFMedVacHA_Carga.GetValue().Format('%Y-%m-%d')


        if self.radioFMedVacHB_Carga.GetStringSelection()=='No':
            self.FMedVacHB_Carga=None
        elif self.radioFMedVacHB_Carga.GetStringSelection()=='Si':
            self.FMedVacHB_Carga=self.datePickerFMedVacHB_Carga.GetValue().Format('%Y-%m-%d')


        if self.radioFMedTieneSeguro_Carga.GetStringSelection()=='No':
            self.txtFMedAseg_Carga.SetValue('')
            self.txtFMedTelAseg_Carga.SetValue('')


        #INICIAMOS VALIDADOR
        self.validator=NotEmptyValidator()

        #VALIDAMOS NOMBRE
        self.validator.SetWindow(self.txtNomAlumno_Carga)
        if self.validator.Validate(self.txtNomAlumno_Carga):
            validaNombre=True
        else:
            validaNombre=False

        #VALIDAMOS APELLIDO
        self.validator.SetWindow(self.txtApeAlumno_Carga)
        if self.validator.Validate(self.txtApeAlumno_Carga):
            validaApe=True
        else:
            validaApe=False

        #VALIDAMOS LUGAR DE NACIMIENTO
        self.validator.SetWindow(self.txtLugarNacAlumno_Carga)
        if self.validator.Validate(self.txtLugarNacAlumno_Carga):
            validaLugarNac=True
        else:
            validaLugarNac=False

        #VALIDAMOS FECHA DE INGRESO
        self.validator.SetWindow(self.datePickerFechaIngAlumno_Carga)
        if self.validator.Validate(self.datePickerFechaIngAlumno_Carga):
            validaFecIngreso=True
        else:
            validaFecIngreso=False

        #VALIDAMOS NOMBRE DE REPRESENTANTE
        self.validator.SetWindow(self.txtNombreRepAlumno_Carga)
        if self.validator.Validate(self.txtNombreRepAlumno_Carga):
            validaNomRep=True
        else:
            validaNomRep=False

        #VALIDAMOS APELLIDO REPRESENTANTE
        self.validator.SetWindow(self.txtApeRepAlumno_Carga)
        if self.validator.Validate(self.txtApeRepAlumno_Carga):
            validaApeRep=True
        else:
            validaApeRep=False

        #VALIDAMOS CEDULA DE REPRESENTANTE
        self.validator.SetWindow(self.txtCiRep_Carga)
        if self.validator.Validate(self.txtCiRep_Carga):
            validaCiRep=True
        else:
            validaCiRep=False

        #VALIDAMOS DIRECION REPRESENTANTE
        self.validator.SetWindow(self.txtDirHabRep_Carga)
        if self.validator.Validate(self.txtDirHabRep_Carga):
            validaDirRep=True
        else:
            validaDirRep=False

        #VALIDAMOS PARENTEZCO RERESENTANTE
        self.validator.SetWindow(self.txtParentescoRep_Carga)
        if self.validator.Validate(self.txtParentescoRep_Carga):
            validaParentRep=True
        else:
            validaParentRep=False

        #VALIDAMOS ORQUESTA
        self.validator.SetWindow(self.choiceOrquAlumno_Carga)
        if self.validator.Validate(self.choiceOrquAlumno_Carga):
            validaOrqAlumno=True
        else:
            validaOrqAlumno=False

        #VALIDAMOS MARCA INSTRUMENTO
        self.validator.SetWindow(self.txtMarcaInstAlumno_Carga)
        if self.validator.Validate(self.txtMarcaInstAlumno_Carga):
            validaMarcaInst=True
        else:
            validaMarcaInst=False


        #VALIDAMOS MODELO INSTRUMENTO
        self.validator.SetWindow(self.txtModeloInstAlumno_Carga)
        if self.validator.Validate(self.txtModeloInstAlumno_Carga):
            validaModeloInst=True
        else:
            validaModeloInst=False

        #VALIDAMOS SERIAL INSTRUMENTO
        self.validator.SetWindow(self.txtSerialInstAlumno_Carga)
        if self.validator.Validate(self.txtSerialInstAlumno_Carga):
            validaSerialInst=True
        else:
            validaSerialInst=False

        #VALIDAMOS PROFESOR
        self.validator.SetWindow(self.txtProfAlumno_Carga)
        if self.validator.Validate(self.txtProfAlumno_Carga):
            validaProf=True
        else:
            validaProf=False

        if (validaNombre and validaApe and validaLugarNac and validaNomRep and validaApeRep
            and validaCiRep and validaDirRep and validaParentRep and validaMarcaInst and validaModeloInst and
            validaSerialInst and validaProf and validaOrqAlumno and validaFecIngreso):
            if self.txtEdadAlumno_Carga.GetValue() != '':

                num_elementos_seleccionados = 0
                for item in range(self.checkCatedras_carga.GetCount()):
                    if self.checkCatedras_carga.IsChecked(item):
                        num_elementos_seleccionados = num_elementos_seleccionados+1
                if num_elementos_seleccionados > 0:
                    try:
                        app.BD.agregarAlumno(str(self.foto), string.capwords(self.txtNomAlumno_Carga.GetValue()),
                            string.capwords(self.txtApeAlumno_Carga.GetValue()),
                            self.txtCiAlumno_Carga.GetValue(),
                            self.datePickerFechaNacAlumno_Carga.GetValue().Format('%Y-%m-%d'),
                            self.datePickerFechaIngAlumno_Carga.GetValue().Format('%Y-%m-%d'),
                            string.capitalize(self.txtLugarNacAlumno_Carga.GetValue()),
                            self.radioSexoAlumno_Carga.GetStringSelection(),
                            self.txtEdadAlumno_Carga.GetValue(),
                            self.txtDirTelHabAlumno_Carga.GetValue(),
                            self.txtDirTelCelAlumno_Carga.GetValue(),
                            self.txtDirEmailalumno_Carga.GetValue(),
                            string.capwords(self.txtDirMunicipioAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirParroquiaAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirSectorAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirUrbarrioAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirAvenidaAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirCalleAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirEdificioAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirCasaAptoAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDirPtoRefAlumno_Carga.GetValue()),
                            string.capwords(self.txtNombreRepAlumno_Carga.GetValue()),
                            string.capwords(self.txtApeRepAlumno_Carga.GetValue()),
                            self.txtCiRep_Carga.GetValue(),
                            string.capitalize(self.txtDirHabRep_Carga.GetValue()),
                            self.txtTelHabRep_Carga.GetValue(),
                            self.txtTelCelRep_Carga.GetValue(),
                            self.txtEmailRep_Carga.GetValue(),
                            string.capitalize(self.txtDirTrabajoRep_Carga.GetValue()),
                            self.txtTelTrabajoRep_Carga.GetValue(),
                            string.capitalize(self.txtOcupacionRep_Carga.GetValue()),
                            string.capitalize(self.txtParentescoRep_Carga.GetValue()),
                            self.radioEstudiaAlumno_Carga.GetStringSelection(),
                            self.EducacionAlumno_Carga,
                            self.txtGradoAlumno_Carga.GetValue(),
                            self.txtAnioAlumno_Carga.GetValue(),
                            self.txtSemestreAlumno_Carga.GetValue(),
                            string.capwords(self.txtInstitAlumno_Carga.GetValue()),
                            string.capitalize(self.txtDireccionInstitAlumno_Carga.GetValue()),
                            self.txtTelefonoInstitAlumno_Carga.GetValue(),
                            self.TipoInstitAlumno_Carga,
                            self.radioConocMusAlumno_Carga.GetStringSelection(),
                            self.elemento[1:],
                            self.choiceOrquAlumno_Carga.GetStringSelection(),
                            string.capitalize(self.txtNivelOrqAlumno_Carga.GetValue()),
                            self.radioInstPropioAlumno_Carga.GetStringSelection(),
                            self.FecAsigInstAlumno_Carga,
                            string.capitalize(self.txtMarcaInstAlumno_Carga.GetValue()),
                            string.capitalize(self.txtModeloInstAlumno_Carga.GetValue()),
                            self.txtSerialInstAlumno_Carga.GetValue(),
                            self.txtNumActFijoInstAlumno_Carga.GetValue(),
                            string.capwords(self.txtProfAlumno_Carga.GetValue()),
                            self.choiceStatusAlumno_Carga.GetStringSelection(),
                            self.radioOtraAgrupAlumno_Carga.GetStringSelection(),
                            string.capwords(self.txtNombreOtraAgrupAlumno_Carga.GetValue()),
                            self.FechaIngOtraAgrupAlumno_Carga,
                            self.txtFMedTipoSangreAlumno_Carga.GetValue(),
                            string.capitalize(self.txtFMedAntecedAlumno_Carga.GetValue()),
                            self.radioFMedVacFA_Carga.GetStringSelection(),
                            self.FMedVacFA_Carga,
                            self.radioFMedVacHA_Carga.GetStringSelection(),
                            self.FMedVacHA_Carga,
                            self.radioFMedVacHB_Carga.GetStringSelection(),
                            self.FMedVacHB_Carga,
                            self.radioFMedEnfCab_Carga.GetStringSelection(),
                            self.radioFMedEnfOid_Carga.GetStringSelection(),
                            self.radioFMedEnfNar_Carga.GetStringSelection(),
                            self.radioFMedEnfGar_Carga.GetStringSelection(),
                            self.radioFMedEnfCor_Carga.GetStringSelection(),
                            self.radioFMedEnfPul_Carga.GetStringSelection(),
                            self.radioFMedEnfVD_Carga.GetStringSelection(),
                            self.radioFMedEnfRi_Carga.GetStringSelection(),
                            self.radioFMedEnfHue_Carga.GetStringSelection(),
                            self.radioFMedEnfArt_Carga.GetStringSelection(),
                            self.radioFMedEnfEnd_Carga.GetStringSelection(),
                            string.capitalize(self.txtFMedOperaciones_Carga.GetValue()),
                            self.txtFMedAlerCom_Carga.GetValue(),
                            self.txtFMedAlerMed_Carga.GetValue(),
                            string.capitalize(self.txtFMedAlerMedEsp_Carga.GetValue()),
                            self.radioFMedTieneSeguro_Carga.GetStringSelection(),
                            string.capitalize(self.txtFMedAseg_Carga.GetValue()),
                            string.capitalize(self.txtFMedTelAseg_Carga.GetValue()),
                            self.txtFMedTelEmerg_Carga.GetValue(),
                            string.capwords(self.txtFMedUnidadMedPref_Carga.GetValue()),
                            string.capwords(self.txtFMedTratante_Carga.GetValue()),
                            self.txtFMedTelTratante_Carga.GetValue(),
                            self.txtFMedCelTratante_Carga.GetValue(),
                            string.capitalize(self.txtFMedEnfPrevia_Carga.GetValue()),
                            string.capitalize(self.txtFMedAperato_Carga.GetValue()))
                        mensaje=wx.MessageDialog(self,u'Alumno Guardado \n\n',"Guardando", wx.OK|wx.ICON_INFORMATION)
                        mensaje.ShowModal()
                        self.cargado=True
                        self.elemento=None
                        self.listaCatedras_carga=[]
                        self.GetParent().limpiarPantalla()
                        self.txtApeAlumno_Carga.SetFocus()
                        app.limpiarFotos()
                        self.foto=None
                        num_elementos_seleccionados=0
                        
                    except lite.Error, e:
                        #error, sacamos dialogo y decimos que hagan configuracion
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                        logging.error('%s - %s'%(e, trace))
                        mensaje=wx.MessageDialog(self,u'Error: \n\n%s'%e,"Error", wx.OK|wx.ICON_HAND)
                        mensaje.ShowModal()
                        self.cargado=False
                    num_elementos_seleccionados=0

                else:
                    mensaje=wx.MessageDialog(self,u'Error: Debe Seleccionar al menos una Cátedra\n\n',"Error", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.cargado=False
            else:
                mensaje=wx.MessageDialog(self,u'Error: La Edad debe ser mayor o igual a 5 Años\n\n',"Error", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
                self.cargado=False
        else:
            if self.notebookAlumno.GetSelection != 0:
                self.notebookAlumno.SetSelection(0)
            self.txtApeAlumno_Carga.SetFocus()
            mensaje=wx.MessageDialog(self,u'Los Campos Resaltados son Obligatorios',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.cargado=False


class panelEdicion (PanelEditAlumno):
    """
    Clase para el manejo de la Edicion de alumnos  en el sistema
    """

    def cargarChoiceEdicion(self):
        """
        Carga el listado de Alumnos en el ChoiceCtrl y desactivar los controles hasta que se seleccione un Alumno
        """

        self.m_choiceNomAlumno.Clear()
        self.m_choiceNomAlumno.Append("SeleccionarAlumno...")
        self.m_choiceNomAlumno.SetSelection( 0 )

        alumnos=app.BD.listarAlumnos() #Consulta a BD

        self.listaID_alumnos=[]
        for alumno in alumnos:
            self.m_choiceNomAlumno.Append(alumno[1]+" "+alumno[2])
            self.listaID_alumnos.append(alumno[0])

        self.Layout()

    def btnFoto_EdicionOnButtonClick(self, event):
        """
        Abrir Frame para captura de imagen
        """

        self.frameVideo = Video(self)
        self.frameVideo.initVideo()
        self.frameVideo.Show()
        self.frameVideo.MakeModal(True)

    def cargarDatosALumno(self, id=None):
        """
        Muestra los datos obtenidos en una consulta a la BD en los campos correspondientes a la informacion del Alumno y su Ficha Medica
        """

        self.flag=False
        AlumnoSeleccionado=self.m_choiceNomAlumno.GetCurrentSelection()

        if not id:
            self.alumnoID=self.listaID_alumnos[AlumnoSeleccionado-1]
            self.flag=False
        else:
            self.alumnoID=id
            self.flag=True

        datosAlumno=app.BD.obtenerDatosAlumno(self.alumnoID)

        #CARGAR CAMPOS

        #DATOS GENERALES
        self.fotoEditar=datosAlumno["fotoAlumno"]

        if os.path.isfile(self.fotoEditar):
            self.bitmapFoto.SetBitmap(wx.Bitmap( self.fotoEditar, wx.BITMAP_TYPE_ANY ))
            self.bitmapFoto.Refresh()
            self.Refresh()
        else:
            self.bitmapFoto.SetBitmap(wx.Bitmap( fotoVacia, wx.BITMAP_TYPE_ANY ))
            self.bitmapFoto.Refresh()
            self.Refresh()

        self.txtApeAlumno_Edicion.SetValue(datosAlumno["apellidoAlumno"])
        self.txtNomAlumno_Edicion.SetValue(datosAlumno["nombreAlumno"])
        self.txtCiAlumno_Edicion.SetValue(datosAlumno["ciAlumno"])

        if datosAlumno["fechaNacAlumno"] != None:
            aN,mN,dN=map(int, datosAlumno["fechaNacAlumno"].split('-'))
            nacimiento=wx.DateTimeFromDMY(dN,mN-1,aN)
            self.datePickerFechaNacAlumno_Edicion.SetValue(nacimiento)

        if datosAlumno["fechaIngAlumno"] != None:
            aI,mI,dI=map(int, datosAlumno["fechaIngAlumno"].split('-'))
            ingreso=wx.DateTimeFromDMY(dI,mI-1,aI)
            self.datePickerFechaIngAlumno_Edicion.SetValue(ingreso)

        self.txtLugarNacAlumno_Edicion.SetValue(datosAlumno["lugarNacAlumno"])

        if datosAlumno["sexoAlumno"]=='Masculino':
            self.radioSexoAlumno_Edicion.SetSelection(0)
        else:
            self.radioSexoAlumno_Edicion.SetSelection(1)

        self.txtEdadAlumno_Edicion.SetValue(str(datosAlumno["edadAlumno"]))
        self.txtDirTelHabAlumno_Edicion.SetValue(datosAlumno["telefonoResAlumno"])
        self.txtDirTelCelAlumno_Edicion.SetValue(datosAlumno["telefonoCelAlumno"])
        self.txtDirEmailalumno_Edicion.SetValue(datosAlumno["emailAlumno"])

        #DIRECCION
        self.txtDirMunicipioAlumno_Edicion.SetValue(datosAlumno["municipio"])
        self.txtDirParroquiaAlumno_Edicion.SetValue(datosAlumno["parroquia"])
        self.txtDirSectorAlumno_Edicion.SetValue(datosAlumno["sector"])
        self.txtDirUrbarrioAlumno_Edicion.SetValue(datosAlumno["urbBarrio"])
        self.txtDirAvenidaAlumno_Edicion.SetValue(datosAlumno["avenida"])
        self.txtDirCalleAlumno_Edicion.SetValue(datosAlumno["calle"])
        self.txtDirEdificioAlumno_Edicion.SetValue(datosAlumno["edificio"])
        self.txtDirCasaAptoAlumno_Edicion.SetValue(datosAlumno["casaApto"])
        self.txtDirPtoRefAlumno_Edicion.SetValue(datosAlumno["ptoReferencia"])

        #REPRESENTANTE
        self.txtNombreRepAlumno_Edicion.SetValue(datosAlumno["nomRepresentante"])
        self.txtApeRepAlumno_Edicion.SetValue(datosAlumno["apellidoRepresentante"])
        self.txtCiRep_Edicion.SetValue(datosAlumno["ciRepresentante"])
        self.txtDirHabRep_Edicion.SetValue(datosAlumno["direccionRepresentante"])
        self.txtTelHabRep_Edicion.SetValue(datosAlumno["telefonoHabRepresentante"])
        self.txtTelCelRep_Edicion.SetValue(datosAlumno["telefonoCelRepresentante"])
        self.txtEmailRep_Edicion.SetValue(datosAlumno["emailRepresentante"])
        self.txtDirTrabajoRep_Edicion.SetValue(datosAlumno["dirTrabajoRepresentante"])
        self.txtTelTrabajoRep_Edicion.SetValue(datosAlumno["telefonoTrabRepresentante"])
        self.txtOcupacionRep_Edicion.SetValue(datosAlumno["ocupacionRepresentante"])
        self.txtParentescoRep_Edicion.SetValue(datosAlumno["parentescoRepresentante" ])

        #ACADEMICOS
        if datosAlumno["estudiaAcademicoAlumno"]=='Si':
            self.radioEstudiaAlumno_Edicion.SetSelection(0)
            self.radioEducacionAlumno_Edicion.Enable(True)
            self.radioTipoInstitAlumno_Edicion.Enable(True)
            self.txtGradoAlumno_Edicion.Enable(True)
            self.txtAnioAlumno_Edicion.Enable(True)
            self.txtSemestreAlumno_Edicion.Enable(True)
            self.txtInstitAlumno_Edicion.Enable(True)
            self.txtDireccionInstitAlumno_Edicion.Enable(True)
            self.txtTelefonoInstitAlumno_Edicion.Enable(True)
        elif datosAlumno["estudiaAcademicoAlumno"]=='No':
            self.radioEstudiaAlumno_Edicion.SetSelection(1)
            self.radioEducacionAlumno_Edicion.Enable(False)
            self.radioTipoInstitAlumno_Edicion.Enable(False)
            self.txtGradoAlumno_Edicion.Enable(False)
            self.txtAnioAlumno_Edicion.Enable(False)
            self.txtSemestreAlumno_Edicion.Enable(False)
            self.txtInstitAlumno_Edicion.Enable(False)
            self.txtDireccionInstitAlumno_Edicion.Enable(False)
            self.txtTelefonoInstitAlumno_Edicion.Enable(False)

        if datosAlumno["nivelAcademicoAlumno"] != None:
            if datosAlumno["nivelAcademicoAlumno"]=='Media':
                self.radioEducacionAlumno_Edicion.SetSelection(0)
            elif datosAlumno["nivelAcademicoAlumno"]==u'Básica':
                self.radioEducacionAlumno_Edicion.SetSelection(1)
            elif datosAlumno["nivelAcademicoAlumno"]=='Diversificada':
                self.radioEducacionAlumno_Edicion.SetSelection(2)
            elif datosAlumno["nivelAcademicoAlumno"]=='Universitaria':
                self.radioEducacionAlumno_Edicion.SetSelection(3)
        else:
            self.radioEducacionAlumno_Edicion.SetSelection(0)

        self.txtGradoAlumno_Edicion.SetValue(datosAlumno["gradoAcademicoAlumno"])
        self.txtAnioAlumno_Edicion.SetValue(datosAlumno["anioAcademicoAlumno"])
        self.txtSemestreAlumno_Edicion.SetValue(datosAlumno["semestreAcademicoAlumno"])
        self.txtInstitAlumno_Edicion.SetValue(datosAlumno["institucionAcademicoAlumno"])
        self.txtDireccionInstitAlumno_Edicion.SetValue(datosAlumno["direccionAcademicoAlumno"])
        self.txtTelefonoInstitAlumno_Edicion.SetValue(datosAlumno["telefonoAcademicoAlumno"])

        if datosAlumno["tipoInstitucionAcademicoAlumno"] != None:
            if datosAlumno["tipoInstitucionAcademicoAlumno"]==u'Pública':
                self.radioTipoInstitAlumno_Edicion.SetSelection(0)
            elif datosAlumno["tipoInstitucionAcademicoAlumno"]=='Privada':
                self.radioTipoInstitAlumno_Edicion.SetSelection(1)
        else:
            self.radioTipoInstitAlumno_Edicion.SetSelection(0)

        #MUSICAL
        if datosAlumno["conocimientosMusicales"] == 'Si':
            self.radioConocMusAlumno_Edicion.SetSelection(0)
        else:
            self.radioConocMusAlumno_Edicion.SetSelection(1)


        if u"Ritmo y Entonación" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(0)
            self.checkCatedras_edicion.SetSelection(0)
        if "Lenguaje Musical" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(1)
            self.checkCatedras_edicion.SetSelection(1)
        if u"Historia de la Música" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(2)
            self.checkCatedras_edicion.SetSelection(2)
        if u"Armonía y Contrapunto" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(3)
            self.checkCatedras_edicion.SetSelection(3)
        if u"Coro" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(4)
            self.checkCatedras_edicion.SetSelection(4)
        if u"Canto Lírico" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(5)
            self.checkCatedras_edicion.SetSelection(5)
        if u"Piano Principal" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(6)
            self.checkCatedras_edicion.SetSelection(6)
        if u"Piano Complementario" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(7)
            self.checkCatedras_edicion.SetSelection(7)
        if u"Flauta Dulce" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(8)
            self.checkCatedras_edicion.SetSelection(8)
        if u"Violín" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(9)
            self.checkCatedras_edicion.SetSelection(9)
        if u"Viola" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(10)
            self.checkCatedras_edicion.SetSelection(10)
        if u"Violoncello" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(11)
            self.checkCatedras_edicion.SetSelection(11)
        if u"Contrabajo" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(12)
            self.checkCatedras_edicion.SetSelection(12)
        if u"Flauta Trasversa" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(13)
            self.checkCatedras_edicion.SetSelection(13)
        if u"Oboe" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(14)
            self.checkCatedras_edicion.SetSelection(14)
        if u"Clarinete" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(15)
            self.checkCatedras_edicion.SetSelection(15)
        if u"Fagot" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(16)
            self.checkCatedras_edicion.SetSelection(16)
        if u"Corno" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(17)
            self.checkCatedras_edicion.SetSelection(17)
        if u"Trompeta" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(18)
            self.checkCatedras_edicion.SetSelection(18)
        if u"Trombón" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(19)
            self.checkCatedras_edicion.SetSelection(19)
        if u"Tuba" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(20)
            self.checkCatedras_edicion.SetSelection(20)
        if u"Saxofón" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(21)
            self.checkCatedras_edicion.SetSelection(21)
        if u"Batería" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(22)
            self.checkCatedras_edicion.SetSelection(22)
        if u"Percusión" in datosAlumno["catedraDatosMusicales"]:
            self.checkCatedras_edicion.Check(23)
            self.checkCatedras_edicion.SetSelection(23)

        if datosAlumno["orquestaDatosMusicales"]==u"Juvenil \"A\"":
            self.choiceOrquAlumno_Edicion.SetSelection(1)
        elif datosAlumno["orquestaDatosMusicales"]==u"Juvenil \"B\"":
            self.choiceOrquAlumno_Edicion.SetSelection(2)
        elif datosAlumno["orquestaDatosMusicales"]==u"Ninguna":
            self.choiceOrquAlumno_Edicion.SetSelection(3)

        self.txtNivelOrqAlumno_Edicion.SetValue(datosAlumno["nivelOrquestalDatosMusicales"])

        if datosAlumno["instrumentoPropio"]=='Si':
            self.radioInstPropioAlumno_Edicion.SetSelection(0)
            self.datepickerFecAsigInstAlumno_Edicion.Enable(False)
            self.datepickerFecAsigInstAlumno_Edicion.Enable(False)
        else:
            self.radioInstPropioAlumno_Edicion.SetSelection(1)
            self.datepickerFecAsigInstAlumno_Edicion.Enable(True)
            self.datepickerFecAsigInstAlumno_Edicion.Enable(True)

        if datosAlumno["fechaAsigInstDatosMusicales"] != None:
            aAsig,mAsig,dAsig=map(int, datosAlumno["fechaAsigInstDatosMusicales"].split('-'))
            asignacion=wx.DateTimeFromDMY(dAsig,mAsig-1,aAsig)
            self.datepickerFecAsigInstAlumno_Edicion.SetValue(asignacion)


        self.txtMarcaInstAlumno_Edicion.SetValue(datosAlumno["marcaInstrumentoDatosMusicales"])
        self.txtModeloInstAlumno_Edicion.SetValue(datosAlumno["modeloInstrumentoDatosMusicales"])
        self.txtSerialInstAlumno_Edicion.SetValue(datosAlumno["serialInstrumentoDatosMusicales"])
        self.txtNumActFijoInstAlumno_Edicion.SetValue(datosAlumno["numeroActivoFijoInstDatosMusicales"])
        self.txtProfAlumno_Edicion.SetValue(datosAlumno["profesorDatosMusicales"])

        if datosAlumno["statusDatosMusicales"]==u"Alumno Regular":
            self.choiceStatusAlumno_Edicion.SetSelection(1)
        elif datosAlumno["statusDatosMusicales"]==u"Alumno Nuevo Ingreso":
            self.choiceStatusAlumno_Edicion.SetSelection(2)
        else:
            self.choiceStatusAlumno_Edicion.SetSelection(0)

        if datosAlumno["otraAgrupacionDatosMusicales"]=='Si':
            self.txtNombreOtraAgrupAlumno_Edicion.Enable(True)
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.Enable(True)
            self.radioOtraAgrupAlumno_Edicion.SetSelection(0)
        elif datosAlumno["otraAgrupacionDatosMusicales"]=='No':
            self.txtNombreOtraAgrupAlumno_Edicion.Enable(False)
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.Enable(False)
            self.radioOtraAgrupAlumno_Edicion.SetSelection(1)

        self.txtNombreOtraAgrupAlumno_Edicion.SetValue(datosAlumno["nombreOtraAgrupacionDatosMusicales"])

        if datosAlumno["fechaIngresoOtraDatosMusicales"] != None:
            aIOtra,mIOtra,dIOtra=map(int, datosAlumno["fechaIngresoOtraDatosMusicales"].split('-'))
            ingreso_otra=wx.DateTimeFromDMY(dIOtra,mIOtra-1,aIOtra)
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.SetValue(ingreso_otra)


        #FICHA MEDICA
        self.txtFMedTipoSangreAlumno_Edicion.SetValue(datosAlumno["tipoSangreFichaMedica"])
        self.txtFMedAntecedAlumno_Edicion.SetValue(datosAlumno["antGeneralesFichaMedica"])

        if datosAlumno["vacunaFAmarilla"]=='Si':
            self.radioFMedVacFA_Edicion.SetSelection(0)
            self.datePickerFMedVacFA_Edicion.Enable(True)
        elif datosAlumno["vacunaFAmarilla"]=='No':
            self.radioFMedVacFA_Edicion.SetSelection(1)
            self.datePickerFMedVacFA_Edicion.Enable(False)

        if datosAlumno["fechaVacunaFAmarilla"] != None:
            aFA,mFA,dFA=map(int, datosAlumno["fechaVacunaFAmarilla"].split('-'))
            fecha_FA=wx.DateTimeFromDMY(dFA,mFA-1,aFA)
            self.datePickerFMedVacFA_Edicion.SetValue(fecha_FA)

        if datosAlumno["vacunaHepatitisA"]=='Si':
            self.radioFMedVacHA_Edicion.SetSelection(0)
            self.datePickerFMedVacHA_Edicion.Enable(True)
        elif datosAlumno["vacunaHepatitisA"]=='No':
            self.radioFMedVacHA_Edicion.SetSelection(1)
            self.datePickerFMedVacHA_Edicion.Enable(False)

        if datosAlumno["fechaVacunaHepatitisA"] != None:
            aHA,mHA,dHA=map(int, datosAlumno["fechaVacunaHepatitisA"].split('-'))
            fecha_HA=wx.DateTimeFromDMY(dHA,mHA-1,aHA)
            self.datePickerFMedVacHA_Edicion.SetValue(fecha_HA)

        if datosAlumno["vacunaHepatitisB"]=='Si':
            self.radioFMedVacHB_Edicion.SetSelection(0)
            self.datePickerFMedVacHB_Edicion.Enable(True)
        elif datosAlumno["vacunaHepatitisB"]=='No':
            self.radioFMedVacHB_Edicion.SetSelection(1)
            self.datePickerFMedVacHB_Edicion.Enable(False)

        if datosAlumno["fechaVacunaHepatitisB"] != None:
            aHB,mHB,dHB=map(int, datosAlumno["fechaVacunaHepatitisB"].split('-'))
            fecha_HB=wx.DateTimeFromDMY(dHB,mHB-1,aHB)
            self.datePickerFMedVacHB_Edicion.SetValue(fecha_HB)

        if datosAlumno["enfCabeza"]=='Si':
            self.radioFMedEnfCab_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfCab_Edicion.SetSelection(1)

        if datosAlumno["enfOido"]=='Si':
            self.radioFMedEnfOid_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfOid_Edicion.SetSelection(1)

        if datosAlumno["enfNariz"]=='Si':
            self.radioFMedEnfNar_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfNar_Edicion.SetSelection(1)

        if datosAlumno["enfGarganta"]=='Si':
            self.radioFMedEnfGar_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfGar_Edicion.SetSelection(1)

        if datosAlumno["enfCorazon"]=='Si':
            self.radioFMedEnfCor_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfCor_Edicion.SetSelection(1)

        if datosAlumno["enfPulmones"]=='Si':
            self.radioFMedEnfPul_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfPul_Edicion.SetSelection(1)

        if datosAlumno["enfViaDigestiva"]=='Si':
            self.radioFMedEnfVD_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfVD_Edicion.SetSelection(1)

        if datosAlumno["enfRiniones"]=='Si':
            self.radioFMedEnfRi_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfRi_Edicion.SetSelection(1)

        if datosAlumno["enfHuesos"]=='Si':
            self.radioFMedEnfHue_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfHue_Edicion.SetSelection(1)

        if datosAlumno["enfArticulaciones"]=='Si':
            self.radioFMedEnfArt_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfArt_Edicion.SetSelection(1)

        if datosAlumno["enfEndocrino"]=='Si':
            self.radioFMedEnfEnd_Edicion.SetSelection(0)
        else:
            self.radioFMedEnfEnd_Edicion.SetSelection(1)

        self.txtFMedOperaciones_Edicion.SetValue(datosAlumno["operaciones"])
        self.txtFMedAlerCom_Edicion.SetValue(datosAlumno["alergiaComida"])
        self.txtFMedAlerMed_Edicion.SetValue(datosAlumno["alergiaMedicamentos"])
        self.txtFMedAlerMedEsp_Edicion.SetValue(datosAlumno["medicamentoEspecifico"])

        if datosAlumno["seguroMedico"]=='Si':
            self.radioFMedTieneSeguro_Edicion.SetSelection(0)
            self.txtFMedAseg_Edicion.Enable(True)
            self.txtFMedTelAseg_Edicion.Enable(True)
        elif datosAlumno["seguroMedico"]=='No':
            self.radioFMedTieneSeguro_Edicion.SetSelection(1)
            self.txtFMedAseg_Edicion.Enable(False)
            self.txtFMedTelAseg_Edicion.Enable(False)

        self.txtFMedAseg_Edicion.SetValue(datosAlumno["aseguradora"])
        self.txtFMedTelAseg_Edicion.SetValue(datosAlumno["telefonoAseguradora"])
        self.txtFMedTelEmerg_Edicion.SetValue(datosAlumno["numeroEmergencia"])
        self.txtFMedUnidadMedPref_Edicion.SetValue(datosAlumno["unidadMedicaPreferencia"])
        self.txtFMedTratante_Edicion.SetValue(datosAlumno["medicoTratante"])
        self.txtFMedTelTratante_Edicion.SetValue(datosAlumno["telefonoMedicoTratante"])
        self.txtFMedCelTratante_Edicion.SetValue(datosAlumno["telefonoCelMedicoTratante"])
        self.txtFMedEnfPrevia_Edicion.SetValue(datosAlumno["otraEnfermedadCondicion"])
        self.txtFMedAperato_Edicion.SetValue(datosAlumno["aparatoquipoMedico"])

    def m_choiceNomAlumnoOnChoice( self, event ):
        for i in range(self.checkCatedras_edicion.GetCount()):
            self.checkCatedras_edicion.Check(i, check=False)

        if not self.m_choiceNomAlumno.GetCurrentSelection()==0:
            self.cargarDatosALumno()
            self.btnFoto_Edicion.Enable(True)
        else:
            #DESACTIVAR CONTROLES
            self.btnFoto_Edicion.Enable(False)
            self.radioEducacionAlumno_Edicion.Enable(True)
            self.txtGradoAlumno_Edicion.Enable(True)
            self.txtAnioAlumno_Edicion.Enable(True)
            self.txtSemestreAlumno_Edicion.Enable(True)
            self.txtInstitAlumno_Edicion.Enable(True)
            self.txtDireccionInstitAlumno_Edicion.Enable(True)
            self.txtTelefonoInstitAlumno_Edicion.Enable(True)
            self.radioTipoInstitAlumno_Edicion.Enable(True)
            self.txtNombreOtraAgrupAlumno_Edicion.Enable(True)
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.Enable(True)
            self.datepickerFecAsigInstAlumno_Edicion.Enable(True)
            self.txtNumActFijoInstAlumno_Edicion.Enable(True)
            self.datePickerFMedVacFA_Edicion.Enable(True)
            self.datePickerFMedVacHA_Edicion.Enable(True)
            self.datePickerFMedVacHB_Edicion.Enable(True)
            self.txtFMedAseg_Edicion.Enable(True)
            self.txtFMedTelAseg_Edicion.Enable(True)
            #LIMPIAR CAMPOS
            #DATOS GENERALES
            self.bitmapFoto.SetBitmap(wx.Bitmap( fotoVacia, wx.BITMAP_TYPE_ANY ))
            self.txtNomAlumno_Edicion.Clear()
            self.txtApeAlumno_Edicion.Clear()
            self.txtCiAlumno_Edicion.Clear()
            self.datePickerFechaNacAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFechaIngAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.txtLugarNacAlumno_Edicion.Clear()
            self.radioSexoAlumno_Edicion.SetSelection(0)
            self.txtEdadAlumno_Edicion.Clear()
            self.txtDirTelHabAlumno_Edicion.Clear()
            self.txtDirTelCelAlumno_Edicion.Clear()
            self.txtDirEmailalumno_Edicion.Clear()

            #DIRECCION
            self.txtDirMunicipioAlumno_Edicion.Clear()
            self.txtDirParroquiaAlumno_Edicion.Clear()
            self.txtDirSectorAlumno_Edicion.Clear()
            self.txtDirUrbarrioAlumno_Edicion.Clear()
            self.txtDirAvenidaAlumno_Edicion.Clear()
            self.txtDirCalleAlumno_Edicion.Clear()
            self.txtDirEdificioAlumno_Edicion.Clear()
            self.txtDirCasaAptoAlumno_Edicion.Clear()
            self.txtDirPtoRefAlumno_Edicion.Clear()

            #REPRESENTANTE
            self.txtNombreRepAlumno_Edicion.Clear()
            self.txtApeRepAlumno_Edicion.Clear()
            self.txtCiRep_Edicion.Clear()
            self.txtDirHabRep_Edicion.Clear()
            self.txtTelHabRep_Edicion.Clear()
            self.txtTelCelRep_Edicion.Clear()
            self.txtEmailRep_Edicion.Clear()
            self.txtDirTrabajoRep_Edicion.Clear()
            self.txtTelTrabajoRep_Edicion.Clear()
            self.txtOcupacionRep_Edicion.Clear()
            self.txtParentescoRep_Edicion.Clear()

            #ACADEMICOS
            self.radioEstudiaAlumno_Edicion.SetSelection(0)
            self.radioEducacionAlumno_Edicion.SetSelection(0)
            self.txtGradoAlumno_Edicion.Clear()
            self.txtAnioAlumno_Edicion.Clear()
            self.txtSemestreAlumno_Edicion.Clear()
            self.txtInstitAlumno_Edicion.Clear()
            self.txtDireccionInstitAlumno_Edicion.Clear()
            self.txtTelefonoInstitAlumno_Edicion.Clear()
            self.radioTipoInstitAlumno_Edicion.SetSelection(0)

            #MUSICAL
            self.radioConocMusAlumno_Edicion.SetSelection(0)
            self.choiceOrquAlumno_Edicion.SetSelection(0)
            self.txtNivelOrqAlumno_Edicion.Clear()
            self.radioInstPropioAlumno_Edicion.SetSelection(0)
            self.datepickerFecAsigInstAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.txtMarcaInstAlumno_Edicion.Clear()
            self.txtModeloInstAlumno_Edicion.Clear()
            self.txtSerialInstAlumno_Edicion.Clear()
            self.txtNumActFijoInstAlumno_Edicion.Clear()
            self.txtProfAlumno_Edicion.Clear()
            self.radioOtraAgrupAlumno_Edicion.SetSelection(0)
            self.txtNombreOtraAgrupAlumno_Edicion.Clear()
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.SetValue(wx.DateTime.Today())

            #FICHA MEDICA
            self.txtFMedTipoSangreAlumno_Edicion.Clear()
            self.txtFMedAntecedAlumno_Edicion.Clear()
            self.radioFMedVacFA_Edicion.SetSelection(0)
            self.datePickerFMedVacFA_Edicion.SetValue(wx.DateTime.Today())
            self.radioFMedVacHA_Edicion.SetSelection(0)
            self.datePickerFMedVacHA_Edicion.SetValue(wx.DateTime.Today())
            self.radioFMedVacHB_Edicion.SetSelection(0)
            self.datePickerFMedVacHB_Edicion.SetValue(wx.DateTime.Today())
            self.radioFMedEnfCab_Edicion.SetSelection(1)
            self.radioFMedEnfOid_Edicion.SetSelection(1)
            self.radioFMedEnfNar_Edicion.SetSelection(1)
            self.radioFMedEnfGar_Edicion.SetSelection(1)
            self.radioFMedEnfCor_Edicion.SetSelection(1)
            self.radioFMedEnfPul_Edicion.SetSelection(1)
            self.radioFMedEnfVD_Edicion.SetSelection(1)
            self.radioFMedEnfRi_Edicion.SetSelection(1)
            self.radioFMedEnfHue_Edicion.SetSelection(1)
            self.radioFMedEnfArt_Edicion.SetSelection(1)
            self.radioFMedEnfEnd_Edicion.SetSelection(1)
            self.txtFMedOperaciones_Edicion.Clear()
            self.txtFMedAlerCom_Edicion.Clear()
            self.txtFMedAlerMed_Edicion.Clear()
            self.txtFMedAlerMedEsp_Edicion.Clear()
            self.radioFMedTieneSeguro_Edicion.SetSelection(0)
            self.txtFMedAseg_Edicion.Clear()
            self.txtFMedTelAseg_Edicion.Clear()
            self.txtFMedTelEmerg_Edicion.Clear()
            self.txtFMedUnidadMedPref_Edicion.Clear()
            self.txtFMedTratante_Edicion.Clear()
            self.txtFMedTelTratante_Edicion.Clear()
            self.txtFMedCelTratante_Edicion.Clear()
            self.txtFMedEnfPrevia_Edicion.Clear()
            self.txtFMedAperato_Edicion.Clear()

    def preCargaRadios(self):
        """
        Inicializaciones Varias del Panel de Edicion de alumnos
        """

        now=datetime.now()
        self.date_str = now.strftime("%Y-%m-%d_%H%M%S")

        self.btnFoto_Edicion.Enable(False)
        self.txtNumActFijoInstAlumno_Edicion.Enable(False)
        self.datepickerFecAsigInstAlumno_Edicion.Enable(False)
        self.txtEdadAlumno_Edicion.SetEditable(False)

    def datePickerFechaNacAlumno_EdicionOnDateChanged(self, event):
        """
        Calculo automatico de la edad del alumno segun su fecha de Nacimiento
        """

        anio_actual=date.today().year
        anio_nacimiento=self.datePickerFechaNacAlumno_Edicion.GetValue().GetYear()
        edad=anio_actual-anio_nacimiento
        if edad >= 5:
            self.txtEdadAlumno_Edicion.SetValue(str(anio_actual-anio_nacimiento))
            return True
        else:
            self.txtEdadAlumno_Edicion.Clear()
            return False


    def radioEstudiaAlumno_EdicionOnRadioBox(self, event):
        """
        Activacion / Desactivacion de diferentes controles segun el alumno estudie o no
        """
        if self.radioEstudiaAlumno_Edicion.GetStringSelection()=='No':
            self.txtGradoAlumno_Edicion.Clear()
            self.txtAnioAlumno_Edicion.Clear()
            self.txtSemestreAlumno_Edicion.Clear()
            self.txtInstitAlumno_Edicion.Clear()
            self.txtDireccionInstitAlumno_Edicion.Clear()
            self.txtTelefonoInstitAlumno_Edicion.Clear()

            self.radioEducacionAlumno_Edicion.Enable(False)
            self.txtGradoAlumno_Edicion.Enable(False)
            self.txtAnioAlumno_Edicion.Enable(False)
            self.txtSemestreAlumno_Edicion.Enable(False)
            self.txtInstitAlumno_Edicion.Enable(False)
            self.txtDireccionInstitAlumno_Edicion.Enable(False)
            self.txtTelefonoInstitAlumno_Edicion.Enable(False)
            self.radioTipoInstitAlumno_Edicion.Enable(False)

        elif self.radioEstudiaAlumno_Edicion.GetStringSelection()=='Si':
            self.txtGradoAlumno_Edicion.Clear()
            self.txtAnioAlumno_Edicion.Clear()
            self.txtSemestreAlumno_Edicion.Clear()
            self.txtInstitAlumno_Edicion.Clear()
            self.txtDireccionInstitAlumno_Edicion.Clear()
            self.txtTelefonoInstitAlumno_Edicion.Clear()

            self.radioEducacionAlumno_Edicion.Enable(True)
            self.txtGradoAlumno_Edicion.Enable(True)
            self.txtAnioAlumno_Edicion.Enable(True)
            self.txtSemestreAlumno_Edicion.Enable(True)
            self.txtInstitAlumno_Edicion.Enable(True)
            self.txtDireccionInstitAlumno_Edicion.Enable(True)
            self.txtTelefonoInstitAlumno_Edicion.Enable(True)
            self.radioTipoInstitAlumno_Edicion.Enable(True)


    def radioInstPropioAlumno_EdicionOnRadioBox(self, event):
        """
        Activacion / Desactivacion de diferentes controles segun el alumno estudie tenga instrumento propio o no
        """

        if self.radioInstPropioAlumno_Edicion.GetStringSelection()=='No':
            self.datepickerFecAsigInstAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.datepickerFecAsigInstAlumno_Edicion.Enable(True)
            self.txtNumActFijoInstAlumno_Edicion.Clear()
            self.txtNumActFijoInstAlumno_Edicion.Enable(True)
        elif self.radioInstPropioAlumno_Edicion.GetStringSelection()=='Si':
            self.datepickerFecAsigInstAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.datepickerFecAsigInstAlumno_Edicion.Enable(False)
            self.txtNumActFijoInstAlumno_Edicion.Enable(False)
            self.txtNumActFijoInstAlumno_Edicion.Clear()


    def radioOtraAgrupAlumno_EdicionOnRadioBox(self, event):
        """
        Activacion / Desactivacion de diferentes controles segun el alumno pertenezca a otra agrupacion  o no
        """

        if self.radioOtraAgrupAlumno_Edicion.GetStringSelection()=='No':
            self.txtNombreOtraAgrupAlumno_Edicion.Clear()
            self.txtNombreOtraAgrupAlumno_Edicion.Enable(False)
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.Enable(False)
        elif self.radioOtraAgrupAlumno_Edicion.GetStringSelection()=='Si':
            self.txtNombreOtraAgrupAlumno_Edicion.Clear()
            self.txtNombreOtraAgrupAlumno_Edicion.Enable(True)
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFechaIngOtraAgrupAlumno_Edicion.Enable(True)


    #ACTIVACION / DESACTIVACION DE DIFERENTES CONTROLES SEGUN LAS VACUNAS QUE TENGA EL ALUMNO

    def radioFMedVacFA_EdicionOnRadioBox( self, event ):
        if self.radioFMedVacFA_Edicion.GetStringSelection()=='No':
            self.datePickerFMedVacFA_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacFA_Edicion.Enable(False)
        elif self.radioFMedVacFA_Edicion.GetStringSelection()=='Si':
            self.datePickerFMedVacFA_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacFA_Edicion.Enable(True)


    def radioFMedVacHA_EdicionOnRadioBox( self, event ):
        if self.radioFMedVacHA_Edicion.GetStringSelection()=='No':
            self.datePickerFMedVacHA_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHA_Edicion.Enable(False)
        elif self.radioFMedVacHA_Edicion.GetStringSelection()=='Si':
            self.datePickerFMedVacHA_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHA_Edicion.Enable(True)


    def radioFMedVacHB_EdicionOnRadioBox( self, event ):
        if self.radioFMedVacHB_Edicion.GetStringSelection()=='No':
            self.datePickerFMedVacHB_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHB_Edicion.Enable(False)
        elif self.radioFMedVacHB_Edicion.GetStringSelection()=='Si':
            self.datePickerFMedVacHB_Edicion.SetValue(wx.DateTime.Today())
            self.datePickerFMedVacHB_Edicion.Enable(True)


    def radioFMedTieneSeguro_EdicionOnRadioBox( self, event ):
        if self.radioFMedTieneSeguro_Edicion.GetStringSelection()=='No':
            self.txtFMedAseg_Edicion.Clear()
            self.txtFMedAseg_Edicion.Enable(False)
            self.txtFMedTelAseg_Edicion.Enable(False)
        elif self.radioFMedTieneSeguro_Edicion.GetStringSelection()=='Si':
            self.txtFMedAseg_Edicion.Clear()
            self.txtFMedAseg_Edicion.Enable(True)
            self.txtFMedTelAseg_Edicion.Enable(True)


    def sdbSizerBtnGuardarOnApplyButtonClick( self, event):
        """
        Acciones al Editar el Alumno en el Sistema
        """

        if not self.m_choiceNomAlumno.GetCurrentSelection()==0 or self.flag:

            if self.radioEstudiaAlumno_Edicion.GetStringSelection()=='No':
                self.EducacionAlumno_Edicion=None
                self.TipoInstitAlumno_Edicion=None
                self.txtGradoAlumno_Edicion.SetValue('')
                self.txtAnioAlumno_Edicion.SetValue('')
                self.txtSemestreAlumno_Edicion.SetValue('')
                self.txtInstitAlumno_Edicion.SetValue('')
                self.txtDireccionInstitAlumno_Edicion.SetValue('')
                self.txtTelefonoInstitAlumno_Edicion.SetValue('')
            else:
                self.EducacionAlumno_Edicion=self.radioEducacionAlumno_Edicion.GetStringSelection()
                self.TipoInstitAlumno_Edicion=self.radioTipoInstitAlumno_Edicion.GetStringSelection()


            if self.radioInstPropioAlumno_Edicion.GetStringSelection()=='Si':
                self.FecAsigInstAlumno_Edicion=None
            else:
                self.FecAsigInstAlumno_Edicion=self.datepickerFecAsigInstAlumno_Edicion.GetValue().Format('%Y-%m-%d')


            if self.radioOtraAgrupAlumno_Edicion.GetStringSelection()=='No':
                self.FechaIngOtraAgrupAlumno_Edicion=None
            else:
                self.FechaIngOtraAgrupAlumno_Edicion=self.datePickerFechaIngOtraAgrupAlumno_Edicion.GetValue().Format('%Y-%m-%d')


            if self.radioFMedVacFA_Edicion.GetStringSelection()=='No':
                self.FMedVacFA_Edicion=None
            elif self.radioFMedVacFA_Edicion.GetStringSelection()=='Si':
                self.FMedVacFA_Edicion=self.datePickerFMedVacFA_Edicion.GetValue().Format('%Y-%m-%d')


            if self.radioFMedVacHA_Edicion.GetStringSelection()=='No':
                self.FMedVacHA_Edicion=None
            elif self.radioFMedVacHA_Edicion.GetStringSelection()=='Si':
                self.FMedVacHA_Edicion=self.datePickerFMedVacHA_Edicion.GetValue().Format('%Y-%m-%d')


            if self.radioFMedVacHB_Edicion.GetStringSelection()=='No':
                self.FMedVacHB_Edicion=None
            elif self.radioFMedVacHB_Edicion.GetStringSelection()=='Si':
                self.FMedVacHB_Edicion=self.datePickerFMedVacHB_Edicion.GetValue().Format('%Y-%m-%d')


            if self.radioFMedTieneSeguro_Edicion.GetStringSelection()=='No':
                self.txtFMedAseg_Edicion.SetValue('')
                self.txtFMedTelAseg_Edicion.SetValue('')


            #INICIAMOS VALIDADOR
            self.validator=NotEmptyValidator()

            #VALIDAMOS NOMBRE
            self.validator.SetWindow(self.txtNomAlumno_Edicion)
            if self.validator.Validate(self.txtNomAlumno_Edicion):
                validaNombre=True
            else:
                validaNombre=False

            #VALIDAMOS APELLIDO
            self.validator.SetWindow(self.txtApeAlumno_Edicion)
            if self.validator.Validate(self.txtApeAlumno_Edicion):
                validaApe=True
            else:
                validaApe=False

            #VALIDAMOS LUGAR DE NACIMIENTO
            self.validator.SetWindow(self.txtLugarNacAlumno_Edicion)
            if self.validator.Validate(self.txtLugarNacAlumno_Edicion):
                validaLugarNac=True
            else:
                validaLugarNac=False

            #VALIDAMOS FECHA DE INGRESO
            self.validator.SetWindow(self.datePickerFechaIngAlumno_Edicion)
            if self.validator.Validate(self.datePickerFechaIngAlumno_Edicion):
                validaFecIngreso=True
            else:
                validaFecIngreso=False

            #VALIDAMOS NOMBRE DE REPRESENTANTE
            self.validator.SetWindow(self.txtNombreRepAlumno_Edicion)
            if self.validator.Validate(self.txtNombreRepAlumno_Edicion):
                validaNomRep=True
            else:
                validaNomRep=False

            #VALIDAMOS APELLIDO REPRESENTANTE
            self.validator.SetWindow(self.txtApeRepAlumno_Edicion)
            if self.validator.Validate(self.txtApeRepAlumno_Edicion):
                validaApeRep=True
            else:
                validaApeRep=False

            #VALIDAMOS CEDULA DE REPRESENTANTE
            self.validator.SetWindow(self.txtCiRep_Edicion)
            if self.validator.Validate(self.txtCiRep_Edicion):
                validaCiRep=True
            else:
                validaCiRep=False

            #VALIDAMOS DIRECION REPRESENTANTE
            self.validator.SetWindow(self.txtDirHabRep_Edicion)
            if self.validator.Validate(self.txtDirHabRep_Edicion):
                validaDirRep=True
            else:
                validaDirRep=False

            #VALIDAMOS PARENTEZCO RERESENTANTE
            self.validator.SetWindow(self.txtParentescoRep_Edicion)
            if self.validator.Validate(self.txtParentescoRep_Edicion):
                validaParentRep=True
            else:
                validaParentRep=False

            #VALIDAMOS ORQUESTA
            self.validator.SetWindow(self.choiceOrquAlumno_Edicion)
            if self.validator.Validate(self.choiceOrquAlumno_Edicion):
                validaOrqAlumno=True
            else:
                validaOrqAlumno=False

            #VALIDAMOS MARCA INSTRUMENTO
            self.validator.SetWindow(self.txtMarcaInstAlumno_Edicion)
            if self.validator.Validate(self.txtMarcaInstAlumno_Edicion):
                validaMarcaInst=True
            else:
                validaMarcaInst=False


            #VALIDAMOS MODELO INSTRUMENTO
            self.validator.SetWindow(self.txtModeloInstAlumno_Edicion)
            if self.validator.Validate(self.txtModeloInstAlumno_Edicion):
                validaModeloInst=True
            else:
                validaModeloInst=False

            #VALIDAMOS SERIAL INSTRUMENTO
            self.validator.SetWindow(self.txtSerialInstAlumno_Edicion)
            if self.validator.Validate(self.txtSerialInstAlumno_Edicion):
                validaSerialInst=True
            else:
                validaSerialInst=False

            #VALIDAMOS PROFESOR
            self.validator.SetWindow(self.txtProfAlumno_Edicion)
            if self.validator.Validate(self.txtProfAlumno_Edicion):
                validaProf=True
            else:
                validaProf=False

            if (validaNombre and validaApe and validaLugarNac and validaNomRep and validaApeRep
                and validaCiRep and validaDirRep and validaParentRep and validaMarcaInst and validaModeloInst and
                validaSerialInst and validaProf and validaOrqAlumno and validaFecIngreso):
                if self.txtEdadAlumno_Edicion.GetValue() != '':
                    num_elementos_seleccionados = 0
                    for item in range(self.checkCatedras_edicion.GetCount()):
                        if self.checkCatedras_edicion.IsChecked(item):
                            num_elementos_seleccionados = num_elementos_seleccionados+1
                    if num_elementos_seleccionados > 0:
                        try:
                            self.labels=[]
                            self.elemento=''
                            for i in range(self.checkCatedras_edicion.GetCount()):
                                if self.checkCatedras_edicion.IsChecked(i):
                                    self.labels.append(self.checkCatedras_edicion.GetString(i))

                            for item in self.labels:
                                self.elemento=self.elemento+','+item

                            app.BD.actualizarAlumno(self.alumnoID, string.capwords(self.txtNomAlumno_Edicion.GetValue()),
                                string.capwords(self.txtApeAlumno_Edicion.GetValue()),
                                self.txtCiAlumno_Edicion.GetValue(),
                                self.datePickerFechaNacAlumno_Edicion.GetValue().Format('%Y-%m-%d'),
                                self.datePickerFechaIngAlumno_Edicion.GetValue().Format('%Y-%m-%d'),
                                string.capitalize(self.txtLugarNacAlumno_Edicion.GetValue()),
                                self.radioSexoAlumno_Edicion.GetStringSelection(),
                                self.txtEdadAlumno_Edicion.GetValue(),
                                self.txtDirTelHabAlumno_Edicion.GetValue(),
                                self.txtDirTelCelAlumno_Edicion.GetValue(),
                                self.txtDirEmailalumno_Edicion.GetValue(),
                                string.capwords(self.txtDirMunicipioAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirParroquiaAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirSectorAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirUrbarrioAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirAvenidaAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirCalleAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirEdificioAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirCasaAptoAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDirPtoRefAlumno_Edicion.GetValue()),
                                string.capwords(self.txtNombreRepAlumno_Edicion.GetValue()),
                                string.capwords(self.txtApeRepAlumno_Edicion.GetValue()),
                                self.txtCiRep_Edicion.GetValue(),
                                string.capitalize(self.txtDirHabRep_Edicion.GetValue()),
                                self.txtTelHabRep_Edicion.GetValue(),
                                self.txtTelCelRep_Edicion.GetValue(),
                                self.txtEmailRep_Edicion.GetValue(),
                                string.capitalize(self.txtDirTrabajoRep_Edicion.GetValue()),
                                self.txtTelTrabajoRep_Edicion.GetValue(),
                                string.capitalize(self.txtOcupacionRep_Edicion.GetValue()),
                                string.capitalize(self.txtParentescoRep_Edicion.GetValue()),
                                self.radioEstudiaAlumno_Edicion.GetStringSelection(),
                                self.EducacionAlumno_Edicion,
                                self.txtGradoAlumno_Edicion.GetValue(),
                                self.txtAnioAlumno_Edicion.GetValue(),
                                self.txtSemestreAlumno_Edicion.GetValue(),
                                string.capwords(self.txtInstitAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtDireccionInstitAlumno_Edicion.GetValue()),
                                self.txtTelefonoInstitAlumno_Edicion.GetValue(),
                                self.TipoInstitAlumno_Edicion,
                                self.radioConocMusAlumno_Edicion.GetStringSelection(),
                                self.elemento[1:],
                                self.choiceOrquAlumno_Edicion.GetStringSelection(),
                                string.capitalize(self.txtNivelOrqAlumno_Edicion.GetValue()),
                                self.radioInstPropioAlumno_Edicion.GetStringSelection(),
                                self.FecAsigInstAlumno_Edicion,
                                string.capitalize(self.txtMarcaInstAlumno_Edicion.GetValue()),
                                string.capitalize(self.txtModeloInstAlumno_Edicion.GetValue()),
                                self.txtSerialInstAlumno_Edicion.GetValue(),
                                self.txtNumActFijoInstAlumno_Edicion.GetValue(),
                                string.capwords(self.txtProfAlumno_Edicion.GetValue()),
                                self.choiceStatusAlumno_Edicion.GetStringSelection(),
                                self.radioOtraAgrupAlumno_Edicion.GetStringSelection(),
                                string.capwords(self.txtNombreOtraAgrupAlumno_Edicion.GetValue()),
                                self.FechaIngOtraAgrupAlumno_Edicion,
                                self.txtFMedTipoSangreAlumno_Edicion.GetValue(),
                                string.capitalize(self.txtFMedAntecedAlumno_Edicion.GetValue()),
                                self.radioFMedVacFA_Edicion.GetStringSelection(),
                                self.FMedVacFA_Edicion,
                                self.radioFMedVacHA_Edicion.GetStringSelection(),
                                self.FMedVacHA_Edicion,
                                self.radioFMedVacHB_Edicion.GetStringSelection(),
                                self.FMedVacHB_Edicion,
                                self.radioFMedEnfCab_Edicion.GetStringSelection(),
                                self.radioFMedEnfOid_Edicion.GetStringSelection(),
                                self.radioFMedEnfNar_Edicion.GetStringSelection(),
                                self.radioFMedEnfGar_Edicion.GetStringSelection(),
                                self.radioFMedEnfCor_Edicion.GetStringSelection(),
                                self.radioFMedEnfPul_Edicion.GetStringSelection(),
                                self.radioFMedEnfVD_Edicion.GetStringSelection(),
                                self.radioFMedEnfRi_Edicion.GetStringSelection(),
                                self.radioFMedEnfHue_Edicion.GetStringSelection(),
                                self.radioFMedEnfArt_Edicion.GetStringSelection(),
                                self.radioFMedEnfEnd_Edicion.GetStringSelection(),
                                string.capitalize(self.txtFMedOperaciones_Edicion.GetValue()),
                                self.txtFMedAlerCom_Edicion.GetValue(),
                                self.txtFMedAlerMed_Edicion.GetValue(),
                                string.capitalize(self.txtFMedAlerMedEsp_Edicion.GetValue()),
                                self.radioFMedTieneSeguro_Edicion.GetStringSelection(),
                                string.capitalize(self.txtFMedAseg_Edicion.GetValue()),
                                string.capitalize(self.txtFMedTelAseg_Edicion.GetValue()),
                                self.txtFMedTelEmerg_Edicion.GetValue(),
                                string.capwords(self.txtFMedUnidadMedPref_Edicion.GetValue()),
                                string.capwords(self.txtFMedTratante_Edicion.GetValue()),
                                self.txtFMedTelTratante_Edicion.GetValue(),
                                self.txtFMedCelTratante_Edicion.GetValue(),
                                string.capitalize(self.txtFMedEnfPrevia_Edicion.GetValue()),
                                string.capitalize(self.txtFMedAperato_Edicion.GetValue()),
                                self.fotoEditar)
                            mensaje=wx.MessageDialog(self,u'Alumno Actualizado \n\n',"Guardando", wx.OK|wx.ICON_INFORMATION)
                            mensaje.ShowModal()
                            self.editado=True
                            self.GetParent().limpiarPantalla()
                            self.txtApeAlumno_Edicion.SetFocus()
                            app.limpiarFotos()
                            self.fotoEditar=None
                            num_elementos_seleccionados=0
                        except lite.Error, e:
                            #error, sacamos dialogo y decimos que hagan configuracion
                            exc_type, exc_value, exc_traceback = sys.exc_info()
                            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                            logging.error('%s - [%s]'%(e, trace))
                            mensaje=wx.MessageDialog(self,u'Error: \n\n%s'%e,"Error", wx.OK|wx.ICON_HAND)
                            mensaje.ShowModal()
                            self.editado=False
                        num_elementos_seleccionados=0
                    else:
                        mensaje=wx.MessageDialog(self,u'Error: Debe Seleccionar una Cátedra\n\n',"Error", wx.OK|wx.ICON_HAND)
                        mensaje.ShowModal()
                        self.editado=False
                else:
                    mensaje=wx.MessageDialog(self,u'Error: La Edad debe ser mayor o igual a 5 Años\n\n',"Error", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.editado=False
            else:
                if self.notebookAlumno.GetSelection != 0:
                    self.notebookAlumno.SetSelection(0)
                self.txtApeAlumno_Edicion.SetFocus()
                mensaje=wx.MessageDialog(self,u'Los Campos Resaltados son Obligatorios',"Error", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
                self.editado=False
        else:
            mensaje=wx.MessageDialog(self,u'Debe Escojer un Alumno',u'Error', wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.editado=False



class busquedaAlumnos(FrameBusqueda):

    """
    clase destinada a manejar todo lo referente a la Eliminacion de Profesores
    """

    def searchAlumnoCtrlOnEnterWindow( self, event ):
        self.m_statusBarElim.SetStatusText(u"Ingrese el nombre, apellido o cédula del alumno a buscar")


    def iniciarListaAlumnos(self):
        app.IconizarFrames(self)

        #Damos formato a la lista
        self.sizerListaAlumnos = wx.BoxSizer(wx.VERTICAL)
        self.panelListaAlumnos.SetSizer( self.sizerListaAlumnos)

        self.ListadoAlumnos  = CheckListCtrl(self.panelListaAlumnos)
        self.ListadoAlumnos.InsertColumn(0, u'ID')
        self.ListadoAlumnos.InsertColumn(1, 'Nombre')
        self.ListadoAlumnos.InsertColumn(2, 'Apellido')
        self.ListadoAlumnos.InsertColumn(3, u'Cédula de Identidad')

        self.ListadoAlumnos.SetColumnWidth(0, 150)
        self.ListadoAlumnos.SetColumnWidth(1, 150)
        self.ListadoAlumnos.SetColumnWidth(2, 150)
        self.ListadoAlumnos.SetColumnWidth(3, 150)

        self.sizerListaAlumnos.Add(self.ListadoAlumnos, 1, wx.EXPAND | wx.TOP, 3)
        self.panelListaAlumnos.Layout()
        self.ListadoAlumnos.Layout()
        self.ListadoAlumnos.Refresh()

    def cargarListadoDeAlumnos(self):
        if self.searchAlumnoCtrl.IsEmpty():
            todos=True
            lista=app.BD.listarAlumnos()
        else:
            todos=False
            lista=app.BD.buscarAlumno(self.searchAlumnoCtrl.GetValue())

        if not lista==[]:
            #Cargamos en la lista, el listado de usuarios obtenidos de la app.BD
            self.ListadoAlumnos.Layout()
            if todos:
                for item in lista:
                    index = self.ListadoAlumnos.InsertStringItem(sys.maxint, str(item[0]))
                    self.ListadoAlumnos.SetStringItem(index, 1, item[1])
                    self.ListadoAlumnos.SetStringItem(index, 2, item[2])
                    self.ListadoAlumnos.SetStringItem(index, 3, item[3])
                self.searchAlumnoCtrl.Clear()
            else:
                for item in lista:
                    index = self.ListadoAlumnos.InsertStringItem(sys.maxint, str(item[0]))
                    self.ListadoAlumnos.SetStringItem(index, 1, item[1])
                    self.ListadoAlumnos.SetStringItem(index, 2, item[2])
                    self.ListadoAlumnos.SetStringItem(index, 3, item[3])
                self.searchAlumnoCtrl.Clear()
        else:
            self.ListadoAlumnos.DeleteAllItems()
            mensaje=wx.MessageDialog(self,'No hay Resultados Coincidentes..!!',"Busqueda", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

    def FrameBusquedaOnClose(self, event):
        self.MakeModal(False)
        self.Destroy()


    def btnCancelElimUsuOnButtonClick( self, event ):
        self.MakeModal(False)
        self.Destroy()


    def btnSelTODOOnButtonClick( self, event ):
        num = self.ListadoAlumnos.GetItemCount()
        for i in range(num):
            self.ListadoAlumnos.CheckItem(i)


    def btnDeSelTODOOnButtonClick( self, event ):
        num = self.ListadoAlumnos.GetItemCount()
        for i in range(num):
            self.ListadoAlumnos.CheckItem(i, False)


    def btnElimAlumnoOnButtonClick( self, event ):
        listaBorrar=[]
        num = self.ListadoAlumnos.GetItemCount()
        if num != 0:
            for i in range(num):
                if self.ListadoAlumnos.IsChecked(i):
                    listaBorrar.append(i)
            sorted(listaBorrar)
            listaBorrar.reverse()
            for j in listaBorrar:
                    item= self.ListadoAlumnos.GetItemText(j)
                    nombreFoto=app.BD.buscarFoto(item)
                    indice=string.find(nombreFoto[0],'FotoAlumno-')
                    if nombreFoto[0] != 'None' and nombreFoto[0] != fotoVacia:
                        os.remove(os.path.join(profilePicDir,nombreFoto[0][indice:]))
                    app.BD.eliminarAlumno(item)
                    self.ListadoAlumnos.DeleteItem(j)
            mensaje=wx.MessageDialog(self,'Alumno(s) Eliminado(s)..!!',"Eliminando", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()
            self.searchAlumnoCtrl.Clear()
        else:
            mensaje=wx.MessageDialog(self,u'Debe especificar un nombre, apellido o cédula de identidad..!!',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.searchAlumnoCtrl.Clear()


    def cargarLista(self):
        try:
            self.cargarListadoDeAlumnos()
        except lite.Error, e:
           #error, sacamos dialogo
           exc_type, exc_value, exc_traceback = sys.exc_info()
           trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
           logging.error('%s - [%s]'%(e, trace))
           mensaje=wx.MessageDialog(self,"Hubo un Error. %s" %e,"Error", wx.OK|wx.ICON_HAND)
           mensaje.ShowModal()

    def searchAlumnoCtrlOnSearchButton( self, event ):
        self.ListadoAlumnos.DeleteAllItems()
        self.cargarLista()


    def searchAlumnoCtrlOnTextEnter( self, event ):
        self.ListadoAlumnos.DeleteAllItems()
        self.cargarLista()


    def searchAlumnoCtrlOnCancelButton(self, event):
        self.searchAlumnoCtrl.Clear()



class busquedaReporttes(FrameBusquedaReportes):

    """
    clase destinada a manejar todo lo referente a la busqueda de alumnos para reportes
    """

    def searchAlumnoCtrlOnEnterWindow( self, event ):
        self.m_statusBarElim.SetStatusText(u"Ingrese el nombre, apellido o cédula del alumno a buscar")


    def iniciarListaAlumnos(self):
        app.IconizarFrames(self)

        #Damos formato a la lista
        self.sizerListaAlumnos = wx.BoxSizer(wx.VERTICAL)
        self.panelListaAlumnos.SetSizer( self.sizerListaAlumnos)

        self.ListadoAlumnos  = wx.ListCtrl(self.panelListaAlumnos, -1, size=(-1,165), style=wx.LC_REPORT)
        self.ListadoAlumnos.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.operacionesDocumento)
        self.ListadoAlumnos.InsertColumn(0, u'ID')
        self.ListadoAlumnos.InsertColumn(1, 'Nombre')
        self.ListadoAlumnos.InsertColumn(2, 'Apellido')
        self.ListadoAlumnos.InsertColumn(3, u'Cédula de Identidad')
        self.ListadoAlumnos.InsertColumn(4, u'Edad')
        self.ListadoAlumnos.InsertColumn(5, u'Sexo')
        self.ListadoAlumnos.InsertColumn(6, u'Fecha de Ingreso')
        self.ListadoAlumnos.InsertColumn(7, u'Instrumento/Cátedra')
        self.ListadoAlumnos.InsertColumn(8, u'Orquesta')
        self.ListadoAlumnos.InsertColumn(9, u'Nivel')

        self.ListadoAlumnos.SetColumnWidth(0, -2)
        self.ListadoAlumnos.SetColumnWidth(1, -2)
        self.ListadoAlumnos.SetColumnWidth(2, -2)
        self.ListadoAlumnos.SetColumnWidth(3, -2)
        self.ListadoAlumnos.SetColumnWidth(4, -2)
        self.ListadoAlumnos.SetColumnWidth(5, -2)
        self.ListadoAlumnos.SetColumnWidth(6, -2)
        self.ListadoAlumnos.SetColumnWidth(7, -2)
        self.ListadoAlumnos.SetColumnWidth(8, -2)
        self.ListadoAlumnos.SetColumnWidth(9, -2)

        self.sizerListaAlumnos.Add(self.ListadoAlumnos, 1, wx.EXPAND | wx.TOP, 3)
        self.panelListaAlumnos.Layout()
        self.ListadoAlumnos.Layout()

    def cargarListadoDeAlumnos(self):
        if self.choiceCatedraBusqRep.GetCurrentSelection() != 0:
            if self.choiceCatedraBusqRep.GetCurrentSelection()==1:
                todos=True
                lista=app.BD.buscarAlumno(self.searchAlumnoCtrl.GetValue())
            else:
                todos=False
                lista=app.BD.buscarAlumno(self.searchAlumnoCtrl.GetValue(), catedra=self.choiceCatedraBusqRep.GetStringSelection())

            if not lista==[]:
                #Cargamos en la lista, el listado de usuarios obtenidos de la app.BD
                self.ListadoAlumnos.Layout()
                if todos:
                    for item in lista:
                        index = self.ListadoAlumnos.InsertStringItem(sys.maxint, str(item[0]))
                        self.ListadoAlumnos.SetStringItem(index, 1, item[1])
                        self.ListadoAlumnos.SetStringItem(index, 2, item[2])
                        self.ListadoAlumnos.SetStringItem(index, 3, item[3])
                        self.ListadoAlumnos.SetStringItem(index, 4, str(item[8]))
                        self.ListadoAlumnos.SetStringItem(index, 5, item[7])
                        self.ListadoAlumnos.SetStringItem(index, 6, item[5])
                        self.ListadoAlumnos.SetStringItem(index, 7, item[14])
                        self.ListadoAlumnos.SetStringItem(index, 8, item[15])
                        self.ListadoAlumnos.SetStringItem(index, 9, item[16])
                    self.searchAlumnoCtrl.Clear()
                else:
                    for item in lista:
                        index = self.ListadoAlumnos.InsertStringItem(sys.maxint, str(item[0]))
                        self.ListadoAlumnos.SetStringItem(index, 1, item[1])
                        self.ListadoAlumnos.SetStringItem(index, 2, item[2])
                        self.ListadoAlumnos.SetStringItem(index, 3, item[3])
                        self.ListadoAlumnos.SetStringItem(index, 4, str(item[8]))
                        self.ListadoAlumnos.SetStringItem(index, 5, item[7])
                        self.ListadoAlumnos.SetStringItem(index, 6, item[5])
                        self.ListadoAlumnos.SetStringItem(index, 7, item[14])
                        self.ListadoAlumnos.SetStringItem(index, 8, item[15])
                        self.ListadoAlumnos.SetStringItem(index, 9, item[16])
                    self.searchAlumnoCtrl.Clear()
            else:
                self.ListadoAlumnos.DeleteAllItems()
                mensaje=wx.MessageDialog(self,'No hay Resultados Coincidentes..!!',"Busqueda", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
        else:
            self.ListadoAlumnos.DeleteAllItems()
            mensaje=wx.MessageDialog(self,u'Debe escojer una opción de la Lista desplegable de Instrumento/Cátedra!!',"Busqueda", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

    def FrameBusquedaOnClose(self, event):
        self.MakeModal(False)
        self.Destroy()

    def operacionesDocumento( self, event ):
        self.docSel=self.ListadoAlumnos.GetItemText(self.ListadoAlumnos.GetFocusedItem())
        lst = [u"Generar Ficha Personal", u"Generar Ficha Médica", "Editar", "Eliminar"]
        dlg=wx.SingleChoiceDialog(self, u"Que Operación desea realizar sobre el Documento Seleccionado?", u'Operación',lst,style=wx.CHOICEDLG_STYLE|wx.CENTRE)
        if (dlg.ShowModal() == wx.ID_OK):
            if dlg.GetSelection()==0:
                self.GenerarFichaPersonal()
            if dlg.GetSelection()==1:
                self.GenerarFichaMedica()
            if dlg.GetSelection()==2:
                self.EditarAlumno()
            if dlg.GetSelection()==3:
                self.EliminarAlumno()
            dlg.Destroy()

    def GenerarFichaPersonal(self):
        ventanaFichaPAlumno=fichaAlumno(self)
        app.IconizarFrames(ventanaFichaPAlumno)
        wx.Frame.SetTitle(ventanaFichaPAlumno, 'Ficha General del Alumno')
        ventanaFichaPAlumno.iniciarPanelReporte('General')
        ventanaFichaPAlumno.Show()
        ventanaFichaPAlumno.MakeModal()

    def GenerarFichaMedica(self):
        ventanaFichaMAlumno=fichaAlumno(self)
        app.IconizarFrames(ventanaFichaMAlumno)
        wx.Frame.SetTitle(ventanaFichaMAlumno, u'Ficha Médica del Alumno')
        ventanaFichaMAlumno.iniciarPanelReporte('Medica')
        ventanaFichaMAlumno.Show()

        ventanaFichaMAlumno.MakeModal()

    def EditarAlumno(self):
        self.GetParent().editar(self.docSel)
        self.MakeModal(False)
        self.Close()

    def EliminarAlumno(self):
        box=wx.MessageDialog(self, "Realmente Desea Eliminar este Alumno ?","Advertencia", wx.YES_NO)
        if box.ShowModal()==wx.ID_YES:
            app.BD.eliminarAlumno(self.docSel)
            self.ListadoAlumnos.DeleteItem(self.ListadoAlumnos.GetFocusedItem())
            mensaje=wx.MessageDialog(self,"Alumno Eliminado","Eliminando", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,"Alumno NO Eliminado","Eliminando", wx.OK|wx.ICON_EXCLAMATION)
            mensaje.ShowModal()

    def btnCancelElimUsuOnButtonClick( self, event ):
        self.MakeModal(False)
        self.Destroy()

    def cargarLista(self):
        try:
            self.cargarListadoDeAlumnos()
        except lite.Error, e:
           #error, sacamos dialogo
           exc_type, exc_value, exc_traceback = sys.exc_info()
           trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
           logging.error('%s - [%s]'%(e, trace))
           mensaje=wx.MessageDialog(self,"Hubo un Error. %s" %e,"Error", wx.OK|wx.ICON_HAND)
           mensaje.ShowModal()

    def btnBuscarReporteOnButtonClick( self, event ):
        self.ListadoAlumnos.DeleteAllItems()
        self.cargarLista()

    def searchAlumnoCtrlOnTextEnter( self, event ):
        self.ListadoAlumnos.DeleteAllItems()
        self.cargarLista()

    def searchAlumnoCtrlOnCancelButton(self, event):
        self.searchAlumnoCtrl.Clear()
        self.ListadoAlumnos.DeleteAllItems()


class fichaAlumno(FrameFichasAlumno):

    def iniciarPanelReporte(self, tipo=None):
        """
        Inicializa el panel para mostrar el control ActiveX PDFWindow que para mostrar documentos PDF generados segun consulta a la Base de datos
        """
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.pdf = None

        self.pdf = PDFWindow(self.panelFicha)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        if tipo=='General':
            self.pdf.LoadFile(app.reporte.CrearFichaAlumno(self.GetParent().docSel))
        elif tipo=='Medica':
            self.pdf.LoadFile(app.reporte.CrearFichaMedicaAlumno(self.GetParent().docSel))

        self.panelFicha.SetSizer(sizer)
        self.panelFicha.Layout()

    def btnCerrarFichaOnButtonClick( self, event ):
        """
        Cierre del Frame Limpieza de archivos temporales
        """
        self.Close()

    def FrameFichasAlumnoOnClose(self, event):
        """
        Cierre del Frame Limpieza de archivos temporales
        """
        self.pdf.Destroy()
        app.limpiarDirectorios()
        self.MakeModal(False)
        self.Destroy()

class FichaGeneral(FrameReporteGeneral):

    def iniciarGrids(self):
        """
        Inicializa los XLSGrid para Cada Hoja del Reporte General (Datos Generales y Ficha Medica)
        """
        self.xlsGrid_1 = XG.XLSGrid(self.panel_FichaGeneral)
        self.xlsGrid_2 = XG.XLSGrid(self.panel_FichaMedica)

    def btnCrearReporteOnButtonClick(self, event):
        """
        Creacion del documento Excel  referente al Reporte General mediante xlwt segun una consulta a la BD
        """

        self.xlsGrid_1.Destroy()
        self.xlsGrid_2.Destroy()

        self.iniciarGrids()

        if self.choiceCatReporte.GetSelection() != 0:

            if self.m_radio_tipo_reporte.GetSelection()==0:
                DATA = app.BD.reporteGeneralAlumnos(catedra=self.choiceCatReporte.GetStringSelection(),tipo=1)
                DATA_2 = app.BD.reporteGeneralFichaMedica(catedra=self.choiceCatReporte.GetStringSelection())
            elif self.m_radio_tipo_reporte.GetSelection()==1:
                DATA = app.BD.reporteGeneralAlumnos(catedra=self.choiceCatReporte.GetStringSelection(),tipo=2)
                DATA_2 = app.BD.reporteGeneralFichaMedica(catedra=self.choiceCatReporte.GetStringSelection())

            try:

                wb = xlwt.Workbook()
                ws = wb.add_sheet("Datos Generales")
                ws_2=wb.add_sheet(u"Ficha Médica")
                
                ###################################################################################
                # Agrego cabeceras con estilo y fijo la primera fila FICHA GENERAL
                ###################################################################################
                heading_xf = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center;' 'borders: left thin, right thin, top thin, bottom thin;' 'pattern: pattern fine_dots, fore_colour pale_blue;')
                data_xf= xlwt.easyxf('borders: left thin, right thin, top thin, bottom thin;')
                if self.m_radio_tipo_reporte.GetSelection()==0:
                    headings = [u'Apellido(s)', u'Nombre(s)', 'C.I', u'Instrumento/Cátedra']
                else:
                    headings = [u'Apellido(s)', u'Nombre(s)', 'C.I', 'Fecha de Nacimiento', 'Fecha de Ingreso', 'Lugar de Nacimiento', 'Sexo', 'Edad', u'Teléfono de Residencia',
                                 u'Teléfono Celular', u'E-Mail', 'Tiene Conocimientos Musicales?', u'Instrumento/Cátedra', 'Orquesta', 'Nivel Orquestal', u'Tiene Instrumento Propio?',
                                 u'Fecha de asignación de Instrumento', 'Marca del Instrumento', 'Modelo del Instrumento', 'Serial del Istrumento', u'Nº Activo Fijo FUNDAMUSICAL',
                                 'Profesor', u'Pertenece a otra agrupación?', u'Nombre de la Agrupación', u'Fecha de Ingreso a la agrupación', 'Municipio', 'Parroquia', 'Sector', u'Urbanización o Barrio',
                                 'Avenida', 'Calle', 'Edificio', 'Casa o Apartamento', 'Pto. de Referencia', 'Nombre del Representante', 'Apellido del Representante', 'C.I del Representante',
                                 u'Dirección del Representante', u'Teléfono Residencia Representante', u'Teléfono Celular Representante', 'E-mail Representante', u'Dirección Laboral Representante',
                                 u'Teléfono Laboral Representante', u'Ocupación del Representante', 'Parentesco del Representante', u'El alumno estudia?', u'Nivel académico del Alumno',
                                 u'Grado', u'Año', 'Semestre', u'Institución donde Estudia', u'Direción de la Institución', u'Teléfono de la Institución', u'Tipo de Institución']
                rowx = 0
                ws.set_panes_frozen(True) # frozen headings instead of split panes
                ws.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
                ws.set_remove_splits(True) # if user does unfreeze, don't leave a split there

                ###################################################################################
                # Agrego cabeceras con estilo y fijo la primera fila FICHA MEDICA
                ###################################################################################
                heading_xf2 = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center;' 'borders: left thin, right thin, top thin, bottom thin;' 'pattern: pattern fine_dots, fore_colour pale_blue;')
                data_xf2= xlwt.easyxf('borders: left thin, right thin, top thin, bottom thin' )
                headings2 = ['Tipo de Sangre', 'Antecedentes Generales', 'Vacunado Fiebre amarilla', 'Fecha de Vacuna', 'Vacunado Hepatitis "A"', 'Fecha de Vacuna',
                                    'Vacunado Hepatitis "B"', 'Fecha de Vacuna', 'Enfermedades Cabeza', u'Enfermedades Oído', u'Enfermedades Naríz','Enfermedades Garganta',
                                    u'Enfermedades Corazón','Enfermedades Pulmones',u'Enfermedades Vías Digestivas',u'Enfermedades Riñones','Enfermedades Huesos',
                                    'Enfermedades Articulaciones', 'Enfermedades Endocrinologicas','Operaciones','Alergias a Comidas', 'Alergias a Medicamentos',
                                    u'Medicamento Específico', u'Tiene Seguro Médico', 'Aseguradora', u'Teléfono de Aseguradora', u'Número de Emergencia',
                                    u'Unidad Médica de Preferencia', u'Médico Tratante', u'Teléfono del Médico Tratante', u'Teléfono Celular del Médico Tratante',
                                    u'Otra Enfermedad o Condición', u'Aparato o Euipo Médico', 'Apellidos','Nombres']
                rowx2 = 0
                ws_2.set_panes_frozen(True) # frozen headings instead of split panes
                ws_2.set_horz_split_pos(rowx2+1) # in general, freeze after last heading row
                ws_2.set_remove_splits(True) # if user does unfreeze, don't leave a split there


                #UBICO LA CABECERA FICHA GENERAL
                for colx, value in enumerate(headings):
                    ws.write(rowx, colx, value, heading_xf)

                #UBICO LA CABECERA FICHA MEDICA
                for colx2, value2 in enumerate(headings2):
                    ws_2.write(rowx2, colx2, value2, heading_xf2)

                #CARGO LA DATA FICHA GENERAL
                for i, row in enumerate(DATA):
                    for j, col in enumerate(row):
                        ws.write(i+1, j, col, data_xf)

                #CARGO LA DATA FICHA MEDICA
                for i2, row2 in enumerate(DATA_2):
                    for j2, col2 in enumerate(row2):
                        ws_2.write(i2+1, j2, col2, data_xf2)

                #MODIFICO EL ANCHO DE LAS COLUMNAS
                width = 250.0 * max([len(row[0]) for row in DATA])
                width_2 = 250.0 * max([len(row2[0]) for row2 in DATA_2])

                for indice1 in range(len(headings)):
                    ws.col(indice1).width=width

                for indice2 in range(len(headings2)):
                    ws_2.col(indice2).width=width_2

                now=datetime.now()
                date_str = now.strftime("%Y-%m-%d_%H%M%S")

                name = "FichaGeneral-%s-%s" % (date_str, os.getpid())
                self.temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.xls', dir='temp',) #CREACION DEL ARCHIVO TEMPORAL
                self.temp.close()

                wb.save(self.temp.name)

                busy = wx.BusyInfo("Creando Reporte General, por favor espere....")
                self.iniciarPanelFichaGeneral(self.temp.name)
                del busy
            except ValueError:
                mensaje=wx.MessageDialog(self,u'No Hay Alumnos Cargados. \n\n',"Error", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'Debe Selecionar una Opción. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()


    def iniciarPanelFichaGeneral(self, filename):
        """
        Iniciar los controles y Widgets Correspondientes para mostrar el XLSGrid
        """

        book = xlrd.open_workbook(filename, formatting_info=True)

        sheetname = "Datos Generales"
        sheet = book.sheet_by_name(sheetname)
        rows, cols = sheet.nrows, sheet.ncols
        comments, texts = XG.ReadExcelCOM(filename, sheetname, rows, cols)

        sheetname_2 = u"Ficha Médica"
        sheet_2 = book.sheet_by_name(sheetname_2)
        rows_2, cols_2 = sheet_2.nrows, sheet_2.ncols
        comments_2, texts_2 = XG.ReadExcelCOM(filename, sheetname_2, rows_2, cols_2)


        self.xlsGrid_1.ClearGrid()
        self.xlsGrid_1.ForceRefresh()
        self.xlsGrid_2.ClearGrid()
        self.xlsGrid_2.ForceRefresh()

        self.xlsGrid_1.PopulateGrid(book, sheet, texts, comments)
        self.xlsGrid_2.PopulateGrid(book, sheet_2, texts_2, comments_2)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_1.Add(self.xlsGrid_1, 1, wx.EXPAND, 5)
        sizer_2.Add(self.xlsGrid_2, 1, wx.EXPAND, 5)
        self.panel_FichaGeneral.SetSizer(sizer_1)
        self.panel_FichaMedica.SetSizer(sizer_2)
        self.panel_FichaGeneral.Layout()
        self.panel_FichaMedica.Layout()

    def open_report(self,path):
        """
        Abre el Documento con la aplicacion por defecto (Excel, OpenOffice, etc)
        """

        try:
            if os.name == 'posix':
                os.popen('evince %s'% path)
            else:
                os.startfile(os.path.normpath(path))
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('[%s]'%trace)
            mensaje=wx.MessageDialog(self.GetParent(),u'Error abriendo el archivo',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnImpFichaGenOnButtonClick(self, event):
        try:
            self.open_report(self.temp.name) #Abre el Documento
        except AttributeError:
            mensaje=wx.MessageDialog(self,u'No Hay Alumnos Cargados. \n\nNo hay Documento que Imprimir',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnCerrarFichaGenOnButtonClick(self, event):
        """
        Acciones al cerrar el Frame con el Boton 'Cerrar' (Limpieza de Directorios)
        """
        self.Close()

    def FrameReporteGeneralOnClose(self, event):
        """
        Acciones al cerrar el Frame (Limpieza de Directorios)
        """

        try:
            app.limpiarDirectorios()
            self.MakeModal(False)
            self.Destroy()
        except:
            logging.error(u'Intento de Cerrar la Aplicación coj un archivo temporal abierto.')
            mensaje=wx.MessageDialog(self.GetParent(),u'Existe un archivo temporal abierto. \n\nDebe Cerrarlo Primero',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
        event.Skip()


class ReporteProfesor(FrameReporteProf):

    def iniciarGrids(self):
        """
        Inicializa los XLSGrid para Cada Hoja del Reporte General (Datos Generales y Ficha Medica)
        """
        self.xlsGrid_1 = XG.XLSGrid(self.panel_RepProf)
        
    def btnCrearReporteOnButtonClick(self, event):
        """
        Creacion del documento Excel  referente al Reporte General mediante xlwt segun una consulta a la BD
        """

        if self.txt_profesor.GetValue() != '':
            self.xlsGrid_1.Destroy()

            self.iniciarGrids()

            DATA = app.BD.reportealumnosProfesor(self.txt_profesor.GetValue())

            try:

                wb = xlwt.Workbook()
                ws = wb.add_sheet("Datos Generales")
                
                ###################################################################################
                # Agrego cabeceras con estilo y fijo la primera fila FICHA GENERAL
                ###################################################################################
                heading_xf = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center;' 'borders: left thin, right thin, top thin, bottom thin;' 'pattern: pattern fine_dots, fore_colour pale_blue;')
                data_xf= xlwt.easyxf('borders: left thin, right thin, top thin, bottom thin;')
                headings = [u'Apellido(s)', u'Nombre(s)', 'C.I', 'Edad', u'Instrumento/Cátedra', u'Profesor']
                rowx = 0
                ws.set_panes_frozen(True) # frozen headings instead of split panes
                ws.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
                ws.set_remove_splits(True) # if user does unfreeze, don't leave a split there

                ###################################################################################
                # Agrego cabeceras con estilo y fijo la primera fila FICHA MEDICA
                ###################################################################################


                #UBICO LA CABECERA FICHA GENERAL
                for colx, value in enumerate(headings):
                    ws.write(rowx, colx, value, heading_xf)

                #CARGO LA DATA FICHA GENERAL
                for i, row in enumerate(DATA):
                    for j, col in enumerate(row):
                        ws.write(i+1, j, col, data_xf)


                #MODIFICO EL ANCHO DE LAS COLUMNAS
                width = 700.0 * max([len(row[0]) for row in DATA])

                for indice1 in range(len(headings)):
                    ws.col(indice1).width=width


                now=datetime.now()
                date_str = now.strftime("%Y-%m-%d_%H%M%S")

                name = "FichaProf-%s-%s" % (date_str, os.getpid())
                self.temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.xls', dir='temp',) #CREACION DEL ARCHIVO TEMPORAL
                self.temp.close()

                wb.save(self.temp.name)

                busy = wx.BusyInfo("Creando Reporte, por favor espere....")
                self.iniciarPanelFichaGeneral(self.temp.name)
                del busy
            except ValueError:
                mensaje=wx.MessageDialog(self,u'No Hay Alumnos Cargados. \n\n',"Error", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
                self.txt_profesor.Clear()
                self.txt_profesor.SetFocus()

        else:
            mensaje=wx.MessageDialog(self,u'Debe ingresar un nombre de Profesor',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def iniciarPanelFichaGeneral(self, filename):
        """
        Iniciar los controles y Widgets Correspondientes para mostrar el XLSGrid
        """

        book = xlrd.open_workbook(filename, formatting_info=True)

        sheetname = "Datos Generales"
        sheet = book.sheet_by_name(sheetname)
        rows, cols = sheet.nrows, sheet.ncols
        comments, texts = XG.ReadExcelCOM(filename, sheetname, rows, cols)


        self.xlsGrid_1.ClearGrid()
        self.xlsGrid_1.ForceRefresh()

        self.xlsGrid_1.PopulateGrid(book, sheet, texts, comments)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
    

        sizer_1.Add(self.xlsGrid_1, 1, wx.EXPAND, 5)
        
        self.panel_RepProf.SetSizer(sizer_1)
        
        self.panel_RepProf.Layout()
        

    def open_report(self,path):
        """
        Abre el Documento con la aplicacion por defecto (Excel, OpenOffice, etc)
        """

        try:
            if os.name == 'posix':
                os.popen('evince %s'% path)
            else:
                os.startfile(os.path.normpath(path))
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('[%s]'%trace)
            mensaje=wx.MessageDialog(self.GetParent(),u'Error abriendo el archivo',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnImpFichaGenOnButtonClick(self, event):
        try:
            self.open_report(self.temp.name) #Abre el Documento
        except AttributeError:
            mensaje=wx.MessageDialog(self,u'No Hay Alumnos Cargados. \n\nNo hay Documento que Imprimir',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnCerrarFichaGenOnButtonClick(self, event):
        """
        Acciones al cerrar el Frame con el Boton 'Cerrar' (Limpieza de Directorios)
        """
        self.Close()

    def FrameReporteProfOnClose(self, event):
        """
        Acciones al cerrar el Frame (Limpieza de Directorios)
        """

        try:
            app.limpiarDirectorios()
            self.MakeModal(False)
            self.Destroy()
        except:
            logging.error(u'Intento de Cerrar la Aplicación coj un archivo temporal abierto.')
            mensaje=wx.MessageDialog(self.GetParent(),u'Existe un archivo temporal abierto. \n\nDebe Cerrarlo Primero',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
        event.Skip()

class FPrincipal(FramePrincipal):

    def IniciarSizers(self):


        self.bienvenida=panelBienvenida(self)

        self.carga=panelCarga(self)
        self.carga.nombre='Carga'
        self.carga.foto=fotoVacia
        self.carga.cargado=False
        self.carga.elemento=''

        self.carga.listaCatedras_carga=[]

        self.carga.Bind(wx.EVT_CHECKLISTBOX, self.carga.EvtCheckListBox, self.carga.checkCatedras_carga)

        self.edicion=panelEdicion(self)
        self.edicion.flag=False
        self.edicion.nombre='Edicion'
        self.edicion.fotoEditar=None
        self.edicion.editado=False

        self.edicion.listaCatedras_edicion=[]

        app.IconizarFrames(self)

        self.sizerFramePrincipal = wx.BoxSizer( wx.HORIZONTAL )
        self.SetSizer( self.sizerFramePrincipal )
        self.sizerFramePrincipal.Add(self.bienvenida, 1, wx.EXPAND | wx.TOP, 3)
        self.sizerFramePrincipal.Add(self.carga, 1, wx.EXPAND | wx.TOP, 3)
        self.sizerFramePrincipal.Add(self.edicion, 1, wx.EXPAND | wx.TOP, 3)
        self.bienvenida.Layout()
        self.Layout()

    def limpiarPantalla(self):

        if self.carga.IsShown():
            self.carga.Hide()
            self.carga.radioEducacionAlumno_Carga.Enable(True)
            self.carga.txtGradoAlumno_Carga.Enable(True)
            self.carga.txtAnioAlumno_Carga.Enable(True)
            self.carga.txtSemestreAlumno_Carga.Enable(True)
            self.carga.txtInstitAlumno_Carga.Enable(True)
            self.carga.txtDireccionInstitAlumno_Carga.Enable(True)
            self.carga.txtTelefonoInstitAlumno_Carga.Enable(True)
            self.carga.radioTipoInstitAlumno_Carga.Enable(True)
            self.carga.txtNombreOtraAgrupAlumno_Carga.Enable(True)
            self.carga.datePickerFechaIngOtraAgrupAlumno_Carga.Enable(True)
            self.carga.datepickerFecAsigInstAlumno_Carga.Enable(True)
            self.carga.txtNumActFijoInstAlumno_Carga.Enable(True)
            self.carga.datePickerFMedVacFA_Carga.Enable(True)
            self.carga.datePickerFMedVacHA_Carga.Enable(True)
            self.carga.datePickerFMedVacHB_Carga.Enable(True)
            self.carga.txtFMedAseg_Carga.Enable(True)
            self.carga.txtFMedTelAseg_Carga.Enable(True)

            #LIMPIAR CAMPOS
            #DATOS GENERALES

            self.carga.bitmapFoto.SetBitmap(wx.Bitmap( fotoVacia, wx.BITMAP_TYPE_ANY ))
            self.carga.txtNomAlumno_Carga.Clear()
            self.carga.txtApeAlumno_Carga.Clear()
            self.carga.txtCiAlumno_Carga.Clear()
            self.carga.datePickerFechaNacAlumno_Carga.SetValue(wx.DateTime.Today())
            self.carga.datePickerFechaIngAlumno_Carga.SetValue(wx.DateTime.Today())
            self.carga.txtLugarNacAlumno_Carga.Clear()
            self.carga.radioSexoAlumno_Carga.SetSelection(0)
            self.carga.txtEdadAlumno_Carga.Clear()
            self.carga.txtDirTelHabAlumno_Carga.Clear()
            self.carga.txtDirTelCelAlumno_Carga.Clear()
            self.carga.txtDirEmailalumno_Carga.Clear()

            #DIRECCION
            self.carga.txtDirMunicipioAlumno_Carga.Clear()
            self.carga.txtDirParroquiaAlumno_Carga.Clear()
            self.carga.txtDirSectorAlumno_Carga.Clear()
            self.carga.txtDirUrbarrioAlumno_Carga.Clear()
            self.carga.txtDirAvenidaAlumno_Carga.Clear()
            self.carga.txtDirCalleAlumno_Carga.Clear()
            self.carga.txtDirEdificioAlumno_Carga.Clear()
            self.carga.txtDirCasaAptoAlumno_Carga.Clear()
            self.carga.txtDirPtoRefAlumno_Carga.Clear()

            #REPRESENTANTE
            self.carga.txtNombreRepAlumno_Carga.Clear()
            self.carga.txtApeRepAlumno_Carga.Clear()
            self.carga.txtCiRep_Carga.Clear()
            self.carga.txtDirHabRep_Carga.Clear()
            self.carga.txtTelHabRep_Carga.Clear()
            self.carga.txtTelCelRep_Carga.Clear()
            self.carga.txtEmailRep_Carga.Clear()
            self.carga.txtDirTrabajoRep_Carga.Clear()
            self.carga.txtTelTrabajoRep_Carga.Clear()
            self.carga.txtOcupacionRep_Carga.Clear()
            self.carga.txtParentescoRep_Carga.Clear()

            #ACADEMICOS
            self.carga.radioEstudiaAlumno_Carga.SetSelection(0)
            self.carga.radioEducacionAlumno_Carga.SetSelection(0)
            self.carga.txtGradoAlumno_Carga.Clear()
            self.carga.txtAnioAlumno_Carga.Clear()
            self.carga.txtSemestreAlumno_Carga.Clear()
            self.carga.txtInstitAlumno_Carga.Clear()
            self.carga.txtDireccionInstitAlumno_Carga.Clear()
            self.carga.txtTelefonoInstitAlumno_Carga.Clear()
            self.carga.radioTipoInstitAlumno_Carga.SetSelection(0)

            #MUSICAL
            for i in range(self.carga.checkCatedras_carga.GetCount()):
                self.carga.checkCatedras_carga.Check(i, check=False)
            self.carga.radioConocMusAlumno_Carga.SetSelection(0)
            self.carga.choiceOrquAlumno_Carga.SetSelection(0)
            self.carga.txtNivelOrqAlumno_Carga.Clear()
            self.carga.radioInstPropioAlumno_Carga.SetSelection(0)
            self.carga.datepickerFecAsigInstAlumno_Carga.SetValue(wx.DateTime.Today())
            self.carga.txtMarcaInstAlumno_Carga.Clear()
            self.carga.txtModeloInstAlumno_Carga.Clear()
            self.carga.txtSerialInstAlumno_Carga.Clear()
            self.carga.txtNumActFijoInstAlumno_Carga.Clear()
            self.carga.txtProfAlumno_Carga.Clear()
            self.carga.radioOtraAgrupAlumno_Carga.SetSelection(0)
            self.carga.txtNombreOtraAgrupAlumno_Carga.Clear()
            self.carga.datePickerFechaIngOtraAgrupAlumno_Carga.SetValue(wx.DateTime.Today())

            #FICHA MEDICA
            self.carga.txtFMedTipoSangreAlumno_Carga.Clear()
            self.carga.txtFMedAntecedAlumno_Carga.Clear()
            self.carga.radioFMedVacFA_Carga.SetSelection(0)
            self.carga.datePickerFMedVacFA_Carga.SetValue(wx.DateTime.Today())
            self.carga.radioFMedVacHA_Carga.SetSelection(0)
            self.carga.datePickerFMedVacHA_Carga.SetValue(wx.DateTime.Today())
            self.carga.radioFMedVacHB_Carga.SetSelection(0)
            self.carga.datePickerFMedVacHB_Carga.SetValue(wx.DateTime.Today())
            self.carga.radioFMedEnfCab_Carga.SetSelection(1)
            self.carga.radioFMedEnfOid_Carga.SetSelection(1)
            self.carga.radioFMedEnfNar_Carga.SetSelection(1)
            self.carga.radioFMedEnfGar_Carga.SetSelection(1)
            self.carga.radioFMedEnfCor_Carga.SetSelection(1)
            self.carga.radioFMedEnfPul_Carga.SetSelection(1)
            self.carga.radioFMedEnfVD_Carga.SetSelection(1)
            self.carga.radioFMedEnfRi_Carga.SetSelection(1)
            self.carga.radioFMedEnfHue_Carga.SetSelection(1)
            self.carga.radioFMedEnfArt_Carga.SetSelection(1)
            self.carga.radioFMedEnfEnd_Carga.SetSelection(1)
            self.carga.txtFMedOperaciones_Carga.Clear()
            self.carga.txtFMedAlerCom_Carga.Clear()
            self.carga.txtFMedAlerMed_Carga.Clear()
            self.carga.txtFMedAlerMedEsp_Carga.Clear()
            self.carga.radioFMedTieneSeguro_Carga.SetSelection(0)
            self.carga.txtFMedAseg_Carga.Clear()
            self.carga.txtFMedTelAseg_Carga.Clear()
            self.carga.txtFMedTelEmerg_Carga.Clear()
            self.carga.txtFMedUnidadMedPref_Carga.Clear()
            self.carga.txtFMedTratante_Carga.Clear()
            self.carga.txtFMedTelTratante_Carga.Clear()
            self.carga.txtFMedCelTratante_Carga.Clear()
            self.carga.txtFMedEnfPrevia_Carga.Clear()
            self.carga.txtFMedAperato_Carga.Clear()

            #MUESTRA LOGO
            self.bienvenida.Show()
            self.cargarAlumnos.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_ALUMNOS, True)

        elif self.edicion.IsShown():
            self.edicion.Hide()

            self.edicion.radioEducacionAlumno_Edicion.Enable(True)
            self.edicion.txtGradoAlumno_Edicion.Enable(True)
            self.edicion.txtAnioAlumno_Edicion.Enable(True)
            self.edicion.txtSemestreAlumno_Edicion.Enable(True)
            self.edicion.txtInstitAlumno_Edicion.Enable(True)
            self.edicion.txtDireccionInstitAlumno_Edicion.Enable(True)
            self.edicion.txtTelefonoInstitAlumno_Edicion.Enable(True)
            self.edicion.radioTipoInstitAlumno_Edicion.Enable(True)
            self.edicion.txtNombreOtraAgrupAlumno_Edicion.Enable(True)
            self.edicion.datePickerFechaIngOtraAgrupAlumno_Edicion.Enable(True)
            self.edicion.datepickerFecAsigInstAlumno_Edicion.Enable(True)
            self.edicion.txtNumActFijoInstAlumno_Edicion.Enable(True)
            self.edicion.datePickerFMedVacFA_Edicion.Enable(True)
            self.edicion.datePickerFMedVacHA_Edicion.Enable(True)
            self.edicion.datePickerFMedVacHB_Edicion.Enable(True)
            self.edicion.txtFMedAseg_Edicion.Enable(True)
            self.edicion.txtFMedTelAseg_Edicion.Enable(True)

            #LIMPIAR CAMPOS
            #DATOS GENERALES

            self.edicion.bitmapFoto.SetBitmap(wx.Bitmap( fotoVacia, wx.BITMAP_TYPE_ANY ))
            self.edicion.txtNomAlumno_Edicion.Clear()
            self.edicion.txtApeAlumno_Edicion.Clear()
            self.edicion.txtCiAlumno_Edicion.Clear()
            self.edicion.datePickerFechaNacAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.edicion.datePickerFechaIngAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.edicion.txtLugarNacAlumno_Edicion.Clear()
            self.edicion.radioSexoAlumno_Edicion.SetSelection(0)
            self.edicion.txtEdadAlumno_Edicion.Clear()
            self.edicion.txtDirTelHabAlumno_Edicion.Clear()
            self.edicion.txtDirTelCelAlumno_Edicion.Clear()
            self.edicion.txtDirEmailalumno_Edicion.Clear()

            #DIRECCION
            self.edicion.txtDirMunicipioAlumno_Edicion.Clear()
            self.edicion.txtDirParroquiaAlumno_Edicion.Clear()
            self.edicion.txtDirSectorAlumno_Edicion.Clear()
            self.edicion.txtDirUrbarrioAlumno_Edicion.Clear()
            self.edicion.txtDirAvenidaAlumno_Edicion.Clear()
            self.edicion.txtDirCalleAlumno_Edicion.Clear()
            self.edicion.txtDirEdificioAlumno_Edicion.Clear()
            self.edicion.txtDirCasaAptoAlumno_Edicion.Clear()
            self.edicion.txtDirPtoRefAlumno_Edicion.Clear()

            #REPRESENTANTE
            self.edicion.txtNombreRepAlumno_Edicion.Clear()
            self.edicion.txtApeRepAlumno_Edicion.Clear()
            self.edicion.txtCiRep_Edicion.Clear()
            self.edicion.txtDirHabRep_Edicion.Clear()
            self.edicion.txtTelHabRep_Edicion.Clear()
            self.edicion.txtTelCelRep_Edicion.Clear()
            self.edicion.txtEmailRep_Edicion.Clear()
            self.edicion.txtDirTrabajoRep_Edicion.Clear()
            self.edicion.txtTelTrabajoRep_Edicion.Clear()
            self.edicion.txtOcupacionRep_Edicion.Clear()
            self.edicion.txtParentescoRep_Edicion.Clear()

            #ACADEMICOS
            self.edicion.radioEstudiaAlumno_Edicion.SetSelection(0)
            self.edicion.radioEducacionAlumno_Edicion.SetSelection(0)
            self.edicion.txtGradoAlumno_Edicion.Clear()
            self.edicion.txtAnioAlumno_Edicion.Clear()
            self.edicion.txtSemestreAlumno_Edicion.Clear()
            self.edicion.txtInstitAlumno_Edicion.Clear()
            self.edicion.txtDireccionInstitAlumno_Edicion.Clear()
            self.edicion.txtTelefonoInstitAlumno_Edicion.Clear()
            self.edicion.radioTipoInstitAlumno_Edicion.SetSelection(0)

            #MUSICAL
            for i in range(self.edicion.checkCatedras_edicion.GetCount()):
                self.edicion.checkCatedras_edicion.Check(i, check=False)
            self.edicion.radioConocMusAlumno_Edicion.SetSelection(0)
            self.edicion.choiceOrquAlumno_Edicion.SetSelection(0)
            self.edicion.txtNivelOrqAlumno_Edicion.Clear()
            self.edicion.radioInstPropioAlumno_Edicion.SetSelection(0)
            self.edicion.datepickerFecAsigInstAlumno_Edicion.SetValue(wx.DateTime.Today())
            self.edicion.txtMarcaInstAlumno_Edicion.Clear()
            self.edicion.txtModeloInstAlumno_Edicion.Clear()
            self.edicion.txtSerialInstAlumno_Edicion.Clear()
            self.edicion.txtNumActFijoInstAlumno_Edicion.Clear()
            self.edicion.txtProfAlumno_Edicion.Clear()
            self.edicion.radioOtraAgrupAlumno_Edicion.SetSelection(0)
            self.edicion.txtNombreOtraAgrupAlumno_Edicion.Clear()
            self.edicion.datePickerFechaIngOtraAgrupAlumno_Edicion.SetValue(wx.DateTime.Today())

            #FICHA MEDICA
            self.edicion.txtFMedTipoSangreAlumno_Edicion.Clear()
            self.edicion.txtFMedAntecedAlumno_Edicion.Clear()
            self.edicion.radioFMedVacFA_Edicion.SetSelection(0)
            self.edicion.datePickerFMedVacFA_Edicion.SetValue(wx.DateTime.Today())
            self.edicion.radioFMedVacHA_Edicion.SetSelection(0)
            self.edicion.datePickerFMedVacHA_Edicion.SetValue(wx.DateTime.Today())
            self.edicion.radioFMedVacHB_Edicion.SetSelection(0)
            self.edicion.datePickerFMedVacHB_Edicion.SetValue(wx.DateTime.Today())
            self.edicion.radioFMedEnfCab_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfOid_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfNar_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfGar_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfCor_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfPul_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfVD_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfRi_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfHue_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfArt_Edicion.SetSelection(1)
            self.edicion.radioFMedEnfEnd_Edicion.SetSelection(1)
            self.edicion.txtFMedOperaciones_Edicion.Clear()
            self.edicion.txtFMedAlerCom_Edicion.Clear()
            self.edicion.txtFMedAlerMed_Edicion.Clear()
            self.edicion.txtFMedAlerMedEsp_Edicion.Clear()
            self.edicion.radioFMedTieneSeguro_Edicion.SetSelection(0)
            self.edicion.txtFMedAseg_Edicion.Clear()
            self.edicion.txtFMedTelAseg_Edicion.Clear()
            self.edicion.txtFMedTelEmerg_Edicion.Clear()
            self.edicion.txtFMedUnidadMedPref_Edicion.Clear()
            self.edicion.txtFMedTratante_Edicion.Clear()
            self.edicion.txtFMedTelTratante_Edicion.Clear()
            self.edicion.txtFMedCelTratante_Edicion.Clear()
            self.edicion.txtFMedEnfPrevia_Edicion.Clear()
            self.edicion.txtFMedAperato_Edicion.Clear()

            #MUESTRA LOGO
            self.bienvenida.Show()
            self.editarAlumnos.Enable(True)
            self.m_toolBar1.EnableTool(ID_EDITAR_ALUMNOS, True)

        self.bienvenida.Layout()
        self.Layout()

    def cargar(self):
        self.bienvenida.Hide()
        if not self.editarAlumnos.IsEnabled():
            self.editarAlumnos.Enable(True)
            self.m_toolBar1.EnableTool(ID_EDITAR_ALUMNOS, True)

        self.cargarAlumnos.Enable(False)
        self.m_toolBar1.EnableTool(ID_CARGAR_ALUMNOS, False)

        if self.edicion.IsShown():
            self.edicion.Hide()
            self.carga.Show()
            self.carga.notebookAlumno.SetSelection(0)
            self.carga.preCargaRadios()
        else:
            self.carga.Show()
            self.carga.notebookAlumno.SetSelection(0)
            self.carga.preCargaRadios()
        self.carga.Layout()
        self.Layout()

    def cargarAlumnosOnMenuSelection( self, event ):
        self.limpiarPantalla()
        self.cargar()
        app.limpiarFotos()


    def editar(self,id=None):
        self.bienvenida.Hide()
        if not self.cargarAlumnos.IsEnabled():
            self.cargarAlumnos.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_ALUMNOS, True)

        self.editarAlumnos.Enable(False)
        self.m_toolBar1.EnableTool(ID_EDITAR_ALUMNOS, False)

        if self.carga.IsShown():
            self.carga.Hide()
            self.edicion.Show()
            self.edicion.notebookAlumno.SetSelection(0)
            if not id:
                self.edicion.cargarChoiceEdicion()
            else:
                self.edicion.cargarChoiceEdicion()
                self.edicion.cargarDatosALumno(id)
            self.edicion.preCargaRadios()
        else:
            self.edicion.Show()
            self.edicion.notebookAlumno.SetSelection(0)
            if not id:
                self.edicion.cargarChoiceEdicion()
            else:
                self.edicion.cargarChoiceEdicion()
                self.edicion.cargarDatosALumno(id)
            self.edicion.preCargaRadios()
        self.edicion.Layout()
        self.Layout()

    def editarAlumnosOnMenuSelection( self, event ):
        self.limpiarPantalla()
        self.editar()
        app.limpiarFotos()

    def eliminar(self):
        self.limpiarPantalla()
        ventanaElimProf = busquedaAlumnos(self)
        app.IconizarFrames(ventanaElimProf)
        ventanaElimProf.Show()
        ventanaElimProf.iniciarListaAlumnos()
        ventanaElimProf.MakeModal()
        app.limpiarFotos()

    def eliminarAlumnoOnMenuSelection( self, event ):
        self.eliminar()


    def fichaDeAlumnoOnMenuSelection(self, event):
        self.limpiarPantalla()
        ventanaFichaAlumno = busquedaReporttes(self)
        app.IconizarFrames(ventanaFichaAlumno)
        ventanaFichaAlumno.Show()
        ventanaFichaAlumno.iniciarListaAlumnos()
        ventanaFichaAlumno.MakeModal()
        app.limpiarFotos()

    def reporteDeAlumnosPorProfesorOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaRepProf=ReporteProfesor(self)
        ventanaRepProf.iniciarGrids()
        app.IconizarFrames(ventanaRepProf)
        wx.Frame.SetTitle(ventanaRepProf, u'Reporte de Alumnos segun Profesor')
        ventanaRepProf.Show()
        ventanaRepProf.MakeModal()
        app.limpiarFotos()


    def reporteGeneralOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaFichaGeneral=FichaGeneral(self)
        ventanaFichaGeneral.iniciarGrids()
        app.IconizarFrames(ventanaFichaGeneral)
        wx.Frame.SetTitle(ventanaFichaGeneral, u'Ficha General')
        ventanaFichaGeneral.Show()
        ventanaFichaGeneral.MakeModal()
        app.limpiarFotos()

    def licenciaOnMenuSelection( self, event ):
        app.IconizarFrames(self)
        licencia = os.path.normpath(os.path.join(licenceDir, "copying"))
        licenseText = open(licencia, "r")
        msg = licenseText.read()
        licenseText.close()
        msg2=wordwrap(msg, 500, wx.ClientDC(self))
        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg2, "Licencia")
        dlg.ShowModal()


    def acercaDeOnMenuSelection(self, event):
        app.IconizarFrames(self)
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = u"Sistema de Gestión de Plantilla de Alumnos"
        info.Version = "1.0"
        info.Description = wordwrap(
            u"El Sistema de Gestión de Plantilla de Alumnos permite la carga de los datos personales y Ficha Médica de los Alumnos, asi como como la emision de los reportes respectivos ",
            350, wx.ClientDC(self))
        info.WebSite = ("http://www.fesnojiv.gob.ve", u"Página Web FUNDAMUSICAL Bolívar")
        info.Developers = [ "Lic. Mario Castro - mariocastro.pva@gmail.com" ]
        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)


    def salirOnMenuSelection( self, event ):
        box=wx.MessageDialog(self, u"Realmente Desea Salir ?","Advertencia", wx.YES_NO | wx.ICON_QUESTION)
        if box.ShowModal()==wx.ID_YES:
            self.Close()

    def FramePrincipalOnClose(self, event):
        self.limpiarPantalla()
        app.limpiarFotos()
        self.Destroy()



class RecuerdaPass(FrameRecuerdaPass):
    """
    Clase para recuperar contraseñas
    """

    def IniciarFrame(self):
        app.IconizarFrames(self)

    def txtRespPreguntaSegOnTextEnter( self, event ):
        self.mostrarPass(self.choicePreguntaSeg.GetStringSelection(), self.txtRespPreguntaSeg.GetValue())


    def mostrarPass(self, pregunta, respuesta):
        passRecuperado=app.BD.recordarPass(pregunta, respuesta)
        if passRecuperado is not None:
            mensaje=wx.MessageDialog(self,u'Nombre de usuario y Contraseña Recuperados:\n\nNombre de Usuario: %s\n\nContraseña: %s'%(passRecuperado[0], passRecuperado[1]),u"Recuperando Contraseña", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'Respuesta Incorrecta',u"Recuperando Contraseña", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnAcettarRecuerdaPassOnButtonClick( self, event ):
       self.mostrarPass(self.choicePreguntaSeg.GetStringSelection(), self.txtRespPreguntaSeg.GetValue())


    def btnCancelarRecuerdaPassOnButtonClick( self, event ):
        self.Close()


class FInicio(FrameLogin):
    """
    clase destinada a manejar todo lo referente a la ventana de Login del Sistema
    """

    def IniciarApp(self):
        try:
            self.usuario=string.lower(self.txtNomUsuario.GetValue())
            self.password=self.txtPass.GetValue()
            hashClave = hashlib.md5()
            hashClave.update(self.txtPass.GetValue())

            #Verificamos el Usuario Correcto en la app.BD

            sesion=app.BD.verificaUsuario(self.usuario,self.password)
            #sesion=app.BD.verificaUsuario(self.usuario,hashClave.hexdigest())
            if sesion:
                ventanaPrincipal = FPrincipal(None)
                app.SetTopWindow(ventanaPrincipal)
                ventanaPrincipal.IdUconectado=sesion[0]
                ventanaPrincipal.nomUconectado=sesion[1]
                ventanaPrincipal.IniciarSizers()
                ventanaPrincipal.Show()
                self.Close()
            else:
                mensajeError=wx.MessageDialog(self, 'Este usuario no existe. \n\nDesea Intentar de nuevo?.',"Error", wx.YES_NO|wx.ICON_QUESTION)
                if mensajeError.ShowModal()==wx.ID_NO:
                    self.Close()
                else:
                    self.txtNomUsuario.Clear()
                    self.txtPass.Clear()
                    self.txtNomUsuario.SetFocus()
        except lite.Error, e:
            #error, sacamos dialogo y decimos que hagan configuracion
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'Error en la conección a la base de Datos. \nIntente de nuevo o haga click en "Cancelar" para salir. \n\n%s'%e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtNomUsuario.Clear()
            self.txtPass.Clear()
            self.txtNomUsuario.SetFocus()
            app.BD.cnn.rollback()
            app.BD.desconectar()
        except UnicodeEncodeError,e:
            #error, sacamos dialogo y decimos que hagan configuracion
            mensaje=wx.MessageDialog(self,u'La contraseña no debe contener caracteres especiales. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtNomUsuario.Clear()
            self.txtPass.Clear()
            self.txtNomUsuario.SetFocus()

    def btnIniciarAplicacionOnButtonClick(self, event):
        self.IniciarApp()


    def txtPassOnTextEnter(self, event):
        self.IniciarApp()


    def btnCancelarAplicacionOnButtonClick(self, event):
        box = wx.MessageDialog(self, "Realmente Desea Salir ?", "Advertencia", wx.YES_NO | wx.ICON_QUESTION)
        if box.ShowModal() == wx.ID_YES:
            self.Close()
            event.Skip()

    def FrameLoginOnClose(self,event):
        self.Destroy()

    def txtContrasenaOnTextEnter(self, event):
        self.IniciarApp()

    def btnRecordarPassOnButtonClick( self, event ):
        ventanaRecordarPass=RecuerdaPass(self)
        ventanaRecordarPass.Show()
        ventanaRecordarPass.IniciarFrame()



#####################################################
## DECLARACION DEL APPLICATION OBJECT
#####################################################
class App(wx.App):

    def __init__(self, redirect=False, filename='log.log'):
        wx.App.__init__(self, redirect, filename)

    def mostrarSplash(self):
        """
        Muestra un Splash de Bienvenida
        """
        pn = os.path.normpath(os.path.join(bitmapDir, "LogoSistema.jpg"))
        image = wx.Image(pn, wx.BITMAP_TYPE_JPEG)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 3000, None, -1)
        wx.Yield()

    def limpiarDirectorios(self):
        listaDir=os.listdir(tempDir)
        if listaDir != []:
            for item in listaDir:
                if not item=='readme.txt':
                    try:
                        os.remove(os.path.join(tempDir, item))
                    except WindowsError:
                        pass

    def limpiarFotos(self):
        listaDir=os.listdir(profilePicDir)

        if 'Thumbs.db' in listaDir:
            listaDir.remove( 'Thumbs.db')

        fotos=[]
        fotosActivas=self.BD.buscarFoto(todos=True)

        if listaDir != [] and fotosActivas != []:
            for foto in fotosActivas:
                indice=string.find(foto[0],'FotoAlumno-')
                fotos.append(foto[0][indice:])

        for item in listaDir:
            if item not in fotos:
                os.remove(os.path.join(profilePicDir, item))

    def IconizarFrames(self, win):
        icon = os.path.normpath(os.path.join(iconDir, "favicon.ico"))

        favicon = wx.Icon(icon, wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.SetIcon(win, favicon)


    def OnInit(self):

        self.BD=ModeloBD()
        self.reporte=Reportes()

        self.SetExitOnFrameDelete (True)

        if self.BD.ContarRegistrosAdmin() == 0:
            mywiz = WizardInicio(None)
            mywiz.RunWizard(mywiz.page1ConfigInicial)
            mywiz.txtNucleo.SetFocus()
            mywiz.Destroy()
        else:
            self.frameInicio = FInicio(None)
            self.IconizarFrames(self.frameInicio)

            self.mostrarSplash()
            self.frameInicio.Show()
            self.frameInicio.txtNomUsuario.SetFocus()
        return True

    def OnExit(self):
        self.limpiarDirectorios()
        self.limpiarFotos()


#######################
########LLAMADA PRINCIPAL
#######################

if __name__ == '__main__':
    logging.basicConfig(filename='logSistemaALumnos.log', filemode='w', format='%(asctime)s : %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    app = App(redirect=False)
    app.MainLoop()
