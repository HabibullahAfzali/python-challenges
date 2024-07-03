import requests
#function to notify whenever the price meet the favorable condition(my_good_price)
def notify_me():
   print("Hi dear! Now it is a good price for you to buy bitcoin!")
   
my_good_price = {'EUR':56000,'USD':62000}
#Call to real time crypto price 
response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR')

#Extrct the data value from response as json
current_price = response.json()

#Conditional boolean variable
good_to_buy = False

# Checks and Campare the Current price with Favorable price
for currency in my_good_price:
    if current_price[currency] <= my_good_price[currency]:
        good_to_buy = True
        break
#If the the price meet it calls notify fuction, otherwise print the currect price
if good_to_buy:
    notify_me()
else:
    print(f"Current Prices: USD {current_price['USD']}, EUR {current_price['EUR']}")