# ~ class Car():
	# ~ """一次模拟汽车的简单尝试"""
	# ~ def __init__(self,make,model,year):  #init前后是双下划线，并且其中的'self'是必须有的
		# ~ """初始化描述汽车的属性"""
		# ~ self.make=make
		# ~ self.model=model
		# ~ self.year=year
		# ~ self.odometer_reading=60

	# ~ def get_descriptive_name(self):
		# ~ """返回整洁的描述性信息"""
		# ~ long_name=str(self.year)+' '+self.make+' '+self.model
		# ~ return long_name.title()

	# ~ def read_odometer(self):
		# ~ """打印一条汽车里程的消息"""
		# ~ print("This car has "+str(self.odometer_reading)+" miles on it.")

	# ~ def update_odometer(self,mileage):  #通过方法修改属性的值 2
		# ~ """
		# ~ 将里程表读书设置为指定的值
		# ~ 静止将里程表读数往回调
		# ~ """
		# ~ if mileage>=self.odometer_reading:
			# ~ self.odometer_reading=mileage
		# ~ else:
			# ~ print("You cannot roll back an odometer!!")
		# ~ self.odometer_reading=mileage

# ~ my_new_car=Car('audi','q7',2018)
# ~ print(my_new_car.get_descriptive_name())
# ~ my_new_car.odometer_reading=23   #直接修改属性的值 1
# ~ my_new_car.update_odometer(23)   #方法调用      #通过方法修改属性的值 2
# ~ my_new_car.read_odometer()       #方法调用





class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):  #__init__前后是双下划线，并且其中的'self'是必须有的
		"""初始化描述汽车的属性"""
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=60

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.upper()

	def read_odometer(self):
		"""打印一条汽车里程的消息"""
		print("This car has "+str(self.odometer_reading)+" miles on it.")

	def update_odometer(self,mileage):  #通过方法修改属性的值 2
		"""
		将里程表读书设置为指定的值
		静止将里程表读数往回调
		"""
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You cannot roll back an odometer!!")

	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading+=miles
my_used_car=Car('bmw','x7',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
	
my_used_car.increment_odometer(1000)
my_used_car.read_odometer()
