import datetime

import pybithumb

orderbook = pybithumb.get_orderbook("BTC")			# 호가정보를 가져 옵니다.
print(orderbook)

ms = int(orderbook['timestamp'])					# 타임스탬프가 문자형으로 되어 있기 때문에 정수형으로 변경
dt = datetime.datetime.fromtimestamp(ms/1000)		# 시간이 ms(밀리세컨드)단위 이기 때문에 s(세컨드)로 바꿔 보기 좋은 형태로 바꾼다.
print(dt)

bids = orderbook['bids']
for bid in bids:
	price = bid['price']
	quant = bid['quantity']
	print("매수호가: ", price, "매수잔량: ", quant)

asks = orderbook['asks']
for ask in asks:
	price = ask['price']
	quant = ask['quantity']
	print("매도호가: ", price, "매도잔량: ", quant)

# for k in orderbook:									# orderbook의 인덱스를 알아본다.
# 	print(k)
# for 문 결과
# timestamp					# 코드 실행 시간
# payment_currency			# 거래 시 지불 화폐 (빗썸이 가상화폐 거래 시 원화 결제만 하기 때문에 고정적이다.)
# order_currency			# 선택한 코인 종류
# bids						# 매수호가
# asks						# 매도호가