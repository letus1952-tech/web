
import os
from typing import List, Dict

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Mi Emprendimiento",
    description="Starter API (FastAPI) lista para Render con CORS y API Key.
Docs: /docs",
    version="1.0.0",
)

# --- CORS ---
# Define tus orígenes permitidos (tu dominio de GitHub Pages)
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:8000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in ALLOWED_ORIGINS if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Seguridad por API Key (sencilla) ---
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "cambia-esto-en-render")

def verify_api_key(authorization: str | None) -> None:
    """Valida 'Authorization: Bearer <API_SECRET_KEY>'"""
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Falta Authorization Bearer")
    token = authorization.split(" ", 1)[1].strip()
    if token != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="API key inválida")

# --- Endpoints ---

@app.get("/status")
def status() -> Dict[str, str]:
    return {"status": "ok", "message": "API funcionando en Render 🚀"}

@app.get("/productos")
def get_productos() -> List[Dict[str, str]]:
    return [
        {"id": 1, "nombre": "Mockup Pro", "precio": "19.99"},
        {"id": 2, "nombre": "API Premium", "precio": "49.00"},
    ]

@app.get("/secure/mi-cuenta")
def secure_me(Authorization: str | None = Header(None)) -> Dict[str, str]:
    verify_api_key(Authorization)
    return {"cuenta": "demo@miempresa.com", "plan": "PRO"}
