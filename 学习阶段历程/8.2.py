#位置实参的传递
# ~ def describe_pet(animal_type,pet_name):
	# ~ print("\nI have a "+animal_type+" .")
	# ~ print("My "+animal_type+"'s name is "+pet_name.title()+" .")
# ~ describe_pet('cat','tony')
# ~ describe_pet('dog','james')


#关键字实参
# ~ def describe_pet(animal_type,pet_name):
	# ~ print("\nI have a "+animal_type+" .")
	# ~ print("My "+animal_type+"'s name is "+pet_name.title()+" .")
# ~ describe_pet(animal_type='cat',pet_name='paul')
# ~ describe_pet(animal_type='snake',pet_name='tony')
# ~ describe_pet(pet_name='paul',animal_type='cat')
#在关键字实参中，可设置相应的默认值，方便调用
def describe_pet(pet_name,animal_type='dog'):
	print("\nI have a "+animal_type+" .")
	print("My "+animal_type+"'s name is "+pet_name.title()+" .")
describe_pet(pet_name='paul')
describe_pet(pet_name='willie')
describe_pet(pet_name='paul',animal_type='cat')
