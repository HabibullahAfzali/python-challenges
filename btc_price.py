import requests

def notify_me():
    
   print("Hi dear! Now it is a good price for you to buy bitcoin!")
my_good_price = {'EUR':56000,'USD':62000}
response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR')
current_price = response.json()

good_to_buy = False
for currency in my_good_price:
    if current_price[currency] <= my_good_price[currency]:
        good_to_buy = True
        break

if good_to_buy:
    notify_me()
else:
    print(f"Current Prices: USD {current_price['USD']}, EUR {current_price['EUR']}")