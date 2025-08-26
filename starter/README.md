
# API en Render (FastAPI) + Frontend en GitHub Pages

Este repositorio es un starter para desplegar una API de FastAPI en Render y consumirla desde un frontend estático (por ejemplo en GitHub Pages).

## 1) Ejecutar localmente
```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
uvicorn main:app --reload
# abrir http://127.0.0.1:8000/docs
```

## 2) Variables de entorno
- `ALLOWED_ORIGINS`: dominios permitidos para CORS. Ej: `https://www.tu-dominio.com,https://tu-dominio.com`
- `API_SECRET_KEY`: clave para proteger endpoints bajo `/secure/*`

## 3) Despliegue en Render (GUI)
1. Sube este repo a GitHub.
2. En Render: **New +** → **Web Service** → *Connect repo*.
3. Configura:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Runtime: Python 3.11
4. Añade variables de entorno (ALLOWED_ORIGINS, API_SECRET_KEY).
5. Deploy.

La URL será algo como: `https://mi-api.onrender.com`

## 4) Despliegue con `render.yaml` (infra-as-code)
En Render: **New +** → **Blueprint** → selecciona este repo. Render leerá `render.yaml` y creará el servicio.

## 5) Probar
- Salud: `GET /status`
- Público: `GET /productos`
- Seguro: `GET /secure/mi-cuenta` con header `Authorization: Bearer <API_SECRET_KEY>`

## 6) Frontend (GitHub Pages) – ejemplo fetch
```html
<button onclick="cargar()">Cargar productos</button>
<pre id="out"></pre>
<script>
async function cargar(){
  const res = await fetch("https://mi-api.onrender.com/productos");
  const data = await res.json();
  document.getElementById("out").textContent = JSON.stringify(data, null, 2);
}
</script>
```

## 7) Dominio propio
- En Render: *Custom Domains* → agrega `api.tu-dominio.com` y sigue las instrucciones de DNS (CNAME).
- Espera a que Render emita el certificado SSL (Let's Encrypt).

## 8) Notas
- Plan Free de Render puede "dormir" por inactividad; la primera petición tarda un poco (cold start).
- Para producción real considera planes de pago y base de datos gestionada.
