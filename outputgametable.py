import time

#converts 1-2 digit integers in 2 carachter long strings
def convert(inp):
	out = str(inp)
	if(len(out)==1):
		return " "+out
	elif(len(out)==2):
		return out
def output():	
	field = open("kalaha_gametable.txt", "r")
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
"U0":4, "D0":4,
"U1":4, "D1":4,
"U2":4, "D2":4,
"U3":4, "D3":4,
"U4":4, "D4":4,
"U5":4, "D5":4,
"R_":0
}
output()

time.sleep(1)

score = {
"L_":0,
"U0":3, "D0":3,
"U1":3, "D1":3,
"U2":3, "D2":3,
"U3":3, "D3":3,
"U4":3, "D4":3,
"U5":3, "D5":3,
"R_":0
}

output()

time.sleep(1)

score = {
"L_":11,
"U0":13, "D0":13,
"U1":31, "D1":13,
"U2":31, "D2":13,
"U3":31, "D3":31,
"U4":31, "D4":31,
"U5":31, "D5":31,
"R_":10
}

output()

