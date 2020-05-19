def menu():
    file = open("Books.txt", "w")
    file.write("1. The Old Man an the Sean\n")
    file.write("2. Song Offerings\n")
    file.write("3. The Little Hourse on the Prairie\n")
    file.write("4. Four Quarters\n")
    file.close()

    print("""
    THE FIBOOK LIBRARY PROGRAM

    MENU
    list - Enter the word list to see the updated book collection.
    add - Enter the word add to add a new book to your book library.
    del - Enter the word del to get rid of a book from your book library.
    exit - Enter the word exit to quit the program.
    """)

    option = ""

    while option != "exit":
        option = str(input("Command: "))
        if option == "list":
            book_list()
        elif option == "add":
            add_book()
        elif option == "del":
            del_book()
        elif option == "exit":
            print("Bye now.")
        else:
            print("Invalid command. Please try again.")


def book_list():
    with open("Books.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)


def add_book():
    name = str(input("Name: "))
    with open("Books.txt", "r") as f:
        line_number = len(f.readlines()) + 1
        entry = "{0}. {1}\n".format(line_number, name)
    with open("Books.txt", "a+") as f:
        f.write(entry)
        print("{0} was added to your book collection.\n".format(name))


def del_book():
    delete = int(input("Number: "))
    with open("Books.txt", "r") as f:
        lines = f.readlines()
        print("{} was deleted\n".format(lines[delete - 1]))
    with open("Books.txt", "w") as f:
        for line in lines:
            if lines.index(line) != (delete-1):
                f.write(line)


def main():
    menu()


if __name__ == "__main__":

    main()
