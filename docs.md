
## Mappia - Stack

Frontend
Framework: Vue.js

Mapa: Leaflet.js com Vue-Leaflet

Estilo: TailwindCSS (ótimo para mobile-first, rápido de estilizar).

Backend
Linguagem: Python (FastAPI)

Banco de Dados:

PostgreSQL + PostGIS (ideal para trabalhar com dados geoespaciais).

Deploy a definir. 

---

## Estrutura de pastas
Estrutura inicial do backend:

mappia-backend/
├── app/
│   ├── __init__.py
│   ├── main.py           ← ponto de entrada
│   ├── models.py         ← ORM (SQLAlchemy)
│   ├── schemas.py        ← Pydantic schemas
│   ├── database.py       ← conexão com o banco
│   ├── crud.py           ← funções de acesso ao banco
│   └── routers/
│       └── events.py     ← endpoints de eventos
├── requirements.txt
├── .env
└── alembic/ (opcional para migrações)