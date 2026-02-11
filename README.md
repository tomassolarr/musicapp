# Music App - Django

Una aplicación web de gestión musical desarrollada como proyecto académico del Diplomado en Desarrollo Web. Permite gestionar artistas, álbumes y canciones con una interfaz moderna y fluida.

## Características

- **Gestión de Artistas**: Crear, editar, eliminar y visualizar artistas musicales
- **Gestión de Álbumes**: Administración de discos asociados a artistas
- **Gestión de Canciones**: Registro de canciones con duración y enlaces a videos
- **Interfaz Moderna**: Diseño limpio estilo Apple con Bootstrap 5
- **Feedback Visual**: Notificaciones toast al realizar acciones
- **Responsive**: Adaptable a dispositivos móviles

## Tecnologías

| Categoría | Tecnología |
|-----------|------------|
| Backend | Python 3.x, Django 5.2 |
| Frontend | HTML5, CSS3, JavaScript |
| Framework CSS | Bootstrap 5.3 |
| Iconos | Bootstrap Icons |
| Base de Datos | SQLite |
| Plantillas | Django Templates |

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd PythonProject

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install django

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

## Uso

1. Accede a `http://127.0.0.1:8000/music/`
2. Agrega tu primer artista usando el botón "Agregar Artista"
3. Añade álbumes asociados al artista
4. Incluye canciones a cada álbum

## Estructura del Proyecto

```
PythonProject/
├── db.sqlite3          # Base de datos
├── manage.py           # Script de gestión Django
├── mysite/             # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── music/              # Aplicación principal
    ├── models.py       # Modelos de datos
    ├── views.py       # Vistas/Controladores
    ├── forms.py       # Formularios
    ├── urls.py        # Rutas
    └── templates/     # Plantillas HTML
```

## Modelos de Datos

- **Artist**: nombre, género
- **Album**: nombre, fecha de publicación, relación con Artist
- **Song**: nombre, duración, video, relación con Album

## Autor

Desarrollado como parte del Diplomado en Desarrollo Web.

## Licencia

Este proyecto es de uso educativo.
