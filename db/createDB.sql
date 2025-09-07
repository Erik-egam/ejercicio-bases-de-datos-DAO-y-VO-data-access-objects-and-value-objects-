-- =========================
-- Tablas principales
-- =========================

CREATE TABLE Producciones (
    id_produccion INTEGER PRIMARY KEY,
    fecha_produccion DATE
);

CREATE TABLE Trabajadores (
    id_trab INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT,
    EPS TEXT,
    ARL TEXT
);

CREATE TABLE Arboles (
    id_arbol INTEGER PRIMARY KEY,
    fecha_siembra DATE,
    terreno TEXT
);

CREATE TABLE Enfermedades (
    id_enfermedad INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    tratamiento TEXT,
    descripcion TEXT,
    causa TEXT
);

CREATE TABLE Tipo_tarea (
    id_tipo_tarea INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);



CREATE TABLE Recolecta (
    id_recolecta INTEGER PRIMARY KEY,
    peso REAL,
    fecha_reco DATE,
    calidad TEXT,
    id_trab INTEGER,
    id_arbol INTEGER,
    id_produccion INTEGER,
    FOREIGN KEY (id_trab) REFERENCES Trabajadores(id_trab),
    FOREIGN KEY (id_arbol) REFERENCES Arboles(id_arbol),
    FOREIGN KEY (id_produccion) REFERENCES Producciones(id_produccion)
);
-- =========================
-- Tablas relacionales
-- =========================



CREATE TABLE Tareas (
    id_tarea INTEGER,
    id_arbol INTEGER,
    id_tipo_tarea INTEGER,
    mezcla TEXT,
    fecha_tarea DATE,
    id_trab INTEGER,
    PRIMARY KEY (id_tarea, id_arbol, id_tipo_tarea),
    FOREIGN KEY (id_trab) REFERENCES Trabajadores(id_trab),
    FOREIGN KEY (id_arbol) REFERENCES Arboles(id_arbol),
    FOREIGN KEY (id_tipo_tarea) REFERENCES Tipo_tarea(id_tipo_tarea)
);

CREATE TABLE Arboles_Enfermedades (
    id_arbol INTEGER,
    id_enfermedad INTEGER,
    fecha_enfermedad DATE,
    PRIMARY KEY (id_arbol, id_enfermedad, fecha_enfermedad),
    FOREIGN KEY (id_arbol) REFERENCES Arboles(id_arbol),
    FOREIGN KEY (id_enfermedad) REFERENCES Enfermedades(id_enfermedad)
);
