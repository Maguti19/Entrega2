import streamlit as st
import os
import time
import glob
from googletrans import Translator
from gtts import gTTS
from PIL import Image

# Crear directorio temporal si no existe
try:
    os.mkdir("temp")
except FileExistsError:
    pass

st.title("Aplicativo AMA.")

st.subheader("Texto a audio.")
st.write("Las interfaces de texto a audio son fundamentales en las interfaces multimodales ya que permiten "
         "una comunicación más accesible y natural, facilitando la inclusión de personas con discapacidades "
         "visuales y permitiendo la interacción en situaciones donde no es posible leer texto. Estas interfaces "
         "también impulsan tecnologías emergentes como los asistentes de voz inteligentes, haciendo que la tecnología "
         "sea más accesible e intuitiva para todos los usuarios")

text = st.text_input("Ingrese el texto:")

def text_to_speech(text, tld):
    tts = gTTS(text, "es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text

if st.button("Convertir"):
    result, output_text = text_to_speech(text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown("## Tu audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
    st.markdown("## Texto en audio:")
    st.write(f"{output_text}")

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted", f)

st.write("Toca el botón y habla lo que quieres traducir")

stt_button = st.button("Inicio", key="stt_button")

if stt_button:
    st.write("Habla y espera a que se traduzca automáticamente.")

    result = st.text_area("Texto traducido:")
    
    stt_button = st.button("Detener")

    if stt_button:
        st.text("Detenido")

remove_files(7)
