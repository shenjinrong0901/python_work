# ~ for number in range(1,21):
 # ~ print(number)
 # ~ print("\n")
# ~ numbers=list(range(1,100))
# ~ print(numbers)
squares=[]
for value in range(1,20,2):
	square=value
	squares.append(square)
print(squares)
print("\n")
squares=[]
for value in range(3,31,3):
	 square=value
	 squares.append(square)
print(squares)
print("\n")
squares=[]
for value in range(1,11):
    square=value**3
    squares.append(square)
print(squares)
print("\n")
squares=[value**3 for value in range(1,11)]
print(squares )
