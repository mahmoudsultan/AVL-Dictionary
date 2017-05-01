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
        if newNode.parent is None:
            #has to be new root
            self.root = newNode

    def delete(self,value):
        node = self.search(value,self.root)
        if node is None:
            print("There is no value {} in the tree".format(value))
            return None
        parent = node.parent
        if node.left is None and node.right is None:
            # if leaf we just remove it
            self.deleteLeaf(node)
        elif node.left != None:
            successor = node.left
            while successor.right != None:
                successor = successor.right
            node.value = successor.value
            self.deleteLeaf(successor)
        else:
            #node.right is not None
            successor = node.right
            while successor.left != None:
                successor = successor.left
            node.value = successor.value
            self.deleteLeaf(successor)

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


if __name__ == '__main__':

    tree = AVLTree()
    l = [5,2,8,1,4,7,3]
    for i in range(len(l)):
        tree.insert(l[i])
        tree.printTree()
        print("\n\n\n")
    print("Height is: {}".format(tree.printHeight()))
    # tree.insert(2)
    # tree.printTree()
    # print("\n\n\n")
    #
    # tree.insert(8)
    # tree.printTree()
    # print("\n\n\n")
    #
    # tree.delete(1)
    # tree.printTree()
    # print("\n\n\n")
    #
    # tree.insert(11)
    # tree.printTree()
    # print("\n\n\n")
    #
    # tree.insert(29)
    # tree.printTree()
    # print("\n\n\n")
    #
    # tree.insert(26)
    # tree.printTree()
    # print("\n\n\n")
    #
    # tree.insert(50)
    # tree.printTree()
