
class AVL-Tree:
    """Clas encapsulating the AVL Tree
    Use only the following methods:
    insert: to insert a value into the Tree
    """
    def insert(self, node, value):
        if self.root is None:
            #must be first insert
            self.root = Node(value)
            return
        if(value > node.value):
            #insert in right subtree
            if node.right is None:
                child = Node()
                child.value = value
                child.parent = node
                child.height = -1
                node.right = child
                balance(node)
            else:
                insert(node.right,value)
        else:
            if node.left is None:
                child = Node()
                child.value = value
                child.parent = node
                child.height = -1
                node.left = child
                balance(node)
            else:
                insert(node.left,value)

    def balance(self,node):


class Node:
    def height
    def value
    def left
    def right
    def parent

    def __init__(self,value):
        self.value = value
