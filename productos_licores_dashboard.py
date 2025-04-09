import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard Productos Licores", layout="wide")

st.title("📊 Dashboard - Productos de Licores en Risaralda")
st.markdown("Análisis de productos con registro sanitario para su distribución en el departamento de Risaralda.")

# Subir el archivo
uploaded_file = st.file_uploader("📁 Sube el archivo CSV de productos de licor", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)

    # Convertir fechas
    df['VIGENCIA DE REGISTRO SANITARIO'] = pd.to_datetime(df['VIGENCIA DE REGISTRO SANITARIO'], errors='coerce', dayfirst=True)
    df['ESTADO REGISTRO'] = np.where(df['VIGENCIA DE REGISTRO SANITARIO'] < pd.Timestamp.today(), 'VENCIDO', 'VIGENTE')

    # Filtros en la barra lateral
    st.sidebar.header("🔎 Filtros")
    productores = st.sidebar.multiselect("Productor", options=df['PRODUCTOR'].unique(), default=None)
    distribuidores = st.sidebar.multiselect("Distribuidor", options=df['NOMBRE EMPRESA DISTRIBUIDORA'].unique(), default=None)
    estado = st.sidebar.multiselect("Estado del Registro", options=df['ESTADO REGISTRO'].unique(), default=df['ESTADO REGISTRO'].unique())
    grado_range = st.sidebar.slider("Grado de Alcohol", float(df['GRADO DE ALCOHOL'].min()), float(df['GRADO DE ALCOHOL'].max()), (10.0, 40.0))

    # Aplicar filtros
    df_filtered = df[
        (df['GRADO DE ALCOHOL'] >= grado_range[0]) &
        (df['GRADO DE ALCOHOL'] <= grado_range[1]) &
        (df['ESTADO REGISTRO'].isin(estado))
    ]

    if productores:
        df_filtered = df_filtered[df_filtered['PRODUCTOR'].isin(productores)]
    if distribuidores:
        df_filtered = df_filtered[df_filtered['NOMBRE EMPRESA DISTRIBUIDORA'].isin(distribuidores)]

    # KPIs
    st.subheader("📌 Indicadores")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Productos", len(df_filtered))
    col2.metric("Productores Únicos", df_filtered['PRODUCTOR'].nunique())
    col3.metric("Porcentaje Registros Vencidos", f"{(df_filtered['ESTADO REGISTRO'].value_counts(normalize=True).get('VENCIDO', 0)*100):.1f}%")

    # Gráficos
    st.subheader("📊 Visualizaciones")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Distribución del Grado de Alcohol")
        fig, ax = plt.subplots()
        sns.histplot(df_filtered['GRADO DE ALCOHOL'], kde=True, bins=20, ax=ax, color='salmon')
        st.pyplot(fig)

    with col2:
        st.markdown("### Estado del Registro Sanitario")
        fig2, ax2 = plt.subplots()
        df_filtered['ESTADO REGISTRO'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'], ax=ax2)
        ax2.set_ylabel("")
        st.pyplot(fig2)

    st.markdown("### 🏭 Top 10 Productores")
    top_productores = df_filtered['PRODUCTOR'].value_counts().head(10)
    st.bar_chart(top_productores)

    st.markdown("### 🏪 Top 10 Distribuidores")
    top_dist = df_filtered['NOMBRE EMPRESA DISTRIBUIDORA'].value_counts().head(10)
    st.bar_chart(top_dist)

    st.markdown("### 📅 Productos con Registro Próximo a Vencerse")
    df_filtered['AÑO VENCIMIENTO'] = df_filtered['VIGENCIA DE REGISTRO SANITARIO'].dt.year
    vencimientos = df_filtered['AÑO VENCIMIENTO'].value_counts().sort_index()
    st.line_chart(vencimientos)

else:
    st.info("Por favor, sube el archivo `Productos_licores.csv` para iniciar el análisis.")