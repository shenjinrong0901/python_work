#元祖定义
dimensions=(200,50)
print(dimensions[0])
print(dimensions[-1])
#遍历元祖中的所有值
dimensions=(200,50)
for dimension in dimensions:
	print(dimension)
print("\n")
#修改元祖变量（即就是重新定义整个元祖）
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions=(400,100)
print("Modified dimensions:")
for dimension in dimensions:
	print(dimension)
#元祖用途：如果需要存储一组数据在程序的整个生命周期内都不变，可使用元祖。


