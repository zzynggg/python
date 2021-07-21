"""Unit Testing for Task 1 and 2"""
__author__ = 'Brendon Taylor'
__docformat__ = 'reStructuredText'
__modified__ = '20/05/2020'
__since__ = '22/05/2020'

import unittest
from hash_table import LinearProbeHashTable
from dictionary import Statistics, Dictionary


def file_len(filename: str) -> int:
    """Calculates the number of lines in a given file"""
    with open(filename, encoding='UTF-8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


class TestDictionary(unittest.TestCase):
    DEFAULT_TABLE_SIZE = 250727
    DEFAULT_HASH_BASE = 31
    DEFAULT_TIMEOUT = 10
    FILENAMES = ['english_small.txt', 'english_large.txt', 'french.txt']
    RANDOM_STR = 'FIT1008 is the best subject!'

    def setUp(self) -> None:
        """ Used by our test cases """
        self.dictionary = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)

    def test_init(self) -> None:
        """ Testing type of our table and the length is 0 """
        self.assertEqual(type(self.dictionary.hash_table), LinearProbeHashTable)
        self.assertEqual(len(self.dictionary.hash_table), 0)

    def test_load_dictionary_statistics(self) -> None:
        """ For each file, doing some basic testing on the statistics generated """
        statistics = Statistics()
        for filename in TestDictionary.FILENAMES:
            words, time, collision_count, probe_total, probe_max, rehash_count = statistics.load_statistics(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE * 2, filename, TestDictionary.DEFAULT_TIMEOUT)
            self.assertGreater(words, 0)
            self.assertLess(time, TestDictionary.DEFAULT_TIMEOUT)
            # TODO: Add your own test cases here

        dic = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)
        # to test the number of collision_count is returned appropriately 
        hashh = LinearProbeHashTable(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)
        self.assertEqual(dic.hash_table.collision_count, hashh.collision_count, "Both collision_count should be the same")
        
        # to test the number of rehash_count is returned appropriately 
        self.assertEqual(dic.hash_table.rehash_count, hashh.rehash_count, "Both rehash_count should be the same")

        # to test the number of probe_max is returned appropriately 
        self.assertEqual(dic.hash_table.probe_max, hashh.probe_max, "Both probe_max should be the same")

    def test_load_dictionary(self) -> None:
        """ Reading a dictionary and ensuring the number of lines matches the number of words
            Also testing the various exceptions are raised correctly """
        for filename in TestDictionary.FILENAMES:
            self.dictionary = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)
            words = self.dictionary.load_dictionary(filename)
            lines = file_len(filename)
            self.assertEqual(words, lines, "Number of words should match number of lines")

        # TODO: Add your own test cases (consider testing exceptions being raised) 
        dic = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)
        # Test the counter and the length of english_small.txt is matched
        words = dic.load_dictionary("english_small.txt", None)
        self.assertEqual(words, dic.counter, "The counter for english_small.txt is incorrect")
            
        # Test the counter and the length of english_large.txt is matched 
        words = dic.load_dictionary("english_large.txt", None)
        self.assertEqual(words, dic.counter, "The counter for english_large.txt is incorrect")

        # Test if pre-condition is enforced correctly (times out raise TimeoutError)
        # It takes some times to run around(105.523s)
        with self.assertRaises(TimeoutError, msg= "Exceeded time limit should have raised TimeoutError"):
            dic.load_dictionary("french.txt", 100)

    def test_add_word(self) -> None:
        """ Testing the ability to add words """
        # TODO: Add your own test cases
        
        # to test the new word added successfully is converted into lower case (upper case)
        new_word = "YONG"
        self.dictionary.add_word(new_word)
        self.assertTrue(self.dictionary.find_word, "new_word failed to add")
        
        # to test for normal valid input (lower case)
        new_word = "yonggg"
        self.dictionary.add_word(new_word)
        self.assertTrue(self.dictionary.find_word, "new_word failed to add")
       
        # to test for integer input (string int)
        new_word = "123"
        self.dictionary.add_word(new_word)
        self.assertTrue(self.dictionary.find_word, "new_word failed to add")
        

    def test_find_word(self) -> None:
        """ Ensuring both valid and invalid words """
        # TODO: Add your own test cases
        
        # to test the upper case added word can be found in hash table (True)
        dic = Dictionary(self.DEFAULT_HASH_BASE, self.DEFAULT_TABLE_SIZE)
        added_word = "SNOOBII"
        self.dictionary.add_word(added_word)
        self.assertTrue(self.dictionary.find_word(added_word), "The word is not in the hash table")

        # to test the lower case added word can be found in hash table (True)
        added_word = "snoopyy"
        self.dictionary.add_word(added_word)
        self.assertTrue(self.dictionary.find_word(added_word), "The word is not in the hash table")

        # to test the added word CANNOT be found in hash table (False)
        added_word = "Snoobii"
        self.dictionary.add_word(added_word)
        self.assertTrue(not self.dictionary.find_word("Biisnoo"), "The word is not in the hash table")
        

    def test_delete_word(self) -> None:
        """ Deleting valid words and ensuring we can't delete invalid words """
        self.dictionary.load_dictionary('english_small.txt')
        table_size = len(self.dictionary.hash_table)
        with self.assertRaises(KeyError):
            self.dictionary.delete_word(TestDictionary.RANDOM_STR)
        self.assertEqual(len(self.dictionary.hash_table), table_size)

        self.dictionary.delete_word('test')
        self.assertEqual(len(self.dictionary.hash_table), table_size - 1)


if __name__ == '__main__':
    unittest.main()

