-- ==========================================================
-- BASE DE DATOS Y RELACIÓN 1:N ENTRE CURSOS Y ESTUDIANTES
-- Ejecuta este archivo una sola vez o vuelve a ejecutarlo
-- si las tablas ya existen (CREATE TABLE IF NOT EXISTS).
-- ==========================================================
CREATE DATABASE IF NOT EXISTS esquema_estudiantes_cursos
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE esquema_estudiantes_cursos;

CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    edad INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    curso_id INT NOT NULL,
    CONSTRAINT fk_estudiantes_curso
        FOREIGN KEY (curso_id)
        REFERENCES cursos(id)
) ENGINE=InnoDB;

-- INSERT IGNORE hace que los datos iniciales no se dupliquen al reejecutar.
INSERT IGNORE INTO cursos (id, nombre)
VALUES
    (1, 'MERN'),
    (2, 'Java'),
    (3, 'Python'),
    (4, 'Fundamentos de la Web');

-- Cada estudiante usa un curso_id válido de la tabla cursos.
INSERT IGNORE INTO estudiantes (id, nombre, apellido, edad, curso_id)
VALUES
    (1, 'Valeria', 'Romero', 25, 1),
    (2, 'Cynthia', 'Castillo', 26, 1),
    (3, 'Patricio', 'Fuentelba', 27, 1),
    (4, 'Kevin', 'Duque', 27, 1),
    (5, 'Andrea', 'Pérez', 22, 2),
    (6, 'Matías', 'Soto', 24, 3);
