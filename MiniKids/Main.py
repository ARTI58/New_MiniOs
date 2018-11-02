# -*- coding: utf-8 -*-

import sys 
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QBasicTimer
from sys import stdin, exit as sys_exit
import Game

class Change(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# self.fon = QPushButton('', self)
		# self.fon.setIcon(QIcon('Фон/Программа.jpg'))
		# self.fon.setGeometry(0,0,1280,720)
		# self.fon.setIconSize(QSize(1280,720))
		self.Big = QWidget()
# #------------------------------------------------------------
# 		self.button_abc = QPushButton('', self.Big)
# 		self.button_abc.setFlat(True)
# 		self.button_abc.setGeometry(584, 94, 396, 177)
# 		self.button_abc.clicked.connect(self.azbuca)

# 		self.button_tetris = QPushButton('', self.Big)
# 		self.button_tetris.setFlat(True)
# 		self.button_tetris.setGeometry(300, 498, 401, 195)
# 		self.button_tetris.clicked.connect(self.tetris)

# 		self.buttont_zmeyka = QPushButton('', self.Big)
# 		self.buttont_zmeyka.setFlat(True)
# 		self.buttont_zmeyka.setGeometry(300, 282, 128, 205)
# 		self.buttont_zmeyka.clicked.connect(self.zmeyka)

# 		self.button_car = QPushButton('', self.Big)
# 		self.button_car.setFlat(True)
# 		self.button_car.setGeometry(713, 541, 268, 153)
# 		self.button_car.clicked.connect(self.Car)

		self.buttont_otvet = QPushButton('', self.Big)
		self.buttont_otvet.setGeometry(22, 95, 266, 254)
		# self.buttont_otvet.setFlat(True)
		# self.buttont_otvet.clicked.connect(self.Otvethic)


# 		self.button_calculator = QPushButton('', self.Big)
# 		self.button_calculator.setFlat(True)
# 		self.button_calculator.setGeometry(991, 95, 266, 332)
# 		self.button_calculator.clicked.connect(self.calcutor)

# # 		self.Button_sms = QPushButton('', self.Big)
# # 		self.Button_sms.setIcon(QIcon("Фото/sms.png"))
# # 		self.Button_sms.setFlat(True)
# # 		self.Button_sms.setGeometry(865, 225, 180, 180)
# # 		self.Button_sms.setIconSize(QSize(180, 180))
# # 		# self.Button_sms.clicked.connect(self.sms)

		self.button_exit = QPushButton('', self.Big)
		# self.button_exit.setFlat(True)
		self.button_exit.setGeometry(1125, 29, 130, 51)
		self.button_exit.clicked.connect(self.fon_exit)
# #-------------------------------------------------------------------Выход
# 		self.exx = QWidget()
# 		self.fon = QPushButton('', self.exx)
# 		self.fon.setIcon(QIcon('фон/Выход.jpg'))
# 		self.fon.setGeometry(0,0,1280,720)
# 		self.fon.setIconSize(QSize(1280,720))

# 		self.loginInput = QLineEdit(self.exx)
# 		self.loginInput.move(562, 380)

# 		self.button = QPushButton('Выйти', self.exx)
# 		self.button.setIconSize(QSize(120, 40))
# 		self.button.setGeometry(535,420,190,50)
# 		self.button.clicked.connect(self.exit)

# 		self.button = QPushButton('Назад', self.exx)
# 		self.button.setIconSize(QSize(120, 40))
# 		self.button.setGeometry(560,480,140,40)
# 		self.button.clicked.connect(self.nazad2)
# 		self.setCentralWidget(self.Big)

# #------------------------------------------------------------------------
		self.setGeometry(0,0, 1280, 720)
		self.setWindowTitle('MiniKids')
		self.show()
# #------------------------------------------------------------------------


# 	def zmeyka(self):
# 		os.system('python Игры/Змейка.py')

# 	def tetris(self):
# 		os.system('python Игры/Тетрис.py')

# 	def Otvethic(self):
# 		os.system('py Ответчик/Ответчик.py')

# 	def calcutor(self):
# 		os.system('py Канкулятор/calkulator.py')

	# def azbuca(self):
	# 	os.system('py азбука/alpha.py')	

	def fon_exit(self):
		self.setCentralWidget(self.exx)

# 	def nazad2(self):
# 		os.system('py main.py')
# 		sys_exit()	

# 	def Car(self):
# 		os.system('python Игры/game.py')		
		
	def exit(self):
		if self.loginInput.text() == '1':
			sys_exit() 	
		if self.loginInput.text() != '1':
			os.system('py main.py')
			sys_exit()	

									


		



app = QApplication(sys.argv)
my_window = Change()
# my_window.showFullScreen()   # На весь экран
app.exec_() 