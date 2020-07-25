# ~ user_0={
    # ~ 'username':'efermi',
	# ~ 'first':'enrico',
	# ~ 'last':'fermi',
# ~ }
# ~ print(user_0)
# ~ for key, value in user_0.items():
	# ~ print("\nKey: " +key)
	# ~ print("\nValue: "+value)

#遍历字典中的所有键-值对
# ~ favourite_languages={
    # ~ 'jen':'python', 
    # ~ 'sarah':'c',
    # ~ 'edward':'ruby',
    # ~ 'phil':'python',
    # ~ }
# ~ for name,language in favourite_languages.items():
	# ~ print("\n")
	# ~ print(name.title()+ "'s favourite language is "+ language.title()+".")	

#遍历字典中的所有键
# ~ favourite_languages={
    # ~ 'jen':'python',
    # ~ 'sarah':'c',
    # ~ 'edward':'ruby',
    # ~ 'phil':'python',
    # ~ }
# ~ friends=['phil','sarah']
# ~ for name in favourite_languages.keys():
	
	# ~ if name in friends:
		# ~ print("Hi "+name.title()+" , I see you favourite language is "+favourite_languages[name].title()+"!")
	# ~ else:
		# ~ print("Hi "+name.title()+", Can you tell me what's you favourite language?")
# ~ if 'erin' not in favourite_languages.keys():
	# ~ print("Erin,please take our poll!")


# ~ favourite_languages={
    # ~ 'jen':'python',
    # ~ 'sarah':'c',
    # ~ 'edward':'ruby',
    # ~ 'phil':'python',
    # ~ }
# ~ for name in sorted(favourite_languages.keys()):
	# ~ print(name.title()+", thank you for taking the poll.")

#遍历字典中的所有值
favourite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("The following languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())
print("\n")
#考虑重复的问题，用set()解决
for language in set(favourite_languages.values()):
	print(language.title())
