#7-4
# ~ prompt="\nPlease choose what you want to add in the pizza:"
# ~ prompt+="\nEnter 'quit' to end this program."
# ~ while True:
	# ~ message=input(prompt)
	# ~ if message=='quit':
		# ~ print("\nThank you for your using.")
		# ~ break
	# ~ else:
		# ~ print("\nWe will add "+message.title()+" in this pizza!")


#7-5
#（错误）
# ~ prompt="\nPlease tell me how old are you ?"
# ~ prompt+="\nEnter 'quit' to end this program."
# ~ while True:
	# ~ age=input(prompt)
	# ~ if age<'3':
		# ~ print("\nThe ticket's price is $0.")
	# ~ elif age<'12':
		# ~ print("\nThe ticket's price is $10.")
	# ~ else:
		# ~ print(The ticket's price is $15.)

# ~ prompt="\nPlease tell me how old are you ?"
# ~ prompt+="\n(Enter 'quit' when you are finished.)"
# ~ while True:
	# ~ age=input(prompt)
	# ~ if age=='quit':
		# ~ break#//若输入为qiut则直接跳出循环！！不在执行之后的程序！！
	# ~ else:
		# ~ age=int(age)#//很关键！！此处将字符串转换成数字，方便下面的程序对数字进行比较。
		# ~ if age<3:
			# ~ print("\nThis ticket is free!")
		# ~ elif(age>3 and age<12):#//两个条件之间可用and进行连接！！
			# ~ print("\nThe ticket's price is $10.")
		# ~ else:
			# ~ print("The ticket's price is $15.")

#7-7
x=22
while (x <=22 and x>=0):
	print(x)
	# ~ x-=1
