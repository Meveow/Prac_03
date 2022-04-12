"""
CP1404 2022SP1 Assignment - 1 Reading Tracker 1.0
Name: Evelyn Soong Kar Wai
Date started: 11 April 2022
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-Meveow
"""

FILENAME = "books.csv"

def main():
    """Introduction and open file."""
    print("Reading Tracker 1.0 - by Evelyn Soong")
    input_file = open(FILENAME)
    menu()

def menu():
    "Four choices in the menu."
    choice = ''
    while choice != 'q':
        print("Menu:\nL - List all books\nA - Add new book\nM - Mark a book as completed\nQ-Quit\n>>> ")
    choice = input("Choose: ").lower()
    if choice == 'l':
        list_books()
    elif choice == 'a':
        add_new()
    elif choice == 'm':
        mark_complete()
    elif choice == 'q':
        quit()
    else:
        print("Invalid menu choice")

def list_books():
    for line in input_file:
        print(line)

def add_new():
    new_book = input("Title: ")
    if new_book == ' ':
        print("Input can not be blank")
        new_author = input("Author: ")
        if new_author == ' ':
            print("Input can not be blank")
            pages = int(input("Pages: "))
            if pages == ' ' or pages <= 0:
                print("Invalid input; enter a valid number")
    FILENAME.append(new_book, new_author, pages)
    print(f"{new_book} by {new_author}, ({pages} pages) added to Reading Tracker")
    menu()

def mark_complete():

    pass

def quit():
    pass
    input_file.close()

main()