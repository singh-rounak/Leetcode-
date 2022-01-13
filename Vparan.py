logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

letters = []
digits = []

for log in logs:
	split = log.split()
	#print(split[1])

	if split[1].isdigit():
		digits.append(log)

	else:
		letters.append(log)

print(letters)
#letters.sort(key = lambda x: (x.split()[1:]))
print('---------------------')
#print(letters)
letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
print(letters)


"""
x: (x.split()[1:]))
['g1 act car', 'a2 act car', 'a8 act zoo', 'ab1 off key dog']
"""