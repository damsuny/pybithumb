import pybithumb

all = pybithumb.get_current_price("ALL")		# 정보를 얻을 수 있는 모든 가상화폐의 가격정보를 받아옵니다.
for k, v in all.items():						# items()는 for문을 통해 key, value 값을 얻을 수 있다.
	print(k, v)

# key 설명
# opening_price : 00시 기준 시가
# closing_price : 00시 기준 종가
# min_price : 00시 기준 저가
# max_price : 00시 기준 고가
# units_traded : 00시 기준 거래량
# acc_trade_value : 00시 기준 거래금액
# prev_closing_price : 전일 종가
# units_traded_24H : 최근 24시간 거래량
# acc_trade_value_24H : 최근 24시간 거래금액
# fluctate_24H : 최근 24시간 변동가
# fluctate_rate_24H : 최근 24시간 변동률

print('-'*200)

for ticker, data in all.items():				# 현재가(종가) 출력
	print(ticker, data['closing_price'])