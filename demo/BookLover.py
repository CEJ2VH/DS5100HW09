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
import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_bookadd = BookLover.BookLover("Huck Finn", "gonefishin@missouri.org", "Picture Books")
        test_bookadd.add_book("The Bible", 2)
        self.assertTrue("The Bible" in test_bookadd.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_add2 = BookLover.BookLover("Dorian Grey", "dontchecktheattic.gov", "Self Help")
        test_add2.add_book("Atlas Shrugged", 3)
        test_add2.add_book("Atlas Shrugged", 3)
        self.assertEqual(test_add2.book_list['book_name'].value_counts()['Atlas Shrugged'], 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_hasread=BookLover.BookLover("Gandalf the Grey", "maiarlover@arda.gov", "Mythology")
        test_hasread.add_book("Beowulf",4)
        self.assertTrue(test_hasread.has_read("Beowulf"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_hasread=BookLover.BookLover("Simba", "justanormallion@aol.com", "Entymology")
        test_hasread.add_book("The Prince",2)
        self.assertFalse(test_hasread.has_read("Recovering From the Loss of a Loved One"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_numbooks = BookLover.BookLover("Jane Bennet", "sistersbeforemisters@pemberly.org", "Romance")
        test_numbooks.add_book("Shakespeare's Sonnets",3)
        test_numbooks.add_book("The Feminine Mystique",4)
        test_numbooks.add_book("He's Just Not that Into You",5)
        test_numbooks.num_books_read()
        expected = 3
        self.assertEqual(test_numbooks.num_books_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        sarahsrecentbooks=BookLover.BookLover("Sarah Hall", "CEJ2VH@virginia.gov", "Historical Fiction")
        sarahsrecentbooks.add_book("Little Women",4)
        sarahsrecentbooks.add_book("The Dutch House",2)
        sarahsrecentbooks.add_book("A Deadly Education",3)
        sarahsrecentbooks.add_book("Queen of the Damned",1)
        sarahfav=sarahsrecentbooks.fav_books()
        fav_nums=sarahfav['book_rating'].to_list()
        favbooks=0
        for nums in fav_nums:
            if nums > 3:
                favbooks += 1
        self.assertTrue(favbooks,len(sarahfav))       
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: C:\Users\Hall\booklover_test.py ===================
test_1_add_book (__main__.BookLoverTestSuite) ... ok
test_2_add_book (__main__.BookLoverTestSuite) ... Error: This book is already in your book list!
ok
test_3_has_read (__main__.BookLoverTestSuite) ... ok
test_4_has_read (__main__.BookLoverTestSuite) ... ok
test_5_num_books_read (__main__.BookLoverTestSuite) ... ok
test_6_fav_books (__main__.BookLoverTestSuite) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.034s

OK
