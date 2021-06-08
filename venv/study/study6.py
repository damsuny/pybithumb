# 먼저 PyQt5 모듈을 이용합니다. 그리고 터미널에서 design을 입력해 디자인한 파일을 사용합니다.
import sys

import pybithumb
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("bull.ui")[0]			# bull.ui 를 불러옵니다.

class MyWindow(QMainWindow, form_class):			# 클래스를 만듭니다. QMainWindow, form_class 를 상속 받습니다.
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		timer = QTimer(self)
		timer.start(5000)							# 5초마다 실행합니다.
		timer.timeout.connect(self.timeout)			# timeout을 불러와 연결합니다.

	def get_market_infos(self, ticker):
		df = pybithumb.get_ohlcv(ticker)
		ma5 = df['close'].rolling(window=5).mean()
		last_ma5 = ma5[-2]
		price = pybithumb.get_current_price(ticker)

		state = None
		if price > last_ma5:						# 현재 상태 파악
			state = "상승장"
		else:
			state = "하락장"

		return price, last_ma5, state

	def timeout(self):								# timeout을 정의합니다.
		for i, ticker in enumerate(tickers):
			item = QTableWidgetItem(ticker)										# 현재 ticker(코인의 이름)을 가져옵니다.
			self.tableWidget.setItem(i, 0, item)								# 코인 이름을 윈도우에 띄웁니다.
			price, last_ma5, state = self.get_market_infos(ticker)				# 다른 정보(종가/5일 이동평균/상태)를 불러옵니다.
			self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))		# 종가(현재가)를 윈도우에 띄웁니다.
			self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))		# 5일 이동평균을 윈도우에 띄웁니다.
			self.tableWidget.setItem(i, 3, QTableWidgetItem(state))				# 상태를 윈도우에 띄웁니다.

app = QApplication(sys.argv)
win = MyWindow()									# 객체를 생성합니다.
win.show()											# 객체를 보여줍니다.
app.exec_()