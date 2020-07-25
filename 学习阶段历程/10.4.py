# ~ import json
# ~ numbers=[2,3,5,7,11,13]
# ~ filename='numbers.json'
# ~ with open(filename,'w') as file_object:
	# ~ json.dump(numbers,file_object)
	
# ~ import json
# ~ filename='numbers.json'
# ~ with open(filename) as file_object:
	# ~ numbers=json.load(file_object)
# ~ print(numbers)


# ~ import json
# ~ username=input("What is your name?")
# ~ filename='username.json'
# ~ with open(filename,'w') as file_object:
	# ~ json.dump(username,file_object)
	# ~ print("We'll remember you when you come back, "+username+"!")

# ~ import json
# ~ filename='username.json'
# ~ with open(filename) as file_object:
	# ~ username=json.load(file_object)
	# ~ print("Welcome back, "+username+"!")


# ~ import json
# ~ filename='username.json'
# ~ try:
	# ~ with open(filename) as file_object:
		# ~ username=json.load(file_object)
# ~ except FileNotFoundError:
	# ~ username=input("What is you name? ")
	# ~ with open(filename,'w') as file_object:
		# ~ json.dump(username,file_object)
		# ~ print("We'll remember you when you come back, "+username+"!")
# ~ else:
	# ~ print("Welcome back, "+username+"!")
	

# ~ import json
# ~ def greet_user():
	# ~ """问候用户，并指出其名字"""
	# ~ filename='username.json'
	# ~ try:
		# ~ with open(filename) as file_object:
			# ~ username=json.load(file_object)
	# ~ except FileNotFoundError:
		# ~ username=input("What is your name? ")
		# ~ with open(filename,'w') as file_object:
			# ~ json.dump(username,file_object)
			# ~ print("We'll remember you when you come back,"+username+"!")
	# ~ else:
		# ~ print("Welcome back, "+username+"!")
		
# ~ greet_user()


# ~ import json
# ~ def get_stored_username():
	# ~ """如果存储了用户名，就获取它"""
	# ~ filename='username.json'
	# ~ try:
		# ~ with open(filename) as file_object:
			# ~ username=json.load(file_object)
	# ~ except FileNotFoundError:
		# ~ return None
	# ~ else:
		# ~ return username
		
# ~ def greet_user():
	# ~ """问候用户，并指出其名字"""
	# ~ username=get_stored_username()
	# ~ if username:
		# ~ print("Welcome back, "+username+"!")
	# ~ else:
		# ~ username=input("What is your name? ")
		# ~ filename='username.json'
		# ~ with open(filename,'w') as file_object:
			# ~ json.dump(username,file_object)
			# ~ print("We'll remember you when you come back,"+username+"!")

# ~ greet_user()


import json
def get_stored_username():
	"""如果存储了用户名，就获取它"""
	filename='username.json'
	try:
		with open(filename) as file_object:
			username=json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username():
	"""提示用户输入用户名"""
	username=input("What's your name? ")
	filename='username.json'
	with open(filename,'w') as file_object:
		json.dump(username,file_object)
	return username
	
def greet_user():
	"""问候用户，并指出其名字"""
	username=get_stored_username()
	if username:
		print("Welconme back,"+username+"!")
	else:
		username=get_new_username()
		print("We'll remember you while you come back, "+username.title()+"!")
		
greet_user()
