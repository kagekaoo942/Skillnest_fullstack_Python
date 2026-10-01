USE bookhub;

-- Completa descripciones antiguas antes de hacerlas obligatorias.
UPDATE libros
SET descripcion = 'Descripción no proporcionada.'
WHERE descripcion IS NULL OR CHAR_LENGTH(TRIM(descripcion)) < 10;

ALTER TABLE libros
    MODIFY COLUMN descripcion TEXT NOT NULL;

CREATE TABLE IF NOT EXISTS favoritos (
    usuario_id INT NOT NULL,
    libro_id INT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (usuario_id, libro_id),
    KEY ix_favoritos_libro (libro_id),
    CONSTRAINT fk_favoritos_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_favoritos_libro
        FOREIGN KEY (libro_id)
        REFERENCES libros(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;
