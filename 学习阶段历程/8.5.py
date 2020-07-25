# ~ def make_pizza(*toppings):#  //'*'让python创建一个名为toppings的空元组，将收到的所有值都封装在这个元组中
	# ~ print(toppings)
# ~ make_pizza('pepperoni')
# ~ make_pizza('mushrooms','green peppers','extra cheese')

# ~ def make_pizza(*toppings):#  //'*'让python创建一个名为toppings的空元组，将收到的所有值都封装在这个元组中
	# ~ print("\nMaking a pizza with the following toppings:")
	# ~ for topping in toppings:
		# ~ print("- "+topping)
# ~ make_pizza('pepperoni')
# ~ make_pizza('mushrooms','green peppers','extra cheese')

# ~ def make_pizza(size,*toppings):
	# ~ print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	# ~ for topping in toppings:
		# ~ print("-"+topping)
# ~ make_pizza(16,'pepperoni')
# ~ make_pizza(12,'mushrooms','green peppers','extra cheese')

# ~ def build_profile(first,last,**user_info):
	# ~ profile={}
	# ~ profile['first_name']=first
	# ~ profile['last_name']=last
	# ~ for key,value in user_info.items():
		# ~ profile[key]=value
	# ~ return profile
# ~ user_profile=build_profile('albert','einstein',location='princetion',field='physics')
# ~ print(user_profile)


# ~ def make_pizza(*toppings):
	# ~ print("\nMaking a pizza with the following toppings:")
	# ~ for topping in toppings:
		# ~ print("-"+topping.title())
# ~ make_pizza('pepperoni')
# ~ make_pizza('mushroms','green peppers','extra cheese')
# ~ make_pizza('beaf','fish','meat')


# ~ def make_pizza(size,*toppings):
	# ~ print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	# ~ for topping in toppings:
		# ~ print("- "+topping)
# ~ make_pizza(22,'meat','beaf','fish')
# ~ make_pizza(20,'pepperoni')
	

#使用任意数量的关键字实参，（例:创建用户简介，但是我不知道将要收集到多少有关用户的信息）
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics',age='22')
print(user_profile)
