import streamlit as st

from googletrans import Translator

from gtts import gTTS

import os

 

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

 

translator = Translator()

 

text = st.text_input("Ingrese el texto:")

 

# Lista de idiomas de destino

languages = {

    "Inglés": "en",

    "Español": "es",

    "Chino Mandarín": "zh-cn",

    "Francés": "fr"

}

 

# Widget para seleccionar el idioma de destino

target_lang = st.selectbox("Seleccione el idioma de destino:", list(languages.keys()))

 

def text_to_speech(text, tld):

    tts = gTTS(text, lang=tld, slow=False)

    try:

        my_file_name = text[0:20]

    except:

        my_file_name = "audio"

    tts.save(f"temp/{my_file_name}.mp3")

    return my_file_name, text

 

if text and target_lang:

    target_lang_code = languages[target_lang]

    translated_text = translator.translate(text, src=source_lang, dest=target_lang_code).text


    if target_lang == "Chino Mandarín":

        target_lang_code = "zh-cn"

    elif target_lang == "Francés":

        target_lang_code = "fr"


    result, output_text = text_to_speech(translated_text, target_lang_code)


    audio_file = open(f"temp/{result}.mp3", "rb")

    audio_bytes = audio_file.read()

    st.markdown(f"## Tu audio:")

    st.audio(audio_bytes, format="audio/mp3", start_time=0)


    st.markdown(f"## Texto en audio:")

    st.write(f" {output_text}")
