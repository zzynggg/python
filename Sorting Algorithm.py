# Yong Zi Ying: 30885027
# Assignment 1: Sorting Algorithm
# Grade: 19.6/20 HD
#%% Task 1:Radix Sort
def best_interval(transactions, t):
    ''' This function is used to search for the total number of transactions within the best interval by using 2 pointers.
    :Input: An unsorted list of non-negative integers and a non-negative integer that represent a length of time in seconds (range).
    :Output: The best interval with minimum start time and the total number of transaction within the best interval. 
    :Time Complexity: Best and worst case will be the same as the best and worst case for radix sort are the same.
                      No matter there's only one element or more in the list, it will be pre-sorted by using radix sort.
                      O (kN) + O (N) = O (kN), where O (kN) is from the radix sort function 
                      (explained in radix_sort function) and N is the length of the input list. 
    :Auxiliary Space Complexity: O (N), which is from radix sort function (explained in radix_sort function). 
                                 In this function, it required extra space for sorting which is O (N) auxiliary space and 
                                 in comparing state does not required any extra space. 
    :Space Complexity: O (kN), which is from radix sort function (explained in radix_sort function). 
                       The input space for comparing state is O (N) and 
                       the extra space for comparing state is O (1) so 
                       the space complexity will be O (kN) + O (N) + O (1) = O (kN)
    :Explanation: The input list will loop once only and 2 pointers are moving along the list 
                  to get the best time interval and the total number of transactions 
                  within the best interval. More details explanation is commented at the code.
    '''
    # === sorting state ===
    new_transactions = radix_sort(transactions) # pre-sort the transactions list
    # === Comparing state ===
    begin_pointer = 0
    exit_pointer = 0
    counter = 0
    max_counter = 0
    best_t = 0

    while begin_pointer < len(new_transactions):
        if len(new_transactions) == 0:  # list is empty
            max_counter = 0
            best_t = 0
            break
        if (new_transactions[0]+t) >= new_transactions[-1]:
            # the first element + t is >= last element
            max_counter = len(new_transactions)
            best_t = new_transactions[-1] - t
            if best_t <= 0:     # best_t cannot be -ve
                best_t = 0
            break

        # exit loop early 
        if (new_transactions[begin_pointer]+t) >= new_transactions[-1] or exit_pointer > len(new_transactions):
            break

        if new_transactions[exit_pointer] <= (new_transactions[begin_pointer]+t): 
            # within the current interval
            exit_pointer += 1
        elif new_transactions[exit_pointer] > (new_transactions[begin_pointer]+t):
            # exceed the current interval
            counter = exit_pointer - begin_pointer  # get the total num of transaction within the interval
            if counter > max_counter:       # get the largest total num of transaction within the list
                max_counter = counter
                best_t = new_transactions[exit_pointer-1] - t
                if best_t <= 0:     # best_t cannot be -ve
                    best_t = 0
                counter = 0
            if (new_transactions[begin_pointer]+t) < new_transactions[exit_pointer]:    
                # duplicated element is found in the list
                begin_pointer += 1

    # extra check to make sure the output is accurate
    counter = len(new_transactions) - begin_pointer     # check the counter again
    if counter > max_counter:       # update the max_counter if new bigger counter is found
        max_counter = counter
        best_t = new_transactions[-1] - t   # update the best_t if new bigger counter is found
        if best_t <= 0:     # best_t cannot be -ve
            best_t = 0
        
    return (best_t, max_counter)
    
    

def radix_sort(transactions):
    ''' To sort the input list into sorted list by calling multiple times of counting sort function.
    :Input: An unsorted list.
    :Output: A sorted list is returned.
    :Time Complexity: Best and Worst complexity will be the same as the iterator doesn't terminate early.
                      O(k) * O(N+M) -> O (kN + kM) = O (kN), where k is the biggest length of the element in the list, 
                      N is the length of the input list and M which is base constant so ignore M. 
                      We will need to call counting sort function for k times.
    :Auxiliary Space Complexity: each counting sort needs O(N + M + N) = O(N), 
                                 where first N is the length of the output_array (new list that is same size with original list)
                                 that is created in the counting sort function based on the length of the input list and 
                                 M (base) is the length of buckets. (count_array). 
                                 A total of N number of items (second N) will be placed into buckets (same as the total items in output_array) 
                                 and M is a constant number (base) so ignore it. 
    :Space Complexity: O(kN+N+M+N) = O(kN), space complexity is input space + extra space. 
                       The input space is the length of the input list(N) and k columns (number of digits) which is O (kN)
                       whereas the extra space from counting sort is O (N + M + N). M is base constant. (explained above) 
    '''

    # find max number of digits
    if len(transactions) > 0:
        max_num = max(transactions)
    else:
        max_num = 0

    base = 10
    columnn = 0
    digit = base**columnn
    # loop the counting sort
    while max_num//digit > 0:
        counting_sort(transactions, digit, base)
        columnn += 1
        digit = base**columnn

    return transactions

def counting_sort(transactions, digit, base):
    ''' To sort the input list column by column into sorted list.
    :Input: An unsorted list, the column that is used to sort currently and the base value.
    :Output: The list is sorted until the current column. 
    :Time Complexity: Best and Worst complexity will be the same as the iterator doesn't terminate early.
                      O(N+M), where N is the length of the input list and
                      M is the biggest length of the element in the list.
    :Auxiliary Space Complexity: O(N + B + N) = O(N), where first N is the length of the output_array that is created 
                                 in the functions based on the length of the input list and 
                                 B (base) is the length of buckets. (count_array)
                                 A total of N number of items (second N) will be placed into buckets (same as the total items in output_array) 
                                 and B is a constant number (base) so ignore it.  
    :Space Complexity: O(N+N+B+N) = O(N), space complexity is input space + extra space. 
                       The input space is the length of the input list which is O (N) 
                       and the extra space is O (N + B + N). (explained above) 
    '''

    size = len(transactions)
    # initialize count array start from index 1 -> max_num
    count_array = [0] * base

    # initialize output array
    output_array = [0] * size

    # allocate number of elements to count array
    # base on the digit (column by column)
    for i in range(0, size):
        ind = transactions[i] // digit 
        count_array[ind%base] += 1

    # reused the count_array for position array 
    for j in range(1, base):
        count_array[j] += count_array[j-1]

    # place the elements base on the position(count_array)
    # loop it in descending order
    for k in range(size-1, -1, -1):
        ind = transactions[k] // digit  # get the right most digit
        output_array[count_array[ind%10] - 1] = transactions[k]
        count_array[ind%10] -= 1

    # reuse and update the original list
    for l in range(0, size):
        transactions[l] = output_array[l]


# %% Task 2: Counting Sort + Radix Sort
def words_with_anagrams(list1, list2):
    ''' Using anagram to compare the words between 2 lists. Output the same anagram word from list1 that appears in list2. 
    List1 will be priorities for output.
    :Input: Two unsorted string lists.
    :Output: A list of word from list1 that appear in list2 based on the same anagram of words.     
    :Time Complexity: Best and worst case will be the same, 
                      O (L1M1 + L2M2), where L1 is the length of list1 and 
                      M1 is the biggest length of the characters of element in list1. L2 is the length of list2 and 
                      M2 is the biggest length of the characters of element in list2.
                      if list1 have only 1 item to compare with multiple items in list2
                      the time complexity will be O (L1M1 + L2M2) vice versa when list2 have 1 item only.
                      (of course the best is when either one of the lists is empty then the best complexity will be O(1))                 
                      The sorting state based on characters, the complexity for list1 is O (L1M1) and list2 is O (L2M2).
                      The sorting state based on string elements, the complexity for list1 is O (L1) and list2 is O (L2).
                      The comparing state complexity is based on the length of list1 which is O (L1) 
                      The comparing state 2 (refer to in-line comment) is constant.
                      Thus, the overall time complexity is O (L1 + L1+ L2 + L1M1 + L2M2) = O (L1M1 + L2M2)
    :Auxiliary Space Complexity: O (L1 + L1 + L2) = O (L1 + L2), where L1 is the length of the 
                                 duplication of list1 (deep copy list1 into new list) and 
                                 a new list is created (output_list) with the same length as list1 (L1). 
                                 The worst scenario is if all elements in list1 is appear in list2 
                                 so entire list1 is returned (L1 extra space needed).
                                 Another new list is created for list2 without duplicate elements, 
                                 the length will be same as the original list2 
                                 if there’s no duplicate element in it (worse scenario). 
    :Space Complexity: O (L1 + L2 + L1 + L2) = O (L1 + L2), space complexity is input space + extra space. 
                       The input space is L1 + L2, where L1 is the length of list1 and L2 is the length of list2.
                       The extra space is O (L1 + L2) (explained above).
    :Explanation: Two lists are given, list1 will be priorities. 
                  All string elements from both lists are sorted in alphabetical order based on the characters in each string elements. [cats -> acst]
                  After sorting each characters of string elements, sort both lists again now is sorted based on the entire string elements. [aelpp, acst -> acst, aelpp]
                  Now, remove the duplicated elements in list2 and start comparing both lists. 
                  While comparing if the element from both lists has same initial character, 
                  it will be compared again based on each characters of the string elements. 
                  More details explanation is commented at the code. 
    '''
    # handle empty list
    if len(list1) == 0 or len(list2) == 0:     # both list are empty
        return []
    
    xori_list1 = list1.copy()       # deep copy the list to prevent data loss (extra space required)
    xori_size = len(xori_list1)     
    output_list = []    # extra space required

    # === Priority list (list1) ===
    for i in range(xori_size):    # sort each *characters* in word 
        xori_list1[i] = counting_sort_alphabet(xori_list1[i])

    for j in range(xori_size): # pair up each element with an unique key
        xori_list1[j] = (xori_list1[j], j)
    
    for _ in range(xori_size):      # sort each *word* in list1 
        sorted_xori_list1 = radix_sort_string(xori_list1, 1)

    # === List 2 ===
    list2_size = len(list2)
    for l in range(list2_size):     # sort each *characters* in word 
        list2[l] = counting_sort_alphabet(list2[l])

    for _ in range(list2_size):     # sort each *word* in list2
        sorted_list2 = radix_sort_string(list2, 2)

    begin = 0   # start pointer
    exitt = 0   # end pointer
    while exitt < len(sorted_list2)-1:      # remove duplicate anagram word in list2
        if sorted_list2[begin] == sorted_list2[exitt+1]:
            exitt += 1
        else:
            sorted_list2[begin+1] = sorted_list2[exitt+1]
            begin += 1
            exitt += 1
    
    sorted_xdupli_list2 = []    # extra space required
    for n in range(exitt):  # list2 without duplicate elements
        sorted_xdupli_list2.append(sorted_list2[n])

    if (len(sorted_list2) < 2):     # restore list2 if only 1 element in list2
        sorted_xdupli_list2 = sorted_list2

    # === Comparing state ===
    a = 0   # list one pointer
    b = 0   # list two pointer
    exit_check = 0  # avoid inf loop
    while a < xori_size:
        if sorted_xori_list1[a][0] == sorted_xdupli_list2[b]:
            # same anagram word found
            ori_pos = sorted_xori_list1[a][1]   # original index of word
            output_list.append(list1[ori_pos])
            a += 1
        elif sorted_xori_list1[a][0] != sorted_xdupli_list2[b]:
            # different anagram word found
            # handle empty string
            if sorted_xori_list1[a][0] == '' and sorted_xdupli_list2[b] != '':
                a += 1
            elif sorted_xori_list1[a][0] != '' and sorted_xdupli_list2[b] == '':
                b += 1
            # compare the first character of the anagram word
            elif (sorted_xori_list1[a][0])[0] > sorted_xdupli_list2[b][0]:  # compare first character
                b += 1
            elif (sorted_xori_list1[a][0])[0] == sorted_xdupli_list2[b][0]:  # compare first character
                # first character same
                pointer1 = 0
                pointer2 = 0
                meet_condition = True
                # comparing state 2
                for _ in range(len(sorted_xori_list1[a][0])):  # length of the word in list1
                    if (sorted_xori_list1[a][0])[pointer1] == (sorted_xdupli_list2[b])[pointer2]:
                        # same initial is found
                        pointer1 += 1
                        pointer2 += 1
                        meet_condition = False
                    elif (sorted_xori_list1[a][0])[pointer1] > (sorted_xdupli_list2[b])[pointer2]:
                        meet_condition = True
                        b += 1
                        break
                    elif (sorted_xori_list1[a][0])[pointer1] < (sorted_xdupli_list2[b])[pointer2]:
                        meet_condition = True
                        a += 1
                        break
                    if pointer2 > len(sorted_xdupli_list2[b])-1:
                        # exceed the length of word from list2 
                        meet_condition = True
                        b += 1
                        break
                # extra check 
                if meet_condition == False:
                    a += 1  # len(word1) < len(word2)
            else:
                # first character different
                a += 1
        
        # extra check (improve accuracy)
        if b >= len(sorted_xdupli_list2)-1:   
            # if list1 longer then list2 maintain the last element of list2 
            exit_check += 1
            b = len(sorted_xdupli_list2)-1

        # exit loop early
        if a > len(sorted_xori_list1)-1 and b == len(sorted_xdupli_list2)-1:
            break
        elif exit_check > a:
            break
        
    return output_list

def radix_sort_string(listt, priority_list):
    ''' To sort the input list into sorted list by calling multiple times of counting sort function.
    :Input: An unsorted list and the priority number for the list (explained later).
    :Output: A sorted list.
    :Time Complexity: Best and Worst complexity will be the same as the iterator doesn't terminate early.
                      O(k) * O(N+M) -> O (kN + kM) = O (kN), where k is the biggest length of the 
                      element in the list, N is the length of the input list and M which is base constant so ignore M. 
                      We will need to call counting sort function for k times.
    :Auxiliary Space Complexity: each counting sort needs O(N + M + N) = O(N), 
                                 where first N is the length of the output_array (new list that is same size with original list)
                                 that is created in the counting sort function based on the length of input list and 
                                 M (base) is the length of buckets (count_array). 
                                 A total of N number of items (second N) will be placed into 
                                 buckets (same as the total items in output_array) and 
                                 M is a constant number (base) so ignore it. 
    :Space Complexity: O(kN+N+M+N) = O(kN), space complexity is input space + extra space. 
                       The input space is the length of the input list, N and k columns (number of digits) which is O (kN)
                       whereas the extra space from counting sort is O (N + M + N). M is base constant. (explained above)  
    :Explanation: The input parameter, priority_list is used to differentiate the list between list1 and list2. 
                  List1 will be priorities because we need to output the word from list1 that appear in list2 
                  when comparing the word from both lists by using anagram. 
                  In order to get back the original words from list1 after comparing, 
                  each elements of list1 are paired up with a unique key 
                  so that the output is the original word (e.g cats) but not the sorted word (e.g acst).  
    '''
    max_word_size = len(listt[0])    # column

    if priority_list == 1:  # list1 with keys
        # find the longest string in listt
        for i in range(len(listt)):
            word_size = len(listt[i][0])
            if word_size > max_word_size:
                max_word_size = word_size
    else:
        # find the longest string in listt
        for word in listt:
            word_size = len(word)
            if word_size > max_word_size:
                max_word_size = word_size

    base = 27   # start at index 1 -> 27
    column = max_word_size - 1  # word len = 4 (index[0-3])
    # loop the string counting sort for column times
    while column >= 0:
        listt = counting_sort_word(listt, column, base, max_word_size, priority_list)
        column -= 1

    return listt

def counting_sort_word(listt, column, base, max_word_size, priority_list):
    ''' To sort the input list column by column into sorted list.
    :Input: An unsorted list, the column that is used to sort currently, the base value, 
            the biggest length of the element in the list and the priority number of the list(explained in radix_sort_string).
    :Output: The list is sorted until the current column.
    :Time Complexity: Best and Worst complexity will be the same as the iterator doesn't terminate early.
                      O(N+M), where N is the length of the input list and
                      M is the biggest length of the element in the list.
    :Auxiliary Space Complexity: O(N + B + N) = O(N), where first N is the length of the output_array that is created 
                                 in the functions based on the length of input list and 
                                 B (base) is the length of buckets (count_array).
                                 A total of N number of items (second N) will be placed into 
                                 buckets (same as the total items in output_array) 
                                 and B is a constant number (base) so ignore it.  
    :Space Complexity: O(N+N+B+N) = O(N), space complexity is input space + extra space. 
                       The input space is the length of the input list which is O (N) 
                       and the extra space is O (N + B + N). (explained above)
    '''
    size = len(listt)
    # initialize count array start from index [0-26]-> 27 slots
    count_array = [0] * base

    # initialize output array
    output_array = [0] * size

    # allocate the char in the correct position ('a' at index 1)
    # ord('a') = 97 -1 = 96
    accurate = ord('a') - 1

    if priority_list == 1: # list1 with keys
        # allocate words to count_array
        # index 0 act as temporary storage
        for i in range(size):
            word = listt[i][0]
            if column < len(word):
                index = ord(word[column]) - accurate
            else:
                index = 0  
            count_array[index] += 1

    else:
        # allocate words to count_array
        # index 0 act as temporary storage
        for word in listt:
            if column < len(word):
                index = ord(word[column]) - accurate
            else:
                index = 0  
            count_array[index] += 1

    # reused the count_array for position array 
    for j in range(1, base):
        count_array[j] += count_array[j-1]

    if priority_list == 1:  # list1 with keys
        # place the elements base on the position(count_array)
        # loop it in descending order
        for k in range(size-1, -1, -1):
            word = listt[k][0]
            if column < len(word):     # get the right most char
                index = ord(word[column]) - accurate
            else:
                index = 0  
            output_array[count_array[index] - 1] = listt[k]     # store the tuple into output_array
            count_array[index] -= 1
    else:
        # place the elements base on the position(count_array)
        # loop it in descending order
        for k in range(size-1, -1, -1):
            word = listt[k]
            if column < len(word):     # get the right most char
                index = ord(word[column]) - accurate
            else:
                index = 0  
            output_array[count_array[index] - 1] = word         # store the word into output_array
            count_array[index] -= 1
    
    return output_array

def counting_sort_alphabet(word):
    ''' To sort the word column by column into sorted word.
    :Input: A word with random alphabetical order (unsorted word).
    :Output: Each alphabet in the word is sorted (sorted word).
    :Time Complexity: Best and Worst complexity will be the same as the iterator doesn't terminate early.
                      O(N+M) = O (N), where N is the length of the word and
                      M is the base of the word which is constant.
    :Auxiliary Space Complexity: O(N + B + N) = O(N), where first N is the length of the output_array that is created 
                                 in the functions based on the length of input word and 
                                 B (base) is the length of buckets (count_array).
                                 A total of N number of characters (second N) will be placed into 
                                 buckets (same as the total items in output_array) 
                                 and B is a constant number (base) so ignore it.  
    :Space Complexity: O(N+N+B+N) = O(N), space complexity is input space + extra space. 
                       The input space is the length of the input word which is O (N) 
                       and the extra space is O (N + B + N). (explained above) 
    '''
    size = len(word)
    base = 27
    # initialize count array start from index [0-26]-> 27 slots
    count_array = [0] * base

    # initialize output array
    output_array = [0] * size

    # allocate the char in the correct position ('a' at index 1)
    # ord('a') = 97 -1 = 96
    accurate = ord('a') - 1
    sorted_word = ""
    
    # allocate characters into count_array
    # index 0 act as temporary storage
    for alphabet in range(size):
        index = ord(word[alphabet]) - accurate
        count_array[index] += 1

    # place the elements base on the position(count_array)
    index = 0
    for i in range(len(count_array)):
        alpha = chr(i + accurate)
        frequency = count_array[i]
        for _ in range(frequency):
            output_array[index] = alpha
            index += 1
    
    # combine each characters into word
    for j in output_array:
        sorted_word += j
    
    return sorted_word
