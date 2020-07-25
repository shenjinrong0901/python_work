def BinaryTree(r):
    return [r,[],[]]

##列表之列表的方法表示数
#①插入左子树
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) >1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

#②插入右子树
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) >1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

##利用节点与引用的方法表示数
#BinartTree类
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

#插入左子树
def insertLeft(self,newNode):
    if self.leftChild == None:
        self.leftChild = BinaryTree(newNode)
    else:
        t = BinaryTree(newNode)
        t.left = self.leftChild
        self.leftChild = t

#插入右子树
def insertRight(self,newNode):
    if self.rightChild == None:
        self.rightChild = BinaryTree(newNode)
    else:
        t = BinaryTree(newNode)
        t.right = self.rightChild
        self.rightChild = t