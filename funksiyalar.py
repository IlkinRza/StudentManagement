class Telebeler():
    def __init__(self,kod,ad,soyad,email,nomre):
        self.kod=kod
        self.ad=ad
        self.soyad=soyad
        self.email=email
        self.nomre=nomre

    def melumatlar(self):
        return (self.kod, self.ad, self.soyad, self.email, self.nomre)

telebe_listi=[]


def melumat_elaveetme():
    i=0
    x=int(input("Nece telebe siyahisi yaratmaq isteyirsiniz? : "))
    while(i<x):
        print("_______________________________________________________")
        print("Yeni tələbə siyahısı yaradın")
        print("_______________________________________________________")
        _kod = int(input("Kodunuzu Daxil Edin: "))
        _ad = input("Adınızı Daxil Edin: ")
        _soyad = input("Soyadınızı Daxil Edin: ")
        _email = input("Emailinizi '@' istifadə edərək əlavə edin: ")
        _nomre = input("Nömrəniz '+994' ilə başlamalıdır: ")
        if (_kod>99 and _kod<=999):
            if "@" in _email and _nomre.startswith("+994"):
                telebe = Telebeler(_kod, _ad, _soyad, _email, _nomre)
                print("Qeydiyyatdan müveffeqiyyetle keçdiniz {} bəy".format(_ad))
                print("_______________________________________________________")
                telebe_listi.append(telebe)
                print(telebe)
            else:
                print("Emailinizi ve ya nömrenizi sehv formatda daxil etmisiniz!!!")
                break
        else:
            print("Kod 3 reqemden ibaret olmalıdır!!!")
            break
        i+=1

def tam_melumatlari_goster():
    print("_______________________________________________________")
    print("Mövcud olan məlumatlar:")
    for i in telebe_listi:
        print(i.melumatlar())

def melumatlari_sil():
    print("_______________________________________________________")
    kod=int(input("Melumatlarınızı silmek ücün evvelce kodunuzu daxil edin: "))
    for i in telebe_listi:
        if(kod==i.kod):
            telebe_listi.remove(i)
            print("Siyahı müveffeqiyyetle silindi...")

def bir_telebe_melumatlari():
    print("_______________________________________________________")
    telebe_adi=input("Məlumatlarınıza göz gəzdirmək üçün adınızı daxil edin: ")
    for i in telebe_listi:
        if(telebe_adi==i.ad):
            print(i.melumatlar())

def melumatlari_yenile():
    print("_______________________________________________________")
    kod=int(input("Melumatlarınızı deyismek ücün evvelce kodunuzu daxil edin: "))
    for i in telebe_listi:
        if(kod!=i.kod):
            print("Kodunuzu düzgün daxil etmemisiniz!!!")
        else:
            print(i.melumatlar())

            kohne_kod = int(input("Kodunuzu deyismek isteyirsinizse indiki kodunuzu daxil edin,yoxsa '0'-a basin: "))
            if (kohne_kod == i.kod):
                yeni_kod = int(input("Yeni kodunuzu daxil edin: "))
                if (yeni_kod > 99 and yeni_kod <= 999):
                    i.kod = yeni_kod
                    print(f"Kodunuzu müveffeqiyyetle deyisdiniz {i.ad} bəy")
                    print("_______________________________________________________")

            kohne_ad = input("Adinizi deyismek isteyirsinizse indiki adinizi daxil edin,yoxsa entere basin: ")
            if (kohne_ad == i.ad):
                yeni_ad = input("Yeni adinizi daxil edin: ")
                i.ad = yeni_ad
                print(f"Adinizi müveffeqiyyetle deyisdiniz {yeni_ad} bəy")
                print("_______________________________________________________")

            kohne_soyad = input("Soyadinizi deyismek isteyirsinizse indiki soyadinizi daxil edin,yoxsa entere basin: ")
            if (kohne_soyad == i.soyad):
                yeni_soyad = input("Yeni soyadinizi daxil edin: ")
                i.soyad = yeni_soyad
                print(f"Soyadinizi müveffeqiyyetle deyisdiniz {i.ad} bəy")
                print("_______________________________________________________")

            kohne_email = input("Emailinizi deyismek isteyirsinizse indiki emailinizi daxil edin,yoxsa entere basin: ")
            if (kohne_email == i.email):
                yeni_email = input("Yeni emailinizi daxil edin: ")
                if "@" in yeni_email:
                    i.email = yeni_email
                    print(f"Emailinizi müveffeqiyyetle deyisdiniz {i.ad} bəy")
                    print("_______________________________________________________")

            kohne_nomre = input("Nömrənizi deyismek isteyirsinizse indiki nömrənizi daxil edin,yoxsa entere basin: ")
            if (kohne_nomre == i.nomre):
                yeni_nomre = input("Yeni nömrenizi daxil edin: ")
                if  yeni_nomre.startswith("+994"):
                    i.nomre = yeni_nomre
                    print(f"Nomrenizi müveffeqiyyetle deyisdiniz {i.ad} bəy")

