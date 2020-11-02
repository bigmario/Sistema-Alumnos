#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Generacion de Reportes
## Ultima Revisión: 19-11-2012 11:05 a.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 07 de Noviembre de 2012
#
# +-------------------------------------------------+#
###########################################################################

import os
import sys
import tempfile
from modelo import ModeloBD
from datetime import datetime, date
import time
from dateutil import relativedelta
from dateutil import rrule
import calendar

#Obtenemos de platypus las clases Paragraph, para escribir párrafos Image, para insertar imágenes y SimpleDocTemplate para definir el DocTemplate.
#Además importamos Spacer, para incluir espacios  e Image para agregar El logo en la cabecera.
from reportlab.platypus import Paragraph
from reportlab.platypus import PageBreak
from reportlab.platypus import Image as Imagen_Reporte
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
#Se carga el módulo apropiado para las tablas:
from reportlab.platypus import Table
#Importamos clase de hoja de estilo de ejemplo.
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
#Se importa el tamaño de la hoja.
from reportlab.lib.pagesizes import letter, legal, landscape, portrait
#Y los colores.
from reportlab.lib import colors

class Reportes:

    def __init__(self):
        self.BD=ModeloBD()

    def CrearFichaAlumno(self, alumno):
        """
        Generacion del documento PDF referente a la Ficha General del Alumno
        """
        datosAlumno=self.BD.obtenerDatosAlumno(alumno)
        self.alumnoID=datosAlumno[0]


        ##############################################################################
        ##############################################################################


        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=12, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='Datos', alignment=TA_LEFT, fontSize=10,))

        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        datos=estiloHoja['Datos']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabeceraFicha.png"
        imagen_logo = Imagen_Reporte(os.path.realpath(fichero_imagen))
        imagen_logo.hAlign = 'LEFT'

        foto_alumno =datosAlumno["fotoAlumno"]
        foto = Imagen_Reporte(os.path.realpath(foto_alumno), width=80,height=60)
        foto.hAlign = 'RIGHT'

        tablaCabecera=[[imagen_logo,'                                                                                               ',foto]]
        header = Table(tablaCabecera)
        story.append(header)

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = u"Ficha de Alumno  - %s, %s</b>" % (unicode(datosAlumno["apellidoAlumno"]), unicode(datosAlumno["nombreAlumno"]))

        #Damos un estilo al segundo párrafo, que será el texto a escribir.
        parrafo2 = Paragraph(cadena, subtitulo)

        #Y lo incluimos en el story.

        story.append(parrafo2)

        #Y a continuación tendríamos la Tabla:

        #Dejamos espacio.

        #################################################################
        datos2= u"<b>Datos del alumno</b>"
        representante=u"<b>Datos del Representante</b>"
        academicos=u"<b>Datos académicos</b>"
        musicales="<b>Datos Musicales</b>"

        parrafo3 = Paragraph(datos2, datos)
        parrafo4 = Paragraph(representante, datos)
        parrafo5 = Paragraph(academicos, datos)
        parrafo6 = Paragraph(musicales, datos)

        if not datosAlumno["fechaIngAlumno"]==None:
            fechaIngreso="%s/%s/%s"%(datosAlumno["fechaIngAlumno"][8:], datosAlumno["fechaIngAlumno"][5:7], datosAlumno["fechaIngAlumno"][:4])
        else:
            fechaIngreso=''

        if not datosAlumno["fechaNacAlumno" ]==None:
            fechaNacimiento="%s/%s/%s"%(datosAlumno["fechaNacAlumno" ][8:], datosAlumno["fechaNacAlumno" ][5:7], datosAlumno["fechaNacAlumno" ][:4])
        else:
            fechaNacimiento=''

        if not datosAlumno["fechaAsigInstDatosMusicales" ]==None:
            fechaAsignaion="%s/%s/%s"%(datosAlumno["fechaAsigInstDatosMusicales" ][8:], datosAlumno["fechaAsigInstDatosMusicales" ][5:7], datosAlumno["fechaAsigInstDatosMusicales" ][:4])
        else:
            fechaAsignaion=''

        if not datosAlumno["fechaIngresoOtraDatosMusicales" ]==None:
            fechaOtraA="%s/%s/%s"%(datosAlumno["fechaIngresoOtraDatosMusicales" ][8:], datosAlumno["fechaIngresoOtraDatosMusicales" ][5:7], datosAlumno["fechaIngresoOtraDatosMusicales" ][:4])
        else:
            fechaOtraA=''

        if not datosAlumno==[]:
            tablaDatosGenerales=[['Apellidos y Nombres:\n %s %s'%(datosAlumno["apellidoAlumno" ],datosAlumno["nombreAlumno" ]),u'Cédula de identidad:\n %s'%datosAlumno["ciAlumno" ], u'Fecha de Ingreso:\n %s'%fechaIngreso],
                                             ['Lugar de Nacimiento:\n %s'%datosAlumno["lugarNacAlumno" ],'Fecha de Nacimiento:\n %s'%fechaNacimiento,'Sexo:\n %s'%datosAlumno["sexoAlumno" ], 'Edad:\n %s'%datosAlumno["edadAlumno" ]],
                                             ['Municipio:\n %s'%datosAlumno["municipio" ],'Parroquia:\n %s'%datosAlumno["parroquia" ],'Sector:\n %s'%datosAlumno["sector" ], 'Urb. / Barrio:\n %s'%datosAlumno["urbBarrio" ]],
                                             ['Avenida:\n %s'%datosAlumno["avenida" ],'Calle:\n %s'%datosAlumno["calle" ],'Edificio:\n %s'%datosAlumno["edificio" ], u'Nº Casa/Apto.:\n %s'%datosAlumno["casaApto" ]],
                                             ['Pto. de Referencia:\n %s'%datosAlumno["ptoReferencia" ]],
                                             ['Telf. Hab:\n %s'%datosAlumno["telefonoResAlumno" ],'Telf. Celular:\n %s'%datosAlumno["telefonoCelAlumno" ],'E-mail:\n %s'%datosAlumno["emailAlumno" ]]
                                            ]

            tablaDatosRepresentante=[['Apellidos y Nombres:\n %s %s'%(datosAlumno["apellidoRepresentante" ],datosAlumno["nomRepresentante" ]),u'Cédula de identidad:\n %s'%datosAlumno["ciRepresentante" ]],
                                                   [u'Dirección de Habitación:\n %s'%datosAlumno["direccionRepresentante" ]],
                                                   ['Telf. Hab:\n %s'%datosAlumno["telefonoHabRepresentante" ],'Telf. Celular:\n %s'%datosAlumno["telefonoCelRepresentante" ],'E-mail:\n %s'%datosAlumno["emailRepresentante" ]],
                                                   [u'Direción de Trabajo:\n %s'%datosAlumno["dirTrabajoRepresentante" ]],
                                                   ['Telf. Trab:\n %s'%datosAlumno["telefonoTrabRepresentante" ],u'Ocupación:\n %s'%datosAlumno["ocupacionRepresentante" ],'Parentesco:\n %s'%datosAlumno["parentescoRepresentante" ]]
                                                  ]

            tablaDatosAcademicos=[['Estudia Actualmente?:\n %s'%datosAlumno["estudiaAcademicoAlumno" ],u'Nivel de Educación:\n %s'%datosAlumno["nivelAcademicoAlumno" ]],
                                                ['Grado:\n %s'%datosAlumno["gradoAcademicoAlumno" ],u'Año:\n %s'%datosAlumno["anioAcademicoAlumno" ],'Semestre:\n %s'%datosAlumno["semestreAcademicoAlumno" ],u'Institución:\n %s'%datosAlumno["institucionAcademicoAlumno" ]],
                                                [u'Dirección:\n %s'%datosAlumno["direccionAcademicoAlumno" ]],
                                                ['Telf.:\n %s'%datosAlumno["telefonoAcademicoAlumno" ],u'Tipo de Institución:\n %s'%datosAlumno["tipoInstitucionAcademicoAlumno" ]]
                                               ]

            tablaDatosMusicales=[['Conocimientos Musicales?:\n %s'%datosAlumno["conocimientosMusicales" ],u'Cátedra a Cursar:\n %s'%datosAlumno["catedraDatosMusicales" ]],
                                            [u'Instrumento Propio?:\n %s'%datosAlumno["instrumentoPropio" ], u'Fecha de Asignación:\n %s'%fechaAsignaion],
                                            ['Marca:\n %s'%datosAlumno["marcaInstrumentoDatosMusicales" ],'Modelo:\n %s'%datosAlumno["modeloInstrumentoDatosMusicales" ], 'Serial:\n %s'%datosAlumno["serialInstrumentoDatosMusicales" ], u'Nº de Activo Fijo FUNDAMUSICAL:\n %s'%datosAlumno["numeroActivoFijoInstDatosMusicales" ]],
                                            ['Orquesta a la que pertenece:\n %s'%datosAlumno["orquestaDatosMusicales" ],'Nivel:\n %s'%datosAlumno["nivelOrquestalDatosMusicales" ],'Profesor:\n %s'%datosAlumno["profesorDatosMusicales" ]],
                                            [u'Pertenece a otra Agrupaicón:\n %s'%datosAlumno["otraAgrupacionDatosMusicales" ], u'Nombre de la Agrupaición:\n %s'%datosAlumno["nombreOtraAgrupacionDatosMusicales" ], u'Fecha de Ingreso:\n %s'%fechaOtraA]
                                           ]

            #Definimos la tabla.
            tabla1 = Table(tablaDatosGenerales,style=[('SPAN',(0,4),(-1,4)), ('SPAN',(2,0),(-1,0)),('SPAN',(2,5),(-1,5))])
            tabla2 = Table(tablaDatosRepresentante, style=[('SPAN',(0,3),(-1,3)), ('SPAN',(1,0),(-1,0)),('SPAN',(0,1),(-1,1))])
            tabla3 = Table(tablaDatosAcademicos, style=[('SPAN',(0,2),(-1,2)), ('SPAN',(1,0),(-1,0)),('SPAN',(1,-1),(3,-1))])
            tabla4 = Table(tablaDatosMusicales)

            #Creamos una caja alrededor de las celdas.
            tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            tabla1.hAlign='LEFT'
            tabla2.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            tabla2.hAlign='LEFT'
            tabla3.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            tabla3.hAlign='LEFT'
            tabla4.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            tabla4.hAlign='LEFT'
            #Y ponemos una malla (rejilla) a la tabla.
            tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla2.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla3.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla4.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            #Y la asignamos al platypus story.
            story.append(parrafo3)
            story.append(tabla1)
            story.append(parrafo4)
            story.append(tabla2)
            story.append(PageBreak())
            story.append(parrafo5)
            story.append(tabla3)
            story.append(parrafo6)
            story.append(tabla4)
        else:
            parrafo5=Paragraph(u'Error', cabecera)
            story.append(parrafo5)
            story.append(Spacer(0,20))

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        name = "FichaAlumno-%s-%s" % (date_str, os.getpid())
        temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir=os.environ['TEMP'],)
        temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        doc.pagesize=landscape(letter)
        doc.build(story)

        #self.open_report(temp.name)
        self.tempFile=temp.name
        return temp.name

    def CrearFichaMedicaAlumno(self, alumno):
        """
        Generacion del documento PDF referente a la Ficha Medica del Alumno
        """
        datosAlumno=self.BD.obtenerDatosAlumno(alumno)
        self.alumnoID=datosAlumno[0]


        ##############################################################################
        ##############################################################################


        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=12, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='Datos', alignment=TA_LEFT, fontSize=10,))

        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        datos=estiloHoja['Datos']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabeceraFicha.png"
        imagen_logo = Imagen_Reporte(os.path.realpath(fichero_imagen))
        imagen_logo.hAlign = 'LEFT'

        foto_alumno =datosAlumno["fotoAlumno"]
        foto = Imagen_Reporte(os.path.realpath(foto_alumno), width=80,height=60)
        foto.hAlign = 'RIGHT'

        tablaCabecera=[[imagen_logo,'                                                                                               ',foto]]
        header = Table(tablaCabecera)
        story.append(header)

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = u"Ficha Médica de Alumno  - %s, %s</b>" % (unicode(datosAlumno["apellidoAlumno"]), unicode(datosAlumno["nombreAlumno"]))

        #Damos un estilo al segundo párrafo, que será el texto a escribir.
        parrafo2 = Paragraph(cadena, subtitulo)

        #Y lo incluimos en el story.

        story.append(parrafo2)

        #Y a continuación tendríamos la Tabla:

        #Dejamos espacio.

        #################################################################
        datos2= u"<b>Datos del alumno</b>"
        representante=u"<b>Datos del Representante</b>"
        academicos=u"<b>Datos Médicos</b>"

        parrafo3 = Paragraph(datos2, datos)
        parrafo4 = Paragraph(representante, datos)
        parrafo5 = Paragraph(academicos, datos)

        if not datosAlumno["fechaIngAlumno"]==None:
            fechaIngreso="%s/%s/%s"%(datosAlumno["fechaIngAlumno"][8:], datosAlumno["fechaIngAlumno"][5:7], datosAlumno["fechaIngAlumno"][:4])
        else:
            fechaIngreso=''

        if not datosAlumno["fechaNacAlumno" ]==None:
            fechaNacimiento="%s/%s/%s"%(datosAlumno["fechaNacAlumno" ][8:], datosAlumno["fechaNacAlumno" ][5:7], datosAlumno["fechaNacAlumno" ][:4])
        else:
            fechaNacimiento=''

        if datosAlumno["fechaVacunaFAmarilla" ] is not None:
            fechaFA="%s/%s/%s"%(datosAlumno["fechaVacunaFAmarilla" ][8:], datosAlumno["fechaVacunaFAmarilla" ][5:7], datosAlumno["fechaVacunaFAmarilla" ][:4])
        else:
            fechaFA=''

        if datosAlumno["fechaVacunaHepatitisA" ] is not None:
            fechaHA="%s/%s/%s"%(datosAlumno["fechaVacunaHepatitisA" ][8:], datosAlumno["fechaVacunaHepatitisA" ][5:7], datosAlumno["fechaVacunaHepatitisA" ][:4])
        else:
            fechaHA=''

        if datosAlumno["fechaVacunaHepatitisB" ] is not None:
            fechaHB="%s/%s/%s"%(datosAlumno["fechaVacunaHepatitisB" ][8:], datosAlumno["fechaVacunaHepatitisB" ][5:7], datosAlumno["fechaVacunaHepatitisB" ][:4])
        else:
            fechaHB=''

        if not datosAlumno==[]:
            tablaDatosGenerales=[['Apellidos y Nombres:\n %s %s'%(datosAlumno["apellidoAlumno" ],datosAlumno["nombreAlumno" ]),u'Cédula de identidad:\n %s'%datosAlumno["ciAlumno" ], u'Fecha de Ingreso:\n %s'%fechaIngreso],
                                             ['Lugar de Nacimiento:\n %s'%datosAlumno["lugarNacAlumno" ],'Fecha de Nacimiento:\n %s'%fechaNacimiento,'Sexo:\n %s'%datosAlumno["sexoAlumno" ], 'Edad:\n %s'%datosAlumno["edadAlumno" ]],
                                             ['Municipio:\n %s'%datosAlumno["municipio" ],'Parroquia:\n %s'%datosAlumno["parroquia" ],'Sector:\n %s'%datosAlumno["sector" ], 'Urb. / Barrio:\n %s'%datosAlumno["urbBarrio" ]],
                                             ['Avenida:\n %s'%datosAlumno["avenida" ],'Calle:\n %s'%datosAlumno["calle" ],'Edificio:\n %s'%datosAlumno["edificio" ], u'Nº Casa/Apto.:\n %s'%datosAlumno["casaApto" ]],
                                             ['Pto. de Referencia:\n %s'%datosAlumno["ptoReferencia" ]],
                                             ['Telf. Hab:\n %s'%datosAlumno["telefonoResAlumno" ],'Telf. Celular:\n %s'%datosAlumno["telefonoCelAlumno" ],'E-mail:\n %s'%datosAlumno["emailAlumno" ]]
                                            ]

            tablaDatosRepresentante=[['Apellidos y Nombres:\n %s %s'%(datosAlumno["apellidoRepresentante" ],datosAlumno["nomRepresentante" ]),u'Cédula de identidad:\n %s'%datosAlumno["ciRepresentante" ]],
                                                   [u'Dirección de Habitación:\n %s'%datosAlumno["direccionRepresentante" ]],
                                                   ['Telf. Hab:\n %s'%datosAlumno["telefonoHabRepresentante" ],'Telf. Celular:\n %s'%datosAlumno["telefonoCelRepresentante" ],'E-mail:\n %s'%datosAlumno["emailRepresentante" ]],
                                                   [u'Direción de Trabajo:\n %s'%datosAlumno["dirTrabajoRepresentante" ]],
                                                   ['Telf. Trab:\n %s'%datosAlumno["telefonoTrabRepresentante" ],u'Ocupación:\n %s'%datosAlumno["ocupacionRepresentante" ],'Parentesco:\n %s'%datosAlumno["parentescoRepresentante" ]]
                                                  ]

            tablaDatosMedicos=[['Tipo de Sangre:\n %s'%datosAlumno["tipoSangreFichaMedica" ],u'Antecedentes Generales:\n %s'%datosAlumno["antGeneralesFichaMedica" ]],
                                                [u'Vac. Fiebre Amarilla:\n %s\nFecha:\n %s'%(datosAlumno["vacunaFAmarilla" ], fechaFA),'Vac. Hepatitis "A": %s\nFecha: %s'%(datosAlumno["vacunaHepatitisA" ], fechaHA),'Vac. Hepatitis "B": %s\nFecha: %s'%(datosAlumno["vacunaHepatitisB" ], fechaHB)],
                                                [u'Cabeza:\n %s'%datosAlumno["enfCabeza" ],  u'Oído:\n %s'%datosAlumno["enfOido" ], u'Nariz:\n %s'%datosAlumno["enfNariz" ]],
                                                [u'Garganta:%s'%datosAlumno["enfGarganta" ], u'Corazón:%s'%datosAlumno["enfCorazon" ],  u'Pulmones:%s'%datosAlumno["enfPulmones" ]],
                                                [u'Vías Digestivas:\n %s'%datosAlumno["enfViaDigestiva" ], u'Riñones:\n %s'%datosAlumno["enfRiniones" ],u'Huesos:\n %s'%datosAlumno["enfHuesos" ]],
                                                [u'Articulaciones:\n %s'%datosAlumno["enfArticulaciones" ], u'Edocrinológico:\n %s'%datosAlumno["enfEndocrino" ]],
                                                [u'Operaciones:\n %s'%datosAlumno["operaciones" ]],
                                                [u'Alergia Comidas:\n %s'%datosAlumno["alergiaComida" ],  u'Alergia Medicamentos:\n %s'%datosAlumno["alergiaMedicamentos" ], u'Medicamento Específico:\n %s'%datosAlumno["medicamentoEspecifico" ]],
                                                [u'Tiene Seguro Médico:\n %s'%datosAlumno["seguroMedico" ],  u'Aseguradora:\n %s'%datosAlumno["aseguradora" ], u'Telf.:\n %s'%datosAlumno["telefonoAseguradora" ]],
                                                [u'En caso de Emergencia Llamar a:\n %s'%datosAlumno["numeroEmergencia" ]],
                                                [u'Unidad Médico Asistenial de su Preferencia:\n %s'%datosAlumno["unidadMedicaPreferencia" ]],
                                                [u'Médico Tratante:\n %s'%datosAlumno["medicoTratante" ],  u'Telf.:\n %s'%datosAlumno["telefonoMedicoTratante" ], u'Telf. Celular:\n %s'%datosAlumno["telefonoCelMedicoTratante" ]],
                                                [u'Otra enfermedad o suceso médico importante:'],
                                                ['%s'%datosAlumno["otraEnfermedadCondicion" ]],
                                                [u'Aparato, equipo o tratamiento especial:'],
                                                ['%s'%datosAlumno["aparatoquipoMedico" ]]
                                               ]

            #Definimos la tabla.
            tabla1 = Table(tablaDatosGenerales,style=[('SPAN',(0,4),(-1,4)), ('SPAN',(2,0),(-1,0)),('SPAN',(2,5),(-1,5))])
            tabla2 = Table(tablaDatosRepresentante, style=[('SPAN',(0,3),(-1,3)), ('SPAN',(1,0),(-1,0)),('SPAN',(0,1),(-1,1))])
            tabla3 = Table(tablaDatosMedicos, style=[('SPAN',(1,0),(-1,0)), ('SPAN',(0,6),(-1,6)), ('SPAN',(0,9),(-1,9)), ('SPAN',(0,10),(-1,10)), ('SPAN',(0,12),(-1,12)), ('SPAN',(0,13),(-1,13)), ('SPAN',(0,14),(-1,14)), ('SPAN',(0,15),(-1,15))])
            #tabla3 = Table(tablaDatosMedicos)

            #Creamos una caja alrededor de las celdas.
            tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            tabla1.hAlign='LEFT'
            tabla2.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            tabla2.hAlign='LEFT'
            tabla3.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            tabla3.hAlign='LEFT'
            #Y ponemos una malla (rejilla) a la tabla.
            tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla2.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla3.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            #Y la asignamos al platypus story.
            story.append(parrafo3)
            story.append(tabla1)
            story.append(parrafo4)
            story.append(tabla2)
            story.append(PageBreak())
            story.append(parrafo5)
            story.append(tabla3)
        else:
            parrafo5=Paragraph(u'Error', cabecera)
            story.append(parrafo5)
            story.append(Spacer(0,20))

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        name = "FichaMedicaAlumno-%s-%s" % (date_str, os.getpid())
        temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir=os.environ['TEMP'],)
        temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        doc.pagesize=landscape(letter)
        doc.build(story)

        #self.open_report(temp.name)
        self.tempFile=temp.name
        return temp.name

    def open_report(self,path):

        try:
            if os.name == 'posix':
                os.popen('evince %s'% path)
            else:
                os.startfile(path)
        except:
            print sys.exc_value
            print sys.exc_type


