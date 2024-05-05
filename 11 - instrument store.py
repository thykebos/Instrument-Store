import tkinter as tk
from tkinter import ttk
import os
from ttkthemes import ThemedStyle
from tkmacosx import Marquee
import random
import sys
import json

def musteri():                 
    global isim
    global kullanicinumara
    isim=giris.get().strip().title()
    kullanicinumara= random.randint(1,1000)
    with open("login.txt","a", encoding="utf-8") as file:
        file.write("kullanici ad: " + isim + "\nkullanici no: " + str(kullanicinumara))
        
    if isim:
        m2.config(text=f" {isim} \n Kullanıcısı Giriş Yaptı \n Numaranız:{kullanicinumara} ")
    else:
        m2.config(text="  HATA! ")

def satinalma():         
    if isim and secilenlist:
        satis.config(text=" SATIN ALINDI ",state='disabled')
    
        if 'gitar' in secilenlist2:
           urun1.config(text=f" Satışı Yapılmıştır ",state='disabled')
        if 'elektrogitar' in secilenlist2:
           urun2.config(text=f" Satışı Yapılmıştır ",state='disabled')
        if 'saz' in secilenlist2:
           urun3.config(text=f" Satışı Yapılmıştır ",state='disabled')
        if 'keman' in secilenlist2:
           urun4.config(text=f" Satışı Yapılmıştır ",state='disabled')
        if 'kemençe' in secilenlist2:
           urun5.config(text=f" Satışı Yapılmıştır ",state='disabled')
        if 'kanun' in secilenlist2:
           urun6.config(text=f" Satışı Yapılmıştır ",state='disabled')

        sonuc={
            "kullanicino": kullanicinumara,
            "urunler": secilenlist2
        }
        sonucjson= json.dumps(sonuc,ensure_ascii=False,indent=4)
        with open("sepet.json","w", encoding='utf-8') as file:
            file.write(sonucjson)
            
    elif not isim and secilenlist:
        satis.config(text="sipariş yok")
    else:
        m3.config(text=" Giriş yapın")

                 

def ensturmansepet():
    global secilenlist
    global secilenlist2
    secilenlist = 0
    secilenlist2 = []
    if gitar1.get():
        secilenlist =secilenlist + 1
        secilenlist2.append("gitar")
    if elektrogitar1.get():
        secilenlist =secilenlist + 1
        secilenlist2.append('elektrogitar')
    if saz1.get():
        secilenlist =secilenlist + 1
        secilenlist2.append("saz")
    if keman1.get():
        secilenlist =secilenlist + 1
        secilenlist2.append("keman")
    if kemence1.get():
        secilenlist =secilenlist + 1
        secilenlist2.append("kemençe")
    if kanun1.get():
        secilenlist =secilenlist + 1
        secilenlist2.append("kanun")    
 
    if secilenlist and isim:
        m3.config(text=f"Sepete Eklenen Ürün Sayısı \n ={secilenlist}\n\n{kullanicinumara} No'lu Kullanıcı")     
    else:
        m3.config(text=" Giriş yapın")
        
       
    if isim:            
        
        m.config(text=" Seçilen Ürün veya Ürünler Sepete Eklenmiştir ") 
    else:
        m.config(text=" Giriş Yapılmalı HATA!")
         
root = tk.Tk()
root.geometry('1200x600')
root.title("SPOTIget")


label = ttk.Label(root, text=" KULLANICI ADI", background='pink', width=13, font=("Calibri", 13), foreground="black")
label.place(x=40,y=220)

giris = ttk.Entry(root, width=15, font=10,background='pink')
giris.place(x=40,y=250)

buton = ttk.Button(root, text="Giriş Yap", command=musteri)
buton.place(x=36,y=281)

style = ThemedStyle(root)
style.theme_use('itft1')

mavi_kutu = ttk.Labelframe(root, width=910, height=580)
mavi_kutu.place(x=270,y=10)

kutu2 = ttk.Label(root, background='#1d8055', width=50,foreground='#bfffe3',text='\n'*11,borderwidth=7, relief="raised")  
kutu2.place(x=350,y=40)

kutu3 = ttk.Label(root, background='#1d8055', width=50,foreground='#bfffe3',text='\n'*11,borderwidth=7, relief="raised")  
kutu3.place(x=800,y=40)

kutu4 = ttk.Label(root, background='#1d8055', width=70,foreground='#bfffe3',text='\n'*16,borderwidth=7, relief="raised")  
kutu4.place(x=350,y=300)

satis= ttk.Button(root, width=12, text="     SATIN AL",command=satinalma)
satis.place(x=890,y=180)

#BU KISIMDAN SONRASI ÜRÜN EKLEME ÜRÜN SATIŞI GİBİ KONULAR OLACAK   kullanılacak genel renk formatı (background='#1d8055' ve foreground='#bfffe3')

gitar1= tk.BooleanVar()
elektrogitar1=tk.BooleanVar()
saz1=tk.BooleanVar()
keman1=tk.BooleanVar()
kemence1=tk.BooleanVar()
kanun1=tk.BooleanVar()

urun1 = ttk.Checkbutton(root, text=" Gitar  ", variable=gitar1,command=ensturmansepet )
urun1.place(x=370,y=65)
urun2 = ttk.Checkbutton(root, text=" Elektro-Gitar  ", variable=elektrogitar1,command=ensturmansepet )
urun2.place(x=370,y=85)
urun3 = ttk.Checkbutton(root, text=" Saz  ", variable=saz1,command=ensturmansepet )
urun3.place(x=370,y=105)
urun4 = ttk.Checkbutton(root, text=" Keman  ", variable=keman1,command=ensturmansepet )
urun4.place(x=370,y=125)
urun5 = ttk.Checkbutton(root, text=" Kemençe  ", variable=kemence1,command=ensturmansepet )
urun5.place(x=370,y=145)
urun6 = ttk.Checkbutton(root, text=" Kanun  ", variable=kanun1,command=ensturmansepet )
urun6.place(x=370,y=165)

m = Marquee(root, fg='#bfffe3', bg='#bababa', text="Telli Çalgı Sepeti",font=2,width=270)
m.place(x=370,y=190)
m.stop(True)
m.bind('<Enter>', lambda _: m.play())
m.bind('<Leave>', lambda _: m.stop())

m2 = Marquee(root, fg='#bfffe3', bg='#bababa', text="",font=2,width=250)
m2.place(x=10,y=10)
m2.stop(True)
m2.bind('<Enter>', lambda _: m2.play())
m2.bind('<Leave>', lambda _: m2.stop())

m3 = Marquee(root, text="", font=("Calibri",14), width=270, background='#bababa', foreground='#bfffe3')
m3.place(x=820, y=63)
m3.bind('<Enter>', lambda _: m3.play())
m3.bind('<Leave>', lambda _: m3.stop())
#PANELDE AŞAĞI KISMADA MÜŞTERİ KONUŞMA KISMI YAPIALCAK OTOMASYON GİBİ !!!!!!!!! # SATIN AL BUTONUYLA BERABER İŞLEVSEL ÖZELLİKLER EKLENMELİ
def destek():
    global bilgi
    bilgi=giris2.get().lower()
    global urunler
    urunler=""
    
    if bilgi=="ürünlerim":
       with open("sepet.json","r", encoding="utf-8") as dosya:
            datalar=json.load(dosya)
            for i in datalar['urunler']:
                if i in secilenlist2:
                    urunler+= '\n'+i
            destekkutu2.config(text=urunler)        
    elif bilgi == "kılavuz":
        destekkutu2.config(text="1. Kullanıcı adı girerek Giriş Yapınız \n2. İstediğiniz Ürünü Seçip Sepete ekleyiniz \n3. Satın Al'a basın ve Ürünlerinizi kontrol edin \n İŞLEM TAMAM")
        
    else:
        destekkutu2.config(text="hata tekrar dene")
                          


destekkutu = ttk.Label(root, text="Destek Türünü Yazınız \n(Kılavuz - Ürünlerim)", width=44,font=("Arial",13), background='#bababa', foreground='#bfffe3')
destekkutu.place(x=367,y=320)

destekkutu2 = ttk.Label(root, text="", width=44,font=("Arial",13), background='#bababa', foreground='#bfffe3')
destekkutu2.place(x=367,y=410)

giris2 = ttk.Entry(root, width=15, font=10)
giris2.place(x=367,y=365)

destekbuton= ttk.Button(root, text="destek al",command=destek)
destekbuton.place(x=550,y=365)



root.mainloop()