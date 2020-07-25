filename='alice.txt'
try:
	with open(filename) as file_object:
		contents=file_object.read()
except FileNotFoundError:
	message="Sorry,the file "+filename+" does not exist."
	print(message)
else:
	#计算文件大致包含多少个单词
	words=contents.split()
	num_words=len(words)
	print("The file "+filename+" has about "+str(num_words)+" words.")
