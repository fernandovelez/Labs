# 🧪 Dashboard - Productos de Licores en Risaralda

Este proyecto corresponde a un laboratorio de análisis de datos en el sector industrial, específicamente en la categoría de **productos de licor registrados para su distribución en el departamento de Risaralda - Colombia**.

Se utiliza **Streamlit** para visualizar dinámicamente la información contenida en el archivo `Productos_licores.csv`, que puede ser obtenido desde el portal oficial de [Datos Abiertos del Gobierno de Colombia](https://www.datos.gov.co/).

---

## 🎯 Objetivos del laboratorio

- Cargar y explorar el dataset sobre productos de licor.
- Analizar información relevante como productor, distribuidor, grado de alcohol y estado del registro sanitario.
- Visualizar insights clave para la toma de decisiones estratégicas.
- Detectar oportunidades de mejora en la cadena de distribución.

---

## 🚀 Funcionalidades del Dashboard

- Filtros interactivos por productor, distribuidor, estado del registro y grado de alcohol.
- Visualización de:
  - Distribución del grado de alcohol
  - Estado del registro sanitario
  - Top 10 productores y distribuidores
  - Productos por año de vencimiento
- Indicadores clave (KPIs)

---

## 📦 Archivos

- `productos_licores_dashboard.py`: script principal del dashboard en Streamlit
- `requirements.txt`: dependencias necesarias para ejecutar la app
- `Productos_licores.csv`: dataset de entrada (debe ser subido manualmente al ejecutar)

---

## 💻 ¿Cómo usar este proyecto?

### 👉 Opción 1: Ejecutar localmente

1. Clona este repositorio o descarga los archivos.
2. Instala los requerimientos:
   ```bash
   pip install -r requirements.txt
