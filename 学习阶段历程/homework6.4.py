#作业6-7
# ~ people_0={
    # ~ 'name':'jinhao',
    # ~ 'old':23,
    # ~ 'gender':'male',
    # ~ }
# ~ people_1={
    # ~ 'name':'qiancheng',
    # ~ 'old':22,
    # ~ 'gender':'male',
# ~ }
# ~ people_2={
    # ~ 'name':'rubbit',
    # ~ 'old':29,
    # ~ 'gender':'female',
# ~ }
# ~ people_3={
    # ~ 'name':'dongdong',
    # ~ 'old':27,
    # ~ 'gender':'female',
# ~ }
# ~ peoples=[people_0,people_1,people_2,people_3]
# ~ for people in peoples:
	# ~ print(people)

#作业6-8
# ~ flower={
    # ~ 'kind':'dog',
    # ~ 'master':'jinhao',
    # ~ }
# ~ wangwang={
    # ~ 'kind':'cat',
    # ~ 'master':'qianchen',
    # ~ }
# ~ wangzai={
    # ~ 'kind':'dog',
    # ~ 'master':'BB',
	# ~ }
# ~ pets=[flower,wangwang,wangzai]
# ~ for pet in pets:
	# ~ print(pet)
	
#作业6-9
# ~ favourite_places={
    # ~ 'guoyue':['shanghai','suzhou','wuxi'],
    # ~ 'wanglu':['suzhou','nanjing','shanghai'],
    # ~ 'caocheng':['chongqing','xiamen','hangzhou'],
    # ~ }
# ~ for name,places in favourite_places.items():
	# ~ print("\n"+name.title()+"'s favourite places are: ")
	# ~ for place in places:
		# ~ print("\t"+place.title())
		
#作业6-10
# ~ friends={
    # ~ 'james':['6','23'],
    # ~ 'paul':['3','33'],
    # ~ 'harden':['13','31'],
    # ~ 'jordan':['23','44'],
    # ~ 'kobe':['8','24'],
    # ~ }
# ~ for name,numbers in friends.items():
	# ~ print("\n"+name.title()+"'s favourite are: ")
	# ~ for number in numbers:
		# ~ print("\t"+number.title())

#作业6-11
cities={
    'shangahai':{
        'country':'china',
        'population':20000000,
        'fact':'The most streamline city in china.',
        },
    'beijing':{
        'country':'china',
        'population':21540000,
        'fact':"The capital of China!",
        },
    'New York':{
        'country':'america',
        'population':8510000,
        'fact':"The most beautical city in the world!",
        },
    }
for city,factor in cities.items():
	print("\nCity: "+city.title())
	basic_information="The city of "+factor['country']+","+factor['fact']
	basic_fact=factor['population']
	print("\tInformation: "+basic_information.title())
	print("\tPopulation: "+str(basic_fact))
	
