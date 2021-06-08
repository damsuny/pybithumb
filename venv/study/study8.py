import pybithumb
import time

con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers():
	balance = bithumb.get_balance(ticker)			# get_balance()는 비트코인의 총 잔고/거래 중인 비트코인의 수량/보유 중인 총원화/주문에 사용된 원화
	print(ticker, ":", balance)
	time.sleep(0.1)