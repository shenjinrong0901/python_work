filename='programming.txt'
with open(filename,'w') as file_object:
	file_object.write("我喜欢看篮球比赛.\n")
	file_object.write("但是喜欢打羽毛球.\n")

with open(filename,'a') as file_object:
	file_object.write("我最喜欢的NBA球队是休斯顿火箭队。\n")
	file_object.write("我最喜欢的羽毛球球员是林丹。\n")
