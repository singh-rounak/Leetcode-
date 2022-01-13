Hashmap = {'A':1, 'B':2, 'C': 3, 'D':4 ,'E':5,'F':6 ,'G':7 ,'H':8 ,'I':9 ,'J':10 ,'K':11 ,'L':12 ,'M':13 ,'N':14 ,'O':15 ,'P':16 ,'Q':17 ,'R':18 ,'S':19 ,'T':20 ,'U':21 ,'V':22 ,'W':23 ,'X':24 ,'Y':25 ,'Z':26}

decrypted = ''
word = 'VTAOG'
k = 2


def get_letter(p):
	for letter, number in Hashmap.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
	    if number == p :
	        return letter


for i in word:
	if i in Hashmap:
		temp = Hashmap[i] - k
		decrypted += get_letter(temp)

print(decrypted)
