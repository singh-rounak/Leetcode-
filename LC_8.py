Roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

print(Roman.values())
print(Roman.keys())

for val in Roman.values():
	print Roman[val]

print(Roman)