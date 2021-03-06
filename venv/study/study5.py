import pybithumb

def bull_market(ticker):
	df = pybithumb.get_ohlcv(ticker)
	ma5 = df['close'].rolling(window=5).mean()
	last_ma5 = ma5[-2]
	price = pybithumb.get_current_price(ticker)

	if price > last_ma5:
		return True
	else:
		return False

tickers = pybithumb.get_tickers()

for ticker in tickers:
	is_bull = bull_market(ticker)
	if is_bull:												# is_bull == True
		print(ticker, "상승장 입니다.")
	else:
		print(ticker, "하락장 입니다.")

# 새로 생긴 코인이 5일치 데이터가 없어서 에러