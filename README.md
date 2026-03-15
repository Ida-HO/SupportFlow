# SupportFlow

Sistema académico de gestión de tickets de soporte técnico desarrollado en Python con arquitectura en capas.

## Descripción general
SupportFlow permite gestionar usuarios, técnicos, tickets e historial. Implementa API REST con Flask y CRUD local.

## Arquitectura
Cliente → Controllers → Services → Models → Database → MySQL


## Estructura del proyecto
```
SupportFlow/
├── api/
│   ├── app.py
│   ├── controllers/
│   │   ├── tecnico_controller.py
│   │   ├── usuario_controller.py
│   │   ├── ticket_controller.py
│   │   └── ticket_historial_controller.py
│   ├── services/
│   │   ├── tecnico_service.py
│   │   ├── usuario_service.py
│   │   ├── ticket_service.py
│   │   └── ticket_historial_service.py
│   ├── models/
│   │   ├── tecnico.py
│   │   ├── usuario.py
│   │   ├── ticket.py
│   │   └── ticket_historial.py
│   └── database/
│       └── db.py
├── CrudSistemaTickets/
│   ├── main.py
│   ├── services/
│   │   ├── tecnico_service.py
│   │   ├── usuario_service.py
│   │   ├── ticket_service.py
│   │   └── ticket_historial_service.py
│   └── models/
│       ├── tecnico.py
│       ├── usuario.py
│       ├── ticket.py
│       └── ticket_historial.py
├── run_all.py
├── architecture.png
├── requirements.txt
└── README.md
```
## Tecnologías
Python, Flask, MySQL, Requests, venv

## Instalación
```
git clone <URL>
cd SupportFlow
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

## Configurar base de datos
Editar api/database/db.py

## Ejecutar
```
python api/app.py
python CrudSistemaTickets/main.py
```

## Autora
Ida Huenchulaf — Proyecto académico.




## Autora: *Ida Huenchulaf*

Proyecto desarrollado como práctica avanzada de arquitectura backend en Python.
