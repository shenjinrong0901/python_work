# ~ with open('text_files\pi_digits.txt')as file_object:
	# ~ contents=file_object.read()
	# ~ print(contents.rstrip())


# ~ file_path=r'C:\Users\shenjinrong\Desktop\filename.txt'
# ~ with open(file_path) as file_object:
	# ~ contents=file_object.read()
	# ~ print(contents.rstrip())


# ~ filename='pi_digits.txt'
# ~ with open(filename) as file_object:

file_path=r'C:\Users\shenjinrong\Desktop\filename.txt'
with open(file_path) as file_object:
	lines=file_object.readlines()
for line in lines:
	print(line)
