import avl_tree
import functools

"""
Dictionary Functionality Module using AVL Tree implementation
"""


def print_info(fun):
    def wrapper(self, *args):
        functools.update_wrapper(wrapper, fun)
        result = fun(self, *args)
        print("After {} Call: Tree size {}".format(fun.__name__, self.size))
        # print(self.tree.height(self.tree.root))
        return result
    return wrapper

class Dictionary:
    """
    This is a Dictionary Class using AVL Trees
    Attributes
    -------
    size (int): size of the dictionary
    tree (AVL tree): AVL tree of the dictionary

    Methods
    -------
    batch_load (filename :str) -> bool: insert words into the dictionary
        from a file

    insert (word :str) -> bool: insert word into the dictionary
        returns false if the word already exists

    delete (word :str) -> bool: delete word from the dictioanry
        returns false if the word does not exist

    lookup(word :str) -> bool, Node: lookup a word in the dictionary

    batch_lookup (filename :str, print=False) -> int: lookup words from file and returns
        the number of words found (if print=True it prints each word and 'YES' or 'NO'
        next to it)

    batch_delete (filename :str) -> bool: delete words provided by a file from
        the dictionary
    """

    def __init__(self):
        self.size = 0
        self.tree = avl_tree.AVLTree()


    def lookup(self, word):
        """
        searches for word in the dictionary returns if found or not and the
        node in the tree representing it
        """
        # print(self.tree.height(self.tree.root))
        node = self.tree.search(word)
        return True if node else False, node

    def insert(self, word):
        """
        searches for the word first to make sure it's not already in the dictionary
        and if not insert it
        """
        found, node = self.lookup(word)
        if found:
            return False
        self.tree.insert(word)
        self.size += 1
        return True

    def batch_load(self, filename):
        try:
            f = open(filename, 'r')
        except FileNotFoundError as e:
            print("File not found")
            return False
        except IOError as e:
            print(e)
            return False

        for word in f:
            self.insert(word.strip())
        return True

    def delete(self, word):
        """
        deletes the word from the dictionary returns false if the word is not
        in the dictionary
        """
        return True if self.tree.delete(word) else False

    def batch_lookup(self, filename, Print=False):
        """
        Looks up word provided in a file and return the number of words found
        if Print then it will print "{word}: 'YES'/'NO'" for each word
        """
        try:
            f = open(filename, 'r')
        except FileNotFoundError as e:
            print("File not found")
            return False
        except IOError as e:
            print(e)
            return False

        count = 0

        for word in f:
            found, node = self.lookup(word.strip())
            if found:
                count += 1
                if Print:
                    print(word.strip(), ": YES")
            else:
                if Print:
                    print(word.strip(), ": NO")
        return count

    def batch_delete(self, filename):
        """
        deletes word provided in a file from the dictionary, returns a Bool
        """
        try:
            f = open(filename, 'r')
        except FileNotFoundError as e:
            print("File not found")
            return False
        except IOError as e:
            print(e)
            return False

        for word in f:
            self.delete(word.strip())

        return True

    def print_words(self):
        self.tree.printTree()

if __name__ == '__main__':
    my_dictionary = Dictionary()
    my_dictionary.batch_load("words.txt")
    print(my_dictionary.size)
    print(my_dictionary.lookup("Hello"))
    # print(my_dictionary.insert("Hello"))
    # print(my_dictionary.insert("goodbye"))
    # print(my_dictionary.delete("Hello"))
    # print(my_dictionary.lookup("Hello"))
    # print(my_dictionary.batch_lookup("words2.txt", True))
