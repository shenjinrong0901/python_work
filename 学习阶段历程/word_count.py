def count_words(filename):
	"""计算一个文件大概包含多少个单词"""
	try:
		with open(filename) as file_object:
			contents=file_object.read()
	except FileNotFoundError:
		# ~ message="Sorry,the file "+filename+" does not exist."
		# ~ print(message)
		pass
	else:
		words=contents.split()
		num_words=len(words)
		print("The file "+filename+" has about "+str(num_words)+" words.")
		
filenames=['alice.txt','siddhartha.txt','little_women.txt','moby_dick.txt']
for filename in filenames:
	count_words(filename)
