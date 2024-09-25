import whisper
#from googletrans import Translator
import translators as ts
from gtts import gTTS
import os
import warnings
warnings.filterwarnings("ignore")
# Step 1: Load the Whisper model and transcribe the audio
def transcribe_audio_to_text(audio_file):
    #model = whisper.load_model("small")
    model = whisper.load_model("small")
    result = model.transcribe(audio_file, language="en")
    return result['text']

# Step 2: Translate English text to Telugu
def translate_text_to_telugu(text):
    if not text:
        return None
    #translator = Translator()  # 'te' is the language code for Telugu
    ts.preaccelerate_and_speedtest()
    print(ts.translators_pool)
    translated_text=ts.translate_text(
        text, translator='google', from_language='en', to_language='te')
    print(translated_text)
    #try:
        #translated_text = translator.translate(text, src='en', dest='te')
        #if translated_text and translated_text.text:
        #    return translated_text.text
        #else:
            #print("Translation returned empty result.")
           # return None
 # Return the translated text
    #except ValueError as e:
     #   print(f"Translation error: {e}")
     #   return None  # Return None or handle the error as needed
    
# Step 3: Convert the translated text to speech
def text_to_speech(text, output_audio_file):
    if not text:
        print("No text to convert to speech.")
        return False
    try:
        tts = gTTS(text=text, lang='te')
        tts.save(output_audio_file)
        return True
    except Exception as e:
        print(f"Text-to-speech error: {e}")
        return False


# Full pipeline: Audio to Telugu speech
def audio_to_telugu(audio_input_file, translated_output_file):
    if not os.path.exists(audio_input_file):
        print(f"Input file not found: {audio_input_file}")
        return
    #output_dir = os.path.dirname(translated_output_file)
    #print(output_dir)
    #if not os.path.exists(output_dir):
    #    os.makedirs(output_dir)
    # Transcribe the audio to text
    english_text = transcribe_audio_to_text(audio_input_file)
    #print("Transcription:", english_text)
    if not english_text:
        print("Transcription failed.")
        return

    # Translate the transcribed text to Telugu
    telugu_text = translate_text_to_telugu(english_text)
    if not telugu_text:
        print("Translation failed.")
        return
    #print("Translation:", telugu_text)
    if text_to_speech(telugu_text, translated_output_file):
        print(f"Telugu audio saved to {translated_output_file}")
    else:
        print("Text-to-speech conversion failed.")
    # Convert the Telugu text to speech
    #text_to_speech(telugu_text, translated_output_file)
    #print(f"Telugu audio saved to {translated_output_file}")


# Input audio file in English
audio_input = "MyNotebook.wav"
# Output translated Telugu audio file
translated_output = "output_telugu_audio.mp3"

# Run the process
audio_to_telugu(audio_input, translated_output)
