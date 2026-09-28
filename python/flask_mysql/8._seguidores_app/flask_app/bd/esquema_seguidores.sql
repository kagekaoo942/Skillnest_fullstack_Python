-- Esquema para la aplicación de auto-relación de usuarios.
CREATE DATABASE IF NOT EXISTS esquema_seguidores
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE esquema_seguidores;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS seguidores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    seguidor_id INT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_seguidores_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    CONSTRAINT fk_seguidores_seguidor
        FOREIGN KEY (seguidor_id) REFERENCES usuarios(id),
    CONSTRAINT uq_usuario_seguidor
        UNIQUE (usuario_id, seguidor_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos de muestra: ejecutar el script más de una vez no duplica estos usuarios.
INSERT INTO usuarios (nombre, apellido, email)
SELECT 'Soraya', 'Montenegro', 'soraya@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE email = 'soraya@email.com'
);

INSERT INTO usuarios (nombre, apellido, email)
SELECT 'Luis F.', 'de la Vega', 'luis@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE email = 'luis@email.com'
);

INSERT INTO usuarios (nombre, apellido, email)
SELECT 'Beatriz', 'Pinzón', 'beatriz@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE email = 'beatriz@email.com'
);

INSERT INTO usuarios (nombre, apellido, email)
SELECT 'Armando', 'Mendoza', 'armando@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE email = 'armando@email.com'
);

INSERT INTO usuarios (nombre, apellido, email)
SELECT 'Mia', 'Colucci', 'mia@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE email = 'mia@email.com'
);

INSERT INTO usuarios (nombre, apellido, email)
SELECT 'Roberto', 'Pardo', 'roberto@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE email = 'roberto@email.com'
);

-- usuario_id es la persona seguida; seguidor_id, quien sigue.
INSERT IGNORE INTO seguidores (usuario_id, seguidor_id)
SELECT usuario.id, seguidor.id
FROM usuarios AS usuario
JOIN usuarios AS seguidor
    ON seguidor.email = 'luis@email.com'
WHERE usuario.email = 'soraya@email.com'
  AND NOT EXISTS (
      SELECT 1 FROM seguidores AS relacion
      WHERE relacion.usuario_id = usuario.id
        AND relacion.seguidor_id = seguidor.id
  );

INSERT IGNORE INTO seguidores (usuario_id, seguidor_id)
SELECT usuario.id, seguidor.id
FROM usuarios AS usuario
JOIN usuarios AS seguidor
    ON seguidor.email = 'armando@email.com'
WHERE usuario.email = 'soraya@email.com'
  AND NOT EXISTS (
      SELECT 1 FROM seguidores AS relacion
      WHERE relacion.usuario_id = usuario.id
        AND relacion.seguidor_id = seguidor.id
  );

INSERT IGNORE INTO seguidores (usuario_id, seguidor_id)
SELECT usuario.id, seguidor.id
FROM usuarios AS usuario
JOIN usuarios AS seguidor
    ON seguidor.email = 'luis@email.com'
WHERE usuario.email = 'beatriz@email.com'
  AND NOT EXISTS (
      SELECT 1 FROM seguidores AS relacion
      WHERE relacion.usuario_id = usuario.id
        AND relacion.seguidor_id = seguidor.id
  );

INSERT IGNORE INTO seguidores (usuario_id, seguidor_id)
SELECT usuario.id, seguidor.id
FROM usuarios AS usuario
JOIN usuarios AS seguidor
    ON seguidor.email = 'luis@email.com'
WHERE usuario.email = 'mia@email.com'
  AND NOT EXISTS (
      SELECT 1 FROM seguidores AS relacion
      WHERE relacion.usuario_id = usuario.id
        AND relacion.seguidor_id = seguidor.id
  );

INSERT IGNORE INTO seguidores (usuario_id, seguidor_id)
SELECT usuario.id, seguidor.id
FROM usuarios AS usuario
JOIN usuarios AS seguidor
    ON seguidor.email = 'beatriz@email.com'
WHERE usuario.email = 'luis@email.com'
  AND NOT EXISTS (
      SELECT 1 FROM seguidores AS relacion
      WHERE relacion.usuario_id = usuario.id
        AND relacion.seguidor_id = seguidor.id
  );
