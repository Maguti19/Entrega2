import os
import streamlit as st
from PIL import Image
import glob
import time

from gtts import gTTS
from googletrans import Translator

st.title("Interfaces Multimodales")
st.subheader("TRADUCTOR")

image = Image.open('traductormorado.jpg')
st.image(image)

st.write("Ingrese el texto que desea traducir y convertir en audio:")
text = st.text_area("Texto")

translator = Translator()

st.title("Texto a Audio")

in_lang = st.selectbox(
    "Selecciona el lenguaje de Entrada",
    ("Inglés", "Español", "Alemán", "Coreano", "Mandarín", "Japonés"),
)
if in_lang == "Inglés":
    input_language = "en"
elif in_lang == "Español":
    input_language = "es"
elif in_lang == "Alemán":
    input_language = "de"
elif in_lang == "Coreano":
    input_language = "ko"
elif in_lang == "Mandarín":
    input_language = "zh-cn"
elif in_lang == "Japonés":
    input_language = "ja"

out_lang = st.selectbox(
    "Selecciona el lenguaje de salida",
    ("Inglés", "Español", "Alemán", "Coreano", "Mandarín", "Japonés"),
)
if out_lang == "Inglés":
    output_language = "en"
elif out_lang == "Español":
    output_language = "es"
elif out_lang == "Alemán":
    output_language = "de"
elif out_lang == "Coreano":
    output_language = "ko"
elif out_lang == "Mandarín":
    output_language = "zh-cn"
elif out_lang == "Japonés":
    output_language = "ja"

english_accent = st.selectbox(
    "Selecciona el acento",
    (
        "Defecto",
        "Español",
        "Reino Unido",
        "Estados Unidos",
        "Canadá",
        "Australia",
        "Irlanda",
        "Sudáfrica",
    ),
)

if english_accent == "Defecto":
    tld = "com"
elif english_accent == "Español":
    tld = "com.mx"
# ... (agregar más opciones según sea necesario)

def text_to_speech(input_language, output_language, text, tld):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = trans_text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text

display_output_text = st.checkbox("Mostrar el texto")

if st.button("Convertir"):
    if text:
        result, output_text = text_to_speech(input_language, output_language, text, tld)
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Tú audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)

        if display_output_text:
            st.markdown(f"## Texto de salida:")
            st.write(f" {output_text}")
    else:
        st.warning("Por favor, ingrese un texto para traducir y convertir en audio.")
