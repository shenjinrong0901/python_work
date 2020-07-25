file_path=r'C:\Users\shenjinrong\Desktop\python_thinkings.txt'
with open(file_path) as file_object:
	lines=file_object.readlines()
for line in lines:
	print(line)
