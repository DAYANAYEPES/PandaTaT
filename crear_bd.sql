CREATE DATABASE PandaTaT;
USE PandaTaT;

CREATE TABLE Roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES Roles(id)
);

CREATE TABLE Estado_pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(50)
);

CREATE TABLE Pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion TEXT,
    usuario_id INT,
    estado_id INT,
    fecha DATETIME,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
    FOREIGN KEY (estado_id) REFERENCES Estado_pedidos(id)
);
