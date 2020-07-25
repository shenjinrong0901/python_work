#9-4
# ~ class Restaurant():
	# ~ def __init__(self,restaurant_name,cuisine_type):
		# ~ self.restaurant_name=restaurant_name
		# ~ self.cuisine_type=cuisine_type
		# ~ self.number_served=0

	# ~ def describe_restaurant(self):
		# ~ print("The restaurant name is "+self.restaurant_name.title()+".")
		# ~ print("The restaurant's cuisine type is "+self.cuisine_type.title()+".")

	# ~ def open_restaurant(self):
		# ~ print("The "+self.restaurant_name.title()+" is openning!")

	# ~ def set_number_served(self):
		# ~ print("There are "+str(self.number_served)+" persons have been served.")

	# ~ def increment_number_served(self,persons):
		# ~ self.number_served+=persons

# ~ my_restaurant=Restaurant('eight bowls','chinese food')
# ~ print(my_restaurant.restaurant_name.title())
# ~ print(my_restaurant.cuisine_type.title())
# ~ my_restaurant.describe_restaurant()
# ~ my_restaurant.open_restaurant()

# ~ my_restaurant.number_served=23
# ~ my_restaurant.set_number_served()

# ~ my_restaurant.increment_number_served(22)
# ~ my_restaurant.set_number_served()



#9-5
class User():
	def __init__(self,first_name,last_name,age):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.login_attempts=0

	def describe_user(self):
		print("The user's name is "+self.first_name.title()+" "+self.last_name.title()+".")
		print("The user's age is "+str(self.age)+".")

	def greet_user(self):
		print("The best wisher for you "+self.first_name.title()+" "+self.last_name.title()+".")

	def increment_login_attempts(self,times):
		self.login_attempts+=times

	def reset_login_attempts(self):
		

user_name=User('james','harden',30)
user_name.describe_user()
user_name.greet_user()

b=User('rusesll','westbrook',31)
b.describe_user()
b.greet_user() 
