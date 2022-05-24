"""CP1404 - Assignment 2
Evelyn Soong Kar Wai"""

class Book:
    """Represent a Book object."""

    def __init__(self, title="", author="", number_of_pages=0, requirement):
        """Initialise a Book instance."""
        self.title = title
        self.author = author
        self.number_of_pages = 0
        self.requirement = requirement

    def __str__(self):
        pass

    def requirement(self):
        pass

    def completed(self):
        if book[3] == 'c\n':
            return completed

    def long_book(self, number_of_pages):
        if number_of_pages > 500:
            return long