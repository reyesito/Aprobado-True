CREATE TABLE IF NOT EXISTS duenios (
    id_duenio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    mail VARCHAR(40),
    telefono INT(20),
    barrio VARCHAR(50),
    PRIMARY KEY(id_duenio)
);

CREATE TABLE IF NOT EXISTS informantes(
    id_informante INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    mail VARCHAR(40),
    telefono INT(20),
    barrio VARCHAR(30),
    PRIMARY KEY(id_informante)
);

CREATE TABLE IF NOT EXISTS mascotas_encontradas (
    id_mascota INT NOT NULL AUTO_INCREMENT,
    animal VARCHAR(20),
    raza VARCHAR(20),
    nombre VARCHAR(20),
    color VARCHAR(20),
    sexo VARCHAR(6),
    tamanio VARCHAR(10),
    latitud double(12,7),
    altitud double(12,7), 
    mail_informante VARCHAR(40),
    telefono_informante INT(20),
    id_informante INT ,
    PRIMARY KEY(id_mascota),
    FOREIGN KEY (id_informante) REFERENCES informantes(id_informante)
);

CREATE TABLE IF NOT EXISTS mascotas_perdidas (
    id_mascota INT NOT NULL AUTO_INCREMENT,
    animal VARCHAR(20),
    raza VARCHAR(20),
    nombre VARCHAR(20),
    color VARCHAR(20),
    sexo VARCHAR(6),
    tamanio VARCHAR(10),
    latitud double(12,7),
    altitud double(12,7), 
    mail_duenio VARCHAR(40),
    telefono_duenio INT(20),
    id_duenio INT,
    PRIMARY KEY(id_mascota),
    FOREIGN KEY (id_duenio) REFERENCES duenios(id_duenio)

);

CREATE TABLE IF NOT EXISTS coordenadas (
    latitud double(12,7),
    altitud double(12,7) 
);

INSERT INTO coordenadas VALUES(-34.617706,-58.368499);
INSERT INTO coordenadas VALUES(-34.6159878,-58.3695973);
INSERT INTO coordenadas VALUES(-34.61595,-58.36987);
INSERT INTO coordenadas VALUES(-34.61852,-58.36984);
INSERT INTO coordenadas VALUES(-34.61576,-58.36992);
INSERT INTO coordenadas VALUES(-34.615696,-58.368585);
INSERT INTO coordenadas VALUES(-34.617825,-58.365533);