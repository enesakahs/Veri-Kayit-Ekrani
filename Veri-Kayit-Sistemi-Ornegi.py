import re
import time

class Register:
    def __init__(self,programname):
        self.programname=programname
        self.loop=True #döngü

    def program(self):
        choice=self.menu()

        if choice=="1":
            print("Kayıt Ekleme Menusune Yönlendiriliyorsunuz..")
            time.sleep(3) #kullanıcıyı 3 sn bekletıyor
            self.addregister() #kayıtekle menusune gectı
        
        if choice=="2":
            print("Kayıt Silme Menusune Yönlendiriliyorsunuz..")
            time.sleep(3)
            self.deleteregister() #kayıtsil menusune gectı

        if choice=="3":
            print("Verilere Erişiliyor..")
            time.sleep(3)
            self.readregister() #kayıtoku menusune gectı

        if choice=="4":
            self.exit() #cıkıs menusune gectı


    def menu(self):
        def control(choice): #menu secım ıslemlerını kontrol edecek
            if re.search("[^1-4]",choice): #secım degerı 1 ve 4 arasında deger alabılır ıf bloguyla bunu kontrol ettık. eger yapılan secım ıcınde 1 ile 4 dısında bir deger varsa demek ıcın ^ ıle belırttık
                raise Exception ("lutfen 1 ve 4 arasında gecerlı bır secım yapınız")
            elif len(choice)!=1: #girilen degerın uzunlugunu burda 1 diye belırtmezsek 14 veya 41 gibi girilen degerlerde sistem icinde 1 ve 4 oldugu ıcın hata vermez
                raise Exception ("lutfen 1 ve 4 arasında gecerlı bır secım yapınız")
        while True:
            try:
                choice=input("merhabalar {}  sistemine hosgeldınız\n\nLutfen yapmak ıstedıgınız ıslemı secınız\n\n1-Kayıt Ekle\n2-Kayıt Sil\n3-Kayıt Oku\n4-Cıkıs Yap\n\n".format(self.programname))
                control(choice)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return choice 


    def addregister(self): #kayıt ekle
        def controlname(name): #AD
            if name.isalpha()==False: #isalpha fonk. kontrol ettıgı yapıyı tamamen karakterlerden olusturuyorsa True döndüren bir yapıdır. Burada alfabetik karakter dısında deger alırsa False dönerse hata versin
                raise Exception ("Adınız alfabetik karakterlerden olusmalıdır")
        while True:
            try:
                name=input("adınız: ")
                controlname(name) #input edilen adı yukarda olusturulan name isimli degıskenı cagırarak kontrol etmesi ıcın cagırdık
            except Exception as Errorname:
                print(Errorname)
                time.sleep(3)
            else:
                break

        def controlsurname(surname): #SOYAD
            if surname.isalpha()==False: #isalpha fonk. kontrol ettıgı yapıyı tamamen karakterlerden olusturuyorsa True döndüren bir yapıdır. Burada alfabetik karakter dısında deger alırsa False dönerse hata versin
                raise Exception ("Soyadınız alfabetik karakterlerden olusmalıdır")
        while True:
            try:
                surname=input("soyadınız: ")
                controlsurname(surname) 
            except Exception as Errorsurname:
                print(Errorsurname)
                time.sleep(3)
            else:
                break

        def controlage(age): #YAS
            if age.isdigit()==False: #isdigit fonk. kontrol ettıgı yapıyı tamamen sayısal karakterlerden olusuyorsa True döndüren bir yapıdır. Burada sayısal karakter dısında deger alırsa False dönerse hata versin
                raise Exception ("Yasınız rakamsal ıfadelerden olusmalıdır")
        while True:
            try:
                age=input("yasınız: ")
                controlage(age) 
            except Exception as Errorage:
                print(Errorage)
                time.sleep(3)
            else:
                break

        def controlTC(tc): #TC
            if tc.isdigit()==False: 
                raise Exception ("Kimlik Numaranız rakamsal ıfadelerden olusmalıdır")
            elif len(tc)!=11:
                raise Exception ("Kimlik Numaranız 11 karakterden olusmalıdır")
        while True:
            try:
                tc=input("TC No: ")
                controlTC(tc) 
            except Exception as Errortc:
                print(Errortc)
                time.sleep(3)
            else:
                break

        def controlmail(mail): #MAIL
            if not re.search("@" and ".com",mail): #eger bulundurmuyorsa demek
                raise Exception ("gecerlı bır mail adresi giriniz")
        while True:
            try:
                mail=input("Mail Adresiniz: ")
                controlmail(mail) 
            except Exception as Errormail:
                print(Errormail)
                time.sleep(3)
            else:
                break


#read() ve readline() metotları çıktı olarak bize bir karakter dizisi verirken, readlines() metodu liste veriyor
        with open("C:/Users/enes_/OneDrive/Masaüstü/Bilgiler.txt","r",encoding="utf-8") as Doc:
            lineNumber=Doc.readlines() 
        if len(lineNumber)==0: #satır sayısı sıfır ise yani dosya boşsa
            ıd=1
        else:
            with open("C:/Users/enes_/OneDrive/Masaüstü/Bilgiler.txt","r",encoding="utf-8") as Doc:
                ıd=int(Doc.readlines()[-1].split("-")[0])+1
            '''
            1- eğer dosya boş ise 1 ile başlat
            2- değil ise en son satıra git
            3- en son satırın 0. indeksini 1 arttır
            4- id değerine eşitle
            '''
        with open("C:/Users/enes_/OneDrive/Masaüstü/Bilgiler.txt","a+",encoding="utf-8") as Doc: #a+ ekleme ıcın
            Doc.write("{}-{} {} {} {} {}\n".format(ıd,name,surname,age,tc,mail))
            print("veriler işlenmiştir..\n")
        self.backtomenu()

    def deleteregister(self): #kayıt sil
        y=input("silmek ıstenılen ID numarasını giriniz..\n")
        with open("C:/Users/enes_/OneDrive/Masaüstü/Bilgiler.txt","r",encoding="utf-8") as Doc:
            List=[]
            List_2=Doc.readlines()
            for i in range(0,len(List_2)):
                List.append(List_2[i].split("-")[0])

        del List_2[List.index(y)]

        with open("C:/Users/enes_/OneDrive/Masaüstü/Bilgiler.txt","w+",encoding="utf-8") as NewDoc:
            for i in List_2:
                NewDoc.write(i)
        print("kayıt siliniyor..")
        time.sleep(3)
        print("kayıt silme işlemi gerceklesti.\n")
        time.sleep(2)
        self.backtomenu()

    def readregister(self): #kayıt oku
        with open("C:/Users/enes_/OneDrive/Masaüstü/Bilgiler.txt","r",encoding="utf-8") as Doc:
            for i in Doc:
                print(i)
        self.backtomenu()

    def exit(self): #cıkıs yap
        print("Otomasyondan cıkıs yapılıyor")
        time.sleep(3)
        self.loop=False
        exit()

    def backtomenu(self):
        while True:
            x=input(print("Ana menuye donmek ıcın 6, Cıkmak ıcın lutfen 5'e basınız.\n"))
            if x=="6":
                print("ana menuye dönüyorsunuz..")
                time.sleep(3)
                self.program()
                break
            elif x=="5":
                self.exit()
                break
            else:
                print("gecerli bir deger giriniz.")

System=Register("Veri Kayıt Otomasyonu")
while System.loop: #sistem degıskenı üzerinden döngü yapısını calıstıracak
    System.program() #menu sureklı karsımıza cıksın diye
