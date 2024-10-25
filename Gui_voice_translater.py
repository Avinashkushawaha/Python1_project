


import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set up default input and output languages
input_lang = "hi"  # Hindi
output_lang = "en"  # English

# Configure the TTS engine to use an English voice
voices = tts_engine.getProperty('voices')
for voice in voices:
    if "en" in voice.id:
        tts_engine.setProperty('voice', voice.id)
        break

# Function to capture and translate speech
def translate_speech():
    try:
        with sr.Microphone() as source:
            lbl_status.config(text="Listening...")
            root.update()  # Update GUI immediately
            
            # Capture voice input
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice, language=input_lang)
            lbl_status.config(text="Recognized Text:")
            
            # Display original text
            txt_original.delete("1.0", tk.END)
            txt_original.insert(tk.END, text)
            
            # Translate the text
            translated_text = GoogleTranslator(source='auto', target=output_lang).translate(text)
            
            # Display translated text
            txt_translated.delete("1.0", tk.END)
            txt_translated.insert(tk.END, translated_text)
            
            # Read translated text aloud
            lbl_status.config(text="Playing Translated Text...")
            tts_engine.say(translated_text)
            tts_engine.runAndWait()
            lbl_status.config(text="Translation and Playback Complete.")

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand the audio.")
    except sr.RequestError:
        messagebox.showerror("Error", "Network error. Check your connection.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Voice Translator")
root.geometry("400x400")
root.config(bg="lightblue")

# Labels and Text Boxes
lbl_title = tk.Label(root, text="Voice Translator", font=("Arial", 20, "bold"), bg="lightblue")
lbl_title.pack(pady=10)

lbl_status = tk.Label(root, text="Press 'Translate' to Start", font=("Arial", 12), bg="lightblue")
lbl_status.pack(pady=5)

lbl_original = tk.Label(root, text="Original Text", font=("Arial", 14), bg="lightblue")
lbl_original.pack(pady=5)

txt_original = tk.Text(root, wrap=tk.WORD, width=40, height=4)
txt_original.pack(pady=5)

lbl_translated = tk.Label(root, text="Translated Text", font=("Arial", 14), bg="lightblue")
lbl_translated.pack(pady=5)

txt_translated = tk.Text(root, wrap=tk.WORD, width=40, height=4)
txt_translated.pack(pady=5)

# Translate Button
btn_translate = tk.Button(root, text="Press here", font=("Arial", 14), command=translate_speech)
btn_translate.pack(pady=20)

root.mainloop()

