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

#Neçə tələbə siyahısı yaratmaq istəyirsinizsə, while ın içindəki dəyərə o ededi verin
def melumat_elaveetme():
    i=0
    while(i<10):
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
    telebe_adı=input("Məlumatlarınıza göz gəzdirmək üçün adınızı daxil edin: ")
    for i in telebe_listi:
        if(telebe_adı==i.ad):
            print(i.melumatlar())


print("""* * * * * Zəhmət olmasa aşağıdakı əməliyyatlardan birini seçin * * * * *
1.Tələbə əlave etmək

2.Bütün tələbə məlumatlarını göstərmək

3.Tələbə məlumatlarını silmək

4.Bir tələbənin məlumatlarını göstərmək

Proqramdan çıxmaq üçün 'q'- ya basın
__________________________________________________
""")

#dövr vasitesile funksiyalarımızı çağıraq
while True:
    print("_______________________________________________________")
    work = input("Əməliyyatı seçin:")
    if work == "q":
        print("Proqramdan çıxılır...")
        break
    elif work=="1":
        melumat_elaveetme()
    elif work=="2":
        tam_melumatlari_goster()
    elif work=="3":
        melumatlari_sil()
    elif work=="4":
        bir_telebe_melumatlari()

