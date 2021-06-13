class Node:
    def __init__(self,item):
        self.item=item
        self.leftchild=None
        self.rightchild=None

def isFullTree(root):
        if root is None:
            return True
        if root.leftchild is None and root.rightchild is None:
            return True
        if root.leftchild is not None and root.rightchild is not None:
            return (isFullTree(root.leftchild) and isFullTree(root.rightchild))
        return False

root = Node(1)
root.rightchild = Node(3)
root.leftchild = Node(2)
root.leftchild.leftchild = Node(4)
root.leftchild.rightchild = Node(5)
root.leftchild.rightchild.leftchild = Node(6)
root.leftchild.rightchild.rightchild = Node(7)
if isFullTree(root):
    print("The Tree is Full Binary Tree")
else:
    print("The Tree is not a Full Binary Tree")