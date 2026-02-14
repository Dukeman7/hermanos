import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import date

st.set_page_config(page_title="ADN: La Constante Familiar", layout="centered")

st.title("🧬 El Algoritmo de nuestra Sangre")
st.markdown("### Una simetría matemática entre dos generaciones")

# --- DATOS DE ENTRADA ---
# Generación Hermanos
h_juancho = date(1969, 6, 28)
h_manuel = date(1971, 11, 24)
h_patricia = date(1974, 4, 24)

# Generación Hijos/Sobrinos
j_daniel = date(2001, 10, 14)
j_luisito = date(2004, 3, 18)
j_maria = date(2006, 9, 20)
j_daniela = date(2009, 1, 29)

# --- CÁLCULOS ---
gaps_h = [
    (h_manuel - h_juancho).days,
    (h_patricia - h_manuel).days
]

gaps_j = [
    (j_luisito - j_daniel).days,
    (j_maria - j_luisito).days,
    (j_daniela - j_maria).days
]

avg_h = sum(gaps_h) / len(gaps_h)
avg_j = sum(gaps_j) / len(gaps_j)

# --- INTERFAZ ---
st.info(f"💡 **Dato curioso:** El promedio de separación entre hermanos es de **{avg_h:.0f} días**, y entre tus hijos es de **{avg_j:.0f} días**. ¡La diferencia es de apenas una semana!")

# Gráfico Comparativo
fig = go.Figure()

fig.add_trace(go.Bar(
    x=['Juancho-Manuel', 'Manuel-Patricia'],
    y=gaps_h,
    name='Hermanos (Gen 1)',
    marker_color='salmon',
    text=gaps_h,
    textposition='auto',
))

fig.add_trace(go.Bar(
    x=['Daniel-Luisito', 'Luisito-María', 'María-Daniela'],
    y=gaps_j,
    name='Hijos/Sobrinos (Gen 2)',
    marker_color='skyblue',
    text=gaps_j,
    textposition='auto',
))

fig.update_layout(
    title="Días de diferencia entre nacimientos",
    yaxis_title="Días",
    barmode='group',
    template='plotly_white'
)

st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN DE LEGADO ---
st.divider()
st.subheader("📋 Resumen de la Frecuencia Familiar")

col1, col2 = st.columns(2)
with col1:
    st.write("**Generación 1**")
    st.write(f"Promedio: {avg_h:.1f} días")
    st.caption("Una precisión de reloj suizo.")

with col2:
    st.write("**Generación 2**")
    st.write(f"Promedio: {avg_j:.1f} días")
    st.caption("El legado matemático continúa.")

st.sidebar.markdown("### 🌹 En memoria")
st.sidebar.write("Patricia (QEPD)")
st.sidebar.write("Siempre presente en nuestra simetría.")
st.sidebar.markdown("---")
st.sidebar.write("🛠️ **Ingeniería de Vida**")
st.sidebar.write("Desarrollado por: Mago Luis")
