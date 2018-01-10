import random


#   Strategy definition for All Hi's
#   Always click's a Hi
def AllHi():
    return True


#   Strategy definition for AllLo
#   Always click's a Low
def AllLo():
    return False


#   Strategy definition for Tit-For-Tat
#   Input: A boolean representing opponent's previous move
#   Output: Opponent's previous move
def TFT(x):
    if x==True:
        return True
    if x==False:
        return False


#   Strategy definition for Flip
#   Always does the opposite of what it did in the previous move
#   Input: The strategy's previous move
#   Output: The opposite of the input
def Flip(x):
    if x==True:
        return False
    if x==False:
        return True


#   Strategy definition for Random
#   Returns a True of False Randomly chosen
def Rand():
    i = random.randint(0, 9990909039403940390)+1
    if i%2==0:
        return True
    if i%2==1:
        return False
