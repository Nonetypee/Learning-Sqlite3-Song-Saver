from veritabanı import *

print("""****************************


1.Şarkı ekle

2.Şarkı sil

3.Veritabanında ki tüm şarkıların süresini hesapla

4. Çıkmak için 'q' basın.


******************************""")


Müzik = Müzikhane()

while True:

    işlem = input("Yapacağınız işlemi seçiniz: ")

    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        break

    elif (işlem == "1"):
        isim = input("Şarkının ismini giriniz: ")
        sanatcii = input("Şarkının Sanatçısını giriniz: ")
        albüm = input("Şarkının Albümünü giriniz: ")
        prod = input("Şarkının Prodüksiyon Şirketini giriniz: ")
        sure = int(input("Şarkı süresini giriniz: "))

        yeni_sarki = Müzik.sarki_ekle(isim,sanatcii,albüm,prod,sure)

    elif (işlem == "2"):
        sil = input("Silmek istediğiniz şarkının adı nedir?:") 

        surr = input("Emin misiniz (E/H) ? : ")

        if (surr == "E"):
            Müzik.sarki_sil(sil)
            print("Şarkı siliniyor...")
            time.sleep(2)
            print("Şarkı silindi.")

        else:
            print("Böyle bir şarkı bulunmamaktadır.")


    elif (işlem == "3"):
        Müzik.sarki_sure_hesapla()

    else:
        print("Geçersiz işlem yaptınız!")
        


