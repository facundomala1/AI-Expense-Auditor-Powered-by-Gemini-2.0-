from fastapi import FastAPI, UploadFile, File
import requests
import base64
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ ERROR FATAL: No se encontró la GOOGLE_API_KEY. Asegúrate de tener el archivo .env creado.")

# URL con el modelo Gemini 2.0
URL_API = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"

def procesar_con_ia_manual(imagen_bytes, mime_type):
    imagen_b64 = base64.b64encode(imagen_bytes).decode('utf-8')

    payload = {
        "contents": [{
            "parts": [
                {
                    "text": """Actúa como un auditor contable experto. Analiza esta imagen.
                    Extrae la siguiente información y entrégala EXCLUSIVAMENTE en formato JSON puro (sin ```json):
                    {
                        "comercio": "Nombre del negocio",
                        "fecha": "YYYY-MM-DD",
                        "total_final": 0.00,
                        "moneda": "USD/ARS",
                        "items": [{"producto": "nombre", "precio": 0.00}],
                        "alerta_fraude": true/false,
                        "razon_alerta": "Explicación o null"
                    }"""
                },
                {
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": imagen_b64
                    }
                }
            ]
        }]
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(URL_API, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Error de Google: {response.text}")

    respuesta_json = response.json()
    try:
        texto_raw = respuesta_json['candidates'][0]['content']['parts'][0]['text']
        texto_limpio = texto_raw.replace("```json", "").replace("```", "").strip()
        return json.loads(texto_limpio)
    except (KeyError, IndexError):
        return {"error": "La IA no pudo procesar la respuesta", "debug": respuesta_json}

@app.post("/auditar")
async def subir_factura(file: UploadFile = File(...)):
    print(f"📥 Recibiendo archivo: {file.filename}...")
    try:
        contenido = await file.read()
        tipo_archivo = file.content_type or "image/jpeg"
        resultado = procesar_con_ia_manual(contenido, tipo_archivo)
        return {
            "estado": "Exito",
            "archivo": file.filename,
            "auditoria": resultado
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"mensaje": "🤖 Auditor IA (Modo Seguro .env) listo"}