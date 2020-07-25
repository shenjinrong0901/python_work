# ~ def make_bread(*toppings):
	# ~ print("\nMaking a bread with the following toppings :")
	# ~ for topping in toppings:
		# ~ print("-"+topping)
# ~ make_bread('meat','beaf')
# ~ make_bread('pepper')
# ~ make_bread('cheese')
	

# ~ def build_profile(first,last,**user_info):
	# ~ profile={}
	# ~ profile['first_name']=first
	# ~ profile['last_name']=last
	# ~ for key,value in user_info.items():
		# ~ profile[key]=value
	# ~ return profile
# ~ user_profile=build_profile('albert','einstein',location='princetion',field='physics')
# ~ print(user_profile)
# ~ my_profile=build_profile('shen','jinrong',location='shanghai',field='math',age='23')
# ~ print(my_profile)


def make_car(maker,kinds,**needs):
	car={}
	car['maker']=maker
	car['kinds']=kinds
	for key,value in needs.items():
		car[key]=value
	return car
design_car=make_car('subaru','outback',color='blue',tow_package=True)
print(design_car)
	
