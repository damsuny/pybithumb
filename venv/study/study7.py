import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb
import time

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("bull.ui")[0]						# bull.ui 를 불러옵니다.

class Worker(QThread):
	finished = pyqtSignal(dict)

	def run(self):
		while True:
			data = {}

			for ticker in tickers:								# 코이별 종가/5일 이동평균/상태를 가져옵니다.
				data[ticker] = self.get_market_infos(ticker)

			self.finished.emit(data)
			time.sleep(2)

	def get_market_infos(self, ticker):
		try:
			df = pybithumb.get_ohlcv(ticker)
			ma5 = df['close'].rolling(window=5).mean()
			last_ma5 = ma5[-2]
			price = pybithumb.get_current_price(ticker)

			state = None
			if price > last_ma5:								# 현재 장상태 파악
				state = "상승장"
			else:
				state = "하락장"

			return price, last_ma5, state

		except:
			return None, None, None

class MyWindow(QMainWindow, form_class):						# 클래스를 만듭니다. QMainWindow, form_class 를 상속 받습니다.
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.worker = Worker()
		self.worker.finished.connect(self.update_table_widget)	# finished 시그널이 나오면 self.update_table_widget()호출
		self.worker.start()

	@pyqtSlot(dict)												# 딕셔너리 객체가 받을 수 있는 슬롯 지정
	def update_table_widget(self, data):
		try:
			for ticker, infos in data.items():					# data가 딕셔너리 형태이기 때문에 ticker, infos를 가져옵니다.(key, value)
				index = tickers.index(ticker)					# tickers 에서 ticker에 해당하는 정보를 가져옵니다.

				self.tableWidget.setItem(index, 0, QTableWidgetItem(ticker))
				self.tableWidget.setItem(index, 1, QTableWidgetItem(str(infos[0])))
				self.tableWidget.setItem(index, 2, QTableWidgetItem(str(infos[1])))
				self.tableWidget.setItem(index, 3, QTableWidgetItem(str(infos[2])))

		except:
			pass

app = QApplication(sys.argv)
win = MyWindow()												# 객체를 생성합니다.
win.show()														# 객체를 보여줍니다.
app.exec_()