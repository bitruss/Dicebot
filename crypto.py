import requests
import json
import random
import string
from random import shuffle

"""
    Function definition for getSeed()
    To generate a random seed on each bet to ensure a fair bet
"""
def getSeed():
    _mixer = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.sample(_mixer, 40))
 

def runWork(move, _price):
    url_ = "https://api.crypto-games.net/v1/placebet/CURRENCY/xxxxYourAPIHerexxxx"
    headers = {'Content-Type': 'application/json'}
	
    _seed = getSeed()
        
    parameter = {"Bet": _price, "Payout": 2.0, "UnderOver": move, "ClientSeed": _seed}
    parameters = json.dumps(parameter)
    _r = requests.post(url_, data = parameters, headers=headers)
    r_ = json.loads(_r.content)
    #print(r_)
    profit_ = r_['Profit']
    if profit_ > 0:
    	return 1
    else:
    	return 0
