rivers={
    'changjiang':'jiangsu',
    'huanghe':'shangdong',
    'nile':'egypt',
}
for river,place in rivers.items():
	print("\nThe "+river.title()+" runs through "+place.title()+".")

print("The following river will be mentioned:")
for river in rivers:
	print("\n")
	print(river.title())

print("The following countries will be mentioned:")
for place in rivers.values():
	print("\n")
	print(place.title())


favourite_languages={
    'jen':'python', 
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
names=['jen','phil','james','sarah']
for name in favourite_languages.keys():
	if name in names:
		print("\nThanks "+name.title()+ "you for your help!")
	else:
		print("\nExcuse,"+name.title()+" ,I invite you to jion us survey.")
