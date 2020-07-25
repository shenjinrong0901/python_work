# ~ alien_0={'color':'green','point':'5'}
# ~ print(alien_0['color'])
# ~ print(alien_0['point'])
# ~ new_points=alien_0['point']
# ~ print("You just earned "+str(new_points)+" points!")

#在字典中添加键-值对
# ~ alien_0={'color':'green','point':'5'}
# ~ print(alien_0)
# ~ alien_0['x_position']=0
# ~ alien_0['y_position']=25
# ~ print(alien_0)


#先创建一个空字典，在其中添加键-值对
# ~ alien_0={}
# ~ alien_0['colar']='green'
# ~ alien_0['point']=5
# ~ print(alien_0)

#修改字典中的值
# ~ alien_0={'color':'green','point':'5'}
# ~ print(alien_0)
# ~ alien_0['point']=10
# ~ print(alien_0)

# ~ alien_0={}
# ~ alien_0['color']='yellow'
# ~ alien_0['point']=5
# ~ print(alien_0)
# ~ alien_0['color']='blue'
# ~ print("Now the alien is "+alien_0['color']+".")


#对一个以不同速度移动的外星人的位置进行跟踪
# ~ alien_0={'x_position':0,'y_position':25,'speed':'fast'}
# ~ print("Original x-position: "+str(alien_0['x_position']))
# ~ if alien_0['speed']=='slow':
   # ~ x_increment=1
# ~ if alien_0['speed']=='medium':
   # ~ x_increment=2
# ~ else:
	# ~ x_increment=3
# ~ alien_0['x_position']=alien_0['x_position']+x_increment
# ~ print("New x-position: "+str(alien_0['x_position']))


#删除键-值对
# ~ alien_0={'color':'green','point':'5'}
# ~ print(alien_0)
# ~ del alien_0['point']
# ~ print(alien_0)


#由类似对象组成的字典
favourite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("Sarah's favourite is "+
    favourite_languages['sarah'].title()+
    ".")

