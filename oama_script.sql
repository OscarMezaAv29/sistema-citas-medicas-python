CREATE DATABASE IF NOT EXISTS oama_citas_python;
USE oama_citas_python;

CREATE TABLE doctores(
    id           int(25) auto_increment not null,
    nombre       varchar(100),
    apellidos    varchar(255),
    cedula       varchar(255),
    especialidad varchar(255),
    consultorio  varchar(255),
    email        varchar(255) not null,
    password     varchar(255) not null,
    fecha        date not null,
    CONSTRAINT doctores PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE citas(
    id                  int(25) auto_increment not null,
    doctor_id           int(25) not null,
    nombre_paciente     varchar(255) not null,
    telefono            varchar(255),
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_cita_doctor FOREIGN KEY(doctor_id) REFERENCES doctores(id)
)ENGINE=InnoDb;