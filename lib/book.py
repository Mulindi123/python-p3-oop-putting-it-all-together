#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = title
        self.page_count = page_count
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if isinstance(title, str) and (title.strip() != ""):
            self._title = title
            return self._title
        else:
            print("Wrong title")

    title = property(get_title, set_title)

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if isinstance(page_count, int) and page_count >0:
            self._page_count = page_count
        else:
            print("Wrong page number")
    
    _page_count = property(get_page_count, set_page_count)
       

book = Book("And Then There Were None", 30)
book.title = "I love to read"
book.page_count = " "