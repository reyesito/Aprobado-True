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
    nombre VARCHAR(20),
    latitud double(12,7),
    altitud double(12,7) 
);

INSERT INTO coordenadas VALUES("Refugio 1",-34.617706,-58.368499);
INSERT INTO coordenadas VALUES("Refugio 2",-34.6159878,-58.3695973);
INSERT INTO coordenadas VALUES("Refugio 3",-34.61595,-58.36987);
INSERT INTO coordenadas VALUES("Refugio 4",-34.61852,-58.36984);
INSERT INTO coordenadas VALUES("Refugio 5",-34.61576,-58.36992);
INSERT INTO coordenadas VALUES("Refugio 6",-34.615696,-58.368585);
INSERT INTO coordenadas VALUES("Refugio 7",-34.617825,-58.365533);


INSERT INTO duenios (nombre, mail, telefono, barrio) VALUES
('Jose', 'josegod@mail.com', '12345', 'Belgrano'),
('Alicia', 'aliciawonderland@mail.com', '4489', 'San Telmo'),
('Gojo', 'gojojjk@mail.com', '1138976', 'Olivos');

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
    telefono_informante,
    id_informante
) VALUES
    ('Perro', 'Labrador', 'Juan', 'Dorado', 'Macho', 'Grande', -34.61570, -58.363073, 'juanperez@mail.com', '12345678',1),
    ('Hamster', 'Sirio', 'Pedro', 'Dorado', 'Macho', 'Chico', -34.62560, -58.368597, 'pedromartinez@mail.com', '55667788',2),
    ('Conejo', 'Angora', 'Lucia', 'Gris', 'Hembra', 'Chico', -34.617700, -58.36880, 'luciaf@mail.com', '66778899',3),
    ('Perico', 'Australiano', 'Carlos', 'Verde', 'Macho', 'Mediano', -34.627694, -58.365688, 'carloslopez@mail.com', '11223344',4),
    ('Gato', 'Siames', 'Ana', 'Blanco', 'Hembra', 'Chico', -34.61540, -58.365433, 'anagomez@mail.com', '09876543',5);

INSERT INTO mascotas_perdidas (
    animal,
    raza,
    nombre,
    color,
    sexo,
    tamanio,
    latitud,
    altitud,
    mail_duenio,
    telefono_duenio,
    id_duenio
) VALUES
    ('Perro', 'Labrador', 'Jose', 'Blanco', 'Macho', 'Mediano', -34.617705, -58.368666, 'josegod@mail.com', '12345',1),
    ('Perro', 'Caniche', 'Alicia', 'Blanco', 'Macho', 'Chico', -34.617716, -58.36985, 'aliciawonderland@mail.com', '4489',2),
    ('Gato', 'Birmano', 'Gojo', 'Blanco', 'Hembra', 'Mediano', -34.615024, -58.36577, 'gojojjk@mail.com', '1138976',3);
   