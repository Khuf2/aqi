# This function converts degrees to an approximate compass direction.

def windDirection(degree):
	# (N=0, E=90, S=180, W=270)
	dir = degree/22.5
	if(dir > 15 or dir <= 1):
		return "N"
	elif(dir > 1 and dir <= 3):
		return "NE"
	elif(dir > 3 and dir <= 5):
		return "E"	
	elif(dir > 5 and dir <= 7):
		return "SE"
	elif(dir > 7 and dir <= 9):
		return "S"
	elif(dir > 9 and dir <= 11):
		return "SW"
	elif(dir > 11 and dir <= 13):
		return "W"
	elif(dir > 13 and dir <= 15):
		return "NW"

def report(data):
	# pass in your data dictionary as data
	# It will be printed out in a series of new lines
	for x in data.keys():
		print (str(x) + " : " + str(data.get(x)))

celcToFar = lambda c : round((c * (9/5) + 32), 1)
metersToMPH = lambda m : round((m * 2.23694), 1)
degree_sign= u'\N{DEGREE SIGN}'