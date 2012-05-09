import time

#converts 1-2 digit integers in 2 carachter long strings
def convert(inp):
	out = str(inp)
	if(len(out)==1):
		return " "+out
	elif(len(out)==2):
		return out
def output():	
	field = open("../res/kalaha_gametable.txt", "r")
	sfield = ""
	#builds a string out of the file
	for line in field:
		sfield+=line
	#replaces wildcard with actual score
	for k, v in score.items():
		sfield=sfield.replace(k, convert(v))
	print(sfield)
	field.close()
#seeds per house
sph = 4
score = {
"L_":0,
"D0":sph,
"D1":sph,
"D2":sph,
"D3":sph,
"D4":sph,
"D5":sph,
"R_":0,
"U5":sph,
"U4":sph, 
"U3":sph, 
"U2":sph, 
"U1":sph, 
"U0":sph, 
}

next = {
"L_":"D0",
"D0":"D1",
"D1":"D2",
"D2":"D3",
"D3":"D4",
"D4":"D5",
"D5":"R_",
"R_":"U5",
"U5":"U4",
"U4":"U3", 
"U3":"U2", 
"U2":"U1", 
"U1":"U0", 
"U0":"L_", 
}

side = {
"D0":1,
"D1":1,
"D2":1,
"D3":1,
"D4":1,
"D5":1,
"U5":2,
"U4":2, 
"U3":2, 
"U2":2, 
"U1":2, 
"U0":2,
}
