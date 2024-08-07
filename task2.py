# 2. Python Data Structure Challenges in Real-World Scenarios


# Objective: This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.


# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.


# Existing Library Data:


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library). # Done

book1, book2 = library
print(book1)
print(book2)


def duplicate():
    while True:

        title =  input("Insert book title or enter quit\n")
        if title == 'quit':
            break
        author = input("Insert author\n")
        if (title, author) not in library:
            library.append((title, author))
            print(library)
        else:
            print("Duplicate book found.")

duplicate()