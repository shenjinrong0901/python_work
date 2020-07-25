#8-9
# ~ def show_magicians(magic_names):
	# ~ print(magic_names)
# ~ magic_names=['james','harden','paul','jordan']
# ~ show_magicians(magic_names)

#8-10
def show_magicians(magic_names):
	print(magic_names)
	
def make_great(magic_names):
	while magic_names:
		current_name=magic_names.pop()
		print("The Great: "+current_name.title())
magic_names=['james','harden','paul','jordan']
make_great(magic_names[:])
show_magicians(magic_names)
