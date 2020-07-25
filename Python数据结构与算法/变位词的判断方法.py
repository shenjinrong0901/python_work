def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26    #标号是0~25
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')  #'a'对应的ASII码是'97',目的是将每个字符变成0~25之间的数
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
        j = 0
        stillOK = True
        #计数器比较
        while j < 26 and stillOK:
            if c1[j] == c2[j]:
                j = j+1
            else:
                stillOK = False
        return stillOK

print(anagramSolution4('apple', 'apple'))

##变位词判断问题
#逐字检查
def anagramSolution(s1,s2):
    alist=list(s2)
    pos1=0
    stillOK=True
    while pos1<len(s1) and stillOK:#循环s1中的每一个字符
        pos2=0
        found=False
        while pos2<len(alist) and not found:
            if s1[pos1]==alist[pos2]:
                found=True
            else:
                pos2=pos2+1
        if found:
            alist[pos2]=None
        else:
            stillOK=False
        pos1=pos1+1
    return stillOK
#print(anagramSolution('abcd','dcba'))
#排序解法
def anagramSolution2(s1,s2):
    alist1=list(s1)
    alist2=list(s2)
    alist1.sort()
    alist2.sort()
    pos=0
    matches=True
    while pos<len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos=pos+1
        else:
            matches=False
    return matches
print(anagramSolution2('abcd','dcba'))
#计数器解法
def anagramSolution3(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')#把a-z转化为0-25   ps:感谢m0_47550366的提醒，此处错误已改正
        c1[pos]=c1[pos]+1#计数
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')  # 把a-z转化为0-25
        c2[pos] = c2[pos] + 1  # 计数
    j=0
    stillOK=True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j=j+1
        else:
            stillOK=False
    return stillOK
print(anagramSolution3('abcd','dcba'))