# dayDayUpQ2.py
dayFactor = 0.005
dayUp = pow(1 + dayFactor, 365)
dayDown = pow(1 - dayFactor, 365)
print('天天向上的力量 : {:.2f}, 天天向下的力量 : {:.2f}'.format(dayUp, dayDown))