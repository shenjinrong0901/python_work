import itertools
list1 = [1, 2, 3, 4, 5]
#所有组合结果
print (list(itertools.combinations(list1, 5)))

list2 = [1, 2, 3,4]
#两个list的笛卡儿积相当于排列结果
print(list(itertools.product(list2, list2)))
#从list中排列出repeat个元素
print(list(itertools.product(list2, repeat=4)))

import scipy.special
#排列数计算
print(scipy.special.perm(5,2))
#组合数计算
print(scipy.special.comb(10,2))
