import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob



from gtts import gTTS
from googletrans import Translator



def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

if st.button("Convertir"):
    source_lang = "es"  # Lenguaje de origen (puedes cambiarlo según tus necesidades)
    target_lang = "en"  # Lenguaje de destino (puedes cambiarlo según tus necesidades)

    translated_text = translate_text(text, source_lang, target_lang)
    result, output_text = text_to_speech(translated_text, tld)
    
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tu audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
    
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")





