players=['charles','harden','jordan','james','paul']
print(players)
print("\nThe first three items in the list are:")
print(players[:3])
print("\n")
for player in players[:3]:
	print(player.title())
print("\n")
for player in players[2:]:
	print(player.title())
print("\n")
my_foods=['pizza','pancake','hamburger','noodle']
friend_foods=my_foods[:]
my_foods.append('hanbaowang')
friend_foods.append('bishengke')
print("My favourite pizzas are")
print(my_foods)
print("My friend's favourite pizza are")
print(friend_foods)
