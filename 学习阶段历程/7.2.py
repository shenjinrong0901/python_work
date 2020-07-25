# ~ current_number=1
# ~ while current_number<=5:
	# ~ print(current_number)
	# ~ current_number+=1    #相当于‘current_number=current_number+1’,即将它的值+1.
	
# ~ prompt="\nTell me something,and I will repeat it back to you: "
# ~ prompt+="\nEnter 'quit' to end the program. "
# ~ message=""
# ~ while message !='quit':
	# ~ message=input(prompt)
	# ~ if message!='quit':
	    # ~ print(message)
	# ~ else:
		# ~ print("\nThank you for your use.")


# ~ prompt="\nTell me something,and I will repeat it back to you: "
# ~ prompt+="\nEnter 'quit' to end the program. "
# ~ active=True
# ~ while active:
	# ~ message=input(prompt)
	# ~ if message=='quit':
		# ~ active=False
	# ~ else:
		# ~ print(message) 


# ~ prompt="\nPlease enter the name of a city you have visited:"
# ~ prompt+="\nEnter 'quit' when you are finished."
# ~ while True:
	# ~ city=input(prompt)
	# ~ if city=='quit':
		# ~ break
	# ~ else:
		# ~ print("I'd love to go to "+city.title()+"!")


#在循环中使用continue
# ~ current_number=0
# ~ while current_number<10:
	# ~ current_number+=1
	# ~ if current_number%2!=0:
		# ~ continue
	# ~ print(current_number)
    
x=1
while x <=5:
	print(x)
	x+=1
