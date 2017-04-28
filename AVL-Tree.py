
class AVL-Tree:
    """Class encapsulating the AVL Tree
    An empty subtree is defined to have a height of -1
    Use only the following methods:
    insert: to insert a value into the Tree
    delete: delete a value from the Tree
    search: returns the node containing the passed value or None if not found
    height: prints the height of the tree
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
    def delete(self,value):

    def search(self,value):

    def height(self):
        if self.root is None:
            return -1
        return self.root.height


    def balance_if_needed(self,node):
        if node.

class Node:
    def height
    def value
    def left
    def right
    def parent

    def __init__(self,value):
        self.value = value
