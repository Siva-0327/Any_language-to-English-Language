from googletrans import Translator
import speech_recognition as sr
import pyglet
from gtts import gTTS
import tkinter
from tkinter import Tk,filedialog
import os

def speech():
     listening = sr.Recognizer()
     with sr.Microphone() as source:
         print("listening\nspeak now...")
         listening.adjust_for_ambient_noise(source,duration=1) # For Noise cancellation
         audio = listening.listen(source)
         text = listening.recognize_google(audio)  
     return text   # This function for recognise your speech and converts into text in which language you speak
def converter():
     try:
         text_con = speech()    
         translator = Translator()   
         translate = translator.translate(text_con,dest = 'en').text  # It will convert in English
         audio_text = translate
         root = Tk()
         root.withdraw()
         filename = filedialog.askdirectory()  # To save the file
         if filename:
             file_path = os.path.join(filename,'converted.txt') 
             with open (file_path,'w+',encoding = 'utf-8') as f1:
                 f1.write(audio_text)
                 f1.seek(0)
                 print(f1.read())
                 f1.close()
             os.chdir(os.path.dirname(file_path))  # To save the mp3 in same file that you have selected
             converted_audio = gTTS(text=audio_text,lang='en',slow =False)
             converted_audio.save("Audio_converted.mp3")
             os.system("start Audio_converted.mp3")
             player = pyglet.media.Player()
             audio_source = pyglet.media.load("Audio_converted.mp3")
             player.queue(audio_source)
             player.play()    # To play the audio
             pyglet.app.exit()
     except sr.UnknownValueError:
          print("Audio not recognised")
     except Exception as e:
          print("An Error occured at ",e)

if __name__ == "__main__":

    converter()
