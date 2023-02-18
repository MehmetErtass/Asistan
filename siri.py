from gtts import gTTS
import os
import time # gecikmeyi sağlar
from playsound import playsound #ekrana mp3 açılmadan oynatır

def konustur(metin):
    tts = gTTS(text=metin,lang="tr")
    #tts.save("metin.mp3")
    #os.system("metin.mp3")
    tts.save("metin1.mp3")
    playsound("metin1.mp3")
    os.remove("metin1.mp3")

def baslangic():
    baslangic_metin="merhaba ben mehmetin asistanıyım . Siz kimsiniz ?"
    konustur(baslangic_metin)
    isim = input("isim gir :")
    if(isim == "mehmet"):
        sohbet_metin = "Hoş geldiniz efendim . Sizlere nasıl yardımcı olabilirim."
        konustur(sohbet_metin)
    elif(isim!="m"):
        konustur("Seni tanımıyorum yabancı. Benden ne istiyorsun. ")

    konustur("Mesela canın sıkıldıysa sohbet yaz sohbet edelim yakışıklı.")
    secimGir = input("secim :")
    if(secimGir == "sohbet"):
        sohbet(isim)
    elif(secimGir != "sohbet"):
        konustur("Şu anda bu isteğinizi gerçekleştiremiyorum.")

def sohbet(isim):
    sohbet_metin = "naber" + isim +"im"
    konustur(sohbet_metin)
    cevap = input("cevap:")
    if(cevap == "iyiyim"):
        sohbet_metin2 = "oh oh çok sevindim"
        konustur(sohbet_metin2)
    elif(cevap == "kötüyüm"):
        sohbet_metin3 = "Neden bir şey mi oldu ? Yapmamı istediğiniz bir şey var mı efendim ?"
        konustur(sohbet_metin3)
        cevap=input("cevap : ")
        if(cevap == "hayır"):
            konustur("iyi sormuyorum sana daha bir şey git hadi.")
        elif(cevap == "evet"):
            konustur("sizin için dua edecegim.")

baslangic()
