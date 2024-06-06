CREATE TABLE IF NOT EXISTS mascotas_encontradas (
    id_mascota INT NOT NULL AUTO_INCREMENT,
    raza VARCHAR(20),
    nombre VARCHAR(20),
    color VARCHAR(20),
    sexo VARCHAR(3),
    tamanio VARCHAR(10),
    barrio VARCHAR(30),
    mail_duenio VARCHAR(40),
    telefono_duenio int(20),
    telefono_informante int(20),
    id_informante INT,
    PRIMARY KEY(id_mascota),
    FOREIGN KEY (telefono_informante) REFERENCES informante(telefono),
    FOREIGN KEY (mail_duenio,telefono_duenio) REFERENCES duenios(mail,telefono)
);
CREATE TABLE IF NOT EXISTS mascotas_perdidas (
    id_mascota INT NOT NULL AUTO_INCREMENT,
    raza VARCHAR(20),
    nombre VARCHAR(20),
    color VARCHAR(20),
    sexo VARCHAR(3),
    tamanio VARCHAR(10),
    barrio VARCHAR(30),
    mail_duenio VARCHAR(40),
    telefono_duenio int(20),
    PRIMARY KEY(id_mascota),
    FOREIGN KEY (mail_duenio,telefono_duenio) REFERENCES duenios(mail,telefono)

);

CREATE TABLE IF NOT EXISTS duenios (
    id_duenio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    mail VARCHAR(40),
    telefono int(20),
    barrio VARCHAR(50),
    PRIMARY KEY(id_duenio)
);

CREATE TABLE IF NOT EXISTS informante(
    id_informante INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
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
