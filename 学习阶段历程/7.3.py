#在列表之间移动元素
# ~ unconfirmed_users=['alice','brian','candace']
# ~ confirmed_users=[]
# ~ while unconfirmed_users:
	# ~ current_user=unconfirmed_users.pop()#pop() 函数用于移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
	# ~ print("Verifying user: "+current_user.title())
	# ~ confirmed_users.append(current_user)
# ~ print("\nThe following users have been confirmed:")
# ~ for confirmed_user in confirmed_users:
	# ~ print(confirmed_user.title())
	
#删除包含特定值的所有列表元素
# ~ pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
# ~ print(pets)
# ~ while 'cat' in pets:
	# ~ pets.remove('cat')
# ~ print(pets)


#使用用户输出来填充字典
responses={}
polling_active=True
while polling_active:
# ~ while True:
	name=input("\nWhat is your name? ")
	response=input("Which mountain would you like to climb someday? ")
	responses[name]=response
	repeat=input("Would you like to let another person respond(Yes/No)")
	if repeat=='no':
		polling_active=False
print("\n---Poll Results---")
for name,response in responses.items():
	print(name+" would like to climb "+response+" .")
	
