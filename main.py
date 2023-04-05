import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from kisi_ekle import *

uygulama=QApplication(sys.argv) 
#uygulama nesnesi oluşturuldu

pencere=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()










#veritabanı işlemleri
import sqlite3

baglanti=sqlite3.connect("kisiler.db")#veritabanı bağlantısı oluşturuldu
islem=baglanti.cursor()#veritabanı işlemleri için cursor nesnesi oluşturuldu
baglanti.commit()#veritabanı işlemlerini kaydetmek için
#ai id integer primary key autoincrement, #id kolonu oluşturuldu
table=islem.execute("create table if not exists kisiler (id integer primary key autoincrement,isim text,yas int,kilo float,boy float,yorum text,cinsiyet text ,vke float)")#kisiler tablosu oluşturuldu
baglanti.commit()#veritabanı işlemlerini kaydetmek için


def kisiEkle():
    isim=ui.ln_isim.text()
    yas=ui.ln_yas.text()
    kilo=ui.ln_kilo.text()
    boy=ui.ln_boy.text()
    yorum=ui.ln_yorum.text()
    cinsiyet=ui.cmb_gender.currentText()
    vke=ui.ln_vke.text()
    
    try:
        ekle = "insert into kisiler (isim,yas,kilo,boy,yorum,cinsiyet,vke) values (?,?,?,?,?,?,?)"#kisiler tablosuna veri ekleme sorgusu
        islem.execute(ekle,(isim,yas,kilo,boy,yorum,cinsiyet,vke))#sorgu çalıştırıldı
        baglanti.commit()#veritabanı işlemlerini kaydetmek için
        kayitListele()
        ui.statusbar.showMessage("Kişi Eklendi",5000)
    except Exception as error :
       ui.statusbar.showMessage("Kişi Eklenemedi ===",+str(error))
    
def kayitListele():
    ui.tbl_listele.clear()
    ui.tbl_listele.setHorizontalHeaderLabels(("id","isim","yas","kilo","boy","yorum","cinsiyet","vke"))
    ui.tbl_listele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#tablodaki sütunları genişletmek için
    sorgu="select * from kisiler"
    islem.execute(sorgu)
    
    for(i,j) in enumerate(islem):
        for(k,l) in enumerate(j):
            ui.tbl_listele.setItem(i,k,QTableWidgetItem(str(l)))
            
            

def cinsiyeteGoreListele():#bunu isme görede yapmak için isim yazıp butona basınca isme göre listeleme yapacak
    listelenecekCinsiyet=ui.cmb_gender_listele.currentText()
    sorgu="select * from kisiler where cinsiyet=?"
    islem.execute(sorgu,(listelenecekCinsiyet,))  #sorgu çalıştırıldı
    ui.tbl_listele.clear()
    ui.tbl_listele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#tablodaki sütunları genişletmek için
    for(i,j) in enumerate(islem):
        for(k,l) in enumerate(j):
            ui.tbl_listele.setItem(i,k,QTableWidgetItem(str(l)))
            
def ismeGoreListele():#bunu isme görede yapmak için isim yazıp butona basınca isme göre listeleme yapacak
    listelenecekİsim=ui.ln_isim_listele.text()
    sorgu="select * from kisiler where isim=?"
    islem.execute(sorgu,( listelenecekİsim,))  #sorgu çalıştırıldı
    ui.tbl_listele.clear()
    ui.tbl_listele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#tablodaki sütunları genişletmek için
    for(i,j) in enumerate(islem):#enumerate fonksiyonu ile sorgu sonucu dönen verileri tabloya yazdırdık index ve değerleri almak için
        for(k,l) in enumerate(j):
            ui.tbl_listele.setItem(i,k,QTableWidgetItem(str(l)))      
            
            
            
                          
                 
def kayitSil():
    sil_mesaj=QMessageBox.question(pencere,"Silme İşlemi","Silmek İstediğinize Emin Misiniz?",QMessageBox.Yes|QMessageBox.No)
    
    if sil_mesaj==QMessageBox.Yes:
        secilen_kayit=ui.tbl_listele.selectedItems()
        silinecek_kayit=secilen_kayit[0].text()
        sorgu="delete from kisiler where id=?"
        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            #kayıt silme işlemi başarılı ise tabloyu yenilemek için
            kayitListele()
            #end
            ui.statusbar.showMessage("Kayıt Silindi",5000)
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Silinemedi ==="+str(error))
    else:
        ui.statusbar.showMessage("silme işlemi iptal edildi",5000)        
 
        
def kayitGuncelle():#isme göre güncelleme yapmak için isim yazıp butona basınca isme göre güncelleme yapacak
    guncelle_mesaj=QMessageBox.question(pencere,"Güncelleme İşlemi","Güncellemek İstediğinize Emin Misiniz?",QMessageBox.Yes|QMessageBox.No)
    if guncelle_mesaj==QMessageBox.Yes: 
         
        try:
            id=ui.ln_id.text()
            isim=ui.ln_isim.text()
            yas=ui.ln_yas.text()
            kilo=ui.ln_kilo.text()
            boy=ui.ln_boy.text()   
            yorum=ui.ln_yorum.text()
            cinsiyet=ui.cmb_gender.currentText()
            vke=ui.ln_vke.text()
            
            if id!="":
                islem.execute("update kisiler set isim=?,yas=?,kilo=?,boy=?,yorum=?,cinsiyet=?,vke=? where id=?",(isim,yas,kilo,boy,yorum,cinsiyet,vke,id))
                kayitListele()   
                ui.statusbar.showMessage("Kayıt Güncellendi",5000)
            else:
                ui.statusbar.showMessage("Yanlış işlem yapıldı",5000)    
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Güncellenemedi ==="+str(error))    
    else:
        ui.statusbar.showMessage("Güncelleme işlemi iptal edildi",5000)      
 
               
#vke hesaplayan fonksiyon
def vke_hesapla():
    kilo=ui.ln_kilo_2.text()
    boy=ui.ln_boy_2.text()
    result=float(kilo) / (float(boy) ** 2)
    ui.lbl_sonuc.setText(str(result))
    
    
    
    
    

                           
               
               


#buton işlemleri
ui.btn_ekle.clicked.connect(kisiEkle)
ui.btn_listele.clicked.connect(kayitListele)
ui.btn_cinsiyete_gore.clicked.connect(cinsiyeteGoreListele)
ui.btn_isme_gore.clicked.connect(ismeGoreListele)
ui.btn_sil.clicked.connect(kayitSil)
ui.btn_guncelle.clicked.connect(kayitGuncelle)
ui.btn_hesapla.clicked.connect(vke_hesapla)

sys.exit(uygulama.exec_())

