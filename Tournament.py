from random import randint, shuffle

import Strategies
from Genetic import fitness, select, crossover, mutate
from crypto import runWork

_wins = 0
loseStreak = 0
winStreak = 0
stopCond = False
amt_ = 0.00001000

hString = ""
lString = ""
tString = ""
fString = ""
rString = ""

Stop = 0

#   Start with a random list of strategies
wkLst = list()
strategies = ["TFT", "AllHi", "AllLo", "Flip", "Rand"]
shuffle(strategies)
for x in range(0,3):
    i = randint(0, len(strategies)-1)
    #print i
    wkLst.append(strategies[i])


flpFlg = True
tftFlg = True

#   Definition for Reset()
#   To reset a whole lotta shxt
def Reset_():
    
    #reset the global string for the strategies fitness
    
    global hString
    global lString
    global tString
    global fString
    global rString
    
    hString = ""
    lString = ""
    tString = ""
    fString = ""
    rString = ""


#   Definition for BuildOffspring
#   Function to build the offspring with the result from an interation
#   First arg is result from match
#   Second arg is result from TFT
#   Third arg is result from Flip
#   Fourth arg is result from Rand
def BuildOffspring(a, b, c, d):
    global hString
    global lString
    global tString
    global fString
    
    if (a is b):
        hString += "1"
        lString += "0"
    else:
        hString += "0"
        lString += "1"
    if a is True and b is c:
        tString += "1"
    else:
        tString += "0"
    if a is True and b is d:
        fString += "1"
    else:
        fString += "0"

    return

#	Definition for Double()
#	to double whatever is given to it
def double(x):
	return x*2


while stopCond == False:
    if len(wkLst) == 0:
        #   Here I will build a dictionary with the strategy name and it's fitness
        print"Building new work"
        dct_ = {}
        dct_["TFT"] = tString
        dct_["Rand"] = rString
        dct_["Flip"] = fString
        dct_["AllHi"] = hString
        dct_["AllLo"] = lString
        
        
        #   Now we have a dictionary with the strategies and their fitness
        #   Next we call the fitness method from the Genetic class 
        #   So we can calculate the fitness and save it to dictionary
        dct__ = dict(fitness(dct_))
        #for ___ in dct__:
            #print ___, dct__[___]
        #   We now have a dictionary of the fittest strategies
        #	Next we select the fittest and save them to list
        lst_ = list(select(dct__))
        
        #   Next thing to do is perform a crossover on the list of fittest strategies
        wkLst_ = list(crossover(lst_))
        
        #   This line is to be muted and unmuted for experimental purpose
        #   Next is to perform a mutation of our strategies
        wkLst = list(mutate(wkLst_, strategies))
        
        #   Now we've updated our list of strategies to use
        #   We reset and go back into the tournament
        Reset_()
    
    #Initiate all strategies for first move
    h_ = Strategies.AllHi()
    l_ = Strategies.AllLo()
    r_ = Strategies.Rand()
    t_ = Strategies.TFT(tftFlg)
    f_ = Strategies.Flip(flpFlg)
	
	#Update the flip flag
    flpFlg = f_

    i_ = wkLst.pop()
    
    if i_ == "TFT":
        mv_ = t_
        print 'TFT running'
    if i_ == "Rand":
        mv_ = r_
        print 'Rand running'
    if i_ == "Flip":
        mv_ = f_
        print 'FLip running'
    if i_ == "AllHi":
        mv_ = h_
        print 'All Hi running'
    if i_ == "AllLo":
        mv_ = l_
        print 'All low running'
    
	print 'Click was', mv_
    
	#Now we do the clicking, get results and evaluate
    x = runWork(mv_, amt_)
	
	#Bet was a win
    if cmp(x, 1)==0:
		tftFlg = mv_
		print 'Won, keep working!\n\n'
		amt_ = 0.00001000
		_wins = _wins+1
		winStreak += 1
		#	Reset loseStreak
		loseStreak = 0
		
		if Stop == 1 or _wins > 19:
			stopCond = True
		
		BuildOffspring(True, mv_, t_, f_)

    else:
		print 'Ouch, finna double up'
		tftFlg = not mv_
		amt_ = double(amt_)
		winStreak = 0
		loseStreak = loseStreak+1
		if loseStreak > 1:
			Stop = 1
		BuildOffspring(False, mv_, t_, f_)
