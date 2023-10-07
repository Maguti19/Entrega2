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



st.title("Interfases Multimodales.")

try:
    os.mkdir("temp")
except:
    pass

st.subheader("Texto a audio y traducción.")
st.write('Las interfaces de texto a audio son fundamentales en las interfaces multimodales ya que permiten '
         'una comunicación más accesible y natural, facilitando la inclusión de personas con discapacidades '
         'visuales y permitiendo la interacción en situaciones donde no es posible leer texto. Estas interfaces '
         'también impulsan tecnologías emergentes como los asistentes de voz inteligentes, haciendo que la tecnología '
       )

source_lang = "es"  # Lenguaje de origen (puedes cambiarlo según tus necesidades)
target_lang = "en"  # Lenguaje de destino (puedes cambiarlo según tus necesidades)

translator = Translator()

text = st.text_input("Ingrese el texto:")

tld = "es"

def text_to_speech(text, tld):
    tts = gTTS(text, "es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text

if text:
    translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
    result, output_text = text_to_speech(translated_text, tld)
    
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tu audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
    
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


