#将字典嵌套在列表中
# ~ alien_0={'color':'green','point':5}
# ~ alien_1={'color':'yellow','point':10}
# ~ alien_2={'color':'red','point':15}
# ~ aliens=[alien_0,alien_1,alien_2]
# ~ for alien in aliens:
	# ~ print(alien)


# ~ aliens=[]#创建一个用于存储外星人的空列表
# ~ for alien_number in range(30):
	# ~ new_alien ={'color':'green','point':5,'speed':'slow'}#定义新外星人的特性
	# ~ aliens.append(new_alien)#将所生成的每一个新外星人添加到列表末尾(由方法append()决定的)
# ~ for alien in aliens[:10]:#遍历整个列表
	# ~ print(alien)#打印
# ~ print("...")
# ~ print("Total number of aliens: "+str(len(aliens)))


#尝试着修改每个外星人的相应元素
aliens=[]#创建一个用于存储外星人的空列表
for alien_number in range(30):
	new_alien ={'color':'green','point':5,'speed':'slow'}#定义新外星人的特性
	aliens.append(new_alien)#将所生成的每一个新外星人添加到列表末尾(由方法append()决定的)
for alien in aliens[0: 3]:#遍历列表的前3个元素
	if alien['color']=='green':
	    alien['color']='yellow'
	    alien['point']=10
	    alien['speed']='medium'
	elif alien['color']=='yellow':
		alien['color']='red'
		alien['point']=15
		alien['speed']='fast'
for alien in aliens[:5]:
	print(alien)
print("...") 
