# from pythonds.basic import Stack
# import string
#
# def infixToPostfix(infixexpr):
#     prec = {}
#     prec["*"] = 3
#     prec["/"] = 3
#     prec["+"] = 2
#     prec["-"] = 2
#     prec["("] = 1
#
#     opStack = Stack()
#     postfixList = []
#
#     tokenList = infixexpr.split()
#
#     for token in tokenList:
#         if token in string.ascii_uppercase:
#             postfixList.append(token)
#         elif token == '(':
#             opStack.push(token)
#         elif token == ')':
#             topToken = opStack.pop()
#             while topToken != '(':
#                 postfixList.append(topToken)
#                 topToken = opStack.pop()
#         else:
#             while (not opStack.isEmpty()) and \
#                 (prec[opStack.peek()] >= prec[token]):
#                      postfixList.append(opStack.pop())
#             opStack.push(token)
#
# #最后若堆栈不为空，则挨个将他们取出来
#     while not opStack.isEmpty():
#         postfixList.append(opStack.pop())
#
#     return " ".join(postfixList)
#
# print(infixToPostfix("( A + B ) * ( C + D )"))

#自己模仿
from pythonds.basic import Stack
import string

def tranfortExpress(expression):
    priority = {}
    priority["/"] = 3
    priority["*"] = 3
    priority["+"] = 2
    priority["-"] = 2
    priority["("] = 1

    emptyStack = Stack()
    emptyList = []

    tokenList = expression.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            emptyList.append(token)
        elif token == '(':
            emptyStack.push(token)
        elif token == ')':
            topToken = emptyStack.pop()
            while topToken != '(':
                emptyList.append(topToken)
                topToken = emptyStack.pop()
        else:
            while (not emptyStack.isEmpty()) and \
                    (priority[emptyStack.peek()] >= priority[token]):
                emptyList.append(emptyStack.pop())
            emptyStack.push(token)
    while not emptyStack.isEmpty():
        emptyList.append(emptyStack.pop())

    return ' '.join(emptyList)

print(tranfortExpress("( A + B ) * ( C + D )"))






