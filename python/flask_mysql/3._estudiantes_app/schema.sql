CREATE DATABASE IF NOT EXISTS esquema_estudiantes;

USE esquema_estudiantes;

CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO estudiantes (nombre, email)
SELECT 'Joe Doe', 'joedoe@email.com'
WHERE NOT EXISTS (SELECT 1 FROM estudiantes);
