#实现stack(以列表的方式来实现堆栈的功能)
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):#将item加入栈顶，无返回值
        return self.items.append(item)
    def pop(self):#将栈顶数据项移除，并返回，栈被修改
        return self.items.pop()
    def peek(self):#"窥视"栈顶数据项，返回栈顶的数但不移除，栈不被修改
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

s=Stack()#创建一个空栈，不包含任何数据项
print(s.isEmpty())    #判断堆栈是否为空，空为True
s.push(4)
s.push('dog')
print(s.peek())
print(s.size())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push('james')
print(s.pop())
