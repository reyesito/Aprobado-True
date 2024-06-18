# Aprobado-True: Lost Pets
##### Proyecto para Introducción a Desarrollo del Software para la Facultad de Ingeniería

- **Nuestro proyecto**
- **¿Quiénes somos parte?**
- **Características**
- **Tecnologías Utilizadas**
- **Instalación**
- **Licencia**

## Nuestro proyecto
   **Creamos una página web dedicada a la búsqueda y reportaje de mascotas que fueron perdidas, con el  fin de poder traerlas de vuelta con sus respectivos dueños, usamos una plantilla HTML de uso permitido y nos presentamos como una ONG de animales, citando nuestra respectiva información.**

**Para reportar a las mascotas, se usaron formularios html cuyas respuestas están conectadas a una base de datos, conectada mediante el uso de una imagen de Docker y de un archivo 'init.sql', cuya información se almacena y obtiene APIs web según el protocolo RESTFUL, por esto se dio uso de jsonify y métodos GET y POST. Además, conectamos el Frontend y el Backend gracias a funciones que nos permiten obtener la información ingresada en la base de datos, que fueron reflejadas en dos listados separados, para mascotas perdidas y encontradas, mediante herramientas de HTML y Flask. Además de las APIs de mascotas, también creamos una API de un mapa interactivo, para que el usuario en el formulario pueda elegir con un click las coordenadas donde vio a la mascota, esto queda reflejado en su propio apartado donde quedan reflejadas todos los animales que fueron reportados; todo esta funcionalidad fue dada gracias a código de Javascript.**

**Entre otras cosas, se usó una base para preservar la homogeneidad de la página en todos los apartados y también se hizo uso de renderizado de errores para los 404 y 500.**

## ¿Quiénes somos parte?
- [Mauro Agustin Duarte Brizuela](https://github.com/AGUST1N18)
- [Santiago Jakim](https://github.com/jakimm7)
- [Andy Mayuri](https://github.com/AndyPinta)
- [Carlos Reyes](https://github.com/reyesito)
- [Bryan Serrantes](https://github.com/Bserrantes)
- [Lautaro Martin Sotelo](https://github.com/Sotelo27)
- [Luisina Tagliani](https://github.com/luishilu)

## Características

- ### Registro de Reportes:  Permite a los usuarios reportar mascotas perdidas y encontradas.
- ### Base de Datos: Almacena todos los reportes para fácil acceso y gestión.
- ### Listado: Muestra todos los reportes en un formato de lista para una rápida visualización.
- ### Mapa Interactivo: Muestra la ubicación de las mascotas reportadas en un mapa para facilitar la búsqueda.


## Tecnologías Utilizadas

- ### Frontend: HTML, CSS, JavaScript, ( bootstrap utilizado por el mismo conjunto de templates )
- ### Backend: Flask-Python
- ### Base de Datos: MySQL
- ### Mapas: openlayers,

## Instalación

### Sigue estos pasos para instalar y ejecutar el proyecto localmente.

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/reyesito/Aprobado-True.git
   
2. **Navega al directorio del proyecto:**
   ```bash
   cd lost-pets
3. **Instala las dependencias del backend:**
   ```bash
    bash init.sh

5. **Iniciar el servidor:**
   ```bash
   flask run
   
6. **Abre tu navegador y navega a http://127.0.0.1:5000**
   
## Contribución
#### Si deseas contribuir a este proyecto, por favor sigue estos pasos:

**1. Haz un fork del repositorio.**

**2. Crea una rama nueva (git checkout -b develop/nueva-funcionalidad).**

**3. Realiza tus cambios y haz commits descriptivos (git commit -m 'Añadida nueva funcionalidad').**

**4. Empuja tus cambios a la rama (git push origin develop/nueva-funcionalidad).**

**5. Abre un Pull Request.**
##   Licencia
Este proyecto está bajo la Licencia FIUBA. Consulta el archivo LICENSE para más detalles.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarnos creando un issue en el repositorio.

> **Importante:** La rama más actualizada es [origin/develop](https://github.com/reyesito/Aprobado-True/tree/develop)