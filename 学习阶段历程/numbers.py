for value in range(1,5):
  print(value) 
for value in range(1,6):
  print(value)
 #创建数字列表
numbers=list(range(1,7))
print(numbers)
print("\n")
#打印1-10内，步长为三的数
even_numbers=list(range(1,11,3))
print(even_numbers)
print("\n")
#打印10个整数的平方，存到列表中
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
print("\n")
#方法二
squares=[]
for number  in range(1,11):
	squares.append(number**2)
print(squares)
print("\n")
#列表解析法
squares=[number**2 for number in range(1,11)]
print(squares)

