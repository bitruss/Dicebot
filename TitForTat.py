"""
Simple bot for betting using the Tit For Tat method
"""
import requests
import json
import random
import string


#Some global variables here
profit_ = 0
betAmount_ = 0.00001000
payout_ = 2.0
flag_ = True        #True bets over 5x.x, False bets under 4x.x
url_ = "https://api.crypto-games.net/v1/placebet/LTC/xxxYourAPIHerexxx"
headers = {'Content-Type': 'application/json'}
numWins_ = 0        #Keep track of how many wins we have 
winStreak_ = 0
stopCond_ = 0
loseStreak_ = 0
curLose_ = 0

"""
    Function definition for getSeed()
    To generate a random seed on each bet to ensure a fair bet
"""
def getSeed():
    _mixer = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.sample(_mixer, 40))
 
"""
=======================================================================
    Function definition for win()
    A boolean function that returns True if bet is won, false otherwise
=======================================================================
"""
def win():
    if profit_ > 0:
        return True
    else:
        return False



def double_(x):
    return x*2



while stopCond_ < 10:
    _seed = getSeed()
    print(_seed)

    parameter = {"Bet": betAmount_, "Payout":payout_, "UnderOver": flag_, "ClientSeed": _seed}
    parameters = json.dumps(parameter)
    _r = requests.post(url_, data = parameters, headers=headers)
    r_ = json.loads(_r.content)
    profit_ = r_['Profit']
    if (win()):
        betAmount_ = 0.00002000
        if flag_:
            flag_ = True
        else:
            flag_ = False
        print "Won!, Betting again"
        numWins_ += 1
        stopCond_ += 1
        curLose_ = 0
        if numWins_ > winStreak_:
            winStreak_ = numWins_

    else:
        print "Loss, doubling up and going harder!"
        curLose_ += 1
        if curLose_ > loseStreak_:
            loseStreak_ = curLose_
        betAmount_ = double_(betAmount_)
        #Switch flag_
        if flag_:
            flag_ = False
        else:
            flag_ = True
        numWins_ = 0
        
print "Win streak: ",winStreak_
print "Losing streak: ",loseStreak_
