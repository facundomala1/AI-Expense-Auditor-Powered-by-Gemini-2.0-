import streamlit as st
import requests
from PIL import Image
import io

# Configuración de la página
st.set_page_config(page_title="AI Auditor 🤖", layout="wide")

st.title("🧾 Auditor de Gastos con Inteligencia Artificial")
st.markdown("Sube una foto de tu factura y la IA extraerá los datos estructurados automáticamente.")

# Dividimos la pantalla en 2 columnas
col1, col2 = st.columns(2)

with col1:
    st.header("1. Sube tu imagen")
    archivo = st.file_uploader("Elige una factura (JPG/PNG)", type=["jpg", "png", "jpeg"])

    if archivo is not None:
        # Mostramos la imagen en pantalla
        imagen = Image.open(archivo)
        # Puedes probar con 300, 350 o 400 hasta que te guste el tamaño
        st.image(imagen, caption="Factura subida", width=350)
        
        # Botón para procesar
        if st.button("✨ Auditar con IA"):
            with col2:
                st.header("2. Resultados")
                with st.spinner("Analizando píxeles con Gemini 2.0 Vision..."):
                    try:
                        # Convertimos la imagen para enviarla a TU propia API (la que tienes corriendo)
                        # Importante: resetear el puntero del archivo al inicio
                        archivo.seek(0)
                        files = {"file": (archivo.name, archivo, archivo.type)}
                        
                        # Llamada a tu Backend (FastAPI)
                        res = requests.post("http://127.0.0.1:8000/auditar", files=files)
                        
                        if res.status_code == 200:
                            data = res.json()
                            auditoria = data["auditoria"]
                            
                            # Mostramos métricas bonitas
                            c1, c2, c3 = st.columns(3)
                            c1.metric("Comercio", auditoria.get("comercio") or "Desconocido")
                            c2.metric("Total", f"${auditoria.get('total_final') or 0}")
                            c3.metric("Fraude", "DETECTADO 🚨" if auditoria.get("alerta_fraude") else "Limpio ✅")
                            
                            st.divider()
                            
                            # Mostramos los items en una tabla
                            st.subheader("🛒 Items Detectados")
                            st.table(auditoria.get("items"))
                            
                            # Mostramos el JSON crudo por si acaso
                            with st.expander("Ver JSON Técnico"):
                                st.json(data)
                                
                        else:
                            st.error(f"Error del servidor: {res.text}")
                            
                    except Exception as e:
                        st.error(f"Error de conexión: {e}")
                        st.info("Asegúrate de que 'main.py' esté corriendo en otra terminal.")