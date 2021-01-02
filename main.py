#web de arama yapmada kullanılan kütüphane:
import webbrowser

#saat için:
from datetime import datetime
import time
#konuşulanları dinleme için:
import speech_recognition as sr

#sesli asistanın konuşması için
from gtts import gTTS
from playsound import playsound

#dosya işlemleri için
import random
import os

#sesleri alabilmek için
r = sr.Recognizer()

#mikrofonu dinlemek için
#dinleneni tanımlamak için voice kısmı kullanılır.
def record(ask = False):

    with sr.Microphone() as source:
        #eğer soru var ise sorunun cevabında kullanmak için:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        #oluşabilecek hatalar için:
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak("Anlayamadım lütfen tekrar eder misin ")
        except sr.RequestError:
            speak("Sistem Çalışmıyor.")

        return voice

#herhangi bir değere göre yanıt verme
#bu kısım opsiyoneldir dilediğinizi ekleyebilirsiniz.

def response(voice):

    if ("merhaba") in voice:
       speak("merhaba")

    if ("nasılsın") in voice:
       speak("iyiyim sen nasılsın?")

    if ("beni dinliyor musun") in voice:
       speak("Evet sizi dinliyorum ")

    if ("saat kaç") in voice:
       speak("Saat " + datetime.now().strftime('%H:%M:%S'))

    #Eğer arama yaptırmak istiyorsak neyi arayacağımızı belirtirmemizi isteyip bunu google da search ediyoruz.
    if ("arama yap") in voice:
        search = record('neyi aramak istiyorsunuz')
        url ='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + " için web de bulduklarım")

    #programı sonlandırmak için:
    if ("görüşürüz" in voice):
        speak("görüşmek üzere")
        exit()


def speak(string):
    #verdiğimiz string'i ses e dönüştürme işlemi
    tts = gTTS(string, lang="tr")
    # sesler için dosya oluşturup daha sonra bu dosyaları sileceğiz.
    rand = random.randint(1,10000)
    file = "audio-" + str(rand) + ".mp3"
    #dosyayı kayıt etmek için
    tts.save(file)
    #dosyayı oynatmak için
    playsound(file)
    #silme işlemi için
    os.remove(file)

#karşılama cümlesi:
speak("Merhaba. Nasıl yardımcı olabilirim?")

#biz sonlandırana kadar devam etmesi için: (sonlandırmak için satır:54-57)
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
"""
Bu versiyon türçedir diğer dil seçenekleri için voice tanımlamasında:
voice = r.recognize_google(audio,lang="xxx") şeklinde olmalıdır.
"""