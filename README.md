# SupportFlow

Sistema completo de gestión de tickets de soporte técnico desarrollado en Python con arquitectura en capas.

El proyecto está dividido en 2 partes principales:

- API REST (Flask)
- Sistema CRUD local (CLI)
- Base de datos MySQL



## ¿Qué hace el proyecto?

SupportFlow permite:

- Crear usuarios
- Crear técnicos
- Crear tickets de soporte
- Registrar historial de tickets
- Listar información desde API o desde sistema CRUD
- Separar lógica en capas (Controllers - Services - Models - Database)

Es un proyecto enfocado en arquitectura profesional backend.



## Arquitectura

El sistema sigue una "arquitectura en capas":

Cliente - Controllers - Services - Models - Database - MySQL

Flujo interno:

1. El cliente realiza una petición.
2. El Controller recibe la solicitud.
3. El Controller llama al Service correspondiente.
4. El Service aplica la lógica de negocio.
5. El Model representa la estructura de datos.
6. Database conecta con MySQL.



## Estructura del proyecto
```
SupportFlow
│
├── api
│   ├── app.py
│   │
│   ├── controllers
│   │   ├── tecnico_controller.py
│   │   ├── usuario_controller.py
│   │   ├── ticket_controller.py
│   │   └── ticket_historial_controller.py
│   │
│   ├── services
│   │   ├── tecnico_service.py
│   │   ├── usuario_service.py
│   │   ├── ticket_service.py
│   │   └── ticket_historial_service.py
│   │
│   ├── models
│   │   ├── tecnico.py
│   │   ├── usuario.py
│   │   ├── ticket.py
│   │   └── ticket_historial.py
│   │
│   └── database
│       └── db.py
│
├── CrudSistemaTickets
│   ├── main.py
│   │
│   ├── services
│   │   ├── tecnico_service.py
│   │   ├── usuario_service.py
│   │   ├── ticket_service.py
│   │   └── ticket_historial_service.py
│   │
│   └── models
│       ├── tecnico.py
│       ├── usuario.py
│       ├── ticket.py
│       └── ticket_historial.py
│
├── runn_all.py
├── architecture.png
├── requirements.txt
├── README.md
```

## Tecnologías utilizadas

- Python 3
- Flask
- MySQL Connector
- Requests
- venv (entorno virtual)
- Arquitectura en capas



## Cómo instalar

### Clonar el repositorio

git clone <URL_DEL_REPOSITORIO>

cd SupportFlow

### Crear entorno virtual

python -m venv venv

### Activar entorno virtual

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

### Instalar dependencias

pip install -r requirements.txt



## Configurar base de datos

1. Instalar MySQL.
2. Crear base de datos.
3. Configurar credenciales en: api/database/db.py



## Cómo ejecutar?

### Todo el sistema

python runn_all.py 

### La API

python api/app.py

La API estará disponible en: http://127.0.0.1:5000

### El sistema CRUD local

python CrudSistemaTickets/main.py



## Componentes principales

### API

- app.py = Inicializa Flask
- Controllers = Manejan endpoints
- Services = Lógica de negocio
- Models = Representación de tablas
- Database = Conexión MySQL

### CRUD local

Sistema independiente para gestión directa desde consola.



## Buenas prácticas implementadas

- Separación clara de responsabilidades
- Arquitectura en capas
- Reutilización de servicios
- Organización modular
- Entorno virtual aislado
- Código estructurado para escalabilidad



## Mejoras futuras

- Autenticación con JWT
- Dockerización 
- Tests automatizado
- Frontend web
- Logs estructurados
- Despliegue en la nube



## Autora: *Ida Huenchulaf*

Proyecto desarrollado como práctica avanzada de arquitectura backend en Python.
