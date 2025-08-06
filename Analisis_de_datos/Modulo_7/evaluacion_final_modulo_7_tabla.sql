--1. Crear la base de datos y su estructura con los datos anteriormente descritos.

CREATE TABLE disqueria.Generos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE disqueria.Autores (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fechaFormacion DATE,
    idGenero INT,
    FOREIGN KEY (idGenero) REFERENCES disqueria.Generos(id)
);

CREATE TABLE disqueria.Formatos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL  
);


CREATE TABLE disqueria.Discos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,  
    duration INT,
    idGenero INT,
    idAutor INT,
    FOREIGN KEY (idGenero) REFERENCES disqueria.Generos(id),
    FOREIGN KEY (idAutor) REFERENCES disqueria.Autores(id)
);


CREATE TABLE disqueria.Productos (
    codigo VARCHAR(100) PRIMARY KEY,
	idDisco INT NOT NULL,
    idFormato INT NOT NULL,  
    precio INT NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    FOREIGN KEY (idDisco) REFERENCES disqueria.Discos(id),
    FOREIGN KEY (idFormato) REFERENCES disqueria.Formatos(id)
);

--2. A partir de los archivos .csv entregados en conjunto con la evaluación, INSERTAR 
-- los datos para cada tabla (1 archivo por )
-- Se usó la función "Import/Export data...por lo que no se entrega un segundo archivo"