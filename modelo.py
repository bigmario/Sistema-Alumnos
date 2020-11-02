#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Manejo de Base de Datos Sqlite3 (MODELO)
## Ultima Revisión: 19-11-2012 11:05 a.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 07 de Noviembre de 2012
#
# +-------------------------------------------------+#
###########################################################################

import sqlite3

class ModeloBD:

    def __init__(self):
        self.conectar()

    def conectar(self):
        """
        Conecta con la Base de daos
        """
        self.cnn = sqlite3.connect('database/BDAlumnos.db')
        self.cnn.row_factory = sqlite3.Row
        self.cursor = self.cnn.cursor()

    def CrearBD(self):
        """
        Crea la Base de Datos
        """
        try:
            query = open('SQL/BDNomina - MEJORADO.sql', 'r').read()
            self.conectar()
            if self.cursor.executescript(query):
                mensajeExito=wx.MessageDialog(self,'Base de Datos Creada Exitosamente',"Creando Base de Datos", wx.OK|wx.ICON_HAND)
                mensajeExito.ShowModal()
        except sqlite3.Error, e:
            self.cnn.rollback()
            mensajeError=wx.MessageDialog(self,'La Base de Datos no pudo ser Creada \n\nError: %s'%e,"Error en Base de Datos", wx.OK|wx.ICON_HAND)
            mensajeError.ShowModal()
        finally:
            self.desconectar()

    def obtenerDatosNucleo(self):
        self.conectar()
        sql="""SELECT * FROM admin"""
        self.cursor.execute(sql)
        datosNucleo= self.cursor.fetchall()
        self.desconectar()
        return datosNucleo

    def recordarPass(self, pregunta, respuesta):
        self.conectar()
        sql="""SELECT loginAdmin, passAdmin FROM Admin WHERE preguntaSegAdmin=? AND respuestaSegAdmin=?"""
        self.cursor.execute(sql, (pregunta, respuesta))
        passRecuperado=self.cursor.fetchone()
        self.desconectar()
        return passRecuperado

    def verificaUsuario(self, usuario, hashClave):
        """
        Verifica si el usuario esta registrado
        """
        self.conectar()
        self.cursor.execute("""SELECT idAdmin, loginAdmin, passAdmin FROM Admin WHERE loginAdmin=? and passAdmin=?""",(usuario, hashClave))
        sesion=self.cursor.fetchone()
        self.desconectar()
        return sesion

    def ContarRegistrosAdmin(self):
        """
        Cuenta los registros en la base de datos de administrador
        """
        self.conectar()
        self.cursor.execute("""SELECT COUNT(*) FROM Admin""")
        resultado=self.cursor.fetchone()
        numero=resultado[0]
        self.desconectar()
        return numero

    def configuracionInicial(self, nucleo, entFed, municipio, nombreAdmin, passAdmin, preguntaSeg, respuestaSeg):
        self.conectar()
        try:
            sql="""INSERT INTO Admin (loginAdmin, passAdmin, nucleoAdmin, entFedAdmin, municipioAdmin, preguntaSegAdmin, respuestaSegAdmin) VALUES (?,?,?,?,?,?,?)"""
            self.cursor.execute(sql, (nombreAdmin, passAdmin, nucleo, entFed, municipio, preguntaSeg, respuestaSeg))
            self.cnn.commit()
            self.desconectar()
        except sqlite3.Error:
            self.cnn.rollback()

    def desconectar(self):
        """
        Desconecta de la base de datos
        """
        self.cursor.close()
        self.cnn.close()

    def agregarAdmin(self, nombreUsuario, passwd):
        """
        Agrega administrador a la aplicacion
        """
        self.conectar()
        try:
            self.cursor.execute("""INSERT INTO Admin(loginadmin, passadmin) VALUES (?,?)""", (nombreUsuario, passwd))
            self.cnn.commit()
        except sqlite3.Error:
            self.cnn.rollback()
        finally:
            self.desconectar()

    def agregarAlumno(self, foto, txtNomAlumno_Carga,
                txtApeAlumno_Carga,
                txtCiAlumno_Carga,
                datePickerFechaNacAlumno_Carga,
                datePickerFechaIngAlumno_Carga,
                txtLugarNacAlumno_Carga,
                radioSexoAlumno_Carga,
                txtEdadAlumno_Carga,
                txtDirTelHabAlumno_Carga,
                txtDirTelCelAlumno_Carga,
                txtDirEmailalumno_Carga,
                txtDirMunicipioAlumno_Carga,
                txtDirParroquiaAlumno_Carga,
                txtDirSectorAlumno_Carga,
                txtDirUrbarrioAlumno_Carga,
                txtDirAvenidaAlumno_Carga,
                txtDirCalleAlumno_Carga,
                txtDirEdificioAlumno_Carga,
                txtDirCasaAptoAlumno_Carga,
                txtDirPtoRefAlumno_Carga,
                txtNombreRepAlumno_Carga,
                txtApeRepAlumno_Carga,
                txtCiRep_Carga,
                txtDirHabRep_Carga,
                txtTelHabRep_Carga,
                txtTelCelRep_Carga,
                txtEmailRep_Carga,
                txtDirTrabajoRep_Carga,
                txtTelTrabajoRep_Carga,
                txtOcupacionRep_Carga,
                txtParentescoRep_Carga,
                radioEstudiaAlumno_Carga,
                radioEducacionAlumno_Carga,
                txtGradoAlumno_Carga,
                txtAnioAlumno_Carga,
                txtSemestreAlumno_Carga,
                txtInstitAlumno_Carga,
                txtDireccionInstitAlumno_Carga,
                txtTelefonoInstitAlumno_Carga,
                radioTipoInstitAlumno_Carga,
                radioConocMusAlumno_Carga,
                choiceCatedraAlumno_Carga,
                choiceOrquAlumno_Carga,
                txtNivelOrqAlumno_Carga,
                radioInstPropioAlumno_Carga,
                datepickerFecAsigInstAlumno_Carga,
                txtMarcaInstAlumno_Carga,
                txtModeloInstAlumno_Carga,
                txtSerialInstAlumno_Carga,
                txtNumActFijoInstAlumno_Carga,
                txtProfAlumno_Carga,
                choiceStatusAlumno_Carga,
                radioOtraAgrupAlumno_Carga,
                txtNombreOtraAgrupAlumno_Carga,
                datePickerFechaIngOtraAgrupAlumno_Carga,
                txtFMedTipoSangreAlumno_Carga,
                txtFMedAntecedAlumno_Carga,
                radioFMedVacFA_Carga,
                datePickerFMedVacFA_Carga,
                radioFMedVacHA_Carga,
                datePickerFMedVacHA_Carga,
                radioFMedVacHB_Carga,
                datePickerFMedVacHB_Carga,
                radioFMedEnfCab_Carga,
                radioFMedEnfOid_Carga,
                radioFMedEnfNar_Carga,
                radioFMedEnfGar_Carga,
                radioFMedEnfCor_Carga,
                radioFMedEnfPul_Carga,
                radioFMedEnfVD_Carga,
                radioFMedEnfRi_Carga,
                radioFMedEnfHue_Carga,
                radioFMedEnfArt_Carga,
                radioFMedEnfEnd_Carga,
                txtFMedOperaciones_Carga,
                txtFMedAlerCom_Carga,
                txtFMedAlerMed_Carga,
                txtFMedAlerMedEsp_Carga,
                radioFMedTieneSeguro_Carga,
                txtFMedAseg_Carga,
                txtFMedTelAseg_Carga,
                txtFMedTelEmerg_Carga,
                txtFMedUnidadMedPref_Carga,
                txtFMedTratante_Carga,
                txtFMedTelTratante_Carga,
                txtFMedCelTratante_Carga,
                txtFMedEnfPrevia_Carga,
                txtFMedAperato_Carga):
        """
        Agrega profesores a la base de datos
        """
        self.conectar()

        self.cursor.execute("""INSERT INTO Alumnos (nombreAlumno,apellidoAlumno,ciAlumno,fechaNacAlumno,fechaIngAlumno,lugarNacAlumno,sexoAlumno,edadAlumno,telefonoResAlumno,telefonoCelAlumno,emailAlumno, fotoAlumno) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (txtNomAlumno_Carga,
            txtApeAlumno_Carga,
            txtCiAlumno_Carga,
            datePickerFechaNacAlumno_Carga,
            datePickerFechaIngAlumno_Carga,
            txtLugarNacAlumno_Carga,
            radioSexoAlumno_Carga,
            txtEdadAlumno_Carga,
            txtDirTelHabAlumno_Carga,
            txtDirTelCelAlumno_Carga,
            txtDirEmailalumno_Carga,
            foto))

        ultimo_id_alumno = self.cursor.lastrowid

        self.cursor.execute("""INSERT INTO DatosMusicales VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (radioConocMusAlumno_Carga,
            choiceCatedraAlumno_Carga,
            choiceOrquAlumno_Carga,
            txtNivelOrqAlumno_Carga,
            radioInstPropioAlumno_Carga,
            datepickerFecAsigInstAlumno_Carga,
            txtMarcaInstAlumno_Carga,
            txtModeloInstAlumno_Carga,
            txtSerialInstAlumno_Carga,
            txtNumActFijoInstAlumno_Carga,
            txtProfAlumno_Carga,
            choiceStatusAlumno_Carga,
            radioOtraAgrupAlumno_Carga,
            txtNombreOtraAgrupAlumno_Carga,
            datePickerFechaIngOtraAgrupAlumno_Carga,
            ultimo_id_alumno))

        self.cursor.execute("""INSERT INTO FichaMedica VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (ultimo_id_alumno,
            txtFMedTipoSangreAlumno_Carga,
            txtFMedAntecedAlumno_Carga,
            radioFMedVacFA_Carga,
            datePickerFMedVacFA_Carga,
            radioFMedVacHA_Carga,
            datePickerFMedVacHA_Carga,
            radioFMedVacHB_Carga,
            datePickerFMedVacHB_Carga,
            radioFMedEnfCab_Carga,
            radioFMedEnfOid_Carga,
            radioFMedEnfNar_Carga,
            radioFMedEnfGar_Carga,
            radioFMedEnfCor_Carga,
            radioFMedEnfPul_Carga,
            radioFMedEnfVD_Carga,
            radioFMedEnfRi_Carga,
            radioFMedEnfHue_Carga,
            radioFMedEnfArt_Carga,
            radioFMedEnfEnd_Carga,
            txtFMedOperaciones_Carga,
            txtFMedAlerCom_Carga,
            txtFMedAlerMed_Carga,
            txtFMedAlerMedEsp_Carga,
            radioFMedTieneSeguro_Carga,
            txtFMedAseg_Carga,
            txtFMedTelAseg_Carga,
            txtFMedTelEmerg_Carga,
            txtFMedUnidadMedPref_Carga,
            txtFMedTratante_Carga,
            txtFMedTelTratante_Carga,
            txtFMedCelTratante_Carga,
            txtFMedEnfPrevia_Carga,
            txtFMedAperato_Carga))

        self.cursor.execute("""INSERT INTO DireccionAlumno VALUES (?,?,?,?,?,?,?,?,?,?)""", (txtDirMunicipioAlumno_Carga,
            txtDirParroquiaAlumno_Carga,
            txtDirSectorAlumno_Carga,
            txtDirUrbarrioAlumno_Carga,
            txtDirAvenidaAlumno_Carga,
            txtDirCalleAlumno_Carga,
            txtDirEdificioAlumno_Carga,
            txtDirCasaAptoAlumno_Carga,
            txtDirPtoRefAlumno_Carga,
            ultimo_id_alumno))

        self.cursor.execute("""INSERT INTO Representente VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (txtNombreRepAlumno_Carga,
            txtApeRepAlumno_Carga,
            txtCiRep_Carga,
            txtDirHabRep_Carga,
            txtTelHabRep_Carga,
            txtTelCelRep_Carga,
            txtEmailRep_Carga,
            txtDirTrabajoRep_Carga,
            txtTelTrabajoRep_Carga,
            txtOcupacionRep_Carga,
            txtParentescoRep_Carga,
            ultimo_id_alumno))

        self.cursor.execute("""INSERT INTO AcademicoAlumno VALUES (?,?,?,?,?,?,?,?,?,?)""", (radioEstudiaAlumno_Carga,
            radioEducacionAlumno_Carga,
            txtGradoAlumno_Carga,
            txtAnioAlumno_Carga,
            txtSemestreAlumno_Carga,
            txtInstitAlumno_Carga,
            txtDireccionInstitAlumno_Carga,
            txtTelefonoInstitAlumno_Carga,
            radioTipoInstitAlumno_Carga,
            ultimo_id_alumno))

        self.cnn.commit()
        self.desconectar()

    def actualizarAlumno(self, alumnoID, txtNomAlumno_Carga,
                txtApeAlumno_Carga,
                txtCiAlumno_Carga,
                datePickerFechaNacAlumno_Carga,
                datePickerFechaIngAlumno_Carga,
                txtLugarNacAlumno_Carga,
                radioSexoAlumno_Carga,
                txtEdadAlumno_Carga,
                txtDirTelHabAlumno_Carga,
                txtDirTelCelAlumno_Carga,
                txtDirEmailalumno_Carga,
                txtDirMunicipioAlumno_Carga,
                txtDirParroquiaAlumno_Carga,
                txtDirSectorAlumno_Carga,
                txtDirUrbarrioAlumno_Carga,
                txtDirAvenidaAlumno_Carga,
                txtDirCalleAlumno_Carga,
                txtDirEdificioAlumno_Carga,
                txtDirCasaAptoAlumno_Carga,
                txtDirPtoRefAlumno_Carga,
                txtNombreRepAlumno_Carga,
                txtApeRepAlumno_Carga,
                txtCiRep_Carga,
                txtDirHabRep_Carga,
                txtTelHabRep_Carga,
                txtTelCelRep_Carga,
                txtEmailRep_Carga,
                txtDirTrabajoRep_Carga,
                txtTelTrabajoRep_Carga,
                txtOcupacionRep_Carga,
                txtParentescoRep_Carga,
                radioEstudiaAlumno_Carga,
                radioEducacionAlumno_Carga,
                txtGradoAlumno_Carga,
                txtAnioAlumno_Carga,
                txtSemestreAlumno_Carga,
                txtInstitAlumno_Carga,
                txtDireccionInstitAlumno_Carga,
                txtTelefonoInstitAlumno_Carga,
                radioTipoInstitAlumno_Carga,
                radioConocMusAlumno_Carga,
                choiceCatedraAlumno_Carga,
                choiceOrquAlumno_Carga,
                txtNivelOrqAlumno_Carga,
                radioInstPropioAlumno_Carga,
                datepickerFecAsigInstAlumno_Carga,
                txtMarcaInstAlumno_Carga,
                txtModeloInstAlumno_Carga,
                txtSerialInstAlumno_Carga,
                txtNumActFijoInstAlumno_Carga,
                txtProfAlumno_Carga,
                choiceStatusAlumno_Carga,
                radioOtraAgrupAlumno_Carga,
                txtNombreOtraAgrupAlumno_Carga,
                datePickerFechaIngOtraAgrupAlumno_Carga,
                txtFMedTipoSangreAlumno_Carga,
                txtFMedAntecedAlumno_Carga,
                radioFMedVacFA_Carga,
                datePickerFMedVacFA_Carga,
                radioFMedVacHA_Carga,
                datePickerFMedVacHA_Carga,
                radioFMedVacHB_Carga,
                datePickerFMedVacHB_Carga,
                radioFMedEnfCab_Carga,
                radioFMedEnfOid_Carga,
                radioFMedEnfNar_Carga,
                radioFMedEnfGar_Carga,
                radioFMedEnfCor_Carga,
                radioFMedEnfPul_Carga,
                radioFMedEnfVD_Carga,
                radioFMedEnfRi_Carga,
                radioFMedEnfHue_Carga,
                radioFMedEnfArt_Carga,
                radioFMedEnfEnd_Carga,
                txtFMedOperaciones_Carga,
                txtFMedAlerCom_Carga,
                txtFMedAlerMed_Carga,
                txtFMedAlerMedEsp_Carga,
                radioFMedTieneSeguro_Carga,
                txtFMedAseg_Carga,
                txtFMedTelAseg_Carga,
                txtFMedTelEmerg_Carga,
                txtFMedUnidadMedPref_Carga,
                txtFMedTratante_Carga,
                txtFMedTelTratante_Carga,
                txtFMedCelTratante_Carga,
                txtFMedEnfPrevia_Carga,
                txtFMedAperato_Carga,
                foto):
        """
        Actualiza Alumnos en la base de datos
        """
        self.conectar()

        self.cursor.execute("""UPDATE Alumnos SET nombreAlumno=?,apellidoAlumno=?,ciAlumno=?,fechaNacAlumno=?,fechaIngAlumno=?,
                                                    lugarNacAlumno=?,sexoAlumno=?,edadAlumno=?,telefonoResAlumno=?,telefonoCelAlumno=?,
                                                    emailAlumno=?, fotoAlumno=? WHERE idALumno=?""", (txtNomAlumno_Carga,
                                                                                                                txtApeAlumno_Carga,
                                                                                                                txtCiAlumno_Carga,
                                                                                                                datePickerFechaNacAlumno_Carga,
                                                                                                                datePickerFechaIngAlumno_Carga,
                                                                                                                txtLugarNacAlumno_Carga,
                                                                                                                radioSexoAlumno_Carga,
                                                                                                                txtEdadAlumno_Carga,
                                                                                                                txtDirTelHabAlumno_Carga,
                                                                                                                txtDirTelCelAlumno_Carga,
                                                                                                                txtDirEmailalumno_Carga,
                                                                                                                foto,
                                                                                                                alumnoID))

        self.cursor.execute("""UPDATE DatosMusicales SET conocimientosMusicales=?,catedraDatosMusicales=?,orquestaDatosMusicales=?,
                                                    nivelOrquestalDatosMusicales=?,instrumentoPropio=?,fechaAsigInstDatosMusicales=?,marcaInstrumentoDatosMusicales=?,
                                                    modeloInstrumentoDatosMusicales=?,serialInstrumentoDatosMusicales=?,numeroActivoFijoInstDatosMusicales=?,
                                                    profesorDatosMusicales=?,statusDatosMusicales=?,otraAgrupacionDatosMusicales=?,nombreOtraAgrupacionDatosMusicales=?,
                                                    fechaIngresoOtraDatosMusicales=?,Alumnos_idAlumno=?
                                                    WHERE Alumnos_idAlumno=?""", (radioConocMusAlumno_Carga,
                                                                                                    choiceCatedraAlumno_Carga,
                                                                                                    choiceOrquAlumno_Carga,
                                                                                                    txtNivelOrqAlumno_Carga,
                                                                                                    radioInstPropioAlumno_Carga,
                                                                                                    datepickerFecAsigInstAlumno_Carga,
                                                                                                    txtMarcaInstAlumno_Carga,
                                                                                                    txtModeloInstAlumno_Carga,
                                                                                                    txtSerialInstAlumno_Carga,
                                                                                                    txtNumActFijoInstAlumno_Carga,
                                                                                                    txtProfAlumno_Carga,
                                                                                                    choiceStatusAlumno_Carga,
                                                                                                    radioOtraAgrupAlumno_Carga,
                                                                                                    txtNombreOtraAgrupAlumno_Carga,
                                                                                                    datePickerFechaIngOtraAgrupAlumno_Carga,
                                                                                                    alumnoID,
                                                                                                    alumnoID))

        self.cursor.execute("""UPDATE FichaMedica SET Alumnos_idAlumno=?,tipoSangreFichaMedica=?,antGeneralesFichaMedica=?,vacunaFAmarilla=?,
                                                    fechaVacunaFAmarilla=?,vacunaHepatitisA=?,fechaVacunaHepatitisA=?,vacunaHepatitisB=?,fechaVacunaHepatitisB=?,enfCabeza=?,
                                                    enfOido=?,enfNariz=?,enfGarganta=?,enfCorazon=?,enfPulmones=?,enfViaDigestiva=?,enfRiniones=?,enfHuesos=?,enfArticulaciones=?,
                                                    enfEndocrino=?,operaciones=?,alergiaComida=?,alergiaMedicamentos=?,medicamentoEspecifico=?,seguroMedico=?,aseguradora=?,
                                                    telefonoAseguradora=?,numeroEmergencia=?,unidadMedicaPreferencia=?,medicoTratante=?,telefonoMedicoTratante=?,
                                                    telefonoCelMedicoTratante=?,otraEnfermedadCondicion=?,aparatoquipoMedico=?
                                                    WHERE Alumnos_idAlumno=?""", (alumnoID,
                                                                                                    txtFMedTipoSangreAlumno_Carga,
                                                                                                    txtFMedAntecedAlumno_Carga,
                                                                                                    radioFMedVacFA_Carga,
                                                                                                    datePickerFMedVacFA_Carga,
                                                                                                    radioFMedVacHA_Carga,
                                                                                                    datePickerFMedVacHA_Carga,
                                                                                                    radioFMedVacHB_Carga,
                                                                                                    datePickerFMedVacHB_Carga,
                                                                                                    radioFMedEnfCab_Carga,
                                                                                                    radioFMedEnfOid_Carga,
                                                                                                    radioFMedEnfNar_Carga,
                                                                                                    radioFMedEnfGar_Carga,
                                                                                                    radioFMedEnfCor_Carga,
                                                                                                    radioFMedEnfPul_Carga,
                                                                                                    radioFMedEnfVD_Carga,
                                                                                                    radioFMedEnfRi_Carga,
                                                                                                    radioFMedEnfHue_Carga,
                                                                                                    radioFMedEnfArt_Carga,
                                                                                                    radioFMedEnfEnd_Carga,
                                                                                                    txtFMedOperaciones_Carga,
                                                                                                    txtFMedAlerCom_Carga,
                                                                                                    txtFMedAlerMed_Carga,
                                                                                                    txtFMedAlerMedEsp_Carga,
                                                                                                    radioFMedTieneSeguro_Carga,
                                                                                                    txtFMedAseg_Carga,
                                                                                                    txtFMedTelAseg_Carga,
                                                                                                    txtFMedTelEmerg_Carga,
                                                                                                    txtFMedUnidadMedPref_Carga,
                                                                                                    txtFMedTratante_Carga,
                                                                                                    txtFMedTelTratante_Carga,
                                                                                                    txtFMedCelTratante_Carga,
                                                                                                    txtFMedEnfPrevia_Carga,
                                                                                                    txtFMedAperato_Carga,
                                                                                                    alumnoID))

        self.cursor.execute("""UPDATE DireccionAlumno SET municipio=?,parroquia=?,sector=?,urbBarrio=?,avenida=?,calle=?,
                                                    edificio=?,casaApto=?,ptoReferencia=?,Alumnos_idAlumno=?
                                                    WHERE Alumnos_idAlumno=? """, (txtDirMunicipioAlumno_Carga,
                                                                                                        txtDirParroquiaAlumno_Carga,
                                                                                                        txtDirSectorAlumno_Carga,
                                                                                                        txtDirUrbarrioAlumno_Carga,
                                                                                                        txtDirAvenidaAlumno_Carga,
                                                                                                        txtDirCalleAlumno_Carga,
                                                                                                        txtDirEdificioAlumno_Carga,
                                                                                                        txtDirCasaAptoAlumno_Carga,
                                                                                                        txtDirPtoRefAlumno_Carga,
                                                                                                        alumnoID,
                                                                                                        alumnoID))

        self.cursor.execute("""UPDATE Representente SET nomRepresentante=?,apellidoRepresentante=?,ciRepresentante=?,direccionRepresentante=?,
                                                    telefonoHabRepresentante=?,telefonoCelRepresentante=?,emailRepresentante=?,dirTrabajoRepresentante=?,
                                                    telefonoTrabRepresentante=?,ocupacionRepresentante=?,parentescoRepresentante=?,Alumnos_idAlumno=?
                                                    WHERE Alumnos_idAlumno=?""", (txtNombreRepAlumno_Carga,
                                                                                                    txtApeRepAlumno_Carga,
                                                                                                    txtCiRep_Carga,
                                                                                                    txtDirHabRep_Carga,
                                                                                                    txtTelHabRep_Carga,
                                                                                                    txtTelCelRep_Carga,
                                                                                                    txtEmailRep_Carga,
                                                                                                    txtDirTrabajoRep_Carga,
                                                                                                    txtTelTrabajoRep_Carga,
                                                                                                    txtOcupacionRep_Carga,
                                                                                                    txtParentescoRep_Carga,
                                                                                                    alumnoID,
                                                                                                    alumnoID))

        self.cursor.execute("""UPDATE AcademicoAlumno SET estudiaAcademicoAlumno=?,nivelAcademicoAlumno=?,gradoAcademicoAlumno=?,
                                                                                      anioAcademicoAlumno=?,semestreAcademicoAlumno=?,institucionAcademicoAlumno=?,
                                                                                      direccionAcademicoAlumno=?,telefonoAcademicoAlumno=?,tipoInstitucionAcademicoAlumno=?,
                                                                                      Alumnos_idAlumno=? WHERE Alumnos_idAlumno=?""", (radioEstudiaAlumno_Carga,
                                                                                                                                                                        radioEducacionAlumno_Carga,
                                                                                                                                                                        txtGradoAlumno_Carga,
                                                                                                                                                                        txtAnioAlumno_Carga,
                                                                                                                                                                        txtSemestreAlumno_Carga,
                                                                                                                                                                        txtInstitAlumno_Carga,
                                                                                                                                                                        txtDireccionInstitAlumno_Carga,
                                                                                                                                                                        txtTelefonoInstitAlumno_Carga,
                                                                                                                                                                        radioTipoInstitAlumno_Carga,
                                                                                                                                                                        alumnoID,
                                                                                                                                                                        alumnoID))

        self.cnn.commit()
        self.desconectar()

    def eliminarAlumno(self, id):
        """
        Elimina Alumnos de la base de datos
        """
        self.conectar()
        try:
            sql1 = """DELETE FROM Alumnos WHERE idAlumno=?"""
            self.cursor.execute("PRAGMA foreign_keys = ON")
            self.cursor.execute(sql1, (id,))
            self.cnn.commit()
        except sqlite3.Error, e:
            print "Error eliminando Profesor %s" % e
            self.cnn.rollback()
        finally:
            self.desconectar()

    def listarAlumnos(self):
        """
        Lista todos los Alumnos registrados
        """
        self.conectar()
        sql = """SELECT DISTINCT * FROM Alumnos INNER JOIN DatosMusicales WHERE Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno ORDER BY idAlumno"""
        self.cursor.execute(sql)
        listado = self.cursor.fetchall()
        self.desconectar()
        return listado

    def reporteGeneralAlumnos(self, catedra=None, tipo=None):
        """
        Genera reportes de Alumnos registrados
        """
        self.conectar()
        if catedra == 'Todas' and tipo == 1:
            sql = """SELECT DISTINCT Alumnos.apellidoAlumno, 
                                     Alumnos.nombreAlumno,
                                     Alumnos.ciAlumno, 
                                     DatosMusicales.catedraDatosMusicales
                     FROM Alumnos INNER JOIN DatosMusicales
                     WHERE Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno 
                     ORDER BY Alumnos.apellidoAlumno ASC"""
            self.cursor.execute(sql)
        elif catedra == 'Todas' and tipo == 2:
            sql="""SELECT DISTINCT Alumnos.apellidoAlumno, Alumnos.nombreAlumno,Alumnos.ciAlumno,Alumnos.fechaNacAlumno, Alumnos.fechaIngAlumno, Alumnos.lugarNacAlumno,
                               Alumnos.sexoAlumno, Alumnos.edadAlumno, Alumnos.telefonoResAlumno, Alumnos.telefonoCelAlumno, Alumnos.emailAlumno,
                               DatosMusicales.conocimientosMusicales, DatosMusicales.catedraDatosMusicales,DatosMusicales.orquestaDatosMusicales,
                               DatosMusicales.nivelOrquestalDatosMusicales, DatosMusicales.instrumentoPropio, DatosMusicales.fechaAsigInstDatosMusicales,
                               DatosMusicales.marcaInstrumentoDatosMusicales, DatosMusicales.modeloInstrumentoDatosMusicales, DatosMusicales.serialInstrumentoDatosMusicales,
                               DatosMusicales.numeroActivoFijoInstDatosMusicales, DatosMusicales.profesorDatosMusicales, DatosMusicales.otraAgrupacionDatosMusicales,
                               DatosMusicales.nombreOtraAgrupacionDatosMusicales, DatosMusicales.fechaIngresoOtraDatosMusicales,
                               DireccionAlumno.municipio, DireccionAlumno.parroquia, DireccionAlumno.sector, DireccionAlumno.urbBarrio, DireccionAlumno.avenida,
                               DireccionAlumno.calle, DireccionAlumno.edificio, DireccionAlumno.casaApto, DireccionAlumno.ptoReferencia,
                               Representente.nomRepresentante,Representente.apellidoRepresentante,Representente.ciRepresentante,Representente.direccionRepresentante,
                               Representente.telefonoHabRepresentante,Representente.telefonoCelRepresentante,Representente.emailRepresentante,
                               Representente.dirTrabajoRepresentante,Representente.telefonoTrabRepresentante,Representente.ocupacionRepresentante,Representente.parentescoRepresentante,
                               AcademicoAlumno.estudiaAcademicoAlumno,AcademicoAlumno.nivelAcademicoAlumno,AcademicoAlumno.gradoAcademicoAlumno,
                               AcademicoAlumno.anioAcademicoAlumno,AcademicoAlumno.semestreAcademicoAlumno,AcademicoAlumno.institucionAcademicoAlumno,
                               AcademicoAlumno.direccionAcademicoAlumno,AcademicoAlumno.telefonoAcademicoAlumno,AcademicoAlumno.tipoInstitucionAcademicoAlumno
                        FROM Alumnos INNER JOIN DatosMusicales INNER JOIN DireccionAlumno INNER JOIN Representente INNER JOIN AcademicoAlumno
                        WHERE Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno AND Alumnos.idAlumno=DireccionAlumno.Alumnos_idAlumno
                            AND Alumnos.idAlumno=Representente.Alumnos_idAlumno
                            AND Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno 
                            AND Alumnos.idAlumno=AcademicoAlumno.Alumnos_idAlumno ORDER BY Alumnos.ciAlumno"""
            self.cursor.execute(sql)
        elif catedra != 'Todas' and tipo == 1:
            sql="""SELECT DISTINCT Alumnos.apellidoAlumno, Alumnos.nombreAlumno,Alumnos.ciAlumno, DatosMusicales.catedraDatosMusicales
                   FROM Alumnos INNER JOIN DatosMusicales
                   WHERE Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno AND DatosMusicales.catedraDatosMusicales like ?
                   ORDER BY DatosMusicales.catedraDatosMusicales ASC"""
            self.cursor.execute(sql, ('%'+catedra+'%',))
        elif catedra != 'Todas' and tipo == 2:
            sql="""SELECT DISTINCT Alumnos.apellidoAlumno, Alumnos.nombreAlumno,Alumnos.ciAlumno,Alumnos.fechaNacAlumno, Alumnos.fechaIngAlumno, Alumnos.lugarNacAlumno,
                               Alumnos.sexoAlumno, Alumnos.edadAlumno, Alumnos.telefonoResAlumno, Alumnos.telefonoCelAlumno, Alumnos.emailAlumno,
                               DatosMusicales.conocimientosMusicales, DatosMusicales.catedraDatosMusicales,DatosMusicales.orquestaDatosMusicales,
                               DatosMusicales.nivelOrquestalDatosMusicales, DatosMusicales.instrumentoPropio, DatosMusicales.fechaAsigInstDatosMusicales,
                               DatosMusicales.marcaInstrumentoDatosMusicales, DatosMusicales.modeloInstrumentoDatosMusicales, DatosMusicales.serialInstrumentoDatosMusicales,
                               DatosMusicales.numeroActivoFijoInstDatosMusicales, DatosMusicales.profesorDatosMusicales, DatosMusicales.otraAgrupacionDatosMusicales,
                               DatosMusicales.nombreOtraAgrupacionDatosMusicales, DatosMusicales.fechaIngresoOtraDatosMusicales,
                               DireccionAlumno.municipio, DireccionAlumno.parroquia, DireccionAlumno.sector, DireccionAlumno.urbBarrio, DireccionAlumno.avenida,
                               DireccionAlumno.calle, DireccionAlumno.edificio, DireccionAlumno.casaApto, DireccionAlumno.ptoReferencia,
                               Representente.nomRepresentante,Representente.apellidoRepresentante,Representente.ciRepresentante,Representente.direccionRepresentante,
                               Representente.telefonoHabRepresentante,Representente.telefonoCelRepresentante,Representente.emailRepresentante,
                               Representente.dirTrabajoRepresentante,Representente.telefonoTrabRepresentante,Representente.ocupacionRepresentante,Representente.parentescoRepresentante,
                               AcademicoAlumno.estudiaAcademicoAlumno,AcademicoAlumno.nivelAcademicoAlumno,AcademicoAlumno.gradoAcademicoAlumno,
                               AcademicoAlumno.anioAcademicoAlumno,AcademicoAlumno.semestreAcademicoAlumno,AcademicoAlumno.institucionAcademicoAlumno,
                               AcademicoAlumno.direccionAcademicoAlumno,AcademicoAlumno.telefonoAcademicoAlumno,AcademicoAlumno.tipoInstitucionAcademicoAlumno
                        FROM Alumnos INNER JOIN DatosMusicales INNER JOIN DireccionAlumno INNER JOIN Representente INNER JOIN AcademicoAlumno
                        WHERE Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno AND Alumnos.idAlumno=DireccionAlumno.Alumnos_idAlumno
                            AND Alumnos.idAlumno=Representente.Alumnos_idAlumno
                            AND Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno AND DatosMusicales.catedraDatosMusicales like ? 
                            AND Alumnos.idAlumno=AcademicoAlumno.Alumnos_idAlumno ORDER BY Alumnos.ciAlumno"""
            self.cursor.execute(sql, ('%'+catedra+'%',))

        reporte = self.cursor.fetchall()
        self.desconectar()
        return reporte

    def reporteGeneralFichaMedica(self, catedra = None):
        """
        Lista todos los profesores registrados
        """
        self.conectar()
        if catedra=='Todas':
            sql="""SELECT DISTINCT FichaMedica.tipoSangreFichaMedica,FichaMedica.antGeneralesFichaMedica, FichaMedica.vacunaFAmarilla, FichaMedica.fechaVacunaFAmarilla, FichaMedica.vacunaHepatitisA,
                                                 FichaMedica.fechaVacunaHepatitisA,FichaMedica.vacunaHepatitisB,FichaMedica.fechaVacunaHepatitisB,FichaMedica.enfCabeza,
                                                 FichaMedica.enfOido,FichaMedica.enfNariz,FichaMedica.enfGarganta,FichaMedica.enfCorazon,FichaMedica.enfPulmones,
                                                 FichaMedica.enfViaDigestiva,FichaMedica.enfRiniones,FichaMedica.enfHuesos,FichaMedica.enfArticulaciones,FichaMedica.enfEndocrino,
                                                 FichaMedica.operaciones,FichaMedica.alergiaComida,FichaMedica.alergiaMedicamentos,FichaMedica.medicamentoEspecifico,
                                                 FichaMedica.seguroMedico,FichaMedica.aseguradora,FichaMedica.telefonoAseguradora,
                                                 FichaMedica.numeroEmergencia,FichaMedica.unidadMedicaPreferencia,FichaMedica.medicoTratante,FichaMedica.telefonoMedicoTratante,
                                                 FichaMedica.telefonoCelMedicoTratante,FichaMedica.otraEnfermedadCondicion,FichaMedica.aparatoquipoMedico, Alumnos.apellidoAlumno, Alumnos.nombreAlumno
                        FROM FichaMedica INNER JOIN DatosMusicales INNER JOIN Alumnos
                        WHERE FichaMedica.Alumnos_idAlumno=DatosMusicales.Alumnos_idAlumno AND FichaMedica.Alumnos_idAlumno=Alumnos.idALumno
                                ORDER BY FichaMedica.Alumnos_idAlumno ASC"""
            self.cursor.execute(sql)
        else:
            sql="""SELECT DISTINCT FichaMedica.tipoSangreFichaMedica,FichaMedica.antGeneralesFichaMedica, FichaMedica.vacunaFAmarilla, FichaMedica.fechaVacunaFAmarilla, FichaMedica.vacunaHepatitisA,
                                                 FichaMedica.fechaVacunaHepatitisA,FichaMedica.vacunaHepatitisB,FichaMedica.fechaVacunaHepatitisB,FichaMedica.enfCabeza,
                                                 FichaMedica.enfOido,FichaMedica.enfNariz,FichaMedica.enfGarganta,FichaMedica.enfCorazon,FichaMedica.enfPulmones,
                                                 FichaMedica.enfViaDigestiva,FichaMedica.enfRiniones,FichaMedica.enfHuesos,FichaMedica.enfArticulaciones,FichaMedica.enfEndocrino,
                                                 FichaMedica.operaciones,FichaMedica.alergiaComida,FichaMedica.alergiaMedicamentos,FichaMedica.medicamentoEspecifico,
                                                 FichaMedica.seguroMedico,FichaMedica.aseguradora,FichaMedica.telefonoAseguradora,
                                                 FichaMedica.numeroEmergencia,FichaMedica.unidadMedicaPreferencia,FichaMedica.medicoTratante,FichaMedica.telefonoMedicoTratante,
                                                 FichaMedica.telefonoCelMedicoTratante,FichaMedica.otraEnfermedadCondicion,FichaMedica.aparatoquipoMedico, Alumnos.apellidoAlumno, Alumnos.nombreAlumno
                        FROM FichaMedica INNER JOIN DatosMusicales INNER JOIN Alumnos
                        WHERE FichaMedica.Alumnos_idAlumno=DatosMusicales.Alumnos_idAlumno AND FichaMedica.Alumnos_idAlumno=Alumnos.idALumno AND DatosMusicales.catedraDatosMusicales like ?
                                ORDER BY FichaMedica.Alumnos_idAlumno ASC"""
            self.cursor.execute(sql, ('%'+catedra+'%',))

        reporte = self.cursor.fetchall()
        self.desconectar()
        return reporte


    def buscarAlumno(self, nombre, catedra=None):
        """
        busca todos los datos de un alumno especifico enre  todos los registrados
        """
        self.conectar()
        if not catedra:
            sql="""SELECT DISTINCT * FROM Alumnos INNER JOIN DatosMusicales WHERE Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno AND (Alumnos.nombreAlumno like ? OR Alumnos.apellidoAlumno like ? OR Alumnos.ciAlumno like ?)"""
            self.cursor.execute(sql, ('%'+unicode(nombre)+'%', '%'+unicode(nombre)+'%','%'+unicode(nombre)+'%',))
        else:
            sql="""SELECT DISTINCT * FROM Alumnos INNER JOIN DatosMusicales WHERE (Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno AND DatosMusicales.catedraDatosMusicales like ?) AND (DatosMusicales.catedraDatosMusicales like ? AND (Alumnos.nombreAlumno like ? OR Alumnos.apellidoAlumno like ? OR Alumnos.ciAlumno like ?))"""
            self.cursor.execute(sql, ('%'+unicode(catedra)+'%', '%'+unicode(catedra)+'%', '%'+unicode(nombre)+'%', '%'+unicode(nombre)+'%','%'+unicode(nombre)+'%',))

        prof= self.cursor.fetchall()
        self.desconectar()
        return prof

    def buscarID_Alumno(self, nombre=None):
        """
        busca el ID de un alumno especifico enre  todos los registrados
        """
        self.conectar()
        if nombre:
            sql="""SELECT DISTINCT ciAlumno FROM Alumnos WHERE ciAlumno = ?"""
            self.cursor.execute(sql, (nombre, ))
        else:
            sql="""SELECT DISTINCT idAlumno FROM Alumnos"""
            self.cursor.execute(sql)
        alumno= self.cursor.fetchone()
        self.desconectar()
        return alumno

    def obtenerDatosAlumno(self, alumno=None):
        self.conectar()
        sql="""SELECT * FROM Alumnos JOIN DatosMusicales JOIN FichaMedica JOIN DireccionAlumno JOIN Representente JOIN AcademicoAlumno
                  WHERE idALumno = ? AND DatosMusicales.Alumnos_idAlumno=Alumnos.idALumno AND FichaMedica.ALumnos_idALumno=Alumnos.idALumno
                             AND DireccionAlumno.Alumnos_idAlumno=Alumnos.idALumno AND Representente.Alumnos_idAlumno=Alumnos.idALumno
                             AND AcademicoAlumno.Alumnos_idAlumno=Alumnos.idALumno"""
        self.cursor.execute(sql, (alumno, ))
        datosAlumno= self.cursor.fetchone()
        self.desconectar()
        return datosAlumno

    def buscarFoto(self, alumno=None, todos=False):
        self.conectar()
        if todos:
            sql = """SELECT fotoAlumno FROM Alumnos"""
            self.cursor.execute(sql)
            nombreFoto = self.cursor.fetchall()
        elif not todos and alumno is not None:
            sql="""SELECT fotoAlumno FROM Alumnos WHERE idALumno = ?"""
            self.cursor.execute(sql, (alumno, ))
            nombreFoto = self.cursor.fetchone()
        self.desconectar()
        return nombreFoto

    def reportealumnosProfesor(self, profesor):
        self.conectar()
        sql="""SELECT DISTINCT Alumnos.apellidoAlumno, Alumnos.nombreAlumno,Alumnos.ciAlumno,Alumnos.edadAlumno,DatosMusicales.catedraDatosMusicales,DatosMusicales.profesorDatosMusicales
                   FROM Alumnos INNER JOIN DatosMusicales
                   WHERE DatosMusicales.profesorDatosMusicales like ? AND Alumnos.idAlumno=DatosMusicales.Alumnos_idAlumno
                   ORDER BY Alumnos.ciAlumno ASC"""
        self.cursor.execute(sql, ('%'+profesor+'%',))
        listado = self.cursor.fetchall()
        self.desconectar()
        return listado

