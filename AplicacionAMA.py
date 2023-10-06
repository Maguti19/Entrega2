import streamlit as st
import os
import time
import glob
from gtts import gTTS
from googletrans import Translator
from PIL import Image

try:
    os.mkdir("temp")
except:
    pass

st.title("Aplicativo AMA")
#image = Image.open('text_to_audio.png')
#st.image(image, width=200)

st.subheader("Texto a audio y traducción.")

text = st.text_input("Ingrese el texto que desea traducir y convertir en audio.")

translator = Translator()

if st.button("Traducir y Convertir a Audio"):
    in_lang = st.selectbox(
        "Selecciona el lenguaje de Entrada",
        ("Inglés", "Español", "Italiano", "Coreano", "Francés", "Japonés"),
    )
    if in_lang == "Inglés":
        input_language = "en"
    elif in_lang == "Español":
        input_language = "es"
    # ... (agregar más idiomas según sea necesario)

    out_lang = st.selectbox(
        "Selecciona el lenguaje de salida",
        ("Inglés", "Español", "Italiano", "Coreano", "Francés", "Japonés"),
    )
    if out_lang == "Inglés":
        output_language = "en"
    elif out_lang == "Español":
        output_language = "es"
    # ... (agregar más idiomas según sea necesario)

    translation = translator.translate(text, src=input_language, dest=output_language)
    translated_text = translation.text

    tts = gTTS(translated_text, lang=output_language, slow=False)
    try:
        my_file_name = translated_text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")

    audio_file = open(f"temp/{my_file_name}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    st.markdown(f"## Texto Traducido:")
    st.write(f" {translated_text}")

    def remove_files(n):
        mp3_files = glob.glob("temp/*mp3")
        if len(mp3_files) != 0:
            now = time.time()
            n_days = n * 86400
            for f in mp3_files:
                if os.stat(f).st_mtime < now - n_days:
                    os.remove(f)
                    print("Deleted ", f)

    remove_files(7)
