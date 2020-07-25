#无序列表
# def sequentialSearch(alist,item):
#     pos = 0
#     found = False
#
#     while pos < len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos = pos +1
#     return found
# print(sequentialSearch([1,2,3,4,5,6,7,89],9))

#有序列表
# import time
# starttime = time.time()
# def orderedSequentialSearch(alist,item):
#
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#
#     return found
#
# print(orderedSequentialSearch([1,4,5,7,8,9,14,15,16,49,70],70))
# endtime = time.time()
# runtime = endtime - starttime
# print('runtime:', runtime)

#二分搜索
def binarySearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found =True
        else:
            if item < alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint + 1
    return found
print(binarySearch([1,4,5,6,7,9,45,56,78,89,93,99],89))

#二分搜索的递归版本
def binarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)
            