#检查是否相等(== 读作：变量car的值时'bmw'嘛？)
cars=['audi','bmw','subaru','toyota']
for car in cars:
	if car=='bmw':
		print(car.upper())
	else:
		print(car.title())
print("\n")
#检查是否不相等(!= )
requested_topping='mushrooms'
if requested_topping!='anchovies':
	print("Hold the anchovies!")
print("\n")
#检查答案是否正确
answer=23
if answer!=24:
	print("That is not the correct answer.Please try again!")
print("\n")
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
	print(user.title()+", you can post a response if you wish.")
