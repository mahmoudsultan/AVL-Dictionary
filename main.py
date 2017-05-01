import dictionary

w = """Dictionary Using AVL Tress \n Essam Emad - Mahmoud Magdy \n Data Structures Lab 2
    Command format:
        {operation} {arguments}
            {arguments} could be a filename or a word

    List of Operations:
        display: to display messages from the batch_lookup
        batch_load: to load dictionary from a file
        batch_delete: to delete words from the dictionary provided by a file
        batch_lookup: to lookup words provided by a file
        insert: to insert a word in the dictionary
        delete: to delete a word from the dictionary
        lookup: to lookup a word
        print: to print words in the trees
        exit: to terminate the program
"""

def main():
    dict = dictionary.Dictionary()
    display = False
    print(w)
    command, args = "", ""
    while command != "exit":
        line = input(">>> ").split(' ')
        if len(line) == 0 or len(line) > 2:
            continue
        elif len(line) == 1:
            command = line[0]
            if command == 'display':
                display = not display
            elif command == 'print':
                dict.print_words()
            continue
        else:
            command, args = line

        if command in ['insert', 'delete', 'batch_load', 'batch_delete']:
            dict.print_info()
            print(dict.__getattribute__(command)(args))
            dict.print_info()
        elif command == 'batch_lookup':
            print("Found: ", dict.batch_lookup(args, display))
        elif command == 'lookup':
            found, _ = dict.lookup(args)
            print("Word is in the Dictionary" if found else "Word is not in the Dictionary")

if __name__ == '__main__':
    main()
