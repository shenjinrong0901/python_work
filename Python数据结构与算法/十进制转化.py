# from pythonds.basic import Stack
# # def baseConverter(decNumber,base):
# #     digits = "0123456789ABCDEF"
# #
# #     remstack = Stack()  #创建一个堆栈
# #
# #     while decNumber > 0:
# #         rem = decNumber % base  #求余数的除法
# #         remstack.push(rem)
# #         decNumber = decNumber // base  #整除法
# #
# #     newString = ""
# #     while not remstack.isEmpty():
# #         newString = newString + digits[remstack.pop()]
# #
# #     return newString
# #
# # print(baseConverter(20,2))

#用递归的方法来实现进制转换
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base , base) +convertString[n%base]

print(toStr(13,2))