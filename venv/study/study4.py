import pybithumb

btc = pybithumb.get_ohlcv("BTC")				# 날짜별 00시 기준 시가/고가/저가/종가/거래량이 저장된 dataframe을 가져옵니다.
close = btc['close']							# 날짜별 종가를 가져옵니다.(dataframe > series)

ma5 = close.rolling(5).mean()					# rolling() 메소드를 사용해 5일 단위로 그룹화하여 평균을 구합니다.
# print(ma5)

last_ma5 = ma5[-2]								# 최근 5일 이동평균 가격

price = pybithumb.get_current_price("BTC")		# 현재 가격

if price > last_ma5:							# 현재 가격이 5일 이동평균 가격보다 높으면 상승장이라고 판단합니다.
	print("상승장 입니다.")
else:											# 현재 가격이 5일 이동평균 가격보다 낮으면 하락장이라고 판단합니다.
	print("하락장 입니다.")