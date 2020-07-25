#age=11
#if age>=18:
	#print("You are old enough to vote!")
	#print("Have you registered to vote yet?")
#else:
	#print("Sorry,you are too young to vote.")
	#print("Please register to vote as soon as you turn 18!")

age=3
if age<4:
	#print("Your admission cost is $0.")
	price=0
elif age<18:
	#print("Your admission cost is $5.")
	price=5
else:
	#print("Your admission cost is $10.") 
	price=10

print("Your admission cost is $"+str(price)+".")

age=100
if age<4:
	price=0
elif age<18:
	price=5
elif age<65:
	price=10
#else:
elif age>65:
	price=5
print("Your admission cost is $"+str(price)+".")
