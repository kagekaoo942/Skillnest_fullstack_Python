CREATE DATABASE IF NOT EXISTS esquema_arepas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE esquema_arepas;

CREATE TABLE IF NOT EXISTS pedidos (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo_arepa VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

INSERT INTO pedidos (nombre, cantidad, tipo_arepa)
VALUES
    ('Valeria', 3, 'pollo'),
    ('Cynthia', 2, 'carne'),
    ('Patricio', 5, 'queso'),
    ('Kevin', 3, 'jamón y queso');
