from pythonds.trees import BinaryTree

r = BinaryTree('a')
a = r.getRootVal()
print(a)
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
