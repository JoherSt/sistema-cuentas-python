CREATE TABLE usuarios 
(
id bigint PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
email VARCHAR(100),
password VARCHAR(100)
)

CREATE TABLE categorias 
(
id bigint PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
description VARCHAR(100)
)

create table tareas 
(
    id BIGINT PRIMARY key AUTO_INCREMENT,
    id_usuario BIGINT,
    description VARCHAR(150),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_vencimiento DATETIME,
    estado VARCHAR(50),
    id_categoria BIGINT
)

create table comentarios
(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_tarea BIGINT,
    id_usuario BIGINT,
    description VARCHAR(100),
    fecha_Creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
