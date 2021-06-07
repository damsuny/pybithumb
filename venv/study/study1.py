import pybithumb
import time

# tickers = pybithumb.get_tickers()				# 모듈에서 정보를 제공하는 코인을 불러옵니다.
# print(tickers)									# 코인의 종류(코드)를 출력합니다.
# print(len(tickers))								# 정보를 제공하는 코인의 갯수를 출력합니다.

# while True:
# 	price = pybithumb.get_current_price("BTC")		# 비트코인의 현재가격을 불러옵니다.
# 	print(price)									# 가져온 비트코인의 현재가격을 출력합니다.
# 	time.sleep(1)									# 1초에 한 번씩 실행합니다.

# for ticker in tickers:							# 코인의 종류별로 현재가격 알아봅니다.
# 	price = pybithumb.get_current_price(ticker)		# 선택 된 코인의 현재 가격을 불러옵니다.
# 	print(ticker, price)							# 코인의 종류와 현재 가격을 출력합니다.
# 	time.sleep(0.1)									# 0.1초 간격을 두고 실행합니다. (공개 API를 이용하는데, 1초에 약 95회 이상 요청하면 블럭되기 때문에 시간차 사용)

# detail = pybithumb.get_market_detail("BTC")			# get_market_detail은 시가, 고가, 저가, 종가(현재가), 거래량을 가져옵니다.
# print(detail)