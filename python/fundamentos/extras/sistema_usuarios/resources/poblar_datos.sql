-- Genera automáticamente el ID 1 para Administrador y el ID 2 para Normal
INSERT INTO tipos_usuario (nombre_tipo) VALUES 
('Administrador'),
('Normal');

-- registro de usuarios
INSERT INTO usuarios (usuario, password, tipo_usuario) VALUES 
('admin_sistema', 'claveUltraSecreta123', 1), -- Vinculado a Administrador (ID 1)
('juan_perez', 'juanito2026', 2),             -- Vinculado a Usuairo normal (ID 2)