#10-3
# ~ filename='username.txt'
# ~ with open(filename,'w') as file_object:
	# ~ file_object.write("金浩\n\n")
	# ~ file_object.write("钱晨\n")

# ~ #10-4
# ~ filename='gust_book.txt'
# ~ while True:
	# ~ your_name=input("请输入你的姓名：")
	# ~ if your_name=='q':
		# ~ break
	# ~ else:
		# ~ print("你好"+your_name+" !")
	# ~ with open(filename,'a') as file_object:
		# ~ file_object.write(your_name+" 已经来过次任务点。\n")

#10-5
filename='reason.txt'
while True:
	user_reason=input("请输入你喜欢编程的原因：")
	if user_reason=='q':
		break
	else:
		print("原因是："+user_reason)
	with open(filename,'a') as file_object:
		file_object.write("原因是："+user_reason+"\n")
