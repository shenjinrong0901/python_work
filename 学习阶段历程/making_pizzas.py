#方法1
# ~ from pizza1 import make_pizza
# ~ make_pizza(16,'pepperoni')
# ~ make_pizza(12,'musheooms','green peppers')

#方法2
# ~ import pizza1
# ~ pizza1.make_pizza(16,'pepperoni')
# ~ pizza1.make_pizza(12,'musheooms','green peppers')
 

#使用as给函数指定别的名字
# ~ from pizza1 import make_pizza as usa
# ~ usa(16,'pepperoni')
# ~ usa(12,'musheooms','green peppers')

import pizza1 as fn
fn.make_pizza(16,'pepperoni')

from pizza1 import *

make_pizza(16,'pepperoni')
make_pizza(12,'musheooms','green peppers')
