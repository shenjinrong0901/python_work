def get_formatted_name(city,country,population=''):
	if population:
		full_message=city+' '+country+' '+str(population)
	else:
		gull_message=city+' '+country
	return full_message.title()
