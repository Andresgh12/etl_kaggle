# streamlit_app.py
import os
import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Conexión a MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["miBase"]

st.title("⚽ Dashboard de Datos de Fútbol")

# Selector de colección
colecciones = db.list_collection_names()
col = st.sidebar.selectbox("Elige colección", colecciones)

# Carga en un DataFrame
docs = list(db[col].find())
if not docs:
    st.write("No hay datos en esta colección.")
    st.stop()

df = pd.DataFrame(docs)
df = df.drop(columns=["_id"])  # opcional

st.subheader(f"Vista de `{col}`")
st.dataframe(df)

# Ejemplo de gráfico: si hay columnas numéricas
numericas = df.select_dtypes("number").columns.tolist()
if numericas:
    choice = st.sidebar.selectbox("Columna numérica para gráfico", numericas)
    st.subheader(f"Gráfico de {choice} por categoría (si existe)")
    # si hay columna ‘season’ o ‘team’, ajusta aquí:
    if "season" in df.columns:
        chart_df = df.groupby("season")[choice].mean().reset_index()
        st.bar_chart(chart_df.set_index("season"))
    else:
        st.line_chart(df[choice])
