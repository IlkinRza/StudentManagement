from funksiyalar import Telebeler,melumat_elaveetme,melumatlari_yenile,melumatlari_sil,bir_telebe_melumatlari,tam_melumatlari_goster

print("""* * * * * Zəhmət olmasa aşağıdakı əməliyyatlardan birini seçin * * * * *
1.Tələbə əlave etmək

2.Bütün tələbə məlumatlarını göstərmək

3.Tələbə məlumatlarını silmək

4.Bir tələbənin məlumatlarını göstərmək

5.Tələbənin məlumatlarının yenilənməsi

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
    elif work=="5":
        melumatlari_yenile()