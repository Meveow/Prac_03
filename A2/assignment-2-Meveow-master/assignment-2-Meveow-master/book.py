"""CP1404 - Assignment 2
Evelyn Soong Kar Wai"""


class Book:
    """Represent a Book object."""

    def __init__(self, title="", author="", number_of_pages=0, is_completed=""):
        """Initialise a Book instance."""
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_completed = True if is_completed == "c" else False

    def __str__(self):
        return f"{self.title} by {self.author}, {self.number_of_pages} pages. {self.is_completed} \n"

    def mark_required(self):
        self.is_completed = "r"

    def mark_completed(self):
        self.is_completed = "c"

    def is_long(self):
        if self.number_of_pages > 500:
            return True
        else:
            return False
