class AVLTree:
    """Class encapsulating the AVL Tree
    An empty subtree is defined to have a height of -1
    Use only the following methods:
    insert: to insert a value into the Tree
    delete: delete a value from the Tree
    search: returns the node containing the passed value or None if not found
    height: returns the height of the given node. Use height(tree.root) to get the height of the tree
    printHeight: Recursively computes the height of the tree and prints it out
    """

    def __init__(self):
        self.root = None
    def insert(self, value, node = -1):
        if self.root is None:
            #must be first insert
            self.root = Node(value)
            self.root.height = 0
            return
        if node == -1:
            node = self.root #because python doesn't support overloading :/
        # print("\n new insert \n")
        if(value > node.value):
            #insert in right subtree
            if node.right is None:
                child = Node(value)
                child.parent = node
                child.height = 0
                node.right = child
            else:
                self.insert(value,node.right)
        else:
            if node.left is None:
                child = Node(value)
                child.parent = node
                child.height = 0
                node.left = child
            else:
                self.insert(value,node.left)
        #after each recursive call update the height and balance
        parent = node.parent
        newNode = None
        if parent != None:
            isLeftChild = parent.left == node
            newNode = self.balance_if_needed(node)
        else:
            newNode = self.balance_if_needed(node)
        if newNode != None:
            self.root = newNode
            newNode.height = max(self.height(node.left), self.height(node.right)) + 1

    def delete(self,value, node = -1):
        if node == -1:
            node = self.search(value,self.root)
        # print("On Delete ROOT IS: {}".format(self.root.value))
        if node is None:
            # print("There is no value {} in the tree".format(value))
            return None
        parent = node.parent
        if node.left is None and node.right is None:
            # if leaf we just remove it
            self.deleteLeaf(node)
        elif node.left is None or node.right is None:
            child = node.left if node.left != None else node.right
            child.parent = parent
            if parent != None:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
            self.balance_if_needed(parent)
            node.parent = None
        else:
            #both of them are not none
            successor = node.left
            while successor.right != None:
                successor = successor.right
            node.value = successor.value
            successor.value = value
            self.delete(value,successor)

        print("\n AVL PRINTING \n")
        self.printTree()
        print("\n")
        return node

    def deleteLeaf(self,node):
        parent = node.parent
        if parent is None:
            #must be root
            self.root = None

        elif parent.left == node:
            parent.left = None
        else:
            parent.right = None
        node.parent = None
        # print("BEFOREOOARFOIASDN BLAALncinasdifnsadifna")
        self.printTree()
        self.balance_if_needed(parent)

    def search(self,value, node = -1):
        if node == -1:
            node = self.root
        if node is None:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self.search(value,node.left)
        else:
            return self.search(value, node.right)

    def height(self, node):
        if node is None:
            return -1
        return node.height

    def printTree(self,node = -1):
        if node == -1:
            node = self.root
        if node is None:
            # print("ROOT IS: {}".format(self.root.value))
            return
        self.printTree(node.left)
        print("v: {} r: {} l: {} h: {}".format(node.value, node.left != None, node.right != None, node.height))
        self.printTree(node.right)

    def balance_if_needed(self,node):
        """Treats this node as the root node of 2 subtrees and balances the given graph if it is needed
        returns the new node that is the root node after balancing"""
        if node is None:
            return
        height = abs(self.printHeight(node.left) - self.printHeight(node.right))
        # print("HEIGHT IS ADSJFIALSJFALISFD: {}".format(height))
        if  height > 1:
            isRight = self.height(node.right) > self.height(node.left)
            biggerChild = node.right if isRight else node.left
            isChildRight = self.height(biggerChild.right)  > self.height(biggerChild.left)
            if isRight != isChildRight:
                # Perform a rotation for child first
                newRoot = self.rotate(isChildRight, biggerChild)
            return self.rotate(isRight,node)

        else:
            # Already balanced
            return node

    def printHeight(self, node = -1):
        if node == -1:
            node = self.root
        if node is None:
            return -1
        firstHeight = self.printHeight(node.left)
        secondHeight = self.printHeight(node.right)
        bigger = max(firstHeight,secondHeight)
        return bigger + 1

    def rotate(self,isLeft,node):
        """"isLeft is true if it is a left rotation"""
        parent = node.parent
        parentLeft = False
        if parent != None and parent.left == node:
            parentLeft = True
        finalNode = node.right
        if isLeft:
            finalNode = node.right
            oldLeft = finalNode.left
            finalNode.left = node
            finalNode.parent = node.parent
            node.parent = finalNode
            node.right = oldLeft
            if oldLeft != None:
                oldLeft.parent = node

        else:
            # print("Final node before is: {} \n \n".format(finalNode.value))
            # self.printTree()
            finalNode = node.left
            oldRight = finalNode.right
            finalNode.right = node
            finalNode.parent = node.parent
            node.parent = finalNode
            node.left = oldRight
            if oldRight != None:
                oldRight.parent = node
            # print("Final node here is: {} \n \n".format(finalNode.value))
            # self.printTree()
        #adjusting the parent pointer
        if parent != None:
            if parentLeft:
                parent.left = finalNode
            else:
                parent.right = finalNode
        else:
            #has to be the root
            self.root = finalNode
        #temporarly
        if finalNode.left != None:
            finalNode.left.height = max(self.height(finalNode.left.left), self.height(finalNode.left.right)) + 1
        if finalNode.right != None:
            finalNode.right.height = max(self.height(finalNode.right.left), self.height(finalNode.right.right)) + 1
        if parent != None:
            parent.height = max(self.height(finalNode.left), self.height(finalNode.right)) + 1


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
