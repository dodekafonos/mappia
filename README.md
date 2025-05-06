# Mappia 🌍

Aplicação web geolocalizada construída com **Vue 3 + Vite** e **Leaflet.js** no frontend, e **FastAPI** no backend.  
Feita por e para rolezeiros.

---

## 📦 Tecnologias

### Frontend
- [Vue 3](https://vuejs.org/)
- [Vite](https://vitejs.dev/)
- [Vue-Leaflet](https://vue-leaflet.github.io/vue-leaflet/)
- [Leaflet.js](https://leafletjs.com/)
- [TailwindCSS](https://tailwindcss.com/)

### Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)
- [Python 3.11+](https://www.python.org/)
- [PostgreSQL + PostGIS](https://postgis.net/) (banco de dados geográfico)

---

## 🚀 Como rodar o projeto

### 🖥️ Frontend

1. Clone o repositório
git clone https://github.com/seu-usuario/mappia.git
cd mappia

2. Instale as dependências
npm install

3. Rode o servidor de desenvolvimento
npm run dev
Acesse o projeto em: http://localhost:5173

### 🐍 Backend (FastAPI)

1. Acesse a pasta do backend
cd backend

2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências
pip install -r requirements.txt

4. Rode o servidor FastAPI
uvicorn main:app --reload


## Acesse a API em: http://localhost:8000
## Acesse a documentação automática em: http://localhost:8000/docs