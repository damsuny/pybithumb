# 먼저 PyQt5 모듈을 이용합니다. 그리고 터미널에서 design을 입력해 디자인한 파일을 사용합니다.
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("bull.ui")[0]

class MyWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

app = QApplication(sys.argv)
win = MyWindow()
win.show()