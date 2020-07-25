import time
start = time.process_time()
alist = [54,26,93,17,77,31,44,55,20]
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue
        print(alist)
    return alist
end = time.process_time()
print('Running time :%s Seconds'%(end - start))
print(insertionSort(alist))