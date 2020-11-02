# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.wizard

ID_CARGAR_ALUMNOS = 1000
ID_EDITAR_ALUMNOS = 1001
ID_ELIMINAR_ALUMNO = 1002
ID_REPORTE_DE_ALUMNOS_POR_PROFESOR = 1003
ID_FICHA_DE_ALUMNO = 1004
ID_REPORTE_GENERAL = 1005
ID_LICENCIA = 1006
ID_ACERCA_DE = 1007

###########################################################################
## Class WizardConfigInicial
###########################################################################

class WizardConfigInicial ( wx.wizard.Wizard ):
	
	def __init__( self, parent ):
		wx.wizard.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuración Inicial del Sistema de Gestión de Plantilla de Alumnos", bitmap = wx.Bitmap( u"bitmaps/logoWizard.png", wx.BITMAP_TYPE_ANY ), pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_pages = []
		
		self.page1ConfigInicial = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.page1ConfigInicial )
		
		bSizer100 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText56 = wx.StaticText( self.page1ConfigInicial, wx.ID_ANY, u"Nombre del Núcleo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		bSizer100.Add( self.m_staticText56, 0, wx.ALL, 5 )
		
		self.txtNucleo = wx.TextCtrl( self.page1ConfigInicial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.txtNucleo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText57 = wx.StaticText( self.page1ConfigInicial, wx.ID_ANY, u"Entidad Federal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		bSizer100.Add( self.m_staticText57, 0, wx.ALL, 5 )
		
		choiceEntFedChoices = [ u"Selecione una Entidad Federal", u"Distrito Capital", u"Amazonas", u"Anzoátegui", u"Apure", u"Aragua", u"Barinas", u"Bolívar", u"Carabobo", u"Cojedes", u"Delta Amacuro", u"Falcón", u"Guárico", u"Lara", u"Mérida", u"Miranda", u"Monagas", u"Nueva Esparta", u"Portuguesa", u"Sucre", u"Táchira", u"Trujillo", u"Vargas", u"Yaracuy", u"Zulia" ]
		self.choiceEntFed = wx.Choice( self.page1ConfigInicial, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceEntFedChoices, 0 )
		self.choiceEntFed.SetSelection( 0 )
		bSizer100.Add( self.choiceEntFed, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText58 = wx.StaticText( self.page1ConfigInicial, wx.ID_ANY, u"Municipio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		bSizer100.Add( self.m_staticText58, 0, wx.ALL, 5 )
		
		choiceMunicipioChoices = []
		self.choiceMunicipio = wx.Choice( self.page1ConfigInicial, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceMunicipioChoices, 0 )
		self.choiceMunicipio.SetSelection( 0 )
		bSizer100.Add( self.choiceMunicipio, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.page1ConfigInicial.SetSizer( bSizer100 )
		self.page1ConfigInicial.Layout()
		bSizer100.Fit( self.page1ConfigInicial )
		self.page2ConfigInicial = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.page2ConfigInicial )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText59 = wx.StaticText( self.page2ConfigInicial, wx.ID_ANY, u"Nombre de Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		bSizer101.Add( self.m_staticText59, 0, wx.ALL, 5 )
		
		self.txtUsuarioAdmin = wx.TextCtrl( self.page2ConfigInicial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.txtUsuarioAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText60 = wx.StaticText( self.page2ConfigInicial, wx.ID_ANY, u"Contraseña", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		bSizer101.Add( self.m_staticText60, 0, wx.ALL, 5 )
		
		self.txtPassAdmin = wx.TextCtrl( self.page2ConfigInicial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.txtPassAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.page2ConfigInicial.SetSizer( bSizer101 )
		self.page2ConfigInicial.Layout()
		bSizer101.Fit( self.page2ConfigInicial )
		self.page3ConfigInicial = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.page3ConfigInicial )
		
		bSizer102 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText61 = wx.StaticText( self.page3ConfigInicial, wx.ID_ANY, u"Pregunta de Seguridad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		bSizer102.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		choicePreguntaSegChoices = [ u"Seleccione...", u"Cual es mi segundo Nombre?", u"Cual es el apellido de soltera de mi madre?", u"Cual es el apellido de soltero de mi padre?", u"Cual es el nombre de mi mascota?" ]
		self.choicePreguntaSeg = wx.Choice( self.page3ConfigInicial, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePreguntaSegChoices, 0 )
		self.choicePreguntaSeg.SetSelection( 0 )
		bSizer102.Add( self.choicePreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText62 = wx.StaticText( self.page3ConfigInicial, wx.ID_ANY, u"Respuesta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		bSizer102.Add( self.m_staticText62, 0, wx.ALL, 5 )
		
		self.txtRespuestaSeg = wx.TextCtrl( self.page3ConfigInicial, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer102.Add( self.txtRespuestaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.page3ConfigInicial.SetSizer( bSizer102 )
		self.page3ConfigInicial.Layout()
		bSizer102.Fit( self.page3ConfigInicial )
		self.page4ConfigInicial = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.page4ConfigInicial )
		
		bSizer103 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.page4ConfigInicial.SetSizer( bSizer103 )
		self.page4ConfigInicial.Layout()
		bSizer103.Fit( self.page4ConfigInicial )
		self.Centre( wx.BOTH )
		
		
		# Connect Events
		self.Bind( wx.wizard.EVT_WIZARD_CANCEL, self.WizardConfigInicialOnWizardCancel )
		self.Bind( wx.wizard.EVT_WIZARD_FINISHED, self.WizardConfigInicialOnWizardFinished )
		self.Bind( wx.wizard.EVT_WIZARD_PAGE_CHANGING, self.WizardConfigInicialOnWizardPageChanging )
		self.choiceEntFed.Bind( wx.EVT_CHOICE, self.choiceEntFedOnChoice )
	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def WizardConfigInicialOnWizardCancel( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardFinished( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardPageChanging( self, event ):
		event.Skip()
	
	def choiceEntFedOnChoice( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameLogin
###########################################################################

class FrameLogin ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ingresar al Sistema", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Nombre de Usuario" ), wx.VERTICAL )
		
		self.txtNomUsuario = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.txtNomUsuario, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( sbSizer1 )
		self.m_panel1.Layout()
		sbSizer1.Fit( self.m_panel1 )
		bSizer6.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel2 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Contraseña" ), wx.VERTICAL )
		
		self.txtPass = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		sbSizer3.Add( self.txtPass, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( sbSizer3 )
		self.m_panel2.Layout()
		sbSizer3.Fit( self.m_panel2 )
		bSizer6.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.btnIniciarAplicacion = wx.Button( self.m_panel4, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnIniciarAplicacion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCancelarAplicacion = wx.Button( self.m_panel4, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btnCancelarAplicacion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel4.SetSizer( gSizer1 )
		self.m_panel4.Layout()
		gSizer1.Fit( self.m_panel4 )
		bSizer6.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel6 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.btnRecordarPass = wx.Button( self.m_panel3, wx.ID_ANY, u"Olvidó su Contraseña??", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.btnRecordarPass, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer6.Add( bSizer7, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		
		self.m_panel3.SetSizer( bSizer6 )
		self.m_panel3.Layout()
		bSizer6.Fit( self.m_panel3 )
		bSizer5.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameLoginOnClose )
		self.txtPass.Bind( wx.EVT_TEXT_ENTER, self.txtPassOnTextEnter )
		self.btnIniciarAplicacion.Bind( wx.EVT_BUTTON, self.btnIniciarAplicacionOnButtonClick )
		self.btnCancelarAplicacion.Bind( wx.EVT_BUTTON, self.btnCancelarAplicacionOnButtonClick )
		self.btnRecordarPass.Bind( wx.EVT_BUTTON, self.btnRecordarPassOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameLoginOnClose( self, event ):
		event.Skip()
	
	def txtPassOnTextEnter( self, event ):
		event.Skip()
	
	def btnIniciarAplicacionOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarAplicacionOnButtonClick( self, event ):
		event.Skip()
	
	def btnRecordarPassOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Gestión de Plantilla de Alumnos", pos = wx.DefaultPosition, size = wx.Size( 1200,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.salir = wx.MenuItem( self.m_menu1, wx.ID_EXIT, u"Salir", u"Salir de la Aplicación", wx.ITEM_NORMAL )
		self.salir.SetBitmap( wx.Bitmap( u"icon/salir.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu1.AppendItem( self.salir )
		
		self.m_menubar1.Append( self.m_menu1, u"Aplicación" ) 
		
		self.m_menu2 = wx.Menu()
		self.cargarAlumnos = wx.MenuItem( self.m_menu2, ID_CARGAR_ALUMNOS, u"Cargar Alumnos", u"seleccione para cargar alumnos al sistema", wx.ITEM_NORMAL )
		self.cargarAlumnos.SetBitmap( wx.Bitmap( u"icon/agregar_usuario.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.AppendItem( self.cargarAlumnos )
		
		self.editarAlumnos = wx.MenuItem( self.m_menu2, ID_EDITAR_ALUMNOS, u"Editar Alumnos", u"seleccione para Editar alumnos en el  sistema", wx.ITEM_NORMAL )
		self.editarAlumnos.SetBitmap( wx.Bitmap( u"icon/editar.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.AppendItem( self.editarAlumnos )
		
		self.eliminarAlumno = wx.MenuItem( self.m_menu2, ID_ELIMINAR_ALUMNO, u"Eliminar Alumno", u"Seleccione para eliminar uno o mas alumnos del Sistema", wx.ITEM_NORMAL )
		self.eliminarAlumno.SetBitmap( wx.Bitmap( u"icon/remover_usuario.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.AppendItem( self.eliminarAlumno )
		
		self.m_menubar1.Append( self.m_menu2, u"Alumnos" ) 
		
		self.m_menu3 = wx.Menu()
		self.reporteDeAlumnosPorProfesor = wx.MenuItem( self.m_menu3, ID_REPORTE_DE_ALUMNOS_POR_PROFESOR, u"Reporte de Alumnos por Profesor", wx.EmptyString, wx.ITEM_NORMAL )
		self.reporteDeAlumnosPorProfesor.SetBitmap( wx.Bitmap( u"icon/clipboard-warning-16-ns.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.reporteDeAlumnosPorProfesor )
		
		self.fichaDeAlumno = wx.MenuItem( self.m_menu3, ID_FICHA_DE_ALUMNO, u"Ficha de Alumno", u"Selecione para crear la Ficha personal del Alumno", wx.ITEM_NORMAL )
		self.fichaDeAlumno.SetBitmap( wx.Bitmap( u"icon/rep_Prof.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.fichaDeAlumno )
		
		self.reporteGeneral = wx.MenuItem( self.m_menu3, ID_REPORTE_GENERAL, u"Reporte General", wx.EmptyString, wx.ITEM_NORMAL )
		self.reporteGeneral.SetBitmap( wx.Bitmap( u"icon/rep_catedra.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.reporteGeneral )
		
		self.m_menubar1.Append( self.m_menu3, u"Reportes" ) 
		
		self.info = wx.Menu()
		self.licencia = wx.MenuItem( self.info, ID_LICENCIA, u"Licencia", u"Muestra Informacion de Licencia", wx.ITEM_NORMAL )
		self.licencia.SetBitmap( wx.Bitmap( u"icon/comment-16-ns.png", wx.BITMAP_TYPE_ANY ) )
		self.info.AppendItem( self.licencia )
		
		self.acercaDe = wx.MenuItem( self.info, ID_ACERCA_DE, u"Acerca de..", wx.EmptyString, wx.ITEM_NORMAL )
		self.acercaDe.SetBitmap( wx.Bitmap( u"icon/infoabout22.png", wx.BITMAP_TYPE_ANY ) )
		self.info.AppendItem( self.acercaDe )
		
		self.m_menubar1.Append( self.info, u"Info" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORZ_LAYOUT|wx.TB_TEXT, wx.ID_ANY ) 
		self.m_toolBar1.AddLabelTool( ID_CARGAR_ALUMNOS, u"Agregar Alumno", wx.Bitmap( u"icon/person-plus-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.AddLabelTool( ID_EDITAR_ALUMNOS, u"Editar Alumno", wx.Bitmap( u"icon/page-pencil-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.AddLabelTool( ID_ELIMINAR_ALUMNO, u"Eliminar Alumno", wx.Bitmap( u"icon/person-minus-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.Realize() 
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FramePrincipalOnClose )
		self.Bind( wx.EVT_MENU, self.salirOnMenuSelection, id = self.salir.GetId() )
		self.Bind( wx.EVT_MENU, self.cargarAlumnosOnMenuSelection, id = self.cargarAlumnos.GetId() )
		self.Bind( wx.EVT_MENU, self.editarAlumnosOnMenuSelection, id = self.editarAlumnos.GetId() )
		self.Bind( wx.EVT_MENU, self.eliminarAlumnoOnMenuSelection, id = self.eliminarAlumno.GetId() )
		self.Bind( wx.EVT_MENU, self.reporteDeAlumnosPorProfesorOnMenuSelection, id = self.reporteDeAlumnosPorProfesor.GetId() )
		self.Bind( wx.EVT_MENU, self.fichaDeAlumnoOnMenuSelection, id = self.fichaDeAlumno.GetId() )
		self.Bind( wx.EVT_MENU, self.reporteGeneralOnMenuSelection, id = self.reporteGeneral.GetId() )
		self.Bind( wx.EVT_MENU, self.licenciaOnMenuSelection, id = self.licencia.GetId() )
		self.Bind( wx.EVT_MENU, self.acercaDeOnMenuSelection, id = self.acercaDe.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FramePrincipalOnClose( self, event ):
		event.Skip()
	
	def salirOnMenuSelection( self, event ):
		event.Skip()
	
	def cargarAlumnosOnMenuSelection( self, event ):
		event.Skip()
	
	def editarAlumnosOnMenuSelection( self, event ):
		event.Skip()
	
	def eliminarAlumnoOnMenuSelection( self, event ):
		event.Skip()
	
	def reporteDeAlumnosPorProfesorOnMenuSelection( self, event ):
		event.Skip()
	
	def fichaDeAlumnoOnMenuSelection( self, event ):
		event.Skip()
	
	def reporteGeneralOnMenuSelection( self, event ):
		event.Skip()
	
	def licenciaOnMenuSelection( self, event ):
		event.Skip()
	
	def acercaDeOnMenuSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameRecuerdaPass
###########################################################################

class FrameRecuerdaPass ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Recuperación de Contraseña", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel11 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Pregunta de Seguidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer11.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		choicePreguntaSegChoices = [ u"Cual es mi segundo Nombre?", u"Cual es el apellido de soltera de mi madre?", u"Cual es el apellido de soltero de mi padre?", u"Cual es el nombre de mi mascota?" ]
		self.choicePreguntaSeg = wx.Choice( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePreguntaSegChoices, 0 )
		self.choicePreguntaSeg.SetSelection( 0 )
		bSizer11.Add( self.choicePreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer11 )
		self.m_panel11.Layout()
		bSizer11.Fit( self.m_panel11 )
		bSizer10.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel12 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText10 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Respuesta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer12.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.txtRespPreguntaSeg = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer12.Add( self.txtRespPreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel12.SetSizer( bSizer12 )
		self.m_panel12.Layout()
		bSizer12.Fit( self.m_panel12 )
		bSizer10.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.btnAcettarRecuerdaPass = wx.Button( self.m_panel13, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnAcettarRecuerdaPass, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCancelarRecuerdaPass = wx.Button( self.m_panel13, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnCancelarRecuerdaPass, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel13.SetSizer( gSizer2 )
		self.m_panel13.Layout()
		gSizer2.Fit( self.m_panel13 )
		bSizer10.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel10.SetSizer( bSizer10 )
		self.m_panel10.Layout()
		bSizer10.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtRespPreguntaSeg.Bind( wx.EVT_TEXT_ENTER, self.txtRespPreguntaSegOnTextEnter )
		self.btnAcettarRecuerdaPass.Bind( wx.EVT_BUTTON, self.btnAcettarRecuerdaPassOnButtonClick )
		self.btnCancelarRecuerdaPass.Bind( wx.EVT_BUTTON, self.btnCancelarRecuerdaPassOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtRespPreguntaSegOnTextEnter( self, event ):
		event.Skip()
	
	def btnAcettarRecuerdaPassOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarRecuerdaPassOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelBienvenida
###########################################################################

class PanelBienvenida ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.Point( 240,10 ), size = wx.Size( 1090,987 ), style = wx.TAB_TRAVERSAL )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel121 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15.Add( self.m_panel121, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline5 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel14 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel14, wx.ID_ANY, wx.Bitmap( u"bitmaps/cabecera.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel14.SetSizer( bSizer151 )
		self.m_panel14.Layout()
		bSizer151.Fit( self.m_panel14 )
		bSizer15.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel12.SetSizer( bSizer15 )
		self.m_panel12.Layout()
		bSizer15.Fit( self.m_panel12 )
		bSizer13.Add( self.m_panel12, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer13 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelCargaAlumno
###########################################################################

class PanelCargaAlumno ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1090,987 ), style = wx.TAB_TRAVERSAL )
		
		self.Hide()
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Carga de Alumnos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		self.m_staticText63.SetFont( wx.Font( 20, 74, 90, 90, False, "MS Shell Dlg 2" ) )
		
		bSizer15.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer48 = wx.BoxSizer( wx.VERTICAL )
		
		self.notebookAlumno = wx.Notebook( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scrolledDatos = wx.ScrolledWindow( self.notebookAlumno, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrolledDatos.SetScrollRate( 10, 5 )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelDatosAlumnos = wx.Panel( self.scrolledDatos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer145 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelFoto_Carga = wx.Panel( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1471 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapFoto = wx.StaticBitmap( self.panelFoto_Carga, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 160,120 ), wx.SUNKEN_BORDER )
		bSizer1471.Add( self.bitmapFoto, 0, wx.ALL, 5 )
		
		self.btnFoto_Carga = wx.Button( self.panelFoto_Carga, wx.ID_ANY, u"Cargar Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1471.Add( self.btnFoto_Carga, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFoto_Carga.SetSizer( bSizer1471 )
		self.panelFoto_Carga.Layout()
		bSizer1471.Fit( self.panelFoto_Carga )
		bSizer145.Add( self.panelFoto_Carga, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer145, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), 0, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText311 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos del Alumno", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		self.m_staticText311.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer191.Add( self.m_staticText311, 0, wx.ALL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
		bSizer191.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer191, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Apellidos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer24.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.txtApeAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.txtApeAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText158 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nombres", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText158.Wrap( -1 )
		bSizer24.Add( self.m_staticText158, 0, wx.ALL, 5 )
		
		self.txtNomAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.txtNomAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"C.I", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer24.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.txtCiAlumno_Carga=wx.lib.masked.TextCtrl(self.panelDatosAlumnos, -1, '',size=(130, -1), mask = '########')
		bSizer24.Add( self.txtCiAlumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText20 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Lugar de Nacimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer25.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.txtLugarNacAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtLugarNacAlumno_Carga.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer25.Add( self.txtLugarNacAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Fecha de Nacimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer25.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.datePickerFechaNacAlumno_Carga = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer25.Add( self.datePickerFechaNacAlumno_Carga, 0, wx.ALL, 5 )
		
		radioSexoAlumno_CargaChoices = [ u"Masculino", u"Femenino" ]
		self.radioSexoAlumno_Carga = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Sexo", wx.DefaultPosition, wx.DefaultSize, radioSexoAlumno_CargaChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioSexoAlumno_Carga.SetSelection( 0 )
		bSizer25.Add( self.radioSexoAlumno_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Edad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer25.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.txtEdadAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.txtEdadAlumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		bSizer124 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText159 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Fecha de Ingreso (menor o igual a la fecha actual)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText159.Wrap( -1 )
		self.m_staticText159.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer124.Add( self.m_staticText159, 0, wx.ALL, 5 )
		
		self.datePickerFechaIngAlumno_Carga = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.datePickerFechaIngAlumno_Carga.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.datePickerFechaIngAlumno_Carga.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer124.Add( self.datePickerFechaIngAlumno_Carga, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer124, 0, wx.EXPAND, 5 )
		
		bSizer282 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText364 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText364.Wrap( -1 )
		self.m_staticText364.SetFont( wx.Font( 10, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer282.Add( self.m_staticText364, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer282, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText24 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Municipio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer29.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.txtDirMunicipioAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirMunicipioAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Parroquia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer29.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.txtDirParroquiaAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirParroquiaAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Sector", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer29.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.txtDirSectorAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirSectorAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Urb./Barrio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		bSizer29.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.txtDirUrbarrioAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirUrbarrioAlumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText28 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Avenida", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer30.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.txtDirAvenidaAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirAvenidaAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Calle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer30.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.txtDirCalleAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirCalleAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Edificio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		bSizer30.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.txtDirEdificioAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirEdificioAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"#Casa/Apto.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		bSizer30.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.txtDirCasaAptoAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirCasaAptoAlumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer30, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText32 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Punto de Referencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		bSizer32.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.txtDirPtoRefAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.txtDirPtoRefAlumno_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText33 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Hab", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		bSizer33.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.txtDirTelHabAlumno_Carga=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer33.Add( self.txtDirTelHabAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Celular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		bSizer33.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.txtDirTelCelAlumno_Carga=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer33.Add( self.txtDirTelCelAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		bSizer33.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.txtDirEmailalumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.txtDirEmailalumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer33, 0, wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer26, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer130 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline5 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer130.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText281 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos del Representante", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )
		self.m_staticText281.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer130.Add( self.m_staticText281, 0, wx.ALL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer130.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer130, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		bSizer251 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer291 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText321 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Apellidos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText321.Wrap( -1 )
		bSizer291.Add( self.m_staticText321, 0, wx.ALL, 5 )
		
		self.txtApeRepAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer291.Add( self.txtApeRepAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText160 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nombres", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText160.Wrap( -1 )
		bSizer291.Add( self.m_staticText160, 0, wx.ALL, 5 )
		
		self.txtNombreRepAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer291.Add( self.txtNombreRepAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText331 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"C.I", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText331.Wrap( -1 )
		bSizer291.Add( self.m_staticText331, 0, wx.ALL, 5 )
		
		self.txtCiRep_Carga=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '',size=(130, -1), mask = '########')
		bSizer291.Add( self.txtCiRep_Carga, 1, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer291, 0, wx.EXPAND, 5 )
		
		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText322 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección Habitación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText322.Wrap( -1 )
		bSizer321.Add( self.m_staticText322, 0, wx.ALL, 5 )
		
		self.txtDirHabRep_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer321.Add( self.txtDirHabRep_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer251.Add( bSizer321, 0, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText37 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Hab", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		bSizer34.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.txtTelHabRep_Carga=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer34.Add( self.txtTelHabRep_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Celular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		bSizer34.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.txtTelCelRep_Carga=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer34.Add( self.txtTelCelRep_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer34.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.txtEmailRep_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.txtEmailRep_Carga, 1, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer3211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3221 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección Trabajo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3221.Wrap( -1 )
		bSizer3211.Add( self.m_staticText3221, 0, wx.ALL, 5 )
		
		self.txtDirTrabajoRep_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer3211.Add( self.txtDirTrabajoRep_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer251.Add( bSizer3211, 0, wx.EXPAND, 5 )
		
		bSizer341 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText371 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Trabajo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		bSizer341.Add( self.m_staticText371, 0, wx.ALL, 5 )
		
		self.txtTelTrabajoRep_Carga=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer341.Add( self.txtTelTrabajoRep_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText381 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Ocupación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )
		bSizer341.Add( self.m_staticText381, 0, wx.ALL, 5 )
		
		self.txtOcupacionRep_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer341.Add( self.txtOcupacionRep_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText391 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Parentesco", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )
		bSizer341.Add( self.m_staticText391, 0, wx.ALL, 5 )
		
		self.txtParentescoRep_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer341.Add( self.txtParentescoRep_Carga, 1, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer341, 0, wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer251, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline8 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer131.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText291 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos Académicos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )
		self.m_staticText291.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer131.Add( self.m_staticText291, 0, wx.ALL, 5 )
		
		self.m_staticline9 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer131.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer131, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		bSizer261 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioEstudiaAlumno_CargaChoices = [ u"Si", u"No" ]
		self.radioEstudiaAlumno_Carga = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Estudia Actualmente", wx.DefaultPosition, wx.DefaultSize, radioEstudiaAlumno_CargaChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioEstudiaAlumno_Carga.SetSelection( 0 )
		bSizer41.Add( self.radioEstudiaAlumno_Carga, 1, wx.ALL, 5 )
		
		radioEducacionAlumno_CargaChoices = [ u"Media", u"Básica", u"Diversificada", u"Universitaria" ]
		self.radioEducacionAlumno_Carga = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Nivel de Educación", wx.DefaultPosition, wx.DefaultSize, radioEducacionAlumno_CargaChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioEducacionAlumno_Carga.SetSelection( 2 )
		bSizer41.Add( self.radioEducacionAlumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer261.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText48 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Grado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		bSizer42.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.txtGradoAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtGradoAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Año", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer42.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.txtAnioAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtAnioAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Semestre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		bSizer42.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		self.txtSemestreAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtSemestreAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Institución", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		bSizer42.Add( self.m_staticText52, 0, wx.ALL, 5 )
		
		self.txtInstitAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtInstitAlumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer261.Add( bSizer42, 0, wx.EXPAND, 5 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText53 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		bSizer43.Add( self.m_staticText53, 0, wx.ALL, 5 )
		
		self.txtDireccionInstitAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.txtDireccionInstitAlumno_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer261.Add( bSizer43, 0, wx.EXPAND, 5 )
		
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		bSizer44.Add( self.m_staticText54, 0, wx.ALL, 5 )
		
		self.txtTelefonoInstitAlumno_Carga=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer44.Add( self.txtTelefonoInstitAlumno_Carga, 1, wx.ALL, 5 )
		
		radioTipoInstitAlumno_CargaChoices = [ u"Pública", u"Privada" ]
		self.radioTipoInstitAlumno_Carga = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Tipo de Institución", wx.DefaultPosition, wx.DefaultSize, radioTipoInstitAlumno_CargaChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioTipoInstitAlumno_Carga.SetSelection( 0 )
		bSizer44.Add( self.radioTipoInstitAlumno_Carga, 1, wx.ALL, 5 )
		
		
		bSizer261.Add( bSizer44, 0, wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer261, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer132 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline10 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer132.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText301 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos Musicales", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )
		self.m_staticText301.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer132.Add( self.m_staticText301, 0, wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer132.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer132, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioConocMusAlumno_CargaChoices = [ u"Si", u"No" ]
		self.radioConocMusAlumno_Carga = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Conocimientos Musicales", wx.DefaultPosition, wx.DefaultSize, radioConocMusAlumno_CargaChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioConocMusAlumno_Carga.SetSelection( 0 )
		bSizer45.Add( self.radioConocMusAlumno_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText55 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Catedra a Cursar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		bSizer45.Add( self.m_staticText55, 0, wx.ALL, 5 )
		
		self.catedras = [u"Ritmo y Entonación",
		"Lenguaje Musical",
		u"Historia de la Música",
		u"Armonía y Contrapunto",
		"Coro",
		u"Canto Lírico",
		"Piano Principal",
		"Piano Complementario",
		"Flauta Dulce",
		u"Violín",
		"Viola",
		"Violoncello",
		"Contrabajo",
		"Flauta Trasversa",
		"Oboe",
		"Clarinete",
		"Fagot",
		"Corno",
		"Trompeta",
		u"Trombón",
		"Tuba",
		u"Saxofón",
		u"Batería",
		u"Percusión",
		u"Dirección Orquestal"]
		self.checkCatedras_carga=wx.CheckListBox( self.panelDatosAlumnos, -1, (80, 50), (200, 80),self.catedras)
		
		
		bSizer45.Add( self.checkCatedras_carga, 0, wx.ALL, 5 )
		
		self.m_staticText58 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nivel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		bSizer45.Add( self.m_staticText58, 0, wx.ALL, 5 )
		
		self.txtNivelOrqAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,80 ), 0 )
		bSizer45.Add( self.txtNivelOrqAlumno_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText59 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		bSizer45.Add( self.m_staticText59, 0, wx.ALL, 5 )
		
		self.txtProfAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer45.Add( self.txtProfAlumno_Carga, 1, wx.ALL, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.panelDatosAlumnos, wx.ID_ANY, u"Status Académico" ), wx.VERTICAL )
		
		choiceStatusAlumno_CargaChoices = [ u"Selecione....", u"Alumno Regular", u"Alumno Nuevo Ingreso" ]
		self.choiceStatusAlumno_Carga = wx.Choice( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceStatusAlumno_CargaChoices, 0 )
		self.choiceStatusAlumno_Carga.SetSelection( 0 )
		sbSizer3.Add( self.choiceStatusAlumno_Carga, 0, wx.ALL, 5 )
		
		
		bSizer45.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer45, 1, wx.EXPAND, 5 )
		
		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText57 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Orquesta a la que Pertenece", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		bSizer46.Add( self.m_staticText57, 0, wx.ALL, 5 )
		
		choiceOrquAlumno_CargaChoices = [ u"Escoja una Orquesta.....", u"Juvenil \"A\"", u"Juvenil \"B\"", u"Ninguna" ]
		self.choiceOrquAlumno_Carga = wx.Choice( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceOrquAlumno_CargaChoices, 0 )
		self.choiceOrquAlumno_Carga.SetSelection( 0 )
		bSizer46.Add( self.choiceOrquAlumno_Carga, 1, wx.ALL, 5 )
		
		radioInstPropioAlumno_CargaChoices = [ u"Si", u"No" ]
		self.radioInstPropioAlumno_Carga = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Instrumento Propio", wx.DefaultPosition, wx.DefaultSize, radioInstPropioAlumno_CargaChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioInstPropioAlumno_Carga.SetSelection( 0 )
		bSizer46.Add( self.radioInstPropioAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText161 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Fecha de Asignación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer46.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		self.datepickerFecAsigInstAlumno_Carga = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer46.Add( self.datepickerFecAsigInstAlumno_Carga, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer46, 1, wx.EXPAND, 5 )
		
		bSizer281 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText360 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Marca del Instrumento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText360.Wrap( -1 )
		bSizer281.Add( self.m_staticText360, 0, wx.ALL, 5 )
		
		self.txtMarcaInstAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtMarcaInstAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText361 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )
		bSizer281.Add( self.m_staticText361, 0, wx.ALL, 5 )
		
		self.txtModeloInstAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtModeloInstAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText362 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Serial", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText362.Wrap( -1 )
		bSizer281.Add( self.m_staticText362, 0, wx.ALL, 5 )
		
		self.txtSerialInstAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtSerialInstAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText363 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nº de Activo Fijo FUNDAMUSICAL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText363.Wrap( -1 )
		bSizer281.Add( self.m_staticText363, 0, wx.ALL, 5 )
		
		self.txtNumActFijoInstAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtNumActFijoInstAlumno_Carga, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer281, 1, wx.EXPAND, 5 )
		
		bSizer47 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioOtraAgrupAlumno_CargaChoices = [ u"Si", u"No" ]
		self.radioOtraAgrupAlumno_Carga = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Pertenece a Otra Agrupación?", wx.DefaultPosition, wx.DefaultSize, radioOtraAgrupAlumno_CargaChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioOtraAgrupAlumno_Carga.SetSelection( 0 )
		bSizer47.Add( self.radioOtraAgrupAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		bSizer47.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.txtNombreOtraAgrupAlumno_Carga = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer47.Add( self.txtNombreOtraAgrupAlumno_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText62 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"fecha de Ingreso", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		bSizer47.Add( self.m_staticText62, 0, wx.ALL, 5 )
		
		self.datePickerFechaIngOtraAgrupAlumno_Carga = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer47.Add( self.datePickerFechaIngOtraAgrupAlumno_Carga, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer47, 1, wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer27, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelDatosAlumnos.SetSizer( gbSizer3 )
		self.panelDatosAlumnos.Layout()
		gbSizer3.Fit( self.panelDatosAlumnos )
		bSizer28.Add( self.panelDatosAlumnos, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.scrolledDatos.SetSizer( bSizer28 )
		self.scrolledDatos.Layout()
		bSizer28.Fit( self.scrolledDatos )
		self.notebookAlumno.AddPage( self.scrolledDatos, u"Datos Generales", True )
		self.scrolledMedica = wx.ScrolledWindow( self.notebookAlumno, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrolledMedica.SetScrollRate( 5, 5 )
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelMedicoALumnos = wx.Panel( self.scrolledMedica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer140 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3111 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Información General", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )
		self.m_staticText3111.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer141.Add( self.m_staticText3111, 0, wx.ALL, 5 )
		
		self.m_staticline33 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer141.Add( self.m_staticline33, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer141, 0, wx.EXPAND, 5 )
		
		bSizer142 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText190 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Tipo de Sangre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText190.Wrap( -1 )
		bSizer142.Add( self.m_staticText190, 0, wx.ALL, 5 )
		
		self.txtFMedTipoSangreAlumno_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer142.Add( self.txtFMedTipoSangreAlumno_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText191 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Antecedentes Generales", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		bSizer142.Add( self.m_staticText191, 0, wx.ALL, 5 )
		
		self.txtFMedAntecedAlumno_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		bSizer142.Add( self.txtFMedAntecedAlumno_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer142, 0, wx.EXPAND, 5 )
		
		bSizer146 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText196 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Vacunas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText196.Wrap( -1 )
		self.m_staticText196.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer146.Add( self.m_staticText196, 0, wx.ALL, 5 )
		
		self.m_staticline34 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer146.Add( self.m_staticline34, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer146, 0, wx.EXPAND, 5 )
		
		bSizer147 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedVacFA_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedVacFA_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Fiebre Amarilla", wx.DefaultPosition, wx.DefaultSize, radioFMedVacFA_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedVacFA_Carga.SetSelection( 0 )
		bSizer147.Add( self.radioFMedVacFA_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText197 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText197.Wrap( -1 )
		bSizer147.Add( self.m_staticText197, 0, wx.ALL, 5 )
		
		self.datePickerFMedVacFA_Carga = wx.DatePickerCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer147.Add( self.datePickerFMedVacFA_Carga, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer147, 0, wx.EXPAND, 5 )
		
		bSizer148 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedVacHA_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedVacHA_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Hepatitis \"A\"", wx.DefaultPosition, wx.DefaultSize, radioFMedVacHA_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedVacHA_Carga.SetSelection( 0 )
		bSizer148.Add( self.radioFMedVacHA_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText198 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText198.Wrap( -1 )
		bSizer148.Add( self.m_staticText198, 0, wx.ALL, 5 )
		
		self.datePickerFMedVacHA_Carga = wx.DatePickerCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer148.Add( self.datePickerFMedVacHA_Carga, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer148, 0, wx.EXPAND, 5 )
		
		bSizer149 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedVacHB_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedVacHB_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Hepatitis \"B\"", wx.DefaultPosition, wx.DefaultSize, radioFMedVacHB_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedVacHB_Carga.SetSelection( 0 )
		bSizer149.Add( self.radioFMedVacHB_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText199 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText199.Wrap( -1 )
		bSizer149.Add( self.m_staticText199, 0, wx.ALL, 5 )
		
		self.datePickerFMedVacHB_Carga = wx.DatePickerCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer149.Add( self.datePickerFMedVacHB_Carga, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer149, 0, wx.EXPAND, 5 )
		
		bSizer1461 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline341 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1461.Add( self.m_staticline341, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText1961 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Enfermedades", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1961.Wrap( -1 )
		self.m_staticText1961.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer1461.Add( self.m_staticText1961, 0, wx.ALL, 5 )
		
		self.m_staticline39 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1461.Add( self.m_staticline39, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer1461, 0, wx.EXPAND, 5 )
		
		bSizer154 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedEnfCab_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfCab_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Cabeza", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfCab_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfCab_Carga.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfCab_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfOid_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfOid_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Oído", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfOid_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfOid_Carga.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfOid_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfNar_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfNar_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Nariz", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfNar_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfNar_Carga.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfNar_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfGar_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfGar_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Garganta", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfGar_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfGar_Carga.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfGar_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfCor_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfCor_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Corazón", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfCor_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfCor_Carga.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfCor_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfPul_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfPul_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Pulmones", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfPul_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfPul_Carga.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfPul_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfVD_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfVD_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Vías Digestivas", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfVD_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfVD_Carga.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfVD_Carga, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer154, 0, wx.EXPAND, 5 )
		
		bSizer1541 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedEnfRi_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfRi_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Riñones", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfRi_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfRi_Carga.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfRi_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfHue_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfHue_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Huesos", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfHue_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfHue_Carga.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfHue_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfArt_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfArt_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Articulaciones", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfArt_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfArt_Carga.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfArt_Carga, 0, wx.ALL, 5 )
		
		radioFMedEnfEnd_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedEnfEnd_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Endocrinológico", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfEnd_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfEnd_Carga.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfEnd_Carga, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer1541, 0, wx.EXPAND, 5 )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText202 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Operaciones (Indique edad, lugar y tratamiento)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )
		bSizer158.Add( self.m_staticText202, 0, wx.ALL, 5 )
		
		self.txtFMedOperaciones_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer158.Add( self.txtFMedOperaciones_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer158, 0, wx.EXPAND, 5 )
		
		bSizer159 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline37 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer159.Add( self.m_staticline37, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText203 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Alergias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText203.Wrap( -1 )
		self.m_staticText203.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer159.Add( self.m_staticText203, 0, wx.ALL, 5 )
		
		self.m_staticline38 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer159.Add( self.m_staticline38, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer159, 0, wx.EXPAND, 5 )
		
		bSizer160 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText204 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Comidas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText204.Wrap( -1 )
		bSizer160.Add( self.m_staticText204, 0, wx.ALL, 5 )
		
		self.txtFMedAlerCom_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer160.Add( self.txtFMedAlerCom_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText205 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Medicamentos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText205.Wrap( -1 )
		bSizer160.Add( self.m_staticText205, 0, wx.ALL, 5 )
		
		self.txtFMedAlerMed_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer160.Add( self.txtFMedAlerMed_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText207 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Medicamento Específico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )
		bSizer160.Add( self.m_staticText207, 0, wx.ALL, 5 )
		
		self.txtFMedAlerMedEsp_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer160.Add( self.txtFMedAlerMedEsp_Carga, 1, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer160, 0, wx.EXPAND, 5 )
		
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline40 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer161.Add( self.m_staticline40, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText208 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Seguro Médico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )
		self.m_staticText208.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer161.Add( self.m_staticText208, 0, wx.ALL, 5 )
		
		self.m_staticline41 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer161.Add( self.m_staticline41, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer161, 0, wx.EXPAND, 5 )
		
		bSizer162 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedTieneSeguro_CargaChoices = [ u"Si", u"No" ]
		self.radioFMedTieneSeguro_Carga = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Tiene Seguro?", wx.DefaultPosition, wx.DefaultSize, radioFMedTieneSeguro_CargaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedTieneSeguro_Carga.SetSelection( 0 )
		bSizer162.Add( self.radioFMedTieneSeguro_Carga, 0, wx.ALL, 5 )
		
		self.m_staticText209 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Aseguradora", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )
		bSizer162.Add( self.m_staticText209, 0, wx.ALL, 5 )
		
		self.txtFMedAseg_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer162.Add( self.txtFMedAseg_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText210 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )
		bSizer162.Add( self.m_staticText210, 0, wx.ALL, 5 )
		
		self.txtFMedTelAseg_Carga=wx.lib.masked.TextCtrl( self.panelMedicoALumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer162.Add( self.txtFMedTelAseg_Carga, 1, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer162, 0, wx.EXPAND, 5 )
		
		bSizer163 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText211 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"En Caso de Emergencia, Llamar a", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer163.Add( self.m_staticText211, 0, wx.ALL, 5 )
		
		self.txtFMedTelEmerg_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer163.Add( self.txtFMedTelEmerg_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer163, 0, wx.EXPAND, 5 )
		
		bSizer166 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText212 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Unidad Médico asistencial de su Preferencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		bSizer166.Add( self.m_staticText212, 0, wx.ALL, 5 )
		
		self.txtFMedUnidadMedPref_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer166.Add( self.txtFMedUnidadMedPref_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer166, 0, wx.EXPAND, 5 )
		
		bSizer168 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText213 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Médico Tratante", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )
		bSizer168.Add( self.m_staticText213, 0, wx.ALL, 5 )
		
		self.txtFMedTratante_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer168.Add( self.txtFMedTratante_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText214 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )
		bSizer168.Add( self.m_staticText214, 0, wx.ALL, 5 )
		
		self.txtFMedTelTratante_Carga=wx.lib.masked.TextCtrl( self.panelMedicoALumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer168.Add( self.txtFMedTelTratante_Carga, 1, wx.ALL, 5 )
		
		self.m_staticText215 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Telf. Celular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )
		bSizer168.Add( self.m_staticText215, 0, wx.ALL, 5 )
		
		self.txtFMedCelTratante_Carga=wx.lib.masked.TextCtrl( self.panelMedicoALumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer168.Add( self.txtFMedCelTratante_Carga, 1, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer168, 0, wx.EXPAND, 5 )
		
		bSizer169 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText216 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"¿Su hijo presenta o ha presentado alguna enfermedad, u otro suceso médico importante no contemplado en esta planilla?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )
		bSizer169.Add( self.m_staticText216, 0, wx.ALL, 5 )
		
		self.m_staticText220 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Describalo a continuación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )
		bSizer169.Add( self.m_staticText220, 0, wx.ALL, 5 )
		
		self.txtFMedEnfPrevia_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer169.Add( self.txtFMedEnfPrevia_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer169, 0, wx.EXPAND, 5 )
		
		bSizer1691 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2161 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"¿Su hijo utiliza algún aparato, equipo o tratamiento especial en forma particular para tratamiento médico?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2161.Wrap( -1 )
		bSizer1691.Add( self.m_staticText2161, 0, wx.ALL, 5 )
		
		self.m_staticText221 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Infórmelo a continuación, anexe informe del especialista", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		bSizer1691.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		self.txtFMedAperato_Carga = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1691.Add( self.txtFMedAperato_Carga, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer1691, 0, wx.EXPAND, 5 )
		
		
		gbSizer5.Add( bSizer140, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		self.panelMedicoALumnos.SetSizer( gbSizer5 )
		self.panelMedicoALumnos.Layout()
		gbSizer5.Fit( self.panelMedicoALumnos )
		bSizer139.Add( self.panelMedicoALumnos, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.scrolledMedica.SetSizer( bSizer139 )
		self.scrolledMedica.Layout()
		bSizer139.Fit( self.scrolledMedica )
		self.notebookAlumno.AddPage( self.scrolledMedica, u"Ficha Médica", False )
		
		bSizer48.Add( self.notebookAlumno, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel18.SetSizer( bSizer48 )
		self.m_panel18.Layout()
		bSizer48.Fit( self.m_panel18 )
		bSizer15.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer49 = wx.BoxSizer( wx.VERTICAL )
		
		sdbSizerBtnGuardar = wx.StdDialogButtonSizer()
		self.sdbSizerBtnGuardarSave = wx.Button( self.m_panel19, wx.ID_SAVE )
		sdbSizerBtnGuardar.AddButton( self.sdbSizerBtnGuardarSave )
		sdbSizerBtnGuardar.Realize();
		
		bSizer49.Add( sdbSizerBtnGuardar, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel19.SetSizer( bSizer49 )
		self.m_panel19.Layout()
		bSizer49.Fit( self.m_panel19 )
		bSizer15.Add( self.m_panel19, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()
		
		# Connect Events
		self.btnFoto_Carga.Bind( wx.EVT_BUTTON, self.btnFoto_CargaOnButtonClick )
		self.datePickerFechaNacAlumno_Carga.Bind( wx.EVT_DATE_CHANGED, self.datePickerFechaNacAlumno_CargaOnDateChanged )
		self.radioEstudiaAlumno_Carga.Bind( wx.EVT_RADIOBOX, self.radioEstudiaAlumno_CargaOnRadioBox )
		self.radioInstPropioAlumno_Carga.Bind( wx.EVT_RADIOBOX, self.radioInstPropioAlumno_CargaOnRadioBox )
		self.radioOtraAgrupAlumno_Carga.Bind( wx.EVT_RADIOBOX, self.radioOtraAgrupAlumno_CargaOnRadioBox )
		self.radioFMedVacFA_Carga.Bind( wx.EVT_RADIOBOX, self.radioFMedVacFA_CargaOnRadioBox )
		self.radioFMedVacHA_Carga.Bind( wx.EVT_RADIOBOX, self.radioFMedVacHA_CargaOnRadioBox )
		self.radioFMedVacHB_Carga.Bind( wx.EVT_RADIOBOX, self.radioFMedVacHB_CargaOnRadioBox )
		self.radioFMedTieneSeguro_Carga.Bind( wx.EVT_RADIOBOX, self.radioFMedTieneSeguro_CargaOnRadioBox )
		self.sdbSizerBtnGuardarSave.Bind( wx.EVT_BUTTON, self.sdbSizerBtnGuardarOnSaveButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnFoto_CargaOnButtonClick( self, event ):
		event.Skip()
	
	def datePickerFechaNacAlumno_CargaOnDateChanged( self, event ):
		event.Skip()
	
	def radioEstudiaAlumno_CargaOnRadioBox( self, event ):
		event.Skip()
	
	def radioInstPropioAlumno_CargaOnRadioBox( self, event ):
		event.Skip()
	
	def radioOtraAgrupAlumno_CargaOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedVacFA_CargaOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedVacHA_CargaOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedVacHB_CargaOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedTieneSeguro_CargaOnRadioBox( self, event ):
		event.Skip()
	
	def sdbSizerBtnGuardarOnSaveButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelEditAlumno
###########################################################################

class PanelEditAlumno ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1090,987 ), style = wx.TAB_TRAVERSAL )
		
		self.Hide()
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Edición de Alumnos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		self.m_staticText63.SetFont( wx.Font( 20, 74, 90, 90, False, "MS Shell Dlg 2" ) )
		
		bSizer15.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer48 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel33 = wx.Panel( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer235 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3222 = wx.StaticText( self.m_panel33, wx.ID_ANY, u"Escoja un Alumno para Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3222.Wrap( -1 )
		bSizer235.Add( self.m_staticText3222, 0, wx.ALL, 5 )
		
		m_choiceNomAlumnoChoices = []
		self.m_choiceNomAlumno = wx.Choice( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceNomAlumnoChoices, 0 )
		self.m_choiceNomAlumno.SetSelection( 0 )
		bSizer235.Add( self.m_choiceNomAlumno, 0, wx.ALL, 5 )
		
		
		self.m_panel33.SetSizer( bSizer235 )
		self.m_panel33.Layout()
		bSizer235.Fit( self.m_panel33 )
		bSizer48.Add( self.m_panel33, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.notebookAlumno = wx.Notebook( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scrolledDatos = wx.ScrolledWindow( self.notebookAlumno, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrolledDatos.SetScrollRate( 10, 5 )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelDatosAlumnos = wx.Panel( self.scrolledDatos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer145 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelFoto_Edicion = wx.Panel( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1471 = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapFoto = wx.StaticBitmap( self.panelFoto_Edicion, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 160,120 ), wx.SUNKEN_BORDER )
		bSizer1471.Add( self.bitmapFoto, 0, wx.ALL, 5 )
		
		self.btnFoto_Edicion = wx.Button( self.panelFoto_Edicion, wx.ID_ANY, u"Editar Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1471.Add( self.btnFoto_Edicion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFoto_Edicion.SetSizer( bSizer1471 )
		self.panelFoto_Edicion.Layout()
		bSizer1471.Fit( self.panelFoto_Edicion )
		bSizer145.Add( self.panelFoto_Edicion, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer145, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), 0, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText311 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos del Alumno", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		self.m_staticText311.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer191.Add( self.m_staticText311, 0, wx.ALL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
		bSizer191.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer191, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Apellidos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer24.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.txtApeAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.txtApeAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText158 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nombres", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText158.Wrap( -1 )
		bSizer24.Add( self.m_staticText158, 0, wx.ALL, 5 )
		
		self.txtNomAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.txtNomAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"C.I", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer24.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.txtCiAlumno_Edicion=wx.lib.masked.TextCtrl(self.panelDatosAlumnos, -1, '',size=(130, -1), mask = '########')
		bSizer24.Add( self.txtCiAlumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText20 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Lugar de Nacimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer25.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.txtLugarNacAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtLugarNacAlumno_Edicion.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer25.Add( self.txtLugarNacAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Fecha de Nacimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer25.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.datePickerFechaNacAlumno_Edicion = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer25.Add( self.datePickerFechaNacAlumno_Edicion, 0, wx.ALL, 5 )
		
		radioSexoAlumno_EdicionChoices = [ u"Masculino", u"Femenino" ]
		self.radioSexoAlumno_Edicion = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Sexo", wx.DefaultPosition, wx.DefaultSize, radioSexoAlumno_EdicionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioSexoAlumno_Edicion.SetSelection( 0 )
		bSizer25.Add( self.radioSexoAlumno_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Edad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer25.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.txtEdadAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.txtEdadAlumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		bSizer124 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText159 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Fecha de Ingreso (menor o igual a la fecha actual)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText159.Wrap( -1 )
		self.m_staticText159.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer124.Add( self.m_staticText159, 0, wx.ALL, 5 )
		
		self.datePickerFechaIngAlumno_Edicion = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.datePickerFechaIngAlumno_Edicion.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.datePickerFechaIngAlumno_Edicion.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer124.Add( self.datePickerFechaIngAlumno_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer124, 0, wx.EXPAND, 5 )
		
		bSizer282 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText364 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText364.Wrap( -1 )
		self.m_staticText364.SetFont( wx.Font( 10, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer282.Add( self.m_staticText364, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer282, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText24 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Municipio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer29.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.txtDirMunicipioAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirMunicipioAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Parroquia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer29.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.txtDirParroquiaAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirParroquiaAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Sector", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer29.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.txtDirSectorAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirSectorAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Urb./Barrio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		bSizer29.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.txtDirUrbarrioAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtDirUrbarrioAlumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText28 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Avenida", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer30.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.txtDirAvenidaAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirAvenidaAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Calle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer30.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.txtDirCalleAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirCalleAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Edificio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		bSizer30.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.txtDirEdificioAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirEdificioAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"#Casa/Apto.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		bSizer30.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.txtDirCasaAptoAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.txtDirCasaAptoAlumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer30, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText32 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Punto de Referencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		bSizer32.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.txtDirPtoRefAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.txtDirPtoRefAlumno_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText33 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Hab", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		bSizer33.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.txtDirTelHabAlumno_Edicion=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer33.Add( self.txtDirTelHabAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Celular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		bSizer33.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.txtDirTelCelAlumno_Edicion=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer33.Add( self.txtDirTelCelAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		bSizer33.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.txtDirEmailalumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.txtDirEmailalumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer33, 0, wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer26, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer130 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline5 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer130.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText281 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos del Representante", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )
		self.m_staticText281.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer130.Add( self.m_staticText281, 0, wx.ALL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer130.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer130, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer251 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer291 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText321 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Apellidos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText321.Wrap( -1 )
		bSizer291.Add( self.m_staticText321, 0, wx.ALL, 5 )
		
		self.txtApeRepAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer291.Add( self.txtApeRepAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText160 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nombres", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText160.Wrap( -1 )
		bSizer291.Add( self.m_staticText160, 0, wx.ALL, 5 )
		
		self.txtNombreRepAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer291.Add( self.txtNombreRepAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText331 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"C.I", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText331.Wrap( -1 )
		bSizer291.Add( self.m_staticText331, 0, wx.ALL, 5 )
		
		self.txtCiRep_Edicion=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '',size=(130, -1), mask = '########')
		bSizer291.Add( self.txtCiRep_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer291, 0, wx.EXPAND, 5 )
		
		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText322 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección Habitación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText322.Wrap( -1 )
		bSizer321.Add( self.m_staticText322, 0, wx.ALL, 5 )
		
		self.txtDirHabRep_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer321.Add( self.txtDirHabRep_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer251.Add( bSizer321, 0, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText37 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Hab", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		bSizer34.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.txtTelHabRep_Edicion=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer34.Add( self.txtTelHabRep_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Celular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		bSizer34.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.txtTelCelRep_Edicion=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer34.Add( self.txtTelCelRep_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer34.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.txtEmailRep_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.txtEmailRep_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer3211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3221 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección Trabajo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3221.Wrap( -1 )
		bSizer3211.Add( self.m_staticText3221, 0, wx.ALL, 5 )
		
		self.txtDirTrabajoRep_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer3211.Add( self.txtDirTrabajoRep_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer251.Add( bSizer3211, 0, wx.EXPAND, 5 )
		
		bSizer341 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText371 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Telf. Trabajo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		bSizer341.Add( self.m_staticText371, 0, wx.ALL, 5 )
		
		self.txtTelTrabajoRep_Edicion=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer341.Add( self.txtTelTrabajoRep_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText381 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Ocupación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )
		bSizer341.Add( self.m_staticText381, 0, wx.ALL, 5 )
		
		self.txtOcupacionRep_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer341.Add( self.txtOcupacionRep_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText391 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Parentesco", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )
		bSizer341.Add( self.m_staticText391, 0, wx.ALL, 5 )
		
		self.txtParentescoRep_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer341.Add( self.txtParentescoRep_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer341, 0, wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer251, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline8 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer131.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText291 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos Académicos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )
		self.m_staticText291.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer131.Add( self.m_staticText291, 0, wx.ALL, 5 )
		
		self.m_staticline9 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer131.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer131, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer261 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioEstudiaAlumno_EdicionChoices = [ u"Si", u"No" ]
		self.radioEstudiaAlumno_Edicion = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Estudia Actualmente", wx.DefaultPosition, wx.DefaultSize, radioEstudiaAlumno_EdicionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioEstudiaAlumno_Edicion.SetSelection( 1 )
		bSizer41.Add( self.radioEstudiaAlumno_Edicion, 1, wx.ALL, 5 )
		
		radioEducacionAlumno_EdicionChoices = [ u"Media", u"Básica", u"Diversificada", u"Universitaria" ]
		self.radioEducacionAlumno_Edicion = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Nivel de Educación", wx.DefaultPosition, wx.DefaultSize, radioEducacionAlumno_EdicionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioEducacionAlumno_Edicion.SetSelection( 0 )
		bSizer41.Add( self.radioEducacionAlumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer261.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText48 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Grado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		bSizer42.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.txtGradoAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtGradoAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Año", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer42.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.txtAnioAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtAnioAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Semestre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		bSizer42.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		self.txtSemestreAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtSemestreAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Institución", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		bSizer42.Add( self.m_staticText52, 0, wx.ALL, 5 )
		
		self.txtInstitAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.txtInstitAlumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer261.Add( bSizer42, 0, wx.EXPAND, 5 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText53 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		bSizer43.Add( self.m_staticText53, 0, wx.ALL, 5 )
		
		self.txtDireccionInstitAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.txtDireccionInstitAlumno_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer261.Add( bSizer43, 0, wx.EXPAND, 5 )
		
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		bSizer44.Add( self.m_staticText54, 0, wx.ALL, 5 )
		
		self.txtTelefonoInstitAlumno_Edicion=wx.lib.masked.TextCtrl( self.panelDatosAlumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer44.Add( self.txtTelefonoInstitAlumno_Edicion, 1, wx.ALL, 5 )
		
		radioTipoInstitAlumno_EdicionChoices = [ u"Pública", u"Privada" ]
		self.radioTipoInstitAlumno_Edicion = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Tipo de Institución", wx.DefaultPosition, wx.DefaultSize, radioTipoInstitAlumno_EdicionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioTipoInstitAlumno_Edicion.SetSelection( 0 )
		bSizer44.Add( self.radioTipoInstitAlumno_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer261.Add( bSizer44, 0, wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer261, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer132 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline10 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer132.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText301 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Datos Musicales", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )
		self.m_staticText301.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer132.Add( self.m_staticText301, 0, wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer132.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( bSizer132, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioConocMusAlumno_EdicionChoices = [ u"Si", u"No" ]
		self.radioConocMusAlumno_Edicion = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Conocimientos Musicales", wx.DefaultPosition, wx.DefaultSize, radioConocMusAlumno_EdicionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioConocMusAlumno_Edicion.SetSelection( 0 )
		bSizer45.Add( self.radioConocMusAlumno_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText55 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Catedra a Cursar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		bSizer45.Add( self.m_staticText55, 0, wx.ALL, 5 )
		
		self.catedras = [u"Ritmo y Entonación",
		"Lenguaje Musical",
		u"Historia de la Música",
		u"Armonía y Contrapunto",
		"Coro",
		u"Canto Lírico",
		"Piano Principal",
		"Piano Complementario",
		"Flauta Dulce",
		u"Violín",
		"Viola",
		"Violoncello",
		"Contrabajo",
		"Flauta Trasversa",
		"Oboe",
		"Clarinete",
		"Fagot",
		"Corno",
		"Trompeta",
		u"Trombón",
		"Tuba",
		u"Saxofón",
		u"Batería",
		u"Percusión",
		u"Dirección Orquestal"]
		self.checkCatedras_edicion=wx.CheckListBox( self.panelDatosAlumnos, -1, (80, 50), (200, 80),self.catedras)
		
		
		bSizer45.Add( self.checkCatedras_edicion, 0, wx.ALL, 5 )
		
		self.m_staticText58 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nivel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		bSizer45.Add( self.m_staticText58, 0, wx.ALL, 5 )
		
		self.txtNivelOrqAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer45.Add( self.txtNivelOrqAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText59 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		bSizer45.Add( self.m_staticText59, 0, wx.ALL, 5 )
		
		self.txtProfAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.txtProfAlumno_Edicion, 1, wx.ALL, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.panelDatosAlumnos, wx.ID_ANY, u"Status Académico" ), wx.VERTICAL )
		
		choiceStatusAlumno_EdicionChoices = [ u"Selecione....", u"Alumno Regular", u"Alumno Nuevo Ingreso" ]
		self.choiceStatusAlumno_Edicion = wx.Choice( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceStatusAlumno_EdicionChoices, 0 )
		self.choiceStatusAlumno_Edicion.SetSelection( 0 )
		sbSizer3.Add( self.choiceStatusAlumno_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer45.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer45, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText57 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Orquesta a la que Pertenece", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		bSizer46.Add( self.m_staticText57, 0, wx.ALL, 5 )
		
		choiceOrquAlumno_EdicionChoices = [ u"Escoja una Orquesta.....", u"Juvenil \"A\"", u"Juvenil \"B\"", u"Ninguna" ]
		self.choiceOrquAlumno_Edicion = wx.Choice( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceOrquAlumno_EdicionChoices, 0 )
		self.choiceOrquAlumno_Edicion.SetSelection( 0 )
		bSizer46.Add( self.choiceOrquAlumno_Edicion, 0, wx.ALL, 5 )
		
		radioInstPropioAlumno_EdicionChoices = [ u"Si", u"No" ]
		self.radioInstPropioAlumno_Edicion = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Instrumento Propio", wx.DefaultPosition, wx.DefaultSize, radioInstPropioAlumno_EdicionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioInstPropioAlumno_Edicion.SetSelection( 0 )
		bSizer46.Add( self.radioInstPropioAlumno_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText161 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Fecha de Asignación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer46.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		self.datepickerFecAsigInstAlumno_Edicion = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer46.Add( self.datepickerFecAsigInstAlumno_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer46, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer281 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText360 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Marca del Instrumento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText360.Wrap( -1 )
		bSizer281.Add( self.m_staticText360, 0, wx.ALL, 5 )
		
		self.txtMarcaInstAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtMarcaInstAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText361 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )
		bSizer281.Add( self.m_staticText361, 0, wx.ALL, 5 )
		
		self.txtModeloInstAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtModeloInstAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText362 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Serial", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText362.Wrap( -1 )
		bSizer281.Add( self.m_staticText362, 0, wx.ALL, 5 )
		
		self.txtSerialInstAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtSerialInstAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText363 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nº de Activo Fijo FUNDAMUSICAL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText363.Wrap( -1 )
		bSizer281.Add( self.m_staticText363, 0, wx.ALL, 5 )
		
		self.txtNumActFijoInstAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.txtNumActFijoInstAlumno_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer281, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer47 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioOtraAgrupAlumno_EdicionChoices = [ u"Si", u"No" ]
		self.radioOtraAgrupAlumno_Edicion = wx.RadioBox( self.panelDatosAlumnos, wx.ID_ANY, u"Pertenece a Otra Agrupación?", wx.DefaultPosition, wx.DefaultSize, radioOtraAgrupAlumno_EdicionChoices, 1, wx.RA_SPECIFY_COLS )
		self.radioOtraAgrupAlumno_Edicion.SetSelection( 0 )
		bSizer47.Add( self.radioOtraAgrupAlumno_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		bSizer47.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.txtNombreOtraAgrupAlumno_Edicion = wx.TextCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer47.Add( self.txtNombreOtraAgrupAlumno_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText62 = wx.StaticText( self.panelDatosAlumnos, wx.ID_ANY, u"fecha de Ingreso", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		bSizer47.Add( self.m_staticText62, 0, wx.ALL, 5 )
		
		self.datePickerFechaIngOtraAgrupAlumno_Edicion = wx.DatePickerCtrl( self.panelDatosAlumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer47.Add( self.datePickerFechaIngOtraAgrupAlumno_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer47, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer3.Add( bSizer27, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelDatosAlumnos.SetSizer( gbSizer3 )
		self.panelDatosAlumnos.Layout()
		gbSizer3.Fit( self.panelDatosAlumnos )
		bSizer28.Add( self.panelDatosAlumnos, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.scrolledDatos.SetSizer( bSizer28 )
		self.scrolledDatos.Layout()
		bSizer28.Fit( self.scrolledDatos )
		self.notebookAlumno.AddPage( self.scrolledDatos, u"Datos Generales", True )
		self.scrolledMedica = wx.ScrolledWindow( self.notebookAlumno, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrolledMedica.SetScrollRate( 5, 5 )
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelMedicoALumnos = wx.Panel( self.scrolledMedica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer140 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3111 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Información General", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )
		self.m_staticText3111.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer141.Add( self.m_staticText3111, 0, wx.ALL, 5 )
		
		self.m_staticline33 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer141.Add( self.m_staticline33, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer141, 0, wx.EXPAND, 5 )
		
		bSizer142 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText190 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Tipo de Sangre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText190.Wrap( -1 )
		bSizer142.Add( self.m_staticText190, 0, wx.ALL, 5 )
		
		self.txtFMedTipoSangreAlumno_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer142.Add( self.txtFMedTipoSangreAlumno_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText191 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Antecedentes Generales", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		bSizer142.Add( self.m_staticText191, 0, wx.ALL, 5 )
		
		self.txtFMedAntecedAlumno_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		bSizer142.Add( self.txtFMedAntecedAlumno_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer142, 0, wx.EXPAND, 5 )
		
		bSizer146 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText196 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Vacunas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText196.Wrap( -1 )
		self.m_staticText196.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer146.Add( self.m_staticText196, 0, wx.ALL, 5 )
		
		self.m_staticline34 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer146.Add( self.m_staticline34, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer146, 0, wx.EXPAND, 5 )
		
		bSizer147 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedVacFA_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedVacFA_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Fiebre Amarilla", wx.DefaultPosition, wx.DefaultSize, radioFMedVacFA_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedVacFA_Edicion.SetSelection( 0 )
		bSizer147.Add( self.radioFMedVacFA_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText197 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText197.Wrap( -1 )
		bSizer147.Add( self.m_staticText197, 0, wx.ALL, 5 )
		
		self.datePickerFMedVacFA_Edicion = wx.DatePickerCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		bSizer147.Add( self.datePickerFMedVacFA_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer147, 0, wx.EXPAND, 5 )
		
		bSizer148 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedVacHA_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedVacHA_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Hepatitis \"A\"", wx.DefaultPosition, wx.DefaultSize, radioFMedVacHA_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedVacHA_Edicion.SetSelection( 0 )
		bSizer148.Add( self.radioFMedVacHA_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText198 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText198.Wrap( -1 )
		bSizer148.Add( self.m_staticText198, 0, wx.ALL, 5 )
		
		self.datePickerFMedVacHA_Edicion = wx.DatePickerCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		bSizer148.Add( self.datePickerFMedVacHA_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer148, 0, wx.EXPAND, 5 )
		
		bSizer149 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedVacHB_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedVacHB_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Hepatitis \"B\"", wx.DefaultPosition, wx.DefaultSize, radioFMedVacHB_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedVacHB_Edicion.SetSelection( 0 )
		bSizer149.Add( self.radioFMedVacHB_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText199 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText199.Wrap( -1 )
		bSizer149.Add( self.m_staticText199, 0, wx.ALL, 5 )
		
		self.datePickerFMedVacHB_Edicion = wx.DatePickerCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		bSizer149.Add( self.datePickerFMedVacHB_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer149, 0, wx.EXPAND, 5 )
		
		bSizer1461 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline341 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1461.Add( self.m_staticline341, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText1961 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Enfermedades", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1961.Wrap( -1 )
		self.m_staticText1961.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer1461.Add( self.m_staticText1961, 0, wx.ALL, 5 )
		
		self.m_staticline39 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1461.Add( self.m_staticline39, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer1461, 0, wx.EXPAND, 5 )
		
		bSizer154 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedEnfCab_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfCab_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Cabeza", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfCab_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfCab_Edicion.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfCab_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfOid_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfOid_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Oído", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfOid_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfOid_Edicion.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfOid_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfNar_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfNar_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Nariz", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfNar_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfNar_Edicion.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfNar_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfGar_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfGar_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Garganta", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfGar_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfGar_Edicion.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfGar_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfCor_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfCor_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Corazón", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfCor_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfCor_Edicion.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfCor_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfPul_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfPul_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Pulmones", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfPul_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfPul_Edicion.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfPul_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfVD_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfVD_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Vías Digestivas", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfVD_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfVD_Edicion.SetSelection( 1 )
		bSizer154.Add( self.radioFMedEnfVD_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer154, 0, wx.EXPAND, 5 )
		
		bSizer1541 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedEnfRi_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfRi_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Riñones", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfRi_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfRi_Edicion.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfRi_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfHue_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfHue_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Huesos", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfHue_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfHue_Edicion.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfHue_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfArt_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfArt_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Articulaciones", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfArt_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfArt_Edicion.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfArt_Edicion, 0, wx.ALL, 5 )
		
		radioFMedEnfEnd_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedEnfEnd_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Endocrinológico", wx.DefaultPosition, wx.DefaultSize, radioFMedEnfEnd_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedEnfEnd_Edicion.SetSelection( 1 )
		bSizer1541.Add( self.radioFMedEnfEnd_Edicion, 0, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer1541, 0, wx.EXPAND, 5 )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText202 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Operaciones (Indique edad, lugar y tratamiento)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )
		bSizer158.Add( self.m_staticText202, 0, wx.ALL, 5 )
		
		self.txtFMedOperaciones_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer158.Add( self.txtFMedOperaciones_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer158, 0, wx.EXPAND, 5 )
		
		bSizer159 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline37 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer159.Add( self.m_staticline37, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText203 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Alergias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText203.Wrap( -1 )
		self.m_staticText203.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer159.Add( self.m_staticText203, 0, wx.ALL, 5 )
		
		self.m_staticline38 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer159.Add( self.m_staticline38, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer159, 0, wx.EXPAND, 5 )
		
		bSizer160 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText204 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Comidas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText204.Wrap( -1 )
		bSizer160.Add( self.m_staticText204, 0, wx.ALL, 5 )
		
		self.txtFMedAlerCom_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer160.Add( self.txtFMedAlerCom_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText205 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Medicamentos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText205.Wrap( -1 )
		bSizer160.Add( self.m_staticText205, 0, wx.ALL, 5 )
		
		self.txtFMedAlerMed_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer160.Add( self.txtFMedAlerMed_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText207 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Medicamento Específico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )
		bSizer160.Add( self.m_staticText207, 0, wx.ALL, 5 )
		
		self.txtFMedAlerMedEsp_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer160.Add( self.txtFMedAlerMedEsp_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer160, 0, wx.EXPAND, 5 )
		
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline40 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer161.Add( self.m_staticline40, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText208 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Seguro Médico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )
		self.m_staticText208.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer161.Add( self.m_staticText208, 0, wx.ALL, 5 )
		
		self.m_staticline41 = wx.StaticLine( self.panelMedicoALumnos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer161.Add( self.m_staticline41, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer161, 0, wx.EXPAND, 5 )
		
		bSizer162 = wx.BoxSizer( wx.HORIZONTAL )
		
		radioFMedTieneSeguro_EdicionChoices = [ u"Si", u"No" ]
		self.radioFMedTieneSeguro_Edicion = wx.RadioBox( self.panelMedicoALumnos, wx.ID_ANY, u"Tiene Seguro?", wx.DefaultPosition, wx.DefaultSize, radioFMedTieneSeguro_EdicionChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioFMedTieneSeguro_Edicion.SetSelection( 0 )
		bSizer162.Add( self.radioFMedTieneSeguro_Edicion, 0, wx.ALL, 5 )
		
		self.m_staticText209 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Aseguradora", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )
		bSizer162.Add( self.m_staticText209, 0, wx.ALL, 5 )
		
		self.txtFMedAseg_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer162.Add( self.txtFMedAseg_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText210 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )
		bSizer162.Add( self.m_staticText210, 0, wx.ALL, 5 )
		
		self.txtFMedTelAseg_Edicion=wx.lib.masked.TextCtrl( self.panelMedicoALumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer162.Add( self.txtFMedTelAseg_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer162, 0, wx.EXPAND, 5 )
		
		bSizer163 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText211 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"En Caso de Emergencia, Llamar a", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer163.Add( self.m_staticText211, 0, wx.ALL, 5 )
		
		self.txtFMedTelEmerg_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer163.Add( self.txtFMedTelEmerg_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer163, 0, wx.EXPAND, 5 )
		
		bSizer166 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText212 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Unidad Médico asistencial de su Preferencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		bSizer166.Add( self.m_staticText212, 0, wx.ALL, 5 )
		
		self.txtFMedUnidadMedPref_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer166.Add( self.txtFMedUnidadMedPref_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer166, 0, wx.EXPAND, 5 )
		
		bSizer168 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText213 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Médico Tratante", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )
		bSizer168.Add( self.m_staticText213, 0, wx.ALL, 5 )
		
		self.txtFMedTratante_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer168.Add( self.txtFMedTratante_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText214 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )
		bSizer168.Add( self.m_staticText214, 0, wx.ALL, 5 )
		
		self.txtFMedTelTratante_Edicion=wx.lib.masked.TextCtrl( self.panelMedicoALumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer168.Add( self.txtFMedTelTratante_Edicion, 1, wx.ALL, 5 )
		
		self.m_staticText215 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Telf. Celular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )
		bSizer168.Add( self.m_staticText215, 0, wx.ALL, 5 )
		
		self.txtFMedCelTratante_Edicion=wx.lib.masked.TextCtrl( self.panelMedicoALumnos, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer168.Add( self.txtFMedCelTratante_Edicion, 1, wx.ALL, 5 )
		
		
		bSizer140.Add( bSizer168, 0, wx.EXPAND, 5 )
		
		bSizer169 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText216 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"¿Su hijo presenta o ha presentado alguna enfermedad, u otro suceso médico importante no contemplado en esta planilla?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )
		bSizer169.Add( self.m_staticText216, 0, wx.ALL, 5 )
		
		self.m_staticText220 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Describalo a continuación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )
		bSizer169.Add( self.m_staticText220, 0, wx.ALL, 5 )
		
		self.txtFMedEnfPrevia_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer169.Add( self.txtFMedEnfPrevia_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer169, 0, wx.EXPAND, 5 )
		
		bSizer1691 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2161 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"¿Su hijo utiliza algún aparato, equipo o tratamiento especial en forma particular para tratamiento médico?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2161.Wrap( -1 )
		bSizer1691.Add( self.m_staticText2161, 0, wx.ALL, 5 )
		
		self.m_staticText221 = wx.StaticText( self.panelMedicoALumnos, wx.ID_ANY, u"Infórmelo a continuación, anexe informe del especialista", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		bSizer1691.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		self.txtFMedAperato_Edicion = wx.TextCtrl( self.panelMedicoALumnos, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1691.Add( self.txtFMedAperato_Edicion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer140.Add( bSizer1691, 0, wx.EXPAND, 5 )
		
		
		gbSizer5.Add( bSizer140, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		self.panelMedicoALumnos.SetSizer( gbSizer5 )
		self.panelMedicoALumnos.Layout()
		gbSizer5.Fit( self.panelMedicoALumnos )
		bSizer139.Add( self.panelMedicoALumnos, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.scrolledMedica.SetSizer( bSizer139 )
		self.scrolledMedica.Layout()
		bSizer139.Fit( self.scrolledMedica )
		self.notebookAlumno.AddPage( self.scrolledMedica, u"Ficha Médica", False )
		
		bSizer48.Add( self.notebookAlumno, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel18.SetSizer( bSizer48 )
		self.m_panel18.Layout()
		bSizer48.Fit( self.m_panel18 )
		bSizer15.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer49 = wx.BoxSizer( wx.VERTICAL )
		
		sdbSizerBtnGuardar = wx.StdDialogButtonSizer()
		self.sdbSizerBtnGuardarApply = wx.Button( self.m_panel19, wx.ID_APPLY )
		sdbSizerBtnGuardar.AddButton( self.sdbSizerBtnGuardarApply )
		sdbSizerBtnGuardar.Realize();
		
		bSizer49.Add( sdbSizerBtnGuardar, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel19.SetSizer( bSizer49 )
		self.m_panel19.Layout()
		bSizer49.Fit( self.m_panel19 )
		bSizer15.Add( self.m_panel19, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()
		
		# Connect Events
		self.m_choiceNomAlumno.Bind( wx.EVT_CHOICE, self.m_choiceNomAlumnoOnChoice )
		self.btnFoto_Edicion.Bind( wx.EVT_BUTTON, self.btnFoto_EdicionOnButtonClick )
		self.datePickerFechaNacAlumno_Edicion.Bind( wx.EVT_DATE_CHANGED, self.datePickerFechaNacAlumno_EdicionOnDateChanged )
		self.radioEstudiaAlumno_Edicion.Bind( wx.EVT_RADIOBOX, self.radioEstudiaAlumno_EdicionOnRadioBox )
		self.radioInstPropioAlumno_Edicion.Bind( wx.EVT_RADIOBOX, self.radioInstPropioAlumno_EdicionOnRadioBox )
		self.radioOtraAgrupAlumno_Edicion.Bind( wx.EVT_RADIOBOX, self.radioOtraAgrupAlumno_EdicionOnRadioBox )
		self.radioFMedVacFA_Edicion.Bind( wx.EVT_RADIOBOX, self.radioFMedVacFA_EdicionOnRadioBox )
		self.radioFMedVacHA_Edicion.Bind( wx.EVT_RADIOBOX, self.radioFMedVacHA_EdicionOnRadioBox )
		self.radioFMedVacHB_Edicion.Bind( wx.EVT_RADIOBOX, self.radioFMedVacHB_EdicionOnRadioBox )
		self.radioFMedTieneSeguro_Edicion.Bind( wx.EVT_RADIOBOX, self.radioFMedTieneSeguro_EdicionOnRadioBox )
		self.sdbSizerBtnGuardarApply.Bind( wx.EVT_BUTTON, self.sdbSizerBtnGuardarOnApplyButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_choiceNomAlumnoOnChoice( self, event ):
		event.Skip()
	
	def btnFoto_EdicionOnButtonClick( self, event ):
		event.Skip()
	
	def datePickerFechaNacAlumno_EdicionOnDateChanged( self, event ):
		event.Skip()
	
	def radioEstudiaAlumno_EdicionOnRadioBox( self, event ):
		event.Skip()
	
	def radioInstPropioAlumno_EdicionOnRadioBox( self, event ):
		event.Skip()
	
	def radioOtraAgrupAlumno_EdicionOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedVacFA_EdicionOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedVacHA_EdicionOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedVacHB_EdicionOnRadioBox( self, event ):
		event.Skip()
	
	def radioFMedTieneSeguro_EdicionOnRadioBox( self, event ):
		event.Skip()
	
	def sdbSizerBtnGuardarOnApplyButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameBusqueda
###########################################################################

class FrameBusqueda ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Busqueda y Eliminación de Alumnos", pos = wx.DefaultPosition, size = wx.Size( 570,316 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer316 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel58 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer317 = wx.BoxSizer( wx.VERTICAL )
		
		self.searchAlumnoCtrl = wx.SearchCtrl( self.m_panel58, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PROCESS_ENTER )
		self.searchAlumnoCtrl.ShowSearchButton( True )
		self.searchAlumnoCtrl.ShowCancelButton( True )
		bSizer317.Add( self.searchAlumnoCtrl, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.m_panel58.SetSizer( bSizer317 )
		self.m_panel58.Layout()
		bSizer317.Fit( self.m_panel58 )
		bSizer316.Add( self.m_panel58, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelListaAlumnos = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer316.Add( self.panelListaAlumnos, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel60 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer318 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnSelTODO = wx.Button( self.m_panel60, wx.ID_ANY, u"Seleccionar Todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer318.Add( self.btnSelTODO, 0, wx.ALL, 5 )
		
		self.btnDeSelTODO = wx.Button( self.m_panel60, wx.ID_ANY, u"Deselecionar Todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer318.Add( self.btnDeSelTODO, 0, wx.ALL, 5 )
		
		
		bSizer318.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnElimAlumno = wx.Button( self.m_panel60, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer318.Add( self.btnElimAlumno, 0, wx.ALL, 5 )
		
		self.btnCancelElimUsu = wx.Button( self.m_panel60, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer318.Add( self.btnCancelElimUsu, 0, wx.ALL, 5 )
		
		
		self.m_panel60.SetSizer( bSizer318 )
		self.m_panel60.Layout()
		bSizer318.Fit( self.m_panel60 )
		bSizer316.Add( self.m_panel60, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer316 )
		self.Layout()
		self.m_statusBarElim = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameBusquedaOnClose )
		self.searchAlumnoCtrl.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.searchAlumnoCtrlOnCancelButton )
		self.searchAlumnoCtrl.Bind( wx.EVT_ENTER_WINDOW, self.searchAlumnoCtrlOnEnterWindow )
		self.searchAlumnoCtrl.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchAlumnoCtrlOnSearchButton )
		self.searchAlumnoCtrl.Bind( wx.EVT_TEXT_ENTER, self.searchAlumnoCtrlOnTextEnter )
		self.btnSelTODO.Bind( wx.EVT_BUTTON, self.btnSelTODOOnButtonClick )
		self.btnDeSelTODO.Bind( wx.EVT_BUTTON, self.btnDeSelTODOOnButtonClick )
		self.btnElimAlumno.Bind( wx.EVT_BUTTON, self.btnElimAlumnoOnButtonClick )
		self.btnCancelElimUsu.Bind( wx.EVT_BUTTON, self.btnCancelElimUsuOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameBusquedaOnClose( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnCancelButton( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnEnterWindow( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnSearchButton( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnTextEnter( self, event ):
		event.Skip()
	
	def btnSelTODOOnButtonClick( self, event ):
		event.Skip()
	
	def btnDeSelTODOOnButtonClick( self, event ):
		event.Skip()
	
	def btnElimAlumnoOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelElimUsuOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameBusquedaReportes
###########################################################################

class FrameBusquedaReportes ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Busqueda de Alumnos para Reportes", pos = wx.DefaultPosition, size = wx.Size( 662,316 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer316 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel58 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer317 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer137 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText167 = wx.StaticText( self.m_panel58, wx.ID_ANY, u"Instrumento/Cátedra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )
		bSizer137.Add( self.m_staticText167, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceCatedraBusqRepChoices = [ u"Escoja una Cátedra....", u"Todas", u"Ritmo y Entonación", u"Lenguaje Musical", u"Historia de la Música", u"Armonía y Contrapunto", u"Coro", u"Canto Lírico", u"Piano Principal", u"Piano Complementario", u"Flauta Dulce", u"Violín", u"Viola", u"Violoncello", u"Contrabajo", u"Flauta Trasversa", u"Oboe", u"Clarinete", u"Fagot", u"Corno", u"Trompeta", u"Trombón", u"Tuba", u"Saxofón", u"Batería", u"Percusión", u"Dirección Orquestal" ]
		self.choiceCatedraBusqRep = wx.Choice( self.m_panel58, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceCatedraBusqRepChoices, 0 )
		self.choiceCatedraBusqRep.SetSelection( 0 )
		bSizer137.Add( self.choiceCatedraBusqRep, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer317.Add( bSizer137, 1, wx.EXPAND, 5 )
		
		bSizer136 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchAlumnoCtrl = wx.SearchCtrl( self.m_panel58, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PROCESS_ENTER )
		self.searchAlumnoCtrl.ShowSearchButton( False )
		self.searchAlumnoCtrl.ShowCancelButton( True )
		bSizer136.Add( self.searchAlumnoCtrl, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer317.Add( bSizer136, 1, wx.EXPAND, 5 )
		
		
		self.m_panel58.SetSizer( bSizer317 )
		self.m_panel58.Layout()
		bSizer317.Fit( self.m_panel58 )
		bSizer316.Add( self.m_panel58, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.panelListaAlumnos = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer316.Add( self.panelListaAlumnos, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel39 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer148 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel60 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer145 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnBuscarReporte = wx.Button( self.m_panel60, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer145.Add( self.btnBuscarReporte, 0, wx.ALL, 5 )
		
		self.btnCancelElimUsu = wx.Button( self.m_panel60, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer145.Add( self.btnCancelElimUsu, 0, wx.ALL, 5 )
		
		
		self.m_panel60.SetSizer( bSizer145 )
		self.m_panel60.Layout()
		bSizer145.Fit( self.m_panel60 )
		bSizer148.Add( self.m_panel60, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel39.SetSizer( bSizer148 )
		self.m_panel39.Layout()
		bSizer148.Fit( self.m_panel39 )
		bSizer316.Add( self.m_panel39, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer316 )
		self.Layout()
		self.m_statusBarElim = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameBusquedaOnClose )
		self.searchAlumnoCtrl.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.searchAlumnoCtrlOnCancelButton )
		self.searchAlumnoCtrl.Bind( wx.EVT_ENTER_WINDOW, self.searchAlumnoCtrlOnEnterWindow )
		self.searchAlumnoCtrl.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchAlumnoCtrlOnSearchButton )
		self.searchAlumnoCtrl.Bind( wx.EVT_TEXT_ENTER, self.searchAlumnoCtrlOnTextEnter )
		self.btnBuscarReporte.Bind( wx.EVT_BUTTON, self.btnBuscarReporteOnButtonClick )
		self.btnCancelElimUsu.Bind( wx.EVT_BUTTON, self.btnCancelElimUsuOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameBusquedaOnClose( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnCancelButton( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnEnterWindow( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnSearchButton( self, event ):
		event.Skip()
	
	def searchAlumnoCtrlOnTextEnter( self, event ):
		event.Skip()
	
	def btnBuscarReporteOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelElimUsuOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameReporteGeneral
###########################################################################

class FrameReporteGeneral ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Reporte General", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer127 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel39 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel37 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self.m_panel37, wx.ID_ANY, wx.Bitmap( u"bitmaps/cabecera.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer139.Add( self.m_bitmap3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel37.SetSizer( bSizer139 )
		self.m_panel37.Layout()
		bSizer139.Fit( self.m_panel37 )
		bSizer141.Add( self.m_panel37, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel391 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1411 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel40 = wx.Panel( self.m_panel391, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer143 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText168 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Escoja un Instrumento / Cátedra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText168.Wrap( -1 )
		bSizer143.Add( self.m_staticText168, 0, wx.ALL, 5 )
		
		choiceCatReporteChoices = [ u"Escoja una Cátedra....", u"Todas", u"Ritmo y Entonación", u"Lenguaje Musical", u"Historia de la Música", u"Armonía y Contrapunto", u"Coro", u"Canto Lírico", u"Piano Principal", u"Piano Complementario", u"Flauta Dulce", u"Violín", u"Viola", u"Violoncello", u"Contrabajo", u"Flauta Trasversa", u"Oboe", u"Clarinete", u"Fagot", u"Corno", u"Trompeta", u"Trombón", u"Tuba", u"Saxofón", u"Batería", u"Percusión", u"Dirección Orquestal" ]
		self.choiceCatReporte = wx.Choice( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceCatReporteChoices, 0 )
		self.choiceCatReporte.SetSelection( 0 )
		bSizer143.Add( self.choiceCatReporte, 0, wx.ALL, 5 )
		
		
		self.m_panel40.SetSizer( bSizer143 )
		self.m_panel40.Layout()
		bSizer143.Fit( self.m_panel40 )
		bSizer1411.Add( self.m_panel40, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel44 = wx.Panel( self.m_panel391, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer148 = wx.BoxSizer( wx.VERTICAL )
		
		m_radio_tipo_reporteChoices = [ u"Resumido", u"Completo" ]
		self.m_radio_tipo_reporte = wx.RadioBox( self.m_panel44, wx.ID_ANY, u"Escoja el Tipo de Resumen", wx.DefaultPosition, wx.DefaultSize, m_radio_tipo_reporteChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radio_tipo_reporte.SetSelection( 0 )
		bSizer148.Add( self.m_radio_tipo_reporte, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel44.SetSizer( bSizer148 )
		self.m_panel44.Layout()
		bSizer148.Fit( self.m_panel44 )
		bSizer1411.Add( self.m_panel44, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_panel41 = wx.Panel( self.m_panel391, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer144 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnCrearReporte = wx.Button( self.m_panel41, wx.ID_ANY, u"Crear Reporte", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer144.Add( self.btnCrearReporte, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel41.SetSizer( bSizer144 )
		self.m_panel41.Layout()
		bSizer144.Fit( self.m_panel41 )
		bSizer1411.Add( self.m_panel41, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel391.SetSizer( bSizer1411 )
		self.m_panel391.Layout()
		bSizer1411.Fit( self.m_panel391 )
		bSizer141.Add( self.m_panel391, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_notebook3 = wx.Notebook( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel_FichaGeneral = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.m_notebook3.AddPage( self.panel_FichaGeneral, u"Ficha General", True )
		self.panel_FichaMedica = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.m_notebook3.AddPage( self.panel_FichaMedica, u"Ficha Médica", False )
		
		bSizer141.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel38 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer140 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnImpFichaGen = wx.Button( self.m_panel38, wx.ID_ANY, u"Imprimir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer140.Add( self.btnImpFichaGen, 0, wx.ALL, 5 )
		
		self.btnCerrarFichaGen = wx.Button( self.m_panel38, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer140.Add( self.btnCerrarFichaGen, 0, wx.ALL, 5 )
		
		
		self.m_panel38.SetSizer( bSizer140 )
		self.m_panel38.Layout()
		bSizer140.Fit( self.m_panel38 )
		bSizer141.Add( self.m_panel38, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel39.SetSizer( bSizer141 )
		self.m_panel39.Layout()
		bSizer141.Fit( self.m_panel39 )
		bSizer127.Add( self.m_panel39, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer127 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameReporteGeneralOnClose )
		self.btnCrearReporte.Bind( wx.EVT_BUTTON, self.btnCrearReporteOnButtonClick )
		self.btnImpFichaGen.Bind( wx.EVT_BUTTON, self.btnImpFichaGenOnButtonClick )
		self.btnCerrarFichaGen.Bind( wx.EVT_BUTTON, self.btnCerrarFichaGenOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameReporteGeneralOnClose( self, event ):
		event.Skip()
	
	def btnCrearReporteOnButtonClick( self, event ):
		event.Skip()
	
	def btnImpFichaGenOnButtonClick( self, event ):
		event.Skip()
	
	def btnCerrarFichaGenOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameFichasAlumno
###########################################################################

class FrameFichasAlumno ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer129 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelPrincipalFicha = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer150 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel34 = wx.Panel( self.panelPrincipalFicha, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer137 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel34, wx.ID_ANY, wx.Bitmap( u"bitmaps/cabecera.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer137.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel34.SetSizer( bSizer137 )
		self.m_panel34.Layout()
		bSizer137.Fit( self.m_panel34 )
		bSizer150.Add( self.m_panel34, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelFicha = wx.Panel( self.panelPrincipalFicha, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer150.Add( self.panelFicha, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel40 = wx.Panel( self.panelPrincipalFicha, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer149 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCerrarFicha = wx.Button( self.m_panel40, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer149.Add( self.btnCerrarFicha, 0, wx.ALL, 5 )
		
		
		self.m_panel40.SetSizer( bSizer149 )
		self.m_panel40.Layout()
		bSizer149.Fit( self.m_panel40 )
		bSizer150.Add( self.m_panel40, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelPrincipalFicha.SetSizer( bSizer150 )
		self.panelPrincipalFicha.Layout()
		bSizer150.Fit( self.panelPrincipalFicha )
		bSizer129.Add( self.panelPrincipalFicha, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer129 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameFichasAlumnoOnClose )
		self.btnCerrarFicha.Bind( wx.EVT_BUTTON, self.btnCerrarFichaOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameFichasAlumnoOnClose( self, event ):
		event.Skip()
	
	def btnCerrarFichaOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameReporteProf
###########################################################################

class FrameReporteProf ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer127 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel39 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel37 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self.m_panel37, wx.ID_ANY, wx.Bitmap( u"bitmaps/cabecera.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer139.Add( self.m_bitmap3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel37.SetSizer( bSizer139 )
		self.m_panel37.Layout()
		bSizer139.Fit( self.m_panel37 )
		bSizer141.Add( self.m_panel37, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel391 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1411 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel40 = wx.Panel( self.m_panel391, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer143 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText168 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Indique un Nombre de Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText168.Wrap( -1 )
		bSizer143.Add( self.m_staticText168, 0, wx.ALL, 5 )
		
		self.txt_profesor = wx.TextCtrl( self.m_panel40, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer143.Add( self.txt_profesor, 0, wx.ALL, 5 )
		
		
		self.m_panel40.SetSizer( bSizer143 )
		self.m_panel40.Layout()
		bSizer143.Fit( self.m_panel40 )
		bSizer1411.Add( self.m_panel40, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel41 = wx.Panel( self.m_panel391, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer144 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnCrearReporte = wx.Button( self.m_panel41, wx.ID_ANY, u"Crear Reporte", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer144.Add( self.btnCrearReporte, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel41.SetSizer( bSizer144 )
		self.m_panel41.Layout()
		bSizer144.Fit( self.m_panel41 )
		bSizer1411.Add( self.m_panel41, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel391.SetSizer( bSizer1411 )
		self.m_panel391.Layout()
		bSizer1411.Fit( self.m_panel391 )
		bSizer141.Add( self.m_panel391, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.panel_RepProf = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141.Add( self.panel_RepProf, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel38 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer140 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnImpFichaGen = wx.Button( self.m_panel38, wx.ID_ANY, u"Imprimir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer140.Add( self.btnImpFichaGen, 0, wx.ALL, 5 )
		
		self.btnCerrarFichaGen = wx.Button( self.m_panel38, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer140.Add( self.btnCerrarFichaGen, 0, wx.ALL, 5 )
		
		
		self.m_panel38.SetSizer( bSizer140 )
		self.m_panel38.Layout()
		bSizer140.Fit( self.m_panel38 )
		bSizer141.Add( self.m_panel38, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel39.SetSizer( bSizer141 )
		self.m_panel39.Layout()
		bSizer141.Fit( self.m_panel39 )
		bSizer127.Add( self.m_panel39, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer127 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameReporteProfOnClose )
		self.btnCrearReporte.Bind( wx.EVT_BUTTON, self.btnCrearReporteOnButtonClick )
		self.btnImpFichaGen.Bind( wx.EVT_BUTTON, self.btnImpFichaGenOnButtonClick )
		self.btnCerrarFichaGen.Bind( wx.EVT_BUTTON, self.btnCerrarFichaGenOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameReporteProfOnClose( self, event ):
		event.Skip()
	
	def btnCrearReporteOnButtonClick( self, event ):
		event.Skip()
	
	def btnImpFichaGenOnButtonClick( self, event ):
		event.Skip()
	
	def btnCerrarFichaGenOnButtonClick( self, event ):
		event.Skip()
	

