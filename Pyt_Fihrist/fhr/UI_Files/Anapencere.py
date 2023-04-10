# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anapencere.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import fhr.UI_Files.fih_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 723)
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnKisiler = QtWidgets.QPushButton(self.centralwidget)
        self.btnKisiler.setMaximumSize(QtCore.QSize(32, 32))
        self.btnKisiler.setObjectName("btnKisiler")
        self.horizontalLayout.addWidget(self.btnKisiler)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.btnAyarlar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAyarlar.setMaximumSize(QtCore.QSize(60, 32))
        self.btnAyarlar.setIconSize(QtCore.QSize(30, 30))
        self.btnAyarlar.setObjectName("btnAyarlar")
        self.horizontalLayout.addWidget(self.btnAyarlar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabKontrol = QtWidgets.QTabWidget(self.centralwidget)
        self.tabKontrol.setStyleSheet("")
        self.tabKontrol.setDocumentMode(False)
        self.tabKontrol.setTabBarAutoHide(False)
        self.tabKontrol.setObjectName("tabKontrol")
        self.tab_Kisiler = QtWidgets.QWidget()
        self.tab_Kisiler.setObjectName("tab_Kisiler")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_Kisiler)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_Kisiler)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabKontrol.addTab(self.tab_Kisiler, "")
        self.tab_Ayarlar = QtWidgets.QWidget()
        self.tab_Ayarlar.setObjectName("tab_Ayarlar")
        self.comboBox = QtWidgets.QComboBox(self.tab_Ayarlar)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.chckBox_Lokal = QtWidgets.QCheckBox(self.tab_Ayarlar)
        self.chckBox_Lokal.setGeometry(QtCore.QRect(180, 30, 76, 20))
        self.chckBox_Lokal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chckBox_Lokal.setChecked(True)
        self.chckBox_Lokal.setTristate(False)
        self.chckBox_Lokal.setObjectName("chckBox_Lokal")
        self.chckBox_Server = QtWidgets.QCheckBox(self.tab_Ayarlar)
        self.chckBox_Server.setGeometry(QtCore.QRect(180, 50, 76, 20))
        self.chckBox_Server.setObjectName("chckBox_Server")
        self.chckBox_Loglama = QtWidgets.QCheckBox(self.tab_Ayarlar)
        self.chckBox_Loglama.setGeometry(QtCore.QRect(290, 30, 75, 20))
        self.chckBox_Loglama.setStyleSheet("")
        self.chckBox_Loglama.setObjectName("chckBox_Loglama")
        self.layoutWidget = QtWidgets.QWidget(self.tab_Ayarlar)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 231, 146))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.txtKod = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtKod.setMaximumSize(QtCore.QSize(60, 16777215))
        self.txtKod.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"     selection-background-color: darkgray;\n"
"}")
        self.txtKod.setText("")
        self.txtKod.setObjectName("txtKod")
        self.horizontalLayout_5.addWidget(self.txtKod)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.txtInstance = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtInstance.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"     selection-background-color: darkgray;\n"
"}")
        self.txtInstance.setText("")
        self.txtInstance.setObjectName("txtInstance")
        self.horizontalLayout_6.addWidget(self.txtInstance)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.txtServer = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtServer.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"     selection-background-color: darkgray;\n"
"}")
        self.txtServer.setText("")
        self.txtServer.setObjectName("txtServer")
        self.horizontalLayout_7.addWidget(self.txtServer)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.txtKullanici = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtKullanici.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"     selection-background-color: darkgray;\n"
"}")
        self.txtKullanici.setText("")
        self.txtKullanici.setObjectName("txtKullanici")
        self.horizontalLayout_8.addWidget(self.txtKullanici)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.txtSifre = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtSifre.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"     selection-background-color: darkgray;\n"
"}")
        self.txtSifre.setText("")
        self.txtSifre.setObjectName("txtSifre")
        self.horizontalLayout_9.addWidget(self.txtSifre)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_Ayarlar)
        self.layoutWidget1.setGeometry(QtCore.QRect(290, 80, 111, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chckBox_Veritabani = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chckBox_Veritabani.setObjectName("chckBox_Veritabani")
        self.verticalLayout_3.addWidget(self.chckBox_Veritabani)
        self.chckBox_SQLite = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chckBox_SQLite.setObjectName("chckBox_SQLite")
        self.verticalLayout_3.addWidget(self.chckBox_SQLite)
        self.chckBox_Text = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chckBox_Text.setObjectName("chckBox_Text")
        self.verticalLayout_3.addWidget(self.chckBox_Text)
        self.chckBox_Mail = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chckBox_Mail.setObjectName("chckBox_Mail")
        self.verticalLayout_3.addWidget(self.chckBox_Mail)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_Ayarlar)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 240, 416, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnBaglan = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnBaglan.setMinimumSize(QtCore.QSize(37, 18))
        self.btnBaglan.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/connected-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBaglan.setIcon(icon)
        self.btnBaglan.setObjectName("btnBaglan")
        self.horizontalLayout_10.addWidget(self.btnBaglan)
        self.btnVeritabani = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnVeritabani.setMinimumSize(QtCore.QSize(37, 18))
        self.btnVeritabani.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/database-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVeritabani.setIcon(icon1)
        self.btnVeritabani.setObjectName("btnVeritabani")
        self.horizontalLayout_10.addWidget(self.btnVeritabani)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnSil.setMinimumSize(QtCore.QSize(37, 18))
        self.btnSil.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/delete-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSil.setIcon(icon2)
        self.btnSil.setObjectName("btnSil")
        self.horizontalLayout_10.addWidget(self.btnSil)
        self.btnEkle = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnEkle.setMinimumSize(QtCore.QSize(37, 18))
        self.btnEkle.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/add-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEkle.setIcon(icon3)
        self.btnEkle.setObjectName("btnEkle")
        self.horizontalLayout_10.addWidget(self.btnEkle)
        self.btnKaydet = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnKaydet.setMinimumSize(QtCore.QSize(37, 18))
        self.btnKaydet.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/save-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnKaydet.setIcon(icon4)
        self.btnKaydet.setObjectName("btnKaydet")
        self.horizontalLayout_10.addWidget(self.btnKaydet)
        self.brnCikis = QtWidgets.QPushButton(self.layoutWidget2)
        self.brnCikis.setMinimumSize(QtCore.QSize(37, 18))
        self.brnCikis.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/exit-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brnCikis.setIcon(icon5)
        self.brnCikis.setObjectName("brnCikis")
        self.horizontalLayout_10.addWidget(self.brnCikis)
        self.txtcdid = QtWidgets.QLineEdit(self.tab_Ayarlar)
        self.txtcdid.setGeometry(QtCore.QRect(260, 190, 41, 22))
        self.txtcdid.setObjectName("txtcdid")
        self.tabKontrol.addTab(self.tab_Ayarlar, "")
        self.horizontalLayout_3.addWidget(self.tabKontrol)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabKontrol.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnKisiler.setText(_translate("MainWindow", "....."))
        self.pushButton_2.setText(_translate("MainWindow", "....."))
        self.pushButton_5.setText(_translate("MainWindow", "....."))
        self.pushButton_3.setText(_translate("MainWindow", "....."))
        self.btnAyarlar.setText(_translate("MainWindow", "Ayarlar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        self.tabKontrol.setTabText(self.tabKontrol.indexOf(self.tab_Kisiler), _translate("MainWindow", "Kisiler"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ms Sql"))
        self.comboBox.setItemText(1, _translate("MainWindow", "My Sql"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Sq Lite"))
        self.chckBox_Lokal.setText(_translate("MainWindow", "Lokal"))
        self.chckBox_Server.setText(_translate("MainWindow", "Server"))
        self.chckBox_Loglama.setText(_translate("MainWindow", "Loglama"))
        self.label.setText(_translate("MainWindow", "Kodu"))
        self.label_2.setText(_translate("MainWindow", "Instance"))
        self.label_3.setText(_translate("MainWindow", "Server"))
        self.label_4.setText(_translate("MainWindow", "Kullanici"))
        self.label_5.setText(_translate("MainWindow", "Sifre"))
        self.chckBox_Veritabani.setText(_translate("MainWindow", "Veritabani"))
        self.chckBox_SQLite.setText(_translate("MainWindow", "SQ Lite"))
        self.chckBox_Text.setText(_translate("MainWindow", "Text"))
        self.chckBox_Mail.setText(_translate("MainWindow", "Mail"))
        self.tabKontrol.setTabText(self.tabKontrol.indexOf(self.tab_Ayarlar), _translate("MainWindow", "Ayarlar"))
    
