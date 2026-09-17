# Sistema Modular de Configuración y Gestión de Usuarios

## Descripción

Aplicación desarrollada en Python para gestionar usuarios desde consola,
aplicando entornos virtuales, gestión de dependencias, variables de entorno,
módulos y paquetes.

## Tecnologías

- Python
- pip
- python-dotenv
- venv
- Git
- GitHub
- Visual Studio Code

## Estructura del proyecto

```
sistema_usuarios/
│── app/
│   │── __init__.py
│   │── usuarios/
│   │   │── __init__.py
│   │   │── gestor.py
│   │   │── validaciones.py
│   │── config/
│   │   │── __init__.py
│   │   │── settings.py
│── .env.example
│── .gitignore
│── main.py
│── requirements.txt
│── README.md
```

## Creación del entorno virtual

En Windows (PowerShell o CMD):

```bash
python -m venv venv
venv\Scripts\activate
```

En Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalación de dependencias

Con el entorno virtual activado, ejecutar:

```bash
pip install -r requirements.txt
```

## Variables de entorno

1. Copiar el archivo `.env.example` a `.env`:

   ```bash
   copy .env.example .env      # Windows
   cp .env.example .env        # Linux / macOS
   ```

2. Editar `.env` y definir las variables:

   ```env
   APP_NAME=Sistema Usuarios
   APP_VERSION=1.0
   ADMIN_USER=admin
   ```

Las variables se cargan mediante `python-dotenv` desde
`app/config/settings.py`.

## Ejecución

Con el entorno virtual activado y las dependencias instaladas, ejecutar
desde la raíz del proyecto:

```bash
python main.py
```

En Linux / macOS, si `python` apunta a Python 2:

```bash
python3 main.py
```

Al iniciar se muestra el menú:

```
1. Registrar usuario
2. Listar usuarios
3. Buscar usuario
4. Salir
```

## Funcionalidades

- Registrar usuarios
- Listar usuarios
- Buscar usuarios
- Validar datos
- Manejar excepciones

## Modularización

### gestor.py

Contiene la clase `GestorUsuarios` con los métodos para registrar,
listar y buscar usuarios en memoria.

### validaciones.py

Contiene las funciones de validación de nombre (no vacío) y edad
(entero positivo).

### settings.py

Carga las variables de entorno definidas en `.env` mediante
`python-dotenv` y las expone al resto de la aplicación.

## Evidencias

### Creación del entorno virtual

![Entorno virtual](capturas/01_entorno_virtual.png)

### Instalación de dependencias

![Dependencias](capturas/02_dependencias.png)

### Ejecución del sistema

![Ejecución](capturas/03_ejecucion.png)

### Variables de entorno

![Variables](capturas/04_variables_entorno.png)

## Video de reflexión

[Video de reflexión en YouTube](https://youtu.be/REEMPLAZAR_CON_LINK_DEL_VIDEO)

> Reemplazar la URL de arriba con el enlace real del video de YouTube
> donde se explica: ventajas de modularizar, importancia de aislar
> dependencias y uso seguro de variables de entorno.

## Autor

Daniel Salas
