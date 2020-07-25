#8-6
# ~ def city_country(city,country):
	# ~ full_information=city+','+country
	# ~ return full_information.title()
# ~ city_message=city_country('shanghai', 'china')
# ~ print(city_message)
# ~ city_message=city_country('beijing', 'china')
# ~ print(city_message)
# ~ city_message=city_country('houston', 'america')
# ~ print(city_message)


#8-7
# ~ def make_album(singer_name,music_name,song_number=''):
	# ~ album={'singer':singer_name,'music':music_name}
	# ~ if song_number:
		# ~ album['number']=song_number
	# ~ return album
# ~ message_1=make_album('jay_chou','no_cry',song_number=30)
# ~ print(message_1)
# ~ print("\n")
# ~ message_2=make_album('lironghao','see')
# ~ print(message_2)
# ~ print("\n")
# ~ message_3=make_album('talay','me',song_number=1)
# ~ print(message_3)


# ~ def get_formatted_name(first_name,last_name):
	# ~ full_name=first_name+' '+last_name
	# ~ return full_name.title()
# ~ while True:
	# ~ print("\nPlease tell me your name:")
	# ~ print("(enter 'q' at any time to quit).")
	# ~ f_name=input("First name: ")
	# ~ if f_name=='q':
		# ~ break
	# ~ l_name=input("Last name: ")
	# ~ if l_name=='q':
		# ~ break
	# ~ formatted_name=get_formatted_name(f_name,l_name)
	# ~ print("\nHello, "+formatted_name+"!")
	

def get_make_album(singer_name,music_name):
	message=singer_name+', '+music_name
	return message.title()
while True:
	print("\nPlease tell me music's singer:")
	print("(enter 'q' at any time to quit).")
	f_name=input("Singer_name: ")
	if f_name=='q':
		break
	l_name=input("Music_name: ")
	if l_name=='q':
		break
	make_album=get_make_album(f_name,l_name)
	print("\nThe album's information is following: "+make_album+".")
