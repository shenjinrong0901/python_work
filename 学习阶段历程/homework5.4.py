#5-8
# ~ users_name=['admin','pc','iphone','ipad','imac']
# ~ if 'eric' in users_name:
	# ~ print("Hello admin,would you like to see a status report?")
# ~ else:
	# ~ print("Hello Eric,thank you for logging in again!")

#5-9
# ~ users_name=[]
# ~ if users_name:
	# ~ for user_name in users_name:
		# ~ print("Hello "+user_name+".")
# ~ else:
	# ~ print("We need to find some users.")

#5-10
# ~ current_users=['james','harden','paul','curry','jordan']
# ~ new_users=['Paul','jordan','rose','bosh','green']
# ~ for new_user in new_users:
	# ~ if new_user.lower() in current_users:
		# ~ print("Sorry,"+new_user+" has been used.")
	# ~ else:
		# ~ print("OK,"+new_user+" can be use.")
		
#5-11
lists=['1','2','3','4','5','6','7','8','9']
for list in lists:
	if list=='1':
		print(list+"st")
	elif list=='2':
		print(list+"nd")
	elif list=='3':
	    print(list+"rd")
	else:
		print(list+"th")
