CREATE TABLE IF NOT EXISTS duenios (
    id_duenio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    mail VARCHAR(40),
    telefono VARCHAR(20),
    barrio VARCHAR(50),
    PRIMARY KEY(id_duenio)
);

CREATE TABLE IF NOT EXISTS informantes(
    id_informante INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    mail VARCHAR(40),
    telefono VARCHAR(20),
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
    barrio VARCHAR(30),
    latitud double(12,7),
    altitud double(12,7), 
    mail_informante VARCHAR(40),
    telefono_informante VARCHAR(20),
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
    barrio VARCHAR(30),
    latitud double(12,7),
    altitud double(12,7), 
    mail_duenio VARCHAR(40),
    telefono_duenio VARCHAR(20),
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


INSERT INTO informantes (nombre, mail, telefono, barrio) VALUES
('Juan', 'juanperez@mail.com', '12345678', 'Barrio A'),
('Pedro', 'pedromartinez@mail.com', '55667788', 'Barrio B'),
('Lucia', 'luciaf@mail.com', '66778899', 'Barrio C'),
('Carlos', 'carloslopez@mail.com', '11223344', 'Barrio D'),
('Ana', 'anagomez@mail.com', '09876543', 'Barrio E');


INSERT INTO mascotas_encontradas (
    animal,
    raza,
    nombre,
    color,
    sexo,
    tamanio,
    latitud,
    altitud,
    mail_informante,
    telefono_informante
) VALUES
    ('Perro', 'Labrador', 'Juan', 'Negro', 'Macho', 'Grande', 40.7128000, -74.0060000, 'juanperez@mail.com', '12345678', 6),
    ('Hamster', 'Sirio', 'Pedro', 'Dorado', 'Macho', 'Pequeño', 35.6895000, 139.6917000, 'pedromartinez@mail.com', '55667788', 7),
    ('Conejo', 'Angora', 'Lucia', 'Gris', 'Hembra', 'Pequeño', 48.8566000, 2.3522000, 'luciaf@mail.com', '66778899', 8),
    ('Perico', 'Australiano', 'Carlos', 'Verde', 'Macho', 'Mediano', 51.5074000, -0.1278000, 'carloslopez@mail.com', '11223344', 9),
    ('Gato', 'Siames', 'Ana', 'Blanco', 'Hembra', 'Pequeño', 34.0522000, -118.2437000, 'anagomez@mail.com', '09876543', 10);
