#列表推导
symbols = '$#*&@!'
code = [ord(symbol) for symbol in symbols]
codes = [ord(symbol) for symbol in symbols if ord(symbol)>40]
print(code)
print(codes)

#生成器表达式
symbols = '$#*&@!'

