# ~ def get_formatted_name(first_name,last_name):
	# ~ """返回整洁的姓名"""
	# ~ full_name=first_name+' '+last_name
	# ~ return full_name.title()
# ~ musician=get_formatted_name('jimi','hendrix')
# ~ print(musician)


# ~ def get_formatted_name(first_name,last_name,middle_name=''):
	# ~ """返回整洁的姓名"""
	# ~ full_name=first_name+' '+middle_name+' '+last_name
	# ~ return full_name.title()
# ~ musician=get_formatted_name('jimi','lee','hendrix')
# ~ print(musician)

# ~ def get_formatted_name(first_name,last_name,middle_name=''):
	# ~ if middle_name:
		# ~ full_name=first_name+' '+middle_name+' '+last_name
	# ~ else:
		# ~ full_name=first_name+' '+last_name
	# ~ return full_name.title()
# ~ musician=get_formatted_name('james','harden')
# ~ print(musician)
# ~ musician=get_formatted_name('jimi','lee','hendrix')


# ~ def build_person(first_name,last_name):
	# ~ person={'first':first_name,'last':last_name}
	# ~ return person
# ~ musician=build_person('james','harden')
# ~ print(musician)

# ~ def build_person(first_name,last_name,age=' '):
	# ~ """返回一个字典，其中包含一个人的额关键信息"""
	# ~ person={'first':first_name,'last':last_name}
	# ~ if age:
		# ~ person['age']=age
	# ~ return person
# ~ musician=build_person('james','harden',age=30)
# ~ print(musician)


#结合使用函数和while
# ~ def get_formatted_name(first_name,last_name):
	# ~ full_name=first_name+' '+last_name
	# ~ return full_name.title()
# ~ #这是个无限循环！
# ~ while True:
	# ~ print("\nPlease tell me your name:")
	# ~ f_name=input("First name: ")
	# ~ l_name=input("Last name: ")
	# ~ formatted_name=get_formatted_name(f_name,l_name)
	# ~ print("\nHello, "+formatted_name+"!")
def get_formatted_name(first_name,last_name):
	full_name=first_name+' '+last_name
	return full_name.title()
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit).")
	f_name=input("First name: ")
	if f_name=='q':
		break
	l_name=input("Last name: ")
	if l_name=='q':
		break
	formatted_name=get_formatted_name(f_name,l_name)
	print("\nHello, "+formatted_name+"!")
