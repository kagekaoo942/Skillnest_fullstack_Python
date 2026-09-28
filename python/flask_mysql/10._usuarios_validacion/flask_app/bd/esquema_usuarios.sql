CREATE DATABASE IF NOT EXISTS esquema_usuarios
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE esquema_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_usuarios_email (email)
) ENGINE=InnoDB;

INSERT INTO usuarios (nombre, apellido, email)
VALUES
    ('Soraya', 'Montenegro', 'soraya@email.com'),
    ('Armando', 'Mendoza', 'armando@email.com'),
    ('Mia', 'Colucci', 'mia@email.com'),
    ('Rubi', 'Perez', 'rubi@email.com');
