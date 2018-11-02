# -*- coding: utf-8 -*-

import sys 
import random
import os
import speech_recognition as sr
import random
# from pygame import mixer
from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import pygame
from pygame import mixer
import datetime
import logging
import webbrowser
import subprocess
mixer.init()
class MyGame(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		# self._recognizer = sr.Recognizer()
		# self._microphone = sr.Microphone()
		now_time = datetime.datetime.now()
		self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
		self._mp3_nameold='111'

		self.myBigWindow = QWidget()
		self.setCentralWidget(self.myBigWindow)
		self.setGeometry(0,0,1000,600)
		self.fon1 = QPushButton(self)
		self.fon1.setIcon(QIcon('C:/Users/ARTI/Desktop/SPLAYPER-master/азбука/Азбука.jpg'))
		self.fon1.setGeometry(0,0,1000,600)
		self.fon1.setIconSize(QSize(1000,600))
		self.fon1.setFlat(True)
		# ----------
		self.bukva1 = QPushButton(self)
		self.bukva1.setGeometry(15,20,112,135)
		self.bukva1.setFlat(True)
		self.bukva1.clicked.connect(self.bukva1con)
		self.bukva2 = QPushButton(self)
		self.bukva2.setGeometry(136,20,112,135)
		self.bukva2.setFlat(True)
		self.bukva2.clicked.connect(self.bukva2con)
		self.bukva3 = QPushButton(self)
		self.bukva3.setGeometry(257,20,112,135)
		self.bukva3.setFlat(True)
		self.bukva3.clicked.connect(self.bukva3con)
		self.bukva4 = QPushButton(self)
		self.bukva4.setGeometry(379,20,112,135)
		self.bukva4.setFlat(True)
		self.bukva4.clicked.connect(self.bukva4con)
		self.bukva5 = QPushButton(self)
		self.bukva5.setGeometry(500,20,112,135)
		self.bukva5.setFlat(True)
		self.bukva5.clicked.connect(self.bukva5con)
		self.bukva6 = QPushButton(self)
		self.bukva6.setGeometry(622,20,112,135)
		self.bukva6.setFlat(True)
		self.bukva6.clicked.connect(self.bukva6con)
		self.bukva7 = QPushButton(self)
		self.bukva7.setGeometry(744,20,112,135)
		self.bukva7.setFlat(True)
		self.bukva7.clicked.connect(self.bukva7con)
		self.bukva8 = QPushButton(self)
		self.bukva8.setGeometry(866,20,112,135)
		self.bukva8.setFlat(True)
		self.bukva8.clicked.connect(self.bukva8con)
		self.bukva9 = QPushButton(self)
		self.bukva9.setGeometry(15,163,112,135)
		self.bukva9.setFlat(True)
		self.bukva9.clicked.connect(self.bukva9con)
		self.bukva10 = QPushButton(self)
		self.bukva10.setGeometry(136,163,112,135)
		self.bukva10.setFlat(True)
		self.bukva10.clicked.connect(self.bukva10con)
		self.bukva11 = QPushButton(self)
		self.bukva11.setGeometry(257,163,112,135)
		self.bukva11.setFlat(True)
		self.bukva11.clicked.connect(self.bukva11con)	
		self.bukva12 = QPushButton(self)
		self.bukva12.setGeometry(379,163,112,135)
		self.bukva12.setFlat(True)
		self.bukva12.clicked.connect(self.bukva12con)
		self.bukva13 = QPushButton(self)
		self.bukva13.setGeometry(500,163,112,135)
		self.bukva13.setFlat(True)
		self.bukva13.clicked.connect(self.bukva13con)
		self.bukva14 = QPushButton(self)
		self.bukva14.setGeometry(622,163,112,135)
		self.bukva14.setFlat(True)
		self.bukva14.clicked.connect(self.bukva14con)
		self.bukva15 = QPushButton(self)
		self.bukva15.setGeometry(744,163,112,135)
		self.bukva15.setFlat(True)
		self.bukva15.clicked.connect(self.bukva15con)
		self.bukva16 = QPushButton(self)
		self.bukva16.setGeometry(866,163,112,135)
		self.bukva16.setFlat(True)
		self.bukva16.clicked.connect(self.bukva16con)
		self.bukva17 = QPushButton(self)
		self.bukva17.setGeometry(15,305,112,135)
		self.bukva17.setFlat(True)
		self.bukva17.clicked.connect(self.bukva17con)
		self.bukva18 = QPushButton(self)
		self.bukva18.setGeometry(136,305,112,135)
		self.bukva18.setFlat(True)
		self.bukva18.clicked.connect(self.bukva18con)
		self.bukva19 = QPushButton(self)
		self.bukva19.setGeometry(257,305,112,135)
		self.bukva19.setFlat(True)
		self.bukva19.clicked.connect(self.bukva19con)
		self.bukva20 = QPushButton(self)
		self.bukva20.setGeometry(379,305,112,135)
		self.bukva20.setFlat(True)
		self.bukva20.clicked.connect(self.bukva20con)
		self.bukva21 = QPushButton(self)
		self.bukva21.setGeometry(500,305,112,135)
		self.bukva21.setFlat(True)
		self.bukva21.clicked.connect(self.bukva21con)
		self.bukva22 = QPushButton(self)
		self.bukva22.setGeometry(622,305,112,135)
		self.bukva22.setFlat(True)
		self.bukva22.clicked.connect(self.bukva22con)
		self.bukva23 = QPushButton(self)
		self.bukva23.setGeometry(744,305,112,135)
		self.bukva23.setFlat(True)
		self.bukva23.clicked.connect(self.bukva23con)
		self.bukva24 = QPushButton(self)
		self.bukva24.setGeometry(866,305,112,135)
		self.bukva24.setFlat(True)
		self.bukva24.clicked.connect(self.bukva24con)
		self.bukva25 = QPushButton(self)
		self.bukva25.setGeometry(15,450,112,135)
		self.bukva25.setFlat(True)
		self.bukva25.clicked.connect(self.bukva25con)
		self.bukva26 = QPushButton(self)
		self.bukva26.setGeometry(136,450,112,135)
		self.bukva26.setFlat(True)
		self.bukva26.clicked.connect(self.bukva26con)
		self.bukva27 = QPushButton(self)
		self.bukva27.setGeometry(257,450,112,135)
		self.bukva27.setFlat(True)
		self.bukva27.clicked.connect(self.bukva27con)
		self.bukva27 = QPushButton(self)
		self.bukva27.setGeometry(379,450,65,135)
		self.bukva27.setFlat(True)
		self.bukva27.clicked.connect(self.bukva28con)
		self.bukva28 = QPushButton(self)
		self.bukva28.setGeometry(460,450,65,135)
		self.bukva28.setFlat(True)
		self.bukva28.clicked.connect(self.bukva29con)
		self.bukva29 = QPushButton(self)
		self.bukva29.setGeometry(545,450,65,135)
		self.bukva29.setFlat(True)
		self.bukva29.clicked.connect(self.bukva30con)
		self.bukva30 = QPushButton(self)
		self.bukva30.setGeometry(622,450,112,135)
		self.bukva30.setFlat(True)
		self.bukva30.clicked.connect(self.bukva31con)
		self.bukva31= QPushButton(self)
		self.bukva31.setGeometry(744,450,112,135)
		self.bukva31.setFlat(True)
		self.bukva31.clicked.connect(self.bukva32con)
		self.bukva32= QPushButton(self)
		self.bukva32.setGeometry(866,450,112,135)
		self.bukva32.setFlat(True)
		self.bukva32.clicked.connect(self.bukva33con)
		

		self.show()

	def bukva1con(self):
		self.say(str("А, Ар-буз"))
	def bukva2con(self):
		self.say(str("Б, Ба-боч-ка"))
	def bukva3con(self):
		self.say(str("В, Ви-но-град"))
	def bukva4con(self):
		self.say(str("Г, Гриб"))
	def bukva5con(self):
		self.say(str("д, Дом"))
	def bukva6con(self):
		self.say(str("Е, Е-нот"))
	def bukva7con(self):
		self.say(str("Ё, ЁЖ"))
	def bukva8con(self):
		self.say(str("Ж, Жи-раф"))
	def bukva9con(self):
		self.say(str("З, За-яц"))
	def bukva10con(self):
		self.say(str("И, Иг-ла"))
	def bukva11con(self):
		self.say(str("Й, Йо-гурт"))
	def bukva12con(self):
		self.say(str("К, Кот"))
	def bukva13con(self):
		self.say(str("Л, Ли-мон"))
	def bukva14con(self):
		self.say(str("М, Мяч"))
	def bukva15con(self):
		self.say(str("Н, Нож-ни-цы"))
	def bukva16con(self):
		self.say(str("О, Оч-ки"))
	def bukva17con(self):
		self.say(str("П, Пи-ла"))
	def bukva18con(self):
		self.say(str("Р, Ры-ба"))
	def bukva19con(self):
		self.say(str("С, Слон"))
	def bukva20con(self):
		self.say(str("Т, Те-ле-фон"))
	def bukva21con(self):
		self.say(str("У, У-лит-ка"))
	def bukva22con(self):
		self.say(str("Ф, Флаг"))
	def bukva23con(self):
		self.say(str("Х, Хлеб"))
	def bukva24con(self):
		self.say(str("Ц, Цып-ле-нок"))
	def bukva25con(self):
		self.say(str("Ч, Чай-ник"))
	def bukva26con(self):
		self.say(str("Ш, Ща-рик"))
	def bukva27con(self):
		self.say(str("Щ, щу-ка" ))
	def bukva28con(self):
		self.say(str("Ъ"))
	def bukva29con(self):
		self.say(str("Ы"))
	def bukva30con(self):
		self.say(str("Ь"))
	def bukva31con(self):
		self.say(str("Э, Экс-ка-ва-тор"))
	def bukva32con(self):
		self.say(str("Ю, Юла"))
	def bukva33con(self):
		self.say(str("Я, Яб-ло-ко"))		


		self.say(str(x))
	def say(self, phrase):
		tts = gTTS(text=phrase, lang="ru")
		tts.save(self._mp3_name)

		# Play answer
		mixer.music.load(self._mp3_name)
		mixer.music.play()
		if(os.path.exists(self._mp3_nameold)):
			os.remove(self._mp3_nameold)
	   
		now_time = datetime.datetime.now()
		self._mp3_nameold=self._mp3_name
		self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
		
		
app = QApplication(sys.argv)
my_window = MyGame()
app.exec_()
