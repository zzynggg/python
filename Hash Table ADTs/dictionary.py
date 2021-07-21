# author: Yong Zi Ying
# Grade: 82.43/95 HD
"""
Task 1 is to create a dictionary class with some methods 
such as load_dictionary, add_word, find_word and delete_word.
Ed can't really support to read english_large.txt and french.txt file
so PyCharm is recommended to test on both file as mentioned above. 

Task 2 is to create a Statistics class with some methods
such as load_statistics and table_load_statistics.
In table_load_statistics will output a csv file named "output_task2.csv"
There's a pdf file named explanation_task2.pdf was attached with some 
explaination and analysis of the graph 
that was plotted from the "output_task2.csv" file.
"""

from referential_array import ArrayR
from hash_table import LinearProbeHashTable
from typing import Tuple
import timeit
import csv

class Statistics:
    # TODO
    """ This class is used to load statistics and output a load statistics table
        in order to create a graph to analys on it. """
    MIN_CAPACITY = 1

    def load_statistics(self, hash_base: int, table_size: int, filename: str, max_time: int) -> Tuple:
        """ Creates a new dictionary with hash_base and table_size and returns the tuple.
        It's depend on the load_dictionary complexity
        :complexity best: O(K), where there is one word read from filename
                          and in __setitem function the first position is empty where K is the 
                          size of the key.
        :complexity worst: O(K + N) when we've searched the entire table in __setitem function
                           where N is the table_size and loop the entire length of filename.
        :pre: the time should not exceed the time limit (handling error)  
        """
        dic = Dictionary(hash_base, table_size)
        
        try:
            timee = dic.end_start
            words = dic.load_dictionary(filename, max_time)
        except TimeoutError:
            words = dic.counter
            timee = max_time
        
        collision_count = dic.hash_table.collision_count
        probe_total = dic.hash_table.probe_total
        probe_max = dic.hash_table.probe_max
        rehash_count = dic.hash_table.rehash_count

        return(words, timee, collision_count, probe_total, probe_max, rehash_count)

    def table_load_statistics(self, max_time:int) -> None:
        """ For each possible combination of values in the table below, 
        uses load_statistics to time how long it takes for load_dictionary to run. 
        For each combination a line should be printed to output_task2.csv 
        :complexity: O(N^3), where N is the length of the filenamee or
                     the length of the hash_base array or the length of 
                     the tablesize array. 
        """
        b = [1, 27183, 250726]
        tablesize = [250727, 402221, 1000081]
        filenamee =  ['english_small.txt', 'english_large.txt', 'french.txt']
        array_size = len(filenamee)**len(filenamee)
        output = ArrayR(max(self.MIN_CAPACITY, array_size))
        m = 0

        for i in range(len(b)):
            for j in range(len(tablesize)):
                for k in range(len(filenamee)):
                    rows = self.load_statistics(b[i], tablesize[j], filenamee[k], max_time)
                    output[m] = [filenamee[k], tablesize[j], b[i], rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]]
                    m += 1

        with open('output_task2.csv', 'w', newline='') as output_task2:
            writer = csv.writer(output_task2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow (["Filename", "Table Size", "b", "Words", "Time", "Collisions", "Probes", "Probe Max", "Rehash"])
            for l in range(len(output)):
                writer.writerow(output[l])
            
class Dictionary:
    # TODO
    """ This class is used to add, find and delete word from the dictionary according to 
        user input option in menu. """

    def __init__(self, hash_base: int, table_size: int) -> None:
        """ Creates a new Hash Table with the given hash base and initial table size, 
        and uses it to initialise the instance variable self.hash_table.
        :complexity: O(1)
        """
        self.hash_table = LinearProbeHashTable(hash_base, table_size)
        self.counter = 0
        self.end_start = 0

    def load_dictionary(self, filename: str, time_limit: int = None) -> int:
        """ Reads a file filename containing one word per line, 
        and adds each word to self.hash_table with integer 1 as the associated data, 
        and returns the number of words successfully read into the hash table.
        :complexity best: O(K), where there is one word read from filename
                          and in __setitem function the first position is empty where K is the 
                          size of the key.
        :complexity worst: O(K + N) when we've searched the entire table in __setitem function
                           where N is the table_size and loop the entire length of filename.
        :raises TimeoutError: when the time_limit is not None 
        :raises TimeoutError: when the self.end_start > time_limit 
        """
        self.counter = 0
        # read file name
        filee = open(filename, "r", encoding='UTF-8')
        start_time = timeit.default_timer() 
        each_lines = filee.readlines()
        for i in each_lines:
            self.hash_table.__setitem__(i.rstrip("\n"), 1)
            self.counter += 1
            end_time = timeit.default_timer() 
            self.end_start = end_time - start_time 
            if time_limit is not None and self.end_start > time_limit:
                filee.close()
                raise TimeoutError ("TIMED OUT!")  
        filee.close()
        return self.counter

    def add_word(self, word: str) -> None:
        """ Adds the given word to the hash table with integer 1 as the associated data. 
        It's depend on the __setitem__ function complexity
        :complexity best: O(K) first position is empty
                           where K is the size of the key
        :complexity worst: O(K + N) when we've searched the entire table
                           where N is the table_size
        """ 
        self.hash_table.__setitem__(word, 1)


    def find_word(self, word: str) -> bool:
        """ Returns True if the word is in the hash table and False otherwise.
        :complexity: O(1)
        """
        return self.hash_table.__contains__(word)
        

    def delete_word(self, word: str) -> None:
        """ Deletes the given word from the hash table.
        It's depend on the __delitem__ function complexity
        :complexity best: O(K) finds the position straight away and doesn't have to rehash
                          where K is the size of the key
        :complexity worst: O(K + N) when it has to rehash all items in the hash table
                           where N is the table size
        :raises KeyError: When a word can't be found in order to delete it
        """
        if self.find_word(word):    # if True
            self.hash_table.__delitem__(word)
        else:
            raise KeyError ("Unsuccessfully delete word. It is not in hash table!") 

    def menu(self) -> None:
        """ Displays a menu and allows the user to read a ﬁle, 
        add a word, ﬁnd a word, delete a word or exit. 
        It also handles any bad user input or errors raised 
        by methods in the class appropriately.   
        :complexity: O(N), where N is either depend on the number of user input option 
                     or depend on the complexity of add_word function or delete_word function
                     or load_dictionary.
        """
        res = ""
        res += "\n--------------------------\n"
        res += "1. Read File\n"
        res += "2. Add Word\n"
        res += "3. Find Word\n"
        res += "4. Delete Word\n"
        res += "5. Exit\n"
        res += "--------------------------"
        print(res)
        opt = int(input("Enter option: "))
        while opt <5:

            if opt == 1:
                """ Read file """
                filee = str(input("Enter filename: "))
                if filee == "":
                    print("[" + filee + "] Invalide filename")
                else:
                    self.load_dictionary(filee, None)
                    print("Successfully read file")
                print("--------------------------")

            elif opt == 2:
                """ Add Word """
                addd = str(input("Enter word: "))
                if addd == "":
                    print("[" + addd + "] Invalide word")
                else:
                    self.add_word(addd.lower())
                    print("[" + addd + "] Successfully added")
                print("--------------------------")

            elif opt == 3:
                """ Find Word """
                findd = str(input("Enter word: "))
                tem = self.find_word(findd.lower())
                if tem:
                    print("[" + findd + "] Found in dictionary")
                else:
                    print("[" + findd + "] Not found in dictionary")
                print("--------------------------")

            elif opt == 4:
                """ Find Word """
                dell = str(input("Enter word: "))
                if dell == "":
                    print("[" + dell + "] Invalide word")
                else:
                    self.delete_word(dell.lower())
                    print("[" + dell + "] Deleted from dictionary")
                print("--------------------------")

            else:
                print("Invalid input")
                print("Please Try Again!")

            print(res)
            opt = int(input("Enter option: "))

if __name__ == '__main__':
    # TODO
    pass
    #dic = Dictionary(31, 17)
    #dic.menu()
    #stat = Statistics()
    #stat.table_load_statistics(10)

