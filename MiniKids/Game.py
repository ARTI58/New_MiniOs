def initUI(self):
	self.button_abc = QPushButton('', self.Big)
	# self.button_abc.setFlat(True)
	self.button_abc.setGeometry(584, 94, 396, 177)
	self.button_abc.clicked.connect(self.azbuca)