CREATE DATABASE clinica;
USE clinica;

CREATE TABLE medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(100),
    cantidad INT,
    precio DECIMAL(10,2)
);