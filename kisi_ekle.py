# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kisi_ekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 992)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 41, 16))
        self.label_5.setObjectName("label_5")
        self.cmb_gender = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_gender.setGeometry(QtCore.QRect(30, 400, 101, 31))
        self.cmb_gender.setObjectName("cmb_gender")
        self.cmb_gender.addItem("")
        self.cmb_gender.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 380, 47, 13))
        self.label_6.setObjectName("label_6")
        self.ln_boy = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_boy.setGeometry(QtCore.QRect(70, 210, 121, 31))
        self.ln_boy.setObjectName("ln_boy")
        self.ln_yorum = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_yorum.setGeometry(QtCore.QRect(70, 270, 231, 91))
        self.ln_yorum.setObjectName("ln_yorum")
        self.ln_yas = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_yas.setGeometry(QtCore.QRect(70, 110, 121, 31))
        self.ln_yas.setObjectName("ln_yas")
        self.ln_kilo = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_kilo.setGeometry(QtCore.QRect(70, 160, 121, 31))
        self.ln_kilo.setObjectName("ln_kilo")
        self.ln_isim = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_isim.setGeometry(QtCore.QRect(70, 60, 121, 31))
        self.ln_isim.setObjectName("ln_isim")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 47, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 480, 101, 21))
        self.label_8.setObjectName("label_8")
        self.ln_vke = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_vke.setGeometry(QtCore.QRect(140, 460, 161, 51))
        self.ln_vke.setObjectName("ln_vke")
        self.tbl_listele = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_listele.setGeometry(QtCore.QRect(330, 60, 601, 451))
        self.tbl_listele.setRowCount(100)
        self.tbl_listele.setColumnCount(8)
        self.tbl_listele.setObjectName("tbl_listele")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 20, 101, 16))
        self.label_9.setObjectName("label_9")
        self.cmb_gender_listele = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_gender_listele.setGeometry(QtCore.QRect(450, 10, 101, 31))
        self.cmb_gender_listele.setObjectName("cmb_gender_listele")
        self.cmb_gender_listele.addItem("")
        self.cmb_gender_listele.addItem("")
        self.btn_cinsiyete_gore = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cinsiyete_gore.setGeometry(QtCore.QRect(570, 10, 51, 31))
        self.btn_cinsiyete_gore.setObjectName("btn_cinsiyete_gore")
        self.btn_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekle.setGeometry(QtCore.QRect(20, 560, 111, 31))
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sil.setGeometry(QtCore.QRect(150, 560, 111, 31))
        self.btn_sil.setObjectName("btn_sil")
        self.btn_guncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guncelle.setGeometry(QtCore.QRect(280, 560, 131, 31))
        self.btn_guncelle.setObjectName("btn_guncelle")
        self.btn_listele = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listele.setGeometry(QtCore.QRect(430, 560, 111, 31))
        self.btn_listele.setObjectName("btn_listele")
        self.ln_isim_listele = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_isim_listele.setGeometry(QtCore.QRect(710, 10, 121, 31))
        self.ln_isim_listele.setObjectName("ln_isim_listele")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(630, 20, 81, 21))
        self.label_10.setObjectName("label_10")
        self.btn_isme_gore = QtWidgets.QPushButton(self.centralwidget)
        self.btn_isme_gore.setGeometry(QtCore.QRect(840, 10, 51, 31))
        self.btn_isme_gore.setObjectName("btn_isme_gore")
        self.ln_id = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_id.setGeometry(QtCore.QRect(300, 600, 91, 31))
        self.ln_id.setObjectName("ln_id")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(280, 610, 47, 21))
        self.label_11.setObjectName("label_11")
        self.ln_kilo_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_kilo_2.setGeometry(QtCore.QRect(670, 570, 121, 31))
        self.ln_kilo_2.setObjectName("ln_kilo_2")
        self.ln_boy_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_boy_2.setGeometry(QtCore.QRect(670, 620, 121, 31))
        self.ln_boy_2.setObjectName("ln_boy_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(630, 570, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(630, 620, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 530, 291, 31))
        self.label.setObjectName("label")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 10, 311, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(800, 570, 41, 41))
        self.label_15.setObjectName("label_15")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(840, 560, 71, 51))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        self.btn_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hesapla.setGeometry(QtCore.QRect(800, 620, 111, 31))
        self.btn_hesapla.setObjectName("btn_hesapla")
        self.lbl_sonuc_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc_2.setGeometry(QtCore.QRect(1210, 640, 61, 51))
        self.lbl_sonuc_2.setObjectName("lbl_sonuc_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(280, 640, 47, 13))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 680, 211, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(30, 700, 341, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(30, 720, 401, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(30, 740, 701, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 760, 481, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(30, 800, 541, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(30, 780, 771, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(560, 800, 371, 61))
        self.label_24.setObjectName("label_24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmb_gender.setCurrentIndex(-1)
        self.cmb_gender_listele.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Yaş"))
        self.label_3.setText(_translate("MainWindow", "Kilo"))
        self.label_4.setText(_translate("MainWindow", "Boy"))
        self.label_5.setText(_translate("MainWindow", "Yorum"))
        self.cmb_gender.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cmb_gender.setItemText(1, _translate("MainWindow", "Kadın"))
        self.label_6.setText(_translate("MainWindow", "Cinsiyet"))
        self.label_7.setText(_translate("MainWindow", "İsim"))
        self.label_8.setText(_translate("MainWindow", "Vücut Kitle Endeksi"))
        self.label_9.setText(_translate("MainWindow", "Cinsiyete göre Listele"))
        self.cmb_gender_listele.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cmb_gender_listele.setItemText(1, _translate("MainWindow", "Kadın"))
        self.btn_cinsiyete_gore.setText(_translate("MainWindow", "Listele"))
        self.btn_ekle.setText(_translate("MainWindow", "Kisi Ekle"))
        self.btn_sil.setText(_translate("MainWindow", "Kisi Sil"))
        self.btn_guncelle.setText(_translate("MainWindow", "Kisi Güncelle İd\'ye Göre"))
        self.btn_listele.setText(_translate("MainWindow", "Kisileri Listele"))
        self.label_10.setText(_translate("MainWindow", "İsim göre Listele"))
        self.btn_isme_gore.setText(_translate("MainWindow", "Listele"))
        self.label_11.setText(_translate("MainWindow", "id"))
        self.label_12.setText(_translate("MainWindow", "Kilo"))
        self.label_13.setText(_translate("MainWindow", "Boy"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Vücut Kitle Endeksini Hesapla</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff00ff;\">DİYETİSYEN OTOMASYONU</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Sonuç="))
        self.lbl_sonuc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff00ff;\">.</span></p></body></html>"))
        self.btn_hesapla.setText(_translate("MainWindow", "Hesapla"))
        self.lbl_sonuc_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">.</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">KULLANIM KILAVUZU</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "1. Kisi eklemek için formda boş alan bırakmayın (id boş kalacak )."))
        self.label_19.setText(_translate("MainWindow", "2. Silmek istediğiniz kişinin tabloda id\'sine tıkladıktan sonra Kisi Sil butonuna tıklayın."))
        self.label_20.setText(_translate("MainWindow", "3. Güncellemek istediğiniz kişinin id\'sini id inputuna yazdıktan sonra formda boş alan kalmayacak şekilde doldurunuz ve Güncelle butonuna tıklayınız."))
        self.label_21.setText(_translate("MainWindow", "4. Vücut kitle indeksini doldurmadan önce hesaplama bölümünden sonucu öğrenerek doldurabilirsiniz."))
        self.label_22.setText(_translate("MainWindow", "6. Listeleme işlemlerini cinsiyete,isme göre yapabilirsiniz veya Kisileri Listele butonuna tıklarsanız hepsi listelenir."))
        self.label_23.setText(_translate("MainWindow", "5. Vücut Kitle İndeksi hesaplama modülünü kullanırken boy metre cinsinden  örnek \' 1.75  \' şeklinde kilo kg cinsinden örnek \'88 \' veya \' 76.5\' şeklinde girilmelidir."))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#5500ff;\">MADE BY EMRE KANDAZOĞLU</span></p></body></html>"))
