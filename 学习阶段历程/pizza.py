#列表存储在字典中
             #一
pizza={
    'crust':'rhick',
    'toppings':['mushrooms','extra cheese'],
}
print("You ordered a "+pizza['crust']+"-crust pizza "+
    "with the following toppings: ")
for topping in pizza['toppings']:
	print("\t"+topping)
              #二
favourite_languages={ 
    'jen':['python','c'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','java'],
    }
for name,languages in favourite_languages.items():
	print("\n"+name.title()+"'s is favourite languages are: ")
	for language in languages:
		print("\t"+language.title())


#字典存储在字典中
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username,user_info in users.items():
	print("\nUsername: "+username.title())
	full_name=user_info['first']+" "+user_info['last']
	location=user_info['location']
	print("\tFull name: "+full_name.title())
	print("\tLocation: "+ location.title()) 
    
