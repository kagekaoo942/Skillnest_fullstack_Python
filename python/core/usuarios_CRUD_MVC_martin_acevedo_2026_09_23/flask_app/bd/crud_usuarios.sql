-- Crea y selecciona la base de datos utilizada por el CRUD.
CREATE DATABASE IF NOT EXISTS crud_usuarios;

USE crud_usuarios;

-- Guarda los datos de contacto y las fechas de auditoría.
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Registros de ejemplo para probar el listado inicial.
INSERT INTO usuarios (nombre, apellido, email) VALUES
("Ricky", "Martin", "ricky@codingdojo.com"),
("Enrique", "Iglesias", "enrique@codingdojo.com"),
("Celia", "Cruz", "celia@codingdojo.com"),
("Ricardo", "Montaner", "ricardo@codingdojo.com");
