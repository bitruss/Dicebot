from random import randint, shuffle

"""
	Function definition for fitness()
	Input: 	A dictionary of strategies and their fitness string
	Output:	A dictionary of strategy names with their calculated fitness
"""
def fitness(dct_):
 	#First thing is for each strategy, calculated the fitness
 	#and put them into a new dictionary
 	retDct_ = {}
 	for _ in dct_:
 		fitn = 0
 		name_ = _
 		_fit = dct_[_]
 		for __ in _fit:
 			if cmp(__, '1') == 0:
 				fitn = fitn + 1
 		retDct_[name_] = fitn
 	return retDct_

"""
	Function definition for select()
	Input: A dictionary of strategies and their calculated fitness
	Output: A list of the fittest ones selected
"""
def select(dct_):
	#I do this part to sort the dictionary 
	lst_ = []
	lst = []
	import operator
	sorted_dct = sorted(dct_.items(), key=operator.itemgetter(1))
	
	lst_.append(sorted_dct.pop())
	lst_.append(sorted_dct.pop())
	nwDct = dict(lst_)
	
	#Here we create a list to return with the good strategies
	for _ in nwDct:
		lst.append(_)
	return lst
		

"""
	Function definition for crossover()
	Input: A list of strategies to work on
	Output:	A list of strategies crossed over and ready for work
"""
def crossover(lst_):
	#Here I'm just doing random stuffs 
	#Maybe later I'll take a look and perfect it
    from random import shuffle
    x = lst_[0]
    shuffle(lst_)
    lst_.append(x)		#I copied the first item, shuffled list and append item to the end
    return lst_

"""
	Function definition for mutate()
	Input: A list of work-ready strategies
	Output: work-ready strategies mutated at rate .15%
"""
def mutate(lst, fulLst):
    for _ in range(0,len(lst)):
        x = randint(0,100)
        if x < 15:
            tmp = lst[_]
            tmpLst = []
            for __ in fulLst:
                if cmp(__, tmp) != 0:
                    tmpLst.append(__)
            shuffle(tmpLst)
            y = randint(0,len(tmpLst))
            lst[_] = fulLst[y]
    return lst
