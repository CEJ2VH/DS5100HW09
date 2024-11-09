import pandas as pd
class BookLover():
    """Description

    Attributes
    ----------
    Name
    Email
    Fav_genre
    Num_Books= # books read, or size of list passed
    Book list
    
    Methods
    -------
    __init__(self, ticker, sector, prices):
        Constructor
    
    def add_book(self,new_book_name,book_rating):
    Adds a book and rating, as long as it doesn't already exist
       
    def has_read(self, book_name_check):
    takes a book name and sees if it's in the list
    
    num_books_read(self):
    returns the length of book list
    
    def fav_books(self):
    Returns book list for all books with a rating of 4 or higher

    """
 
    
    def __init__(self, name, email, fav_genre, num_books = 0,book_list = pd.DataFrame({'book_name':[], 'book_rating':[]}) ):
        self.name = name
        self.email=email
        self.fav_genre=fav_genre
        self.num_books=num_books
        self.book_list=book_list

    def add_book(self,new_book_name,book_rating):
        for x in self.book_list['book_name']:
            if x == new_book_name:
                #Printing out a response and not telling the user 
                print("Error: This book is already in your book list!")
                break
        else:
            new_book = pd.DataFrame({'book_name': [new_book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)      
        
    def has_read(self, book_name_check):
        read_check=False 
        if book_name_check in self.book_list['book_name'].values:
                read_check=True
        return read_check
    
    def num_books_read(self):
        num_books=len(self.book_list.index)
        return num_books
        
    def fav_books(self):
        fav_books_list = self.book_list.loc[self.book_list['book_rating'] > 3]
        return fav_books_list
