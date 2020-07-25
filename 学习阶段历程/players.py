players=['charles','harden','jordan','james','paul']
print(players)
print(players[0:3])
print(players[1:5])
print(players[1:])
print(players[:4])
print(players[-3:])
print("\n")
print("Here are the first three NBA players on my team:")
for player in players[:3]:
   print(player.upper())
print("\n")
my_foods=['rice','noodle','pizz','falafel']
friend_foods=my_foods[:]
my_foods.append('annoli')
friend_foods.append('ice cream')
print("My favourite food are:")
print(my_foods)
print("\nMy friend's favourite food are")
print(friend_foods)
