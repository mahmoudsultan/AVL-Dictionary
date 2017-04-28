class AVLTree:
    """Class encapsulating the AVL Tree
    An empty subtree is defined to have a height of -1
    Use only the following methods:
    insert: to insert a value into the Tree
    delete: delete a value from the Tree
    search: returns the node containing the passed value or None if not found
    height: returns the height of the given node. Use height(tree.root) to get the height of the tree
    """

    def __init__(self):
        self.root = None
    def insert(self, value, node = -1):
        if self.root is None:
            #must be first insert
            self.root = Node(value)
            return
        if node == -1:
            node = self.root #because python doesn't support overloading :/
        print("\n new insert \n")
        if(value > node.value):
            #insert in right subtree
            if node.right is None:
                child = Node(value)
                child.parent = node
                child.height = -1
                node.right = child
            else:
                self.insert(value,node.right)
        else:
            if node.left is None:
                child = Node(value)
                child.parent = node
                child.height = -1
                node.left = child
            else:
                self.insert(value,node.left)
        #after each recursive call update the height and balance
        parent = node.parent
        newNode = None
        if parent != None:
            newNode = self.balance_if_needed(node)
            isLeftChild = parent.left == node
            newNode.parent = parent
            if isLeftChild:
                parent.left = newNode
            else:
                parent.right = newNode
        else:
            newNode = self.balance_if_needed(node)
        newNode.height = max(self.height(node.left), self.height(node.right))

    def delete(self,value):
        return
    def search(self,value):
        return
    def height(self, node):
        if node is None:
            return -1
        return node.height

    def printTree(self,node = -1):
        if node == -1:
            node = self.root
        if node is None:
            return
        self.printTree(node.left)
        print(node.value)
        self.printTree(node.right)

    def balance_if_needed(self,node):
        """Treats this node as the root node of 2 subtrees and balances the given graph if it is needed
        returns the new node that is the root node after balancing"""
        if abs(self.height(node.left) - self.height(node.right)) > 1:
            isRight = self.height(node.right) > self.height(node.left)
            biggerChild = node.right if isRight else node.left
            isChildRight = self.height(biggerChild.right)  > self.height(biggerChild.left)
            if isRight != isChildRight:
                # Perform a rotation for child first
                newRoot = self.rotate(isChildRight, biggerChild)
                newRoot.parent = node
                if isRight:
                    node.right = newRoot
                else:
                    node.left = newRoot
            return self.rotate(isRight,node)

        else:
            # Already balanced
            return node

    def rotate(self,isLeft,node):
        """"isLeft is true if it is a left rotation"""
        if isLeft:
            finalNode = node.right
            oldLeft = node.right.left
            node.right.left = node
            node.parent = node.right.left
            node.right = oldLeft
            if oldLeft != None:
                oldLeft.parent = node
            return finalNode

        else:
            finalNode = node.left
            oldRight = node.left.right
            node.left.right = node
            node.parent = node.left.right
            node.left = oldRight
            if oldRight != None:
                oldRight.parent = node
            return finalNode


class Node:
    # def height = None
    # def value = None
    # def left = None
    # def right = None
    # def parent = None

    def __init__(self,value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


tree = AVLTree()
tree.insert(41)
tree.printTree()
tree.insert(20)
tree.printTree()

tree.insert(65)
tree.printTree()

tree.insert(11)
tree.printTree()

tree.insert(29)
tree.printTree()

tree.insert(26)
tree.printTree()

tree.insert(50)
tree.printTree()
