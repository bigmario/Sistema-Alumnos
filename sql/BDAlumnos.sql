-- Creator:       MySQL Workbench 5.2.38/ExportSQLite plugin 2009.12.02
-- Author:        Mario Castro
-- Caption:       New Model
-- Project:       Name of the project
-- Changed:       2012-09-21 13:07
-- Created:       2012-09-17 10:44
PRAGMA foreign_keys = OFF;

-- Schema: sistemaAlumnos
BEGIN;
CREATE TABLE "Alumnos"(
  "idAlumno" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idAlumno">=0),
  "nombreAlumno" VARCHAR(45) NOT NULL,
  "apellidoAlumno" VARCHAR(45) NOT NULL,
  "ciAlumno" VARCHAR(45),
  "fechaNacAlumno" DATE NOT NULL,
  "fechaIngAlumno" DATE NOT NULL,
  "lugarNacAlumno" VARCHAR(100) NOT NULL,
  "sexoAlumno" VARCHAR(45) NOT NULL,
  "edadAlumno" INTEGER NOT NULL,
  "telefonoResAlumno" VARCHAR(45),
  "telefonoCelAlumno" VARCHAR(45),
  "emailAlumno" VARCHAR(45),
  "fotoAlumno" VARCHAR(500) DEFAULT NULL
);
CREATE TABLE "DatosMusicales"(
  "conocimientosMusicales" VARCHAR(2) NOT NULL,
  "catedraDatosMusicales" VARCHAR(45) NOT NULL,
  "orquestaDatosMusicales" VARCHAR(100),
  "nivelOrquestalDatosMusicales" VARCHAR(45),
  "instrumentoPropio" VARCHAR(2) NOT NULL,
  "fechaAsigInstDatosMusicales" DATE,
  "marcaInstrumentoDatosMusicales" VARCHAR(45) NOT NULL,
  "modeloInstrumentoDatosMusicales" VARCHAR(45) NOT NULL,
  "serialInstrumentoDatosMusicales" VARCHAR(45) NOT NULL,
  "numeroActivoFijoInstDatosMusicales" VARCHAR(45),
  "profesorDatosMusicales" VARCHAR(100) NOT NULL,
  "otraAgrupacionDatosMusicales" VARCHAR(2) NOT NULL,
  "nombreOtraAgrupacionDatosMusicales" VARCHAR(100),
  "fechaIngresoOtraDatosMusicales" VARCHAR(45),
  "Alumnos_idAlumno" INTEGER PRIMARY KEY NOT NULL,
  CONSTRAINT "fk_DatosMusicales_Alumnos1"
    FOREIGN KEY("Alumnos_idAlumno")
    REFERENCES "Alumnos"("idAlumno")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE "FichaMedica"(
  "Alumnos_idAlumno" INTEGER PRIMARY KEY NOT NULL,
  "tipoSangreFichaMedica" VARCHAR(45),
  "antGeneralesFichaMedica" VARCHAR(300),
  "vacunaFAmarilla" VARCHAR(2),
  "fechaVacunaFAmarilla" DATE,
  "vacunaHepatitisA" VARCHAR(2),
  "fechaVacunaHepatitisA" DATE,
  "vacunaHepatitisB" VARCHAR(2),
  "fechaVacunaHepatitisB" DATE,
  "enfCabeza" VARCHAR(2),
  "enfOido" VARCHAR(2),
  "enfNariz" VARCHAR(2),
  "enfGarganta" VARCHAR(2),
  "enfCorazon" VARCHAR(2),
  "enfPulmones" VARCHAR(2),
  "enfViaDigestiva" VARCHAR(2),
  "enfRiniones" VARCHAR(2),
  "enfHuesos" VARCHAR(2),
  "enfArticulaciones" VARCHAR(2),
  "enfEndocrino" VARCHAR(2),
  "operaciones" VARCHAR(300),
  "alergiaComida" VARCHAR(200),
  "alergiaMedicamentos" VARCHAR(200),
  "medicamentoEspecifico" VARCHAR(200),
  "seguroMedico" VARCHAR(2),
  "aseguradora" VARCHAR(200),
  "telefonoAseguradora" VARCHAR(45),
  "numeroEmergencia" VARCHAR(45),
  "unidadMedicaPreferencia" VARCHAR(200),
  "medicoTratante" VARCHAR(100),
  "telefonoMedicoTratante" VARCHAR(45),
  "telefonoCelMedicoTratante" VARCHAR(45),
  "otraEnfermedadCondicion" VARCHAR(300),
  "aparatoquipoMedico" VARCHAR(300),
  CONSTRAINT "fk_FichaMedica_Alumnos1"
    FOREIGN KEY("Alumnos_idAlumno")
    REFERENCES "Alumnos"("idAlumno")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE "DireccionAlumno"(
  "municipio" VARCHAR(100),
  "parroquia" VARCHAR(45),
  "sector" VARCHAR(45),
  "urbBarrio" VARCHAR(45),
  "avenida" VARCHAR(45),
  "calle" VARCHAR(45),
  "edificio" VARCHAR(45),
  "casaApto" VARCHAR(45),
  "ptoReferencia" VARCHAR(45),
  "Alumnos_idAlumno" INTEGER PRIMARY KEY NOT NULL,
  CONSTRAINT "fk_DireccionAlumno_Alumnos"
    FOREIGN KEY("Alumnos_idAlumno")
    REFERENCES "Alumnos"("idAlumno")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE "Representente"(
  "nomRepresentante" VARCHAR(100) NOT NULL,
  "apellidoRepresentante" VARCHAR(100) NOT NULL,
  "ciRepresentante" VARCHAR(45) NOT NULL,
  "direccionRepresentante" VARCHAR(300) NOT NULL,
  "telefonoHabRepresentante" VARCHAR(100),
  "telefonoCelRepresentante" VARCHAR(100),
  "emailRepresentante" VARCHAR(45),
  "dirTrabajoRepresentante" VARCHAR(200),
  "telefonoTrabRepresentante" VARCHAR(45),
  "ocupacionRepresentante" VARCHAR(100),
  "parentescoRepresentante" VARCHAR(45) NOT NULL,
  "Alumnos_idAlumno" INTEGER PRIMARY KEY NOT NULL,
  CONSTRAINT "fk_Representente_Alumnos1"
    FOREIGN KEY("Alumnos_idAlumno")
    REFERENCES "Alumnos"("idAlumno")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE "AcademicoAlumno"(
  "estudiaAcademicoAlumno" VARCHAR(2) NOT NULL,
  "nivelAcademicoAlumno" VARCHAR(45),
  "gradoAcademicoAlumno" VARCHAR(45),
  "anioAcademicoAlumno" VARCHAR(45),
  "semestreAcademicoAlumno" VARCHAR(45),
  "institucionAcademicoAlumno" VARCHAR(45),
  "direccionAcademicoAlumno" VARCHAR(45),
  "telefonoAcademicoAlumno" VARCHAR(45),
  "tipoInstitucionAcademicoAlumno" VARCHAR(45),
  "Alumnos_idAlumno" INTEGER PRIMARY KEY NOT NULL,
  CONSTRAINT "fk_AcademicoAlumno_Alumnos1"
    FOREIGN KEY("Alumnos_idAlumno")
    REFERENCES "Alumnos"("idAlumno")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE TABLE "Admin"(
  "idAdmin" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idAdmin">=0),
  "loginAdmin" VARCHAR(45) NOT NULL,
  "passAdmin" VARCHAR(45) NOT NULL,
  "nucleoAdmin" VARCHAR(45) NOT NULL,
  "preguntaSegAdmin" VARCHAR(45) NOT NULL,
  "respuestaSegAdmin" VARCHAR(45) NOT NULL,
  "entFedAdmin" VARCHAR(45) NOT NULL,
  "municipioAdmin" VARCHAR(45) NOT NULL
);
COMMIT;
