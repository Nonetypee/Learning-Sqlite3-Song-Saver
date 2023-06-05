import sqlite3
import time


class Şarkı():
    def __init__(self,isim,sanatçı,albüm,prod,sarki_suresi):

        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prod = prod
        self.sarki_suresi = sarki_suresi

        

    def __str__(self):
        return "İsim: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nŞarkı Süresi: {}\n".format(self.isim,self.sanatçı,self.albüm,self.prod,self.sarki_suresi)
        



class Müzikhane():
    def __init__(self):
        self.baglanti_olustur()


    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("müzikhane.db") 

        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS şarkılar (isim TEXT, sanatçı TEXT, Albüm TEXT ,Prodüksiyon Şirketi TEXT,sarki_suresi INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()


    def sarki_ekle(self,isim,sanatci,album,prod,sure):
        sorgu = "INSERT INTO şarkılar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(isim,sanatci,album,prod,sure))
        
        self.baglanti.commit()  

    def sarki_sil(self,sarki):
        sorgu = "DELETE FROM şarkılar where isim = ?"

        self.cursor.execute(sorgu,(sarki,))

        self.baglanti.commit()


    def sarki_sure_hesapla(self):

        sorgu = "Select * from şarkılar"

        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()

        
        if (len(liste) == 0):
            print("Müzikhanede hiçbir şarkı bulunmamaktadır.")


        else:
            a = 0
            for i in liste:
                a+=i[4]
            print(a)
    



    