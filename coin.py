
import requests
import json


global_url = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=100&currency=EUR'


response = requests.get(global_url)

result = response.json()

#===show pure json
#print(result)


#===show json tree 
ordered_result=(json.dumps(result, sort_keys=True, indent=4))
#print(ordered_result)


#===storing datas from json, important not from json tree==
all_coins = result['coins']
#print(all_coins)




#===getting speciefied datas from coins 

list_names = []
list_prices = []
list_marketCaps = []
list_pricesChange1d = []

for x in all_coins:
	
	#===going throw pure json data
	name = x['name']
	price = x['price']
	marketCap = x['marketCap']

	
	#===rounding pure json data

	round_price = round(price,3)
	round_marketCap = round(marketCap,2)
	

	#===add datas to the lists

	list_names.append(name)
	list_prices.append(round_price)
	list_marketCaps.append(round_marketCap)
	
	#===if you want to store more datas, ceck jason tree and put it here



#===printing finished datas in terminal
	
""" print("         ")
	print(list_names)
	print("         ")
	print(list_prices)
	print("         ")
	print(list_marketCaps)"""

	
#===Convert datas back to json

json_names = json.dumps(list_names)
json_price = json.dumps(list_prices)
json_marketCaps = json.dumps(list_marketCaps)


print(json_names)
print("         ")
print(json_price)
print("         ")
print(json_marketCaps)


#===creating a file and store json data in this file 

name_data = open("name_data.txt", "w")
price_data = open("price_data.txt", "w")
marketCap_data = open("marketCap_data.txt", "w")

name_data.write(json_names)
price_data.write(json_price)
marketCap_data.write(json_marketCaps)


