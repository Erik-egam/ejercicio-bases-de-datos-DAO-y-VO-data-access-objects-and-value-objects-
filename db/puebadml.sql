SELECT * FROM Trabajadores;
SELECT * From Arboles;




-- --------------------------------------------
-- INSERTAMOS VARIOS VALORES PARA HACER PRUEBAS
-- --------------------------------------------
-- =========================
-- Producciones
-- =========================
INSERT INTO Producciones (id_produccion, fecha_produccion) VALUES
(1, '2025-01-15'),
(2, '2025-02-10');

-- =========================
-- Trabajadores
-- =========================
INSERT INTO Trabajadores (id_trab, nombre, telefono, EPS, ARL) VALUES
(1, 'Carlos Pérez', '3001234567', 'Sura', 'Colpatria'),
(2, 'Ana Gómez', '3017654321', 'Sanitas', 'Positiva'),
(3, 'Luis Rodríguez', '3021112233', 'Compensar', 'Colmena');

-- =========================
-- Árboles
-- =========================
INSERT INTO Arboles (id_arbol, fecha_siembra, terreno) VALUES
(1, '2020-02-19', 'Lote A'),
(2, '2011-12-31', 'Lote B'),
(3, '2001-07-11', 'Lote C');

-- =========================
-- Enfermedades
-- =========================
INSERT INTO Enfermedades (id_enfermedad, nombre, tratamiento, descripcion, causa) VALUES
(1, 'Royas', 'Fungicida X', 'Manchas anaranjadas en hojas', 'Hongo'),
(2, 'Marchitez', 'Fungicida Y', 'Decaimiento de ramas', 'Patógeno del suelo'),
(3, 'Antracnosis', 'Cobre', 'Lesiones oscuras en hojas', 'Hongo Colletotrichum');

-- =========================
-- Tipo_tarea
-- =========================
INSERT INTO Tipo_tarea (id_tipo_tarea, nombre) VALUES
(1, 'Fertilización'),
(2, 'Poda'),
(3, 'Riego'),
(4, 'Fumigación');

-- =========================
-- Recolecta
-- =========================
INSERT INTO Recolecta (id_recolecta, peso, fecha_reco, calidad, id_trab, id_arbol, id_produccion) VALUES
(1, 20.5, '2025-01-16', 'A', 1, 1, 1),
(2, 15.2, '2025-01-16', 'B', 2, 2, 1),
(3, 18.0, '2025-02-11', 'A', 3, 3, 2);

-- =========================
-- Tareas (relación N:M)
-- =========================
INSERT INTO Tareas (id_tarea, id_arbol, id_tipo_tarea, mezcla, fecha_tarea, id_trab) VALUES
(1, 1, 1, 'NPK 10-10-10', '2025-01-05', 1), -- Carlos fertilizó Árbol 1
(2, 2, 2, NULL, '2025-01-07', 2),           -- Ana podó Árbol 2
(3, 1, 3, NULL, '2025-01-10', 3),           -- Luis regó Árbol 1
(4, 3, 4, 'Fungicida X', '2025-02-01', 1);  -- Carlos fumigó Árbol 3

-- =========================
-- Árboles_Enfermedades (relación N:M)
-- =========================
INSERT INTO Arboles_Enfermedades (id_arbol, id_enfermedad, fecha_enfermedad) VALUES
(1, 1, '2025-01-20'), -- Árbol 1 tuvo roya
(2, 2, '2025-02-02'), -- Árbol 2 con marchitez
(3, 3, '2025-02-05'); -- Árbol 3 con antracnosis
