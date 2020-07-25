#9-6 冰淇淋小店
# ~ class Restaurant():
    # ~ def __init__(self,restaurant_name,cuisine_type):
        # ~ #self.属性 的作用获取形参restaurant_name的值，并存储到restaurant_name中
        # ~ #以供实例使用
        # ~ self.restaurant_name = restaurant_name
        # ~ self.cuisine_type = cuisine_type
        # ~ self.number_served = 0

    # ~ def set_number_served(self,set_number):
        # ~ #使用方法设置number_served属性的值
        # ~ self.number_served = set_number

    # ~ def increment_number_served(self,increment_number):
        # ~ self.number_served += increment_number

    # ~ def describe_restaurant(self):
        # ~ print('\n您所在的餐厅是：' + self.restaurant_name +
              # ~ '\n餐饮类型是：' + self.cuisine_type +
              # ~ '\n就餐人数为：' + str(self.number_served) +
              # ~ '人')

    # ~ def open_restaurant(self):
        # ~ print('餐厅正在营业！')

# ~ class IceCreamStand(Restaurant):

    # ~ def __init__(self,restaurant_name,cuisine_type):
        # ~ super().__init__(restaurant_name,cuisine_type)
        # ~ #给子类设置新的属性
        # ~ self.flavors = ['抹茶味','苹果味','原味奶油']

    # ~ def describe_icecream(self):
        # ~ print('\n本店提供的冰激凌有' + '3种:')
        # ~ for show_flavors in self.flavors:
            # ~ print(show_flavors)
            
# ~ my_icecream = IceCreamStand('冰雪皇后','冰激凌')
# ~ my_icecream.open_restaurant()
# ~ my_icecream.set_number_served(15)
# ~ my_icecream.increment_number_served(35)
# ~ my_icecream.describe_restaurant()
# ~ my_icecream.describe_icecream()


#9-7 管理员
# ~ class User():
    # ~ def __init__(self,first_name,last_name):
        # ~ self.first_name=first_name
        # ~ self.last_name=last_name
        # ~ self.login_attempts=0
        
    # ~ def describe_user(self):
        # ~ print(self.first_name.title()+self.last_name.title())
        
    # ~ def greet_user(self):
        # ~ print("Hello,"+self.first_name.title()+self.last_name.title())
        
    # ~ def increment_login_attempts(self):
        # ~ self.login_attempts+=1
        
    # ~ def reset_login_attempts(self):
        # ~ self.login_attempts=0
        # ~ return self.login_attempts
        
        
# ~ class Admin(User):
    # ~ def __init__(self,first_name,last_name):
        # ~ """初始化父类的属性，再初始化子类的属性"""
        # ~ super().__init__(first_name,last_name)
        # ~ self.privileges=['can add post','can delete post','can ban user']
        
    # ~ def show_privileges(self):
        # ~ for n in self.privileges:
            # ~ print("This admin "+n)
            
             
# ~ Z=Admin('jinrong','shen')
# ~ Z.describe_user()
# ~ Z.show_privileges()


#9-8权限
# ~ class User():
    # ~ def __init__(self,first_name,last_name,age,phone_number):
        # ~ self.first_name=first_name
        # ~ self.last_name=last_name
        # ~ self.age=age
        # ~ self.phone_number=phone_number
       
    # ~ def describe_user(self):
        # ~ print(self.first_name.title()+self.last_name.title())
        
    # ~ def greet_user(self):
        # ~ print("Hello,"+self.first_name.title()+self.last_name.title())
        
        
# ~ class Privileges():
	# ~ def __init__(self):
		# ~ self.privileges=["can add psot","can delete post","can be user"]
		
	# ~ def show_privileges(self):
		# ~ print("The power of admin are:")
		# ~ for privilege in self.privileges:
			# ~ print(privilege)
			

# ~ class Admin(User):
	# ~ def __init__(self,first_name,last_name,age,phone_number):
		# ~ super().__init__(first_name,last_name,age,phone_number)
		# ~ self.privileges=Privileges()
		
		
# ~ user_one=User('james',' harden',30,'17802586130')
# ~ user_one.describe_user()
# ~ user_one.greet_user()

# ~ admin=Admin('james','harden',30,'17802586130')
# ~ admin.privileges.show_privileges()


#9-9	
class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
		
	def get_descriptive_name(self):
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")
		
	def update_odometer(self,mileage):
		if mileage>=self.odometer.reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self,miles):
		self.odometer_reading+=miles

class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	def __init__(self,battery_size=85): 
		"""初始化电瓶的属性"""
		self.battery_size=battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a "+str(self.battery_size)+"-kwh battery.")

	def upgrade_battery(self):
		"""检查电瓶容量"""
		
	
	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程"""
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=270
		message="This car can go approximately "+str(range)
		message+=" miles on a full charge."
		print(message)
		
	
		
class ElectriCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery=Battery()

my_tesla=ElectriCar('tesla','model 3',2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
