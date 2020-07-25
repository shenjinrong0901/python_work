#10-6
# ~ print("Please give me two number.")
# ~ print("Enter 'q' to quit.\n")
# ~ while True:
	# ~ first_number=input("First_number:\n")
	# ~ if first_number=='q':
		# ~ break
	# ~ second_number=input("Second_number:\n")
	# ~ if second_number=='q':
		# ~ break
	# ~ try:
		# ~ answer=int(first_number)+int(second_number)
	# ~ except TypeError:
		# ~ message="\nSorry you don't give me the correct number!"
		# ~ print(message)
	# ~ else:
		# ~ print(answer)

#10-7
# ~ while True:
	# ~ try:
		# ~ first_number=input("Please input the first:")
		# ~ if first_number=='q':
			# ~ break
		# ~ else:
			# ~ x=int(first_number)
		# ~ second_number=input("Please input the second:")
		# ~ if second_number=='q':
			# ~ break
		# ~ else:
			# ~ y=int(second_number)
	# ~ except ValueError:
		# ~ print("sorry,I really need a number.")
	# ~ else:
		# ~ num=x+y
		# ~ print("The number is "+str(num) +" .")


#10-8
# ~ filenames=['cats.txt','fishs.txt','dogs.txt']
# ~ for filename in filenames:
	# ~ try:
		# ~ with open(filename) as file_object:
			# ~ contents=file_object.read()
			# ~ print("\nTheir names are: "+contents+".")
	# ~ except FileNotFoundError:
		# ~ print("\nSorry,I can't find the file.")
		# ~ pass
		
#10-9
# ~ def count_words(filename):
	# ~ """计算一个文件中包含多少the"""
	# ~ try:
		# ~ with open(filename) as file_object:
			# ~ contents=file_object.read()
	# ~ except FileNotFoundError:
		# ~ pass
	# ~ else:
		# ~ line=contents.split()
		# ~ line.lower().count('the')
		# ~ print("The file "+filename+" has about "+str(line.lower().count('the'))+"'the'.")
# ~ filenames=['alice.txt','siddhartha.txt']
# ~ for filename in filenames:
	# ~ count_words(filename)

#10-10-1
# ~ filename='alice.txt'
# ~ try:
	# ~ with open(filename) as file_object:
		# ~ contents=file_object.read()
# ~ except FileNotFoundError:
	# ~ pass
# ~ else:
	# ~ number1=contents.count('the')
	# ~ print("This file has "+str(number1)+"'the' words.")
	# ~ number2=contents.lower().count('the')
	# ~ print("\nThis file has "+str(number2)+"'the' and 'The' words.")


#10-10-2
def count_numbers(filename):
	try:
		with open(filename) as file_object:
			contents=file_object.read()
	except FileNotFoundError:
		pass
	else:
		number1=contents.count('the')
	print("This file has "+str(number1)+"'the' words.")
	number2=contents.lower().count('the')
	print("This file has "+str(number2)+"'the' and 'The' words.")
filenames=['alice.txt','siddhartha.txt']
for filename in filenames:
	count_numbers(filename)
