#7-8
# ~ sandwich_orders=['fish','meat','beaf']
# ~ finished_sandwiches=[]
# ~ while sandwich_orders:
	# ~ current_sandwich=sandwich_orders.pop()
	# ~ print("I made you "+current_sandwich.title()+" sandwich.")
	# ~ finished_sandwiches.append(current_sandwich)
# ~ print("\nThe following sandwich have been made: ")
# ~ for finished_sandwiche in finished_sandwiches:
	# ~ print("\n\t"+finished_sandwiche.title()+" sandwich." )


#7-9
# ~ sandwich_orders=['pastrami','beaf','pastrami','fish','pastrami']
# ~ print("The pastrami sandwich has been sold out in this shop!")
# ~ while 'pastrami' in sandwich_orders:
	# ~ sandwich_orders.remove('pastrami')
# ~ print(sandwich_orders)


#7-10
responses={}
place_active=True
while place_active:
	name=input("\nWhat is you name?")
	response=input("If you could visit one place in the world,where would you go?")
	responses[name]=response
	repeat=input("Would you like to let another person respond?(yes/no)")
	if repeat=='no':
		place_active=False
print("\n---Results---")
for name,response in responses.items():
	print(name.title()+" would like to visit "+response.title()+" .")
	
