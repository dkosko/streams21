import requests
from time import sleep
# 1
# for crypt in ['BTC', 'LTC', 'DASH']:
#     url = "https://bitbay.net/API/Public/{Currency[0]}{Currency[1]}/{Category}.json".format(Currency=[crypt, 'USD'],
#                                                                                             Category='trades')
#     response = requests.get(url)
#     print("Status_code : ", response.status_code)
#     print(response.json())


# 2
url = "https://bitbay.net/API/Public/{Currency[0]}{Currency[1]}/{Category}.json".format(Currency=['DASH', 'USD'],
                                                                                        Category='trades')
while 1:
    data = requests.get(url).json()  #get data from api in json format
    total_buy = 0
    total_sell = 0
    for dict in data:
        if dict['type'] == 'sell':
            total_sell += dict['price']
        elif dict['type'] == 'buy':
            total_buy += dict['price']
    sell_buy_diff = 1 - (total_sell-total_buy)/total_buy
    print("Difference between sell and buy prices = ", sell_buy_diff*100, "%")
    sleep(5)

#data = [{'date': 1400230002, 'price': 446.67, 'type': 'sell', 'amount': 0.117858, 'tid': '0'}, {'date': 1400230012, 'price': 446.67, 'type': 'sell', 'amount': 0.0823241, 'tid': '1'}, {'date': 1400230023, 'price': 446.67, 'type': 'sell', 'amount': 0.0657015, 'tid': '2'}, {'date': 1400230048, 'price': 446.59, 'type': 'sell', 'amount': 0.06795, 'tid': '3'}, {'date': 1400230111, 'price': 446.55, 'type': 'buy', 'amount': 0.17960501, 'tid': '4'}, {'date': 1400230156, 'price': 446.6, 'type': 'buy', 'amount': 0.109718, 'tid': '5'}, {'date': 1400230165, 'price': 446.6, 'type': 'buy', 'amount': 0.223914, 'tid': '6'}, {'date': 1400230332, 'price': 446.55, 'type': 'sell', 'amount': 0.32798201, 'tid': '7'}, {'date': 1400230338, 'price': 446.6, 'type': 'buy', 'amount': 0.0474541, 'tid': '8'}, {'date': 1400230375, 'price': 446.59, 'type': 'buy', 'amount': 0.37618399, 'tid': '9'}, {'date': 1400230382, 'price': 446.55, 'type': 'sell', 'amount': 0.30691701, 'tid': '10'}, {'date': 1400230428, 'price': 446.3, 'type': 'sell', 'amount': 0.0499402, 'tid': '11'}, {'date': 1400230459, 'price': 446.3, 'type': 'sell', 'amount': 0.063362, 'tid': '12'}, {'date': 1400230476, 'price': 446.3, 'type': 'sell', 'amount': 0.0562178, 'tid': '13'}, {'date': 1400230608, 'price': 446.29, 'type': 'sell', 'amount': 0.13658801, 'tid': '14'}, {'date': 1400230664, 'price': 446.31, 'type': 'buy', 'amount': 0.85142601, 'tid': '15'}, {'date': 1400230684, 'price': 446.31, 'type': 'buy', 'amount': 0.123233, 'tid': '16'}, {'date': 1400230696, 'price': 446.29, 'type': 'sell', 'amount': 0.40727001, 'tid': '17'}, {'date': 1400230708, 'price': 446.29, 'type': 'sell', 'amount': 0.0658345, 'tid': '18'}, {'date': 1400230816, 'price': 446.31, 'type': 'buy', 'amount': 0.0974883, 'tid': '19'}, {'date': 1400230875, 'price': 446.29, 'type': 'sell', 'amount': 0.55380702, 'tid': '20'}, {'date': 1400230969, 'price': 446.31, 'type': 'buy', 'amount': 0.15532599, 'tid': '21'}, {'date': 1400231018, 'price': 446.29, 'type': 'buy', 'amount': 0.834243, 'tid': '22'}, {'date': 1400231063, 'price': 446.59, 'type': 'buy', 'amount': 0.0837031, 'tid': '23'}, {'date': 1400231121, 'price': 446.99, 'type': 'buy', 'amount': 0.354314, 'tid': '24'}, {'date': 1400231224, 'price': 446.64, 'type': 'buy', 'amount': 0.43353301, 'tid': '25'}, {'date': 1400231238, 'price': 447.7, 'type': 'buy', 'amount': 0.0695504, 'tid': '26'}, {'date': 1400231254, 'price': 446.18, 'type': 'sell', 'amount': 0.0786383, 'tid': '27'}, {'date': 1400231262, 'price': 446.18, 'type': 'sell', 'amount': 0.199119, 'tid': '28'}, {'date': 1400231272, 'price': 446.18, 'type': 'sell', 'amount': 0.0564867, 'tid': '29'}, {'date': 1400231286, 'price': 447.9, 'type': 'buy', 'amount': 0.0510159, 'tid': '30'}, {'date': 1400231296, 'price': 446.18, 'type': 'sell', 'amount': 0.246426, 'tid': '31'}, {'date': 1400231306, 'price': 446.18, 'type': 'sell', 'amount': 0.12941, 'tid': '32'}, {'date': 1400232643, 'price': 448.08, 'type': 'buy', 'amount': 0.30946401, 'tid': '33'}, {'date': 1400232789, 'price': 448.14, 'type': 'buy', 'amount': 0.111572, 'tid': '34'}, {'date': 1400233113, 'price': 446.11, 'type': 'sell', 'amount': 0.0895814, 'tid': '35'}, {'date': 1400235739, 'price': 446.69, 'type': 'sell', 'amount': 0.0517398, 'tid': '36'}, {'date': 1400235781, 'price': 446.69, 'type': 'sell', 'amount': 0.124217, 'tid': '37'}, {'date': 1400235851, 'price': 446.9, 'type': 'buy', 'amount': 0.0490042, 'tid': '38'}, {'date': 1400235932, 'price': 446.9, 'type': 'buy', 'amount': 0.0540433, 'tid': '39'}, {'date': 1400235969, 'price': 446.7, 'type': 'sell', 'amount': 0.39539701, 'tid': '40'}, {'date': 1400236026, 'price': 446.7, 'type': 'sell', 'amount': 0.101232, 'tid': '41'}, {'date': 1400236106, 'price': 446.7, 'type': 'sell', 'amount': 0.943371, 'tid': '42'}, {'date': 1400236160, 'price': 446.9, 'type': 'buy', 'amount': 1.62143004, 'tid': '43'}, {'date': 1400242237, 'price': 447.56, 'type': 'buy', 'amount': 0.101455, 'tid': '44'}, {'date': 1400242280, 'price': 447.05, 'type': 'sell', 'amount': 0.116085, 'tid': '45'}, {'date': 1400242290, 'price': 447.05, 'type': 'sell', 'amount': 0.0863228, 'tid': '46'}, {'date': 1400242303, 'price': 447.05, 'type': 'sell', 'amount': 0.378775, 'tid': '47'}, {'date': 1400242310, 'price': 447.9, 'type': 'buy', 'amount': 0.15842301, 'tid': '48'}, {'date': 1400242335, 'price': 447.05, 'type': 'sell', 'amount': 0.123985, 'tid': '49'}]



