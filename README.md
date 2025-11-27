# 🧾 AI Expense Auditor (Powered by Gemini 2.0)

Sistema inteligente de procesamiento de documentos (IDP) que utiliza **Inteligencia Artificial Generativa Multimodal** para auditar facturas y recibos en tiempo real.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green) ![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red) ![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%202.0-orange)

## 🚀 Descripción del Proyecto

Este proyecto resuelve el problema de la carga manual de datos contables. A diferencia de los sistemas OCR tradicionales, utiliza un **LLM (Large Language Model)** de visión para "entender" el contexto de la imagen, permitiendo:

1.  **Extracción Estructurada:** Convierte imágenes desordenadas en JSON limpio.
2.  **Detección de Fraude:** Analiza los items comprados para detectar gastos no autorizados (ej. alcohol, juegos) automáticamente.
3.  **Resiliencia:** Funciona con fotos borrosas, arrugadas o con formatos no estándar sin necesidad de reentrenamiento.

## 🏗️ Arquitectura Técnica

El sistema sigue una arquitectura de microservicios desacoplada:

-   **Frontend:** Aplicación web interactiva construida con **Streamlit**.
-   **Backend:** API RESTful de alto rendimiento con **FastAPI**.
-   **AI Engine:** Integración con **Google Gemini 2.0 Flash** vía API REST pura (compatible con Python 3.8+).

## 🛠️ Tecnologías Clave

-   **Lenguaje:** Python
-   **Frameworks:** FastAPI, Uvicorn, Streamlit
-   **Librerías:** Requests, Pillow, Python-Multipart
-   **Servicios Externos:** Google Generative Language API

## ⚙️ Instalación y Uso Local

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/facundomala1/AI-Expense-Auditor-Powered-by-Gemini-2.0-.git](https://github.com/facundomala1/AI-Expense-Auditor-Powered-by-Gemini-2.0-.git)
    cd AI_Auditor
    ```

2.  **Configurar entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install fastapi uvicorn requests streamlit pillow python-multipart
    ```

4.  **Configurar API Key:**
    Abre `main.py` y coloca tu `GOOGLE_API_KEY`.

5.  **Ejecutar el sistema (Requiere 2 terminales):**

    *Terminal 1 (Backend):*
    ```bash
    uvicorn main:app --reload
    ```

    *Terminal 2 (Frontend):*
    ```bash
    streamlit run app.py
    ```

## 📸 Demo

![alt text](image.png)
---
Desarrollado por Facundo Mala - [LinkedIn](www.linkedin.com/in/facundo-mala-933a74249) - [GitHub](https://github.com/facundomala1)