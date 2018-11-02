import smtplib, sys
from email.mime.text import MIMEText
from email.header import Header
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
class Change(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		self.fon = QPushButton('', self)
		self.fon.setIcon(QIcon('Фон.jpg'))
		self.fon.setGeometry(0,0,1366,768)
		self.fon.setIconSize(QSize(1366,768))

		self.fon = QPushButton('', self)
		self.fon.setIcon(QIcon('ma.png'))
		self.fon.setGeometry(30,0,225,247)
		self.fon.setIconSize(QSize(225,247))

		self.myMom = QWidget()
		self.myCheck = QWidget()
		self.textformyCheck = QLabel('Введите код,пришедший вам на почту(У ВАС 1 МИНУТА(Артур,добавишь таймер сам))',self.myCheck)
		self.checkformyCheck = QLineEdit(self.myCheck)
		self.textformyCheck.move(50,90)
		self.checkformyCheck.move(50,110)
		self.checkbuton = QPushButton('Проверить',self.myCheck)
		self.textcheckbuton = QLabel('',self.myCheck)
		self.textcheckbuton.move(50,110)
		self.checkbuton.move(50,130)
		self.checkbuton.clicked.connect(self.myTry)

		nameText = QLabel('Введите почту', self.myMom)
		self.primerText = QLabel('Пример почты: \n \n user.123@mail.ru', self.myMom)
		nameText.move(50, 50)
		self.primerText.move(150,10)
		self.log = QLineEdit(self.myMom)
		self.log.move(50, 70)
		surnameText = QLabel('Введите пароль', self.myMom)
		surnameText.move(50, 90)
		self.password = QLineEdit(self.myMom)
		self.password.move(50, 110)
		self.setCentralWidget(self.myMom)
		self.registbutton = QPushButton('Зарегистрироваться',self.myMom)
		self.registbutton.move(50, 135)
		self.registbutton.clicked.connect(self.setForm) #------------------------------------------------------------------
		self.vhodbutton = QPushButton('Войти',self.myMom)
		self.vhodbutton.move(50, 165)
		self.vhodbutton.clicked.connect(self.checkForm)
		# x = 'Hn3jAr'
		self.setCentralWidget(self.myMom)
		self.show()
		self.setGeometry(0,0,1280,720)
	def checkForm(self):
		pass
	def setForm(self):
		# conn = sqlite3.connect('myfile.db')
		# cursor = conn.cursor()
		# cursor.execute('DROP TABLE users')
		# cursor.execute("""CREATE TABLE users
		# 	(login VARCHAR(30),
		# 	password VARCHAR(30))
		# 	""")
		# print(cursor.fetchall())
		# query = """INSERT INTO users (login, password)
		# VALUES (?, ?)"""
		# cursor.execute(query, (self.log.text(), self.password.text()))
		# conn.commit()
		# self.log.setText('')
		# self.password.setText('')
		# cursor.close()
		# conn.close()
		self.setCentralWidget(self.myCheck)
		self.mailsender()
	def myTry(self):
		if self.checkformyCheck.text() == 'Hn3jAr':
			os.system('python3 Main.py')
		else:
			self.textcheckbuton.setText('НЕВЕРНО')
			exit()			
	def mailsender(self):
		# x = random.choice(['Hn3jAr', 'J013fA4', 'aq3BA5'])
		x = 'Hn3jAr'
		f =  self.log.text()
		mail_sender = f
		mail_receiver = f
		username = f
		password = 'omar090910'
		server = smtplib.SMTP('smtp.mail.ru:587')
		subject = u'Тестовый email от'
		body = 'Ваш уникальный код: '+ x
		msg = MIMEText(body, 'plain', 'utf-8')
		msg['Subject'] = Header(subject, 'utf-8')
		server.starttls()
		server.ehlo()
		server.login(username,password)	
		server.sendmail(mail_sender, mail_receiver, msg.as_string())
		server.quit()
app = QApplication(sys.argv)
my_window = Change()
my_window.showFullScreen()

app.exec_()
