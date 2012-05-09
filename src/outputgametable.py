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
score = {
"L_":0,
"D0":4,
"D1":4,
"D2":4,
"D3":4,
"D4":4,
"D5":4,
"R_":0,
"U5":4,
"U4":4, 
"U3":4, 
"U2":4, 
"U1":4, 
"U0":4, 
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
