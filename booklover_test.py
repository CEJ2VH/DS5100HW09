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
