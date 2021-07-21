# Yong Zi Ying
# 30885027
# assignment3
#%% Task 1
class Node:
    ''' This class is used to create node.
    '''
    def __init__(self, size = 5, uid = 0, asciii = "", frequency = 0, nodeData=[0,0,0]):
        ''' This method is used to create and initialize a new node.
        :Input: The size of link (child) is fixed to 5 including terminal (empty string, $), unique ID that represent each unique word, 
                ascii of the word, frequency and an array with fixed length to store data [ID, asciiSeq, frequency]
        :Output: No output is required
        :Time Complexity: Best and Worst time complexity will be the same which is O (1) for normal initialization 
        :Auxiliary Space Complexity: No extra space is needed
        :Space Complexity: O (1), space complexity is input space + extra space.
                           The input size will be O (1) because the size for self.link is constant (fix to 5) and 
                           the array self.node_data size is fix to length of 3 as well and there’s no extra space needed.
        :Explanation: The size of link is fixed to 5 as the range of character is A to D including terminal. 
                      A unique ID is assigned to each unique word to create a fake link to the last node (terminal). 
                      Ascii is the sequence of the word (“ABC” = “123”). Frequency is used to count the word in the trie.
                      The reason to save each node data into another array is when the pointer is at the last character of 
                      the word (“ABC”, let’s say at “C”) then I need to compare with the value that store in terminal node
                      with current node (“C”) data. I can get the terminal node data from it array without moving the 
                      pointer backward to compare in order to avoid high time complexity for comparison. More details
                      explanation is commented at the code.
        ''' 
        self.link = [None] * size       # new child, $ABCD
        self.unique_id = uid            # to store unique id for each unique word
        self.ascii_word_seq = asciii    # to store the acsii of the word
        self.frequency = frequency      # to store the frequency
        self.node_data = nodeData       # an array to store all node data

class SequenceDatabase:
    ''' This class is used to add new word and search for the query of the word.
    '''
    def __init__(self):
        ''' This method is used to initialize the instances.
        :Input: No input is required
        :Output: No output is required
        :Time Complexity: Best and Worst time complexity will be the same which is O (1) for normal initialization. Same as Node class.
        :Auxiliary Space Complexity: No extra space is needed
        :Space Complexity: Space complexity is input space + extra space.
                           There’s no input size and no extra space needed.
        :Explanation: Create a node starting at root. The reason of creating self.uniqueID is to make it as a 
                      global variable (static) so if a new unique word is added, increment previous ID by 1 will be the new 
                      ID. A new array list is created to store the unique word so that I can get back the word by using the 
                      unique ID that represent the index of the unique word in self.uniqueWord array without looping 
                      through entire array. More details explanation is commented at the code.    
        '''
        self.root = Node()      # first node (source)
        self.uniqueID = 0       # static variable/global
        self.uniqueWord = []    # to store unique word

    def addSequence(self, s):
        ''' This method is used to add new word into the trie recursively.
        :Input: A single word to add. (s)
        :Output: No output is required 
        :Time Complexity: O (s+s) = O (s). Best and Worst time complexity will be the same which is O (s), 
                          where s is the number of characters of the word (s = len(s)) which is same to the 
                          time complexity for addSequenceAux () method. 
        :Auxiliary Space Complexity: O (N), where N is the length of uniqueWord array. It is depending on
                                     the number of times that invoke addSequence() method and 
                                     the uniqueness of each new added word.    
        :Space Complexity: O (s + N), space complexity is input space + extra space.
                           The input space is O (s) where s is the number of characters of word. (s = len(s))
                           The extra space is O (N) where N is the length of uniqueWord array. (explained above).
        :Explanation: A pointer is at the first node of the trie which is root. Loop the word (s) in order to get 
                      the ascii index of each character (“ABC” = “123”).  Invoke addSequenceAux() method to perform 
                      recursion. More details explanation is commented at the code.
        '''
        current_node = self.root    # start from root
        string_ascii_seq = ""
        for char in range(len(s)):  # to get ascii index of each char O (s)
            index = ord(s[char]) - 65 + 1    # $ = 0, A = 1/65
            string_ascii_seq += str(index)
        self.addSequenceAux(current_node, s, 0, string_ascii_seq) # perform recursion O (s)

    def addSequenceAux(self, current_node, s, counter, string_ascii_seq):
        ''' This method is used to create new node for each unique character if it is not existing and 
            add or update data to each node.
        :Input: Current node that the pointer is pointed at, word (s), a counter, the sequence of ascii word index. 
        :Output: No output is required. 
        :Time Complexity: Best and Worst time complexity will be the same which is O (s), 
                          where s is the number of characters of the word (s = len(s)). 
                          The time complexity for compWord () method will be O (1). (explained in compWord())
        :Auxiliary Space Complexity: O (N), where N is the length of uniqueWord array. It is depending on
                                     the number of times that invoke addSequence() method and 
                                     the uniqueness of each new added word.    
        :Space Complexity: O (s + N), space complexity is input space + extra space.
                           The input space is O (2s) = O (s) where s is the number of characters of word (string) and 
                           the sequence of ascii word index will be O (s) too. The rest of the input will be constant.
                           The extra space is O (N) where N is the length of uniqueWord array. (explained above).
        :Explanation: Loop the word recursively to either create new node or update the current pointer if the node is exist. 
                      By going into the list no data will be added into each node when it recurse back the unique ID, ascii 
                      index sequence, frequency and nodeData array of the node is updated. As the data in each node will
                      be the OPTIMAL data means at each Node the unique ID is used to create a fake link to link the node
                      with the terminal node with the same Unique ID in order to avoid high time complexity. 
                      If higher frequency is found then update the frequency for each node 
                      else if the frequency is the same, smaller lexicography word will be chosen. 
                      There is a compWord() method to search for the smaller lexicography word with O (1) time complexity. 
                      More details explanation is commented at the code.
        '''
        if counter == len(s): # base case
            index = 0
            if current_node.link[index] is None:            # terminal doesn't exist
                current_node.link[index] = Node()           # create new node
                current_node = current_node.link[index]     # update pointer
                # save current wordID, ascii and freq at leaf #
                current_node.ascii_word_seq = string_ascii_seq   # sequence of acsii word index 
                self.uniqueID += 1              # update the ID with previous ID + 1 
                current_node.unique_id = self.uniqueID      # assign unique id to the new unique word
                self.uniqueWord.append(s)       # append new unique word into an array
                current_node.frequency += 1     # update frequency
            else:   # terminal exist
                current_node = current_node.link[index]     # update pointer
                current_node.frequency += 1     # update frequency
            # store node data into node data array
            current_node.node_data = [current_node.unique_id, current_node.ascii_word_seq, current_node.frequency]
            return current_node.node_data   

        else:   # induction 
            index = ord(s[counter]) - 65 + 1                # $ = 0, A = 1
            if current_node.link[index] is None:            # node not exist
                current_node.link[index] = Node()           # creating new node                
                current_node = current_node.link[index]     # update pointer
            else:   # node exist
                current_node = current_node.link[index]     # update pointer
            newString = self.addSequenceAux(current_node, s, counter+1, string_ascii_seq)   # recurse
            # ~~ recurse back ~~ 
            if newString[2] > current_node.node_data[2]:    # bigger frequency found
                current_node.unique_id = newString[0]       # update the ID
                current_node.ascii_word_seq = newString[1]  # update the sequence of ascii word index
                current_node.frequency = newString[2]       # update the freq
                # save the optimal data into current node
                current_node.node_data = [current_node.unique_id, current_node.ascii_word_seq, current_node.frequency]
            elif newString[2] == current_node.node_data[2]: # same freq found
                if newString[1][0] < current_node.node_data[1][0]:    # if new string(previous) first char smaller than current string first char
                    current_node.unique_id = newString[0]   # update the ID
                    current_node.ascii_word_seq = newString[1]        # update the sequence of ascii word index
                    current_node.frequency = newString[2]   # update the freq
                    # save the optimal data into current node
                    current_node.node_data = [current_node.unique_id, current_node.ascii_word_seq, current_node.frequency]         
                elif newString[1][0] == current_node.node_data[1][0]: # if new string (previous) first char == current string first char 
                    # search for the smaller lexi 
                    small_lexi = self.compWord(newString[0], newString[1], current_node.node_data[0], current_node.node_data[1])
                    current_node.unique_id = small_lexi[0]  # update the ID
                    current_node.ascii_word_seq = small_lexi[1]        # update the sequence of ascii word index
                    current_node.frequency = newString[2]   # update the freq
                    # save the optimal data into current node
                    current_node.node_data = [current_node.unique_id, current_node.ascii_word_seq, current_node.frequency]
                    
            # IF query is "" save the optimal data at ROOT #
            if newString[2] > self.root.node_data[2]:       # bigger frequency found
                self.root.unique_id = newString[0]          # update the root's ID
                self.root.ascii_word_seq = newString[1]     # update the root's sequence of acsii word index
                self.root.frequency = newString[2]          # update the root's frequency
                # update the root's array with optimal data
                self.root.node_data = [self.root.unique_id, self.root.ascii_word_seq, self.root.frequency] 
            elif newString[2] == self.root.node_data[2]:  # same freq found
                if newString[1][0] < self.root.node_data[1][0]:     # if new string (previous) first char smaller than root string first char
                    self.root.unique_id = newString[0]      # update the root's ID
                    self.root.ascii_word_seq = newString[1] # update the root's sequence of acsii word index
                    self.root.frequency = newString[2]      # update the root's frequency
                    # update the root's array with optimal data
                    self.root.node_data = [self.root.unique_id, self.root.ascii_word_seq, self.root.frequency]  
                elif newString[1][0] == self.root.node_data[1][0]:   # if new string (previous) first char == root string first char 
                    # search for the smaller lexi 
                    small_lexi = self.compWord(newString[0], newString[1], self.root.node_data[0], self.root.node_data[1])
                    self.root.unique_id = small_lexi[0]     # update the root's ID
                    self.root.ascii_word_seq = small_lexi[1]# update the root's sequence of acsii word index
                    self.root.frequency = newString[2]      # update the root's frequency
                    # update the root's array with optimal data
                    self.root.node_data = [self.root.unique_id, self.root.ascii_word_seq, self.root.frequency]

            return current_node.node_data
            
    def compWord(self, newWordID, newWord, oldWordID, oldWord):
        ''' This method is used to compare 2 strings and get the smaller lexicography word.
        :Input: First word’s ID, first word, second word’s ID and second word.
        :Output: The smaller lexicography of word’s ID and word.
        :Time Complexity: Best and Worst time complexity will be the same which is O (1) as it is just a simple comparison.
        :Auxiliary Space Complexity: O (K), where K is the length of smaller_lexi array which is fixed to length of 2.
        :Space Complexity: O (N + M + K), space complexity is input space + extra space.
                           The input space is O (N + M) where N is the number of characters in the first word 
                           and M is the number of characters in the second word.
                           The extra space is O (K), where K is the length of smaller_lexi array which is fixed to length of 2. (explained above). 
        :Explanation: Subtracting both word length (“1234”,”123”) and get the differences (N). 
                      The word with smaller length will append with N number of 0. 
                      After appending it, both words will have the same length. 
                      The longer length of word is used to subtract the updated shorter length of word (“1234 - 1230”). 
                      If the differences are positive means the updated shorter length of word have smaller lexicography of word 
                      else if the differences are negative means the longer length of word have smaller lexicography of word. 
                      The ID and the word of the smaller lexicography word will return. 
                      If both words have same length, there is not needed to append extra zero. 
                      More details explanation is commented at the code.    
        '''
        newWordlen = len(newWord)
        oldWordlen = len(oldWord)
        temp_new = newWord  # prevent ori word been changed
        temp_old = oldWord  # prevent ori word been changed
        smaller_lexi = []   # to return smaller lexi ID and word
        if oldWordlen > newWordlen:
            lenNeeded = oldWordlen - newWordlen     # x
            temp_new += str(0)*lenNeeded            # shorter word need to append x num of 0
            diff = int(oldWord) - int(temp_new) 
            if diff < 0:    # neg = oldword smaller
                smaller_lexi = [oldWordID, oldWord]
                return smaller_lexi 
            elif diff > 0:  # pos = newword smaller
                smaller_lexi = [newWordID, newWord]
                return smaller_lexi 
        elif oldWordlen < newWordlen:
            lenNeeded = newWordlen - oldWordlen     # x
            temp_old += str(0)*lenNeeded            # shorter word need to append x num of 0
            diff = int(newWord) - int(temp_old) 
            if diff < 0:    # neg = newword smaller
                smaller_lexi = [newWordID, newWord]
                return smaller_lexi 
            elif diff > 0:  # pos = oldword smaller
                smaller_lexi = [oldWordID, oldWord]
                return smaller_lexi 
        elif oldWordlen == newWordlen:  # normal comparison
            diff = int(newWord) - int(oldWord)
            if diff < 0:    # neg = neword smaller
                smaller_lexi = [newWordID, newWord]
                return smaller_lexi 
            elif diff > 0:  # pos = oldword smaller
                smaller_lexi = [oldWordID, oldWord]
                return smaller_lexi 
            elif diff == 0: # both exactly the same
                smaller_lexi = [oldWordID, oldWord]
                return smaller_lexi 

    def query(self, q):
        ''' This method is used to search the given string (query) from the trie.
        :Input: A string (q)
        :Output: A word with higher frequency or high frequency with smaller lexicography word
        :Time Complexity: Best and Worst time complexity will be the same which is O (q), 
                          where q is the number of characters of the word (q = len(q)).
        :Auxiliary Space Complexity: No extra space is needed.
        :Space Complexity: O (q), space complexity is input space + extra space.
                           The input space is O (q), where q is the number of characters of the word (q). 
                           There is no extra space needed (explained above). 
        :Explanation: Now, the unique ID is used to find the word with higher frequency or high frequency 
                      with smaller lexicography word within the trie. The unique ID is used to retrieve the word with 
                      higher frequency or high frequency with smaller lexicography word from the uniqueWord array. 
                      The first index of uniqueWord array is 0 and the first unique ID is 1. Thus, unique ID need to 
                      decrement by 1 in order to tally with the index in uniqueWord array. IF the query is “” then the first
                      link (height =1) with higher frequency or high frequency with smaller lexicography word will return 
                      else if the input string is not existing in the trie, return None. More details explanation is commented at the code.
        '''
        current_node = self.root     # start from root
        result = ""

        if q == "":     # constant
            if len(self.uniqueWord) != 0: # trie has at least 1 word
                return self.uniqueWord[self.root.unique_id-1]   # global data is saved at root
            else:       # no string in trie
                return None   

        for char in q:
            index = ord(char) - 65 + 1    # convert ascii to index
            if current_node.link[index] is not None:      # exist
                # uniqueArray at index 0 == uniqueID at index 1
                current_node = current_node.link[index]   # update pointer
                result = self.uniqueWord[current_node.unique_id-1]
            else:       # q does not exist in trie
                return None 
        return result

#%% Task 2
class SuffixNode:
    ''' This class is used to create new node for suffix trie.
    '''
    def __init__(self, size = 5):
        ''' This method is used to create and initialize a new node.
        :Input: The size of link (child) is fixed to 5 including terminal (empty string, $)
        :Output: No output is required
        :Time Complexity: Best and Worst time complexity will be the same which is O (1) for normal initialization. 
        :Auxiliary Space Complexity: O (N), where N is the length of self.suffixIndex 
                                     which is depends on the appended suffix index(ID). 
        :Space Complexity: O (N), space complexity is input space + extra space.
                           The input size will be O (1) because the size for self.link is constant (fix to 5).
                           The extra space is O (N), where N is the length of self.suffixIndex (explained above).
        :Explanation: self.suffixIndex is used to append the suffix index of the character of the word. The node 
                      will have more than one suffix index if the character is repeated in the word.
                      More details explanation is commented at the code.
        '''
        self.link = [None] * size 
        self.suffixIndex = []

class PrefixNode:
    ''' This class is used to create new node for prefix trie.
    '''
    def __init__(self, size = 5):
        ''' This method is used to create and initialize a new node.
        :Input: The size of link (child) is fixed to 5 including terminal (empty string, $)
        :Output: No output is required
        :Time Complexity: Best and Worst time complexity will be the same which is O (1) for normal initialization. 
        :Auxiliary Space Complexity: O (N), where N is the length of self.prefixIndex 
                                     which is depends on the appended prefix index(ID). 
        :Space Complexity: O (N), space complexity is input space + extra space.
                           The input size will be O (1) because the size for self.link is constant (fix to 5).
                           The extra space is O (N), where N is the length of self.prefixIndex (explained above).
        :Explanation: self.prefixIndex is used to append the prefix index of the character of the word. The node 
                      will have more than one prefix index if the character is repeated in the word.
                      More details explanation is commented at the code.
        '''
        self.link = [None] * size 
        self.prefixIndex = []

class OrfFinder:
    ''' This class is used to create a suffix trie and prefix trie. 
        The given start and end is used to find the substring with the start and the end without overlapping.
    '''

    def __init__(self, input_word):
        ''' This method is used to initialize all global variable and invoke suffixAddWord method and 
            prefixAddWord method to create suffix trie and prefix trie.
        :Input: An input word. (input_word)
        :Output: No output is required. 
        :Time Complexity: O (2(N**2)) = O (N**2). Best and Worst time complexity will be O (N**2), 
                          where N is the length of input_word. The time complexity for suffixAddWord and 
                          PrefixAddWord are O (N**2) each, O (N**2 + N**2) = O (2 (N**2)). 
                          More details explanation will be elaborated at each method. 
        :Auxiliary Space Complexity: No extra space is required. 
        :Space Complexity: O (N), space complexity is input space + extra space.
                           The input space is O(N), where N is the length of input_word and 
                           no extra space is needed (explained above).
        :Explanation: The both trie’s counter is used to get the index for each character of the substrings. 
                      It invokes self.suffixAddWord(input_word) to create a suffix trie to get the starting array 
                      and self.prefixAddWord(input_word) to create a prefix trie to get the ending array. 
                      More details explanation will be elaborated at each method and in this method is commented at the code.
        '''
        self.suffixRoot = SuffixNode()              # create the first node for suffix
        self.prefixRoot = PrefixNode()              # create the first node for prefix
        self.inputWord = input_word                 # make it as global,for ref to back ori substring
        self.suffixIndexCounter = 0                 # suffix start from 0 (ascending)
        self.prefixIndexCounter = len(input_word)-1 # prefix start from the last index (descending)
        self.suffixAddWord(input_word)              # create suffix trie
        self.prefixAddWord(input_word)              # create prefix trie

    def suffixAddWord(self, word):
        ''' This method is used to create the suffix trie recursively. 
        :Input: A word. 
        :Output: No output is required
        :Time Complexity: Best and Worst time complexity will be O (N**2), where N is the length of the word.
        :Auxiliary Space Complexity: O (M), where M is the length of suffixArray 
                                     which is depend on the number of range of each suffixes. 
        :Space Complexity: O (N + M), space complexity is input space + extra space.
                           The input space is O (N), where N is the length of the word.
                           The extra space is O (M), where M is the length of suffxArray. (explained above). 
        :Explanation: The suffixArray is used to store the range of each suffixes then 
                      it is used to loop the word and create the suffix trie in ASCENDING order of the word.
                      # ascending order is not to sort the word, 
                      # it is following the original sequence of the word
                      In suffix trie is "AABB" while in prefix tris is "BBAA". 
                      More details explanation is commented at the code.    
        '''
        current_node = self.suffixRoot   # start from root
        suffixArray = []                 # store substring of word
        lenOfWord = len(word)
        
        for i in range(1, lenOfWord+1):  # index start from 1
            suffixArray.append([i, lenOfWord])  # to get the range of each suffixes
            
        for suf in suffixArray:         # add char into suffix trie
            startIndex = suf[0] - 1
            endIndex = suf[-1]
            self.suffixAddWordAux(current_node, word, startIndex, endIndex) # add the substring into trie
            self.suffixIndexCounter += 1 # the suffix index start from 0

    def suffixAddWordAux(self, current_node, word, startIndex, endIndex):
        ''' This method is used to create new node for each unique character if it is not existing 
            and add or update data to each node.
        :Input: Current node that the pointer is pointed at, a word, the start index to loop the substring 
                and loop until the end index. 
        :Output: No output is required. 
        :Time Complexity: Best and Worst time complexity will be the same which is O (N), 
                          where N is the length of word (suffixes) 
        :Auxiliary Space Complexity: No extra space is required. 
        :Space Complexity: O (N), space complexity is input space + extra space.
                           The input space is O (N), where N is the length of the word and 
                           no extra space is needed (explained above). 
        :Explanation: When traverse into the suffix trie, all node will save the current suffix index. 
                      If same character is found in the word, then the latest suffix index will append 
                      into the node’s suffixIndex array instead of replacing it. The trie didn’t do anything 
                      when it is recursing back. More details explanation is commented at the code. 
        '''
        if startIndex >= endIndex:   # basecase
            index = 0
            if current_node.link[index] is None:           # terminal doesn't exist
                current_node.link[index] = SuffixNode()    # create new node
                current_node = current_node.link[index]    # update pointer
                current_node.suffixIndex.append(self.suffixIndexCounter)  # suffix index/ID
            else:                   # terminal exist
                current_node = current_node.link[index]    # update pointer
        else:                       # reduction
            index = ord(word[startIndex]) - 65 + 1         # $ = 0, A = 1
            if current_node.link[index] is None:           # node not exist
                current_node.link[index] = SuffixNode()    # creating new node                
                current_node = current_node.link[index]    # update pointer
                current_node.suffixIndex.append(self.suffixIndexCounter)  # suffix index/ID
            else:                                          # node exist
                current_node = current_node.link[index]    # update pointer  
                current_node.suffixIndex.append(self.suffixIndexCounter)  # suffix index/ID
            self.suffixAddWordAux(current_node, word, startIndex+1, endIndex)
            
    def prefixAddWord(self, word):
        ''' This method is used to create the prefix trie recursively. 
        :Input: A word. 
        :Output: No output is required
        :Time Complexity: O (N + N**2) = O (N**2). Best and Worst time complexity will be O (N**2), 
                          where N is the length of the word. The word is revered and 
                          the reversed time complexity is linear which is O (N).
        :Auxiliary Space Complexity: O (M), where M is the length of prefixArray 
                                     which is depend on the number of range of each prefixes. 
        :Space Complexity: O (N + M), space complexity is input space + extra space.
                           The input space is O (N), where N is the length of the word.
                           The extra space is O (M), where M is the length of prefxArray (explained above). 
        :Explanation: The prefixArray is used to store the range of each prefixes then 
                      it is used to loop the word and create the prefix trie in DESCENDING order.
                      # descending order is not to sort the word in descending, 
                      # it is just reversed the original sequence of the word
                      In suffix trie is "AABB" while in prefix tris is "BBAA".
                      More details explanation is commented at the code.    
        '''
        current_node = self.prefixRoot    # start from root
        prefixArray = []                  # store substring of word
        prefixWord = "".join(reversed(word))    # reverse
        lenOfWord = len(prefixWord)

        for i in range(1, lenOfWord+1):   # index start from 1
            prefixArray.append([i, lenOfWord])  # to get the range of each prefixes

        for pre in prefixArray:           # add char into prefix trie
            startIndex = pre[0] - 1
            endIndex = pre[-1]
            self.prefixAddWordAux(current_node, prefixWord, startIndex, endIndex) # add the substring into trie
            self.prefixIndexCounter -= 1  # the prefix index start from len(word)-1

    def prefixAddWordAux(self, current_node, prefixWord, startIndex, endIndex):
        ''' This method is used to create new node for each unique character if it is not existing 
            and add or update data to each node.
        :Input: Current node that the pointer is pointed at, a word (reverse of the original word), 
                the start index to loop the substring and loop until the end index. 
        :Output: No output is required. 
        :Time Complexity: Best and Worst time complexity will be the same which is O (N), 
                          where N is the length word (prefixes)
        :Auxiliary Space Complexity: No extra space is required. 
        :Space Complexity: O (N), space complexity is input space + extra space.
                           The input space is O (N), where N is the length of the word and 
                           no extra space is needed (explained above). 
        :Explanation: When traverse into the prefix trie, all node will save the current prefix index. 
                      If same character is found in the word, then the latest prefix index will append into the node’s 
                      prefixIndex array instead of replacing it. The trie didn’t do anything when it is recursing back. 
                      More details explanation is commented at the code.      
        '''
        if startIndex >= endIndex:   # basecase
            index = 0
            if current_node.link[index] is None:           # terminal doesn't exist
                current_node.link[index] = PrefixNode()    # create new node
                current_node = current_node.link[index]    # update pointer
                current_node.prefixIndex.append(self.prefixIndexCounter)  # prefix index/ID
            else:                   # terminal exist
                current_node = current_node.link[index]    # update pointer
        else:                       # reduction
            index = ord(prefixWord[startIndex]) - 65 + 1   # $ = 0, A = 1
            if current_node.link[index] is None:           # node not exist
                current_node.link[index] = PrefixNode()    # creating new node                
                current_node = current_node.link[index]    # update pointer
                current_node.prefixIndex.append(self.prefixIndexCounter)  # prefix index/ID
            else:                   # node exist
                current_node = current_node.link[index]    # update pointer
                current_node.prefixIndex.append(self.prefixIndexCounter)  # prefix index/ID
            self.prefixAddWordAux(current_node, prefixWord, startIndex+1, endIndex)

    def find(self, start, end):
        ''' This method is used to find the substring with the given start and end.
        :Input: The start word and the end word.
        :Output: An output list of substring which is between the starting word and the ending word. 
        :Time Complexity: Best time complexity will be O (1), where the total length of start and end is more than the input word.  
                          Worst time complexity will be O (len(start) + len(end) + len(U)), 
                          where start is the length of starting word, end is the length of ending word 
                          and U is the number of characters in the output list.
        :Auxiliary Space Complexity: O (U), where U is the number of characters in the output list.
        :Space Complexity: O (len(start) + len(end) + len(U)), space complexity is input space + extra space.
                           The input space is O (len(start) + len(end)), where start is the length of starting word 
                           and end is the length of ending word.
                           The extra space is O (U), where U is the number of characters in the output list (explained above). 
        :Explanation: Suffix trie is used to get the starting index of the substring while prefix trie is used to 
                      get the ending index of the substring. By using both trie, it is possible to get all the substring with 
                      start and end word. More details explanation is commented at the code.    
        '''
        suffix_current_node = self.suffixRoot     # start from root
        prefix_current_node = self.prefixRoot     # start from root
        output = []                               
        startArray = 0                            # to get the starting index
        endArray = 0                              # to get the ending index

        totalLen = len(start) + len(end)          # exit early
        if totalLen > len(self.inputWord):
            return output

        counterStart = 0
        for startChar in start:                   # to get the starting index
            index = ord(startChar) - 65 + 1       # convert ascii to index
            if suffix_current_node.link[index] is not None:     # exist
                suffix_current_node = suffix_current_node.link[index]   # update pointer
                if counterStart == len(start)-1:  # take the last char of starting word
                    startArray = suffix_current_node.suffixIndex   # start char exist in suffix trie (ascii index)
            else:                  # starting char does not exist in suffix trie
                return output
            counterStart += 1

        counterEnd = 0
        reverseEnd = "".join(reversed(end))       # reversed the end word
        for endChar in reverseEnd: # search for last end char in suffix trie
            index = ord(endChar) - 65 + 1         # convert ascii to index
            if prefix_current_node.link[index] is not None:    # exist
                prefix_current_node = prefix_current_node.link[index]   # update pointer
                if counterEnd == len(reverseEnd)-1:   # take the first char of reversed end word 
                    endArray = prefix_current_node.prefixIndex  # exist in prefix trie
            else:               # ending char does not exist in prefix trie
                return output
            counterEnd += 1

        oriWordRange = []
        for starting in startArray:             # to get the range of substring with the start and end
            for ending in endArray:
                diff = ending - starting + 1    # inclusive
                if diff >= totalLen:        # more then totalLen means no overlapping 
                    oriWordRange.append([starting, ending])

        for result in range(len(oriWordRange)): # loop to get the substring
            startIndex = oriWordRange[result][0]
            endIndex = oriWordRange[result][1]
            element = []
            for i in range(startIndex, endIndex+1): # inclusive
                element.append(self.inputWord[i])
            element = "".join(element)
            output.append(element)
        return output
