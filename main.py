import requests

my_good_price = 12361.3

def inform_morti():
  print("Salam price is good to buy")
  #API_key = ""
  #Url = " ****** %s *****" %API_key
  #payload ={"reseptor":"******", "message": "price is as low as %i" %price}
  #reponse = requests.post(Url, data=payload)
  #print(response)

response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")

price = (float(response.json() ["data"]["amount"]))

if (price < my_good_price):
  inform_morti()

else:
  print("No, its not yet")

print (price)