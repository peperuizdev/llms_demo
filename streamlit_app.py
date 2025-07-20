import streamlit as st
from app.generator import generate_text
from app.image_generator import generate_image_url
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador IA de Contenidos", layout="centered")

st.title("🧠 Generador de Contenidos con LLM + Imagen IA")

with st.form("content_form"):
    topic = st.text_input("📝 Tema del contenido", value="Inteligencia Artificial")
    platform = st.selectbox("📱 Plataforma", ["Twitter", "LinkedIn", "Instagram", "Blog"])
    submit = st.form_submit_button("Generar contenido")

if submit:
    with st.spinner("🔄 Generando texto..."):
        prompt = f"Escribe un contenido atractivo para {platform} sobre el tema: {topic}."
        result = generate_text(prompt)

    st.subheader("📄 Contenido generado:")
    st.write(result)

    with st.spinner("🎨 Generando imagen con IA..."):
        image_data = generate_image_url(topic)

    st.subheader("🖼️ Imagen generada por IA:")

    if image_data:
        # Mostrar imagen generada por IA en formato base64
        components.html(f'<img src="{image_data}" width="512"/>', height=550)
    else:
        st.warning("No se pudo generar la imagen.")
