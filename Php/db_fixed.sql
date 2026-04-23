CREATE DATABASE IF NOT EXISTS task_db;
USE task_db;

CREATE TABLE usuarios (
id bigint PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
email VARCHAR(100),
password VARCHAR(255)
);

CREATE TABLE categorias (
id bigint PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
description VARCHAR(100)
);

CREATE TABLE tareas (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_usuario BIGINT,
    description VARCHAR(150),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_vencimiento DATETIME,
    estado VARCHAR(50),
    id_categoria BIGINT
);

CREATE TABLE comentarios (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_tarea BIGINT,
    id_usuario BIGINT,
    description VARCHAR(100),
    fecha_Creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

