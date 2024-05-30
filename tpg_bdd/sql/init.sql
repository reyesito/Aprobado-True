CREATE TABLE IF NOT EXISTS mascotas (
    id_mascota INT NOT NULL AUTO_INCREMENT,
    raza VARCHAR(20),
    nombre VARCHAR(20),
    color VARCHAR(20),
    sexo VARCHAR(3),
    edad_aprox VARCHAR(10),
    barrio VARCHAR(30),
    PRIMARY KEY(id_mascota)

);

CREATE TABLE IF NOT EXISTS duenios (
    id_registro INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    mail VARCHAR(40),
    telefono int(20),
    barrio VARCHAR(50),
    PRIMARY KEY(id_registro)
);

CREATE TABLE IF NOT EXISTS informante(
    id_informante INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    mail VARCHAR(40),
    telefono int(20),
    barrio VARCHAR(30),
    PRIMARY KEY(id_informante)
);

CREATE TABLE IF NOT EXISTS coordenadas (
    latitud double(12,7),
    altitud double(12,7) 
);

INSERT INTO coordenadas VALUES(-34.6159878,-58.3695973);
INSERT INTO coordenadas VALUES(-34.61595,-58.36987);
INSERT INTO coordenadas VALUES(-34.61852,-58.36994);
INSERT INTO coordenadas VALUES(-34.6185219,-58.3699406);
