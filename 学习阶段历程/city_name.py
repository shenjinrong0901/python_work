from city_functions import get_formatted_name
print("Enter 'q' at any time to quit!")
while True:
	city=input("\nPlease give me your city: ")
	if city=='q':
		break
	country=input("\nPiease give your country: ")
	if country=='q':
		break
	population=input("\nPlease give your city'spopulation: ")
	if population=='q':
		break
	
	city_name=get_formatted_name(city,country,str(population))
	print("The neatly formatted name: "+city_name+'!')
