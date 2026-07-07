CREATE DATABASE	usuarios_db;
USE usuarios_db;
-- 1. Crear la tabla de referencia para los tipos de usuario (Requisito para la FK)
CREATE TABLE tipos_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_tipo VARCHAR(50) NOT NULL UNIQUE
);

-- Insertamos los roles básicos para que la base de datos sea funcional
INSERT INTO tipos_usuario (nombre_tipo) VALUES ('Administrador'), ('Normal');


-- 2. Crear la tabla 'usuarios' según la imagen
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    tipo_usuario INT NOT NULL,
    
    -- Campos de auditoría (Estándar de la industria)
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    
    -- Restricción de Llave Foránea (FK)
    CONSTRAINT fk_usuario_tipo FOREIGN KEY (tipo_usuario) 
        REFERENCES tipos_usuario(id)
);