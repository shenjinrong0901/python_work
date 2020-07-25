# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum
#
# sum = listsum([1,3,5,7,9])
# print(sum)

#用递归的方法来结局就和问题
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])  #调用了自己
sum = listsum([1,3,5,7,9])
print(sum)