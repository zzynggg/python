# author: Yong Zi Ying
"""
Task 3 is to create a new class which is Frequency class with some methods 
such as add_file and rarity. 

This task is add a new function into Frequency class which is ranking funciton.
A function frequency_analysis is created outside the Frequency class in order
to output the ranking, the word frequency and the rarity of word.
"""

from hash_table import LinearProbeHashTable
from dictionary import Dictionary
from list_adt import ArrayList
from enum import Enum
from typing import Tuple
from string import punctuation
import sys


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    MISSPELT = 3


class Frequency:
    # TODO
    """ This class is to make sure that the new word from the filename file is added into 
        a new hash table and determine the word Frequency. The ranking will be determined as well. """
    MIN_CAPACITY = 1
    def __init__(self)->None:
        """ Initialises a new Hash Table, as well as an instance of Dictionary.
        :Complexity: O(1)
        """
        self.new_hash_table = LinearProbeHashTable(250726, 1000081)
        self.dic = Dictionary(250726, 1000081)  #based on task 2 observation 
        self.dic.load_dictionary("english_large.txt", 10) 
        self.max_word = ("", 0)

    def add_file(self, filename:str)->None:
        """ Reads each word from filename into the hash table, 
        and its data is the number of times the word has been read into the hash table. 
        :complexity best: O(P*Q), where P is the length of the line that read from a 
                          specific filename, Q is the length of word of each line
                          and first position is empty in __setitem__ function.
        :complexity worst: O(P*Q*(K+N)), where P is the length of the line that read from a 
                           specific filename, Q is the length of word of each line,
                           K is the size of the key and when we've searched the entire table
                           where N is the table_size
        """
        filee = open(filename, "r",encoding='UTF-8')
        each_lines = filee.readlines()
        for i in each_lines: 
            wordd = i.split()
            for j in wordd:
                each_word = j.strip(punctuation).lower()
                if self.dic.find_word(each_word):      # if it's in dictionary 
                    if not each_word in self.new_hash_table: # if it's not in hash table
                        self.new_hash_table[each_word] = 1                  
                    else:
                        self.new_hash_table[each_word] = self.new_hash_table[each_word]+1
                    if self.new_hash_table[each_word] > self.max_word[1]:
                        self.max_word = (each_word, self.new_hash_table[each_word])
        filee.close()
        
    def rarity(self, word: str) -> Rarity:
        """  Given a word, returns its rarity score as an enumerated value.
        It's depend on the __setitem__ function complexity
        :complexity best: O(K) first position is empty
                           where K is the size of the key
        :complexity worst: O(K + N) when we've searched the entire table
                           where N is the table_size
        :pre: the word should be found (handling error) 
        """    
        try:
            occurences = self.new_hash_table[word]
        except KeyError:
            return Rarity.MISSPELT

        if occurences >= self.max_word[1]/100:
            return Rarity.COMMON
        elif occurences < self.max_word[1]/1000:
            return Rarity.RARE
        elif occurences < self.max_word[1]/100 and occurences >= self.max_word[1]/1000:
            return Rarity.UNCOMMON


    def ranking(self) -> ArrayList[Tuple]:
        """ Returns a list of known words (word, frequency) ordered by their frequency count 
        in descending order. The returned list of words must be have been sorted by Quicksort. 
        :complexity: O(N), where N is the length of the self.new_hash_table.table.
        """
        array_list = ArrayList(max(self.MIN_CAPACITY, len(self.new_hash_table)))
        # must copy and insert all your non-empty (key, value) tuples from the Hash Table  into an ArrayList.
        counter = 0
        for i in range(len(self.new_hash_table.table)):     # O(N)
            if self.new_hash_table.table[i] is not None:
                array_list.insert(counter, self.new_hash_table.table[i])   
                counter += 1
        self.dec_quick_sort(array_list)
        return array_list

    def dec_quick_sort (self, array: ArrayList[Tuple])-> None:
        """ This code is taken from lecture slide.
        Determine the start and end pointer and pass it to quick_sort_aux function.
        :complexity: O(1)
        """
        start = 0
        end = len (array) - 1
        self.quick_sort_aux(array, start, end)

    def quick_sort_aux (self, array: ArrayList[Tuple] , start: int, end: int)-> None:
        """ This code is taken from lecture slide.
        Pass the array, start and end to partition function and call itself again
        to enter the partition funciton to divide and conquer. 
        :complexity: O(Nlog(N)), where log(N) is for the division in partition function
                     and N is for the loop in partition function
        """
        if start < end:
            boundary = self.partition(array, start, end)
            self.quick_sort_aux(array, start, boundary - 1)
            self.quick_sort_aux(array, boundary+1, end)

    def partition(self, array: ArrayList[Tuple] , start: int, end: int)-> int:
        """ This code is taken from lecture slide.
        Divide and conquer the array and sort it before returned.
        :complexity: O (NlogN), where log(N) is happen in the division
                     and N is the length of end+1
        """
        mid = (start+end)//2        # log(N)
        pivot = array[mid][1]
        self.swap(array, start, mid)
        boundary = start
        for k in range(start+1, end+1):     # O(N)
            if array[k][1] > pivot:
                boundary += 1
                self.swap(array, k, boundary)
        self.swap(array, start, boundary)
        return boundary

    def swap(self, array: ArrayList[Tuple] , start: int, end: int)-> None:
        """ Exchange the position of elements.
        :complexity:O (1)
        """
        array[start], array[end] = array[end], array[start]
        

def frequency_analysis() -> None:
    """ Creates an instance of class Frequency, adds 215-0.txt to it and generates the ranking list. 
    It should prompt the user for the number of rankings to show. 
    :complexity: Not required 
    :raises ValueError: if the input value is lesser than equal to zero
    :pre: input value should bigger than zero (handling)
    :pre: input value should be interger ONLY (handling)
    """
    # TODO
    fre = Frequency()
    fre.add_file("215-0.txt")
    rank = fre.ranking()
    flag = True
    counter = 0
    ranking_counter = 1
    
    while flag:
        try:
            wordss = int(input("Please enter a frequency: "))
            if wordss <= 0:
                raise ValueError ("Frequency should be larger than zero.")

        except(TypeError, ValueError):
            print("Please enter a valid frequency.\n")

        else:
            flag = False
    
    while wordss != 0:
        # output ranking, word, frequency, rarity of the word
        print("Ranking: ", ranking_counter, "| Word: ", rank[counter][0], "| Frequency: ",rank[counter][1], "| Rarity: ", fre.rarity(rank[counter][0]))
        counter += 1
        wordss -= 1
        ranking_counter += 1
        

if __name__ == '__main__':
    frequency_analysis()
