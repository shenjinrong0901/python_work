# ~ requested_toppings=['mushrooms','extra cheese']
# ~ if 'mushrooms' in requested_toppings:
	# ~ print("Adding mushrooms.")
# ~ if 'pepperoni' in requested_toppings:
	# ~ print("Adding pepperoni.")
# ~ if 'extra cheese' in requested_toppings:
	# ~ print("Adding extra cheese.")
# ~ print("\nFinished making your pizza!")


# ~ requested_toppings=['mushrooms','extra cheese','green peppers']
# ~ for requested_topping in requested_toppings:
	# ~ if requested_topping=='green peppers':
		# ~ print("Sorry,we are out of green peppers right now.")
	# ~ else:
	    # ~ print("Adding "+requested_topping+".")
# ~ print("\nHave a good dinner!Best wishes for you.")

#确定列表不是空的
# ~ requested_toppings=[]
# ~ if requested_toppings:
	# ~ for requested_topping in requested_toppings:
		# ~ print("Adding "+requested_topping+".")
	# ~ print("\nBest wishes for you!")
# ~ else:
	# ~ print("Are you sure you want a plain pizza?")

#使用多个列表
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding "+requested_topping+".")
	else:
		print("Sorry,we dont't have "+requested_topping+".")
print("\nFinished making your pizza!")
