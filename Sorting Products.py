# Yong Zi Ying: 30885027
# Assignment Part 1 & Assignment Part 2
# Grade: Part 1 = 10/10 HD; Part 2 = 11/12 HD
"""
Author: <Yong Zi Ying> (<30885027>)

In this assignment we implement the backend of an intelligent product
search engine where potential customers can search a database of products
characterised by different features taking into account the customer's
preferences.

Functions for 1 and 2 are due in Part 1 of the assignment. Functions
for 3 and 4 are due in Part 2.

As a global conventions, to select products based on hard criteria,
we will use Python objects representing conditions. These are represented
as triples (i, c, v) where i is an integer feature index, c is a relation
symbol in ['<', '<=' '==', '>=', '>', '!='], and v is some feature value.
A product (represented by a feature vector) _satisfies_ condition (i, c, v)
if its i-th feature value is in relation c with the value v. This will be
implemented in a function 'satisfies'. For example:
>>> inexpensive = (4, '<=', 1000)
>>> satisfies(['Nova 5T', 'Huawei', 6.26, 3750, 497], inexpensive)
True
>>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], inexpensive)
False

For more information see the function documentations below and the
assignment sheet.
"""


# Part 1 (due Week 6) #


def satisfies(product, cond):
    """
    Determines whether a product satisfies a given condition.

    Input : A product feature list (product() and a condition
            (cond) as specified above.
    Output: True if cond holds for the product otherwise False.

    For example, consider the following conditions:
    >>> inexpensive = (4, '<=', 1000)
    >>> large_screen = (2, '>=', 6.3)
    >>> apple_product = (1, '==', 'Apple')

    With this the function behaves as follows:
    >>> satisfies(['Nova 5T', 'Huawei', 6.26, 3750, 497], inexpensive)
    True
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], inexpensive)
    False
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], large_screen)
    False
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], apple_product)
    True

    >>> ikea_products = [['SUNDICK','wardrobe','white',172,80,279],
    ...                  ['GRONLID','sofa','light green',104,247,999],
    ...                  ['VEDBO','armchair','grey',75,73,199],
    ...                  ['ALEX','desk','white',76,131,199]]
    >>> cheap_furniture = (5, '<=',750)
    >>> colourful = (2, '!=', 'white')
    >>> tall = (3,'>=', 100)

    >>> satisfies(ikea_products[0], colourful)
    False
    >>> satisfies(ikea_products[1], tall)
    True

    <Paragraph on problem, challenges, and overall approach.>
    The problem in this task is to check whether the user input product list has or hasn’t fulfilled 
    the user input condition then return a Boolean result.
    A comparison between the user input condition with the product list are required.
    The challenge in this task is implementing the specified condition as shown above and 
    compare with the specific element in the user input product list.
    This was achieved by not hard coded the conditions in this function in order to allow more 
    conditions to be tested and compared.
    In my code, if the condition fulfills after comparing with the element in the product list it 
    returns a Boolean True, otherwise return False.

    <Paragraph on specific programming techniques and Python
     language elements used.>
    I solved this task by using if statement to differentiate the type of condition by using the 
    string operator(c) and another if statement is used to compare the limitation(v) of condition 
    with the fixed index element in product list (products[i]) in order to return a Boolean result.
    In this function, I included all types of operator to test with more conditions other than the
    three conditions as specified above.
    To further explain it, I added a new product list which is ikea_products, some behaviors and
    new conditions to test with my code and its work.
     
    """
    
    #inexpensive & cheap_furniture(extra)
    i,c,v = cond
    if c == '<=':
        if product[i]<= v:
            return True
        else:
            return False
        
    #large_screen & tall(extra)
    elif c == '>=':
        if product[i]>= v:
            return True
        else:
            return False
        
    #colourful(extra)
    elif c == '!=':
        if product[i]!= v:
            return True
        else:
            return False
        
    elif c == '>':
        if product[i]> v:
            return True
        else:
            return False
        
    elif c == '<':
        if product[i]< v:
            return True
        else:
            return False
        
    #apple_product
    elif c == '==':
        if product[i] == v:
            return True
        else:
            return False
     


def selection(products, conditions):
    """
    Filters a given product table by a list of conditions.

    Input : A product table (products) and a list of conditions
            (conditions) consisting of triples (i, c, v) as specified
            in the module documentation.
    Output: The list of products satisfying all conditions.

    For example let's assume the following database of phones
    with features name, manufacturer, size, battery capacity, price.
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3300, 598],
    ...           ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    Then the function behaves as follows:
    >>> large_screen = (2, '>=', 6.3)
    >>> cheap = (4, '<=', 400)
    >>> selection(phones, [cheap, large_screen])
    [['Reno Z', 'Oppo', 6.4, 4035, 397]]
    >>> not_apple = (1, '!=', 'Apple')
    >>> selection(phones, [not_apple])
    [['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    <Paragraph on problem, challenges, and overall approach.>
    This function has selecting list problem depending on the user input conditions which means 
    looping and comparing elements are needed to iterate the conditions and compare with the 
    elements in the products list.
    The challenges in this task are selecting the products list according to the user input 
    conditions and return the products list without duplication that fulfil all the conditions.
    In order to achieve it, some new lists are created to finalize the products list and return the 
    appropriate products list.  
    In my solution, the selected products list which fulfil the conditions are appended into a new 
    list (lst) then the lst list need to be filtered before returning it as in the same products list will
    appear more than one time in the lst list if it fulfils all conditions. 
    Thus, the repeated products list will return once only and the other duplicated products list
    are removed. 


    <Paragraph on specific programming techniques and Python
     language elements used.>
    To solve this task, I choose for-loop to loop over all the conditions and the products list.
    In the nested loops, if statement is used differentiate type of condition by using the string 
    operator(c) and another if statement is used to compare the limitation(v) of condition with the 
    fixed index element in product list (products[i]) in order to append the products list which fulfil 
    the conditions. Furthermore, I used append() built-in function to append the selected lists 
    into a new list (lst).
    To prevent list duplication, len () built-in function is used to calculate the length of the 
    conditions that user input. If the length of conditions is more than one, filtering the list is
    needed else return the lst list. The filtering process consists of two loops. In the first loop,
    there is an if statement and a count() built-in function to count the number of different
    products list appear in the new list (lst) is it equals to the length of the conditions. If it is, it
    fulfils all conditions then it will be appended into another new list (repeat). 
    While in the second loop, an if statement and ‘not in’ operator are used to remove the
    duplicated list in lst list which fulfil all conditions and return it once only.

    """

    #select the products list that fulfil conditions#
    lst=[]
    for a in conditions:
        i, c, v = a
        for prod in products:
            #cheap
            if c == '<=':
                if prod[i] <= v:   
                    lst.append(prod)
            #large_screen
            elif c == '>=':
                if prod[i] >= v:
                    lst.append(prod)
            elif c == '<':
                if prod[i] < v:
                    lst.append(prod)
            elif c == '==':
                if prod[i] == v: 
                    lst.append(prod)
            elif c == '>':
                if prod[i] > v:        
                    lst.append(prod)
            #not_apple
            elif c == '!=':
                if prod[i] != v:
                    lst.append(prod)
     
    #analyse the fulfil conditions#
    if len(conditions) > 1:
        repeat=[]
        for i in lst:
            if lst.count(i) == len(conditions):     
                repeat.append(i)                    #append the repeated list that fulfil all conditions
             
        final_lst = [] 
        for x in repeat: 
            if x not in final_lst:                  #to remove extra repeated list
                final_lst.append(x) 
        return final_lst                            #return the repeated list ONCE only
    else:
        #if and only if user input only one condition 
        return lst
    


def linearly_ranked(products, weights):
    """
    Ranks products in order of preference as specified by a linear
    weight vector.

    Input : Product table (products) with n columns, list of
            weights of length n containing at position i the
            linear weight for product feature column i or None if
            no weight is specified for column i
            (must be None for non-numeric column).
            At least one weight must be different from None.
    Output: A new table containing all products from the input table
            in decreasing order of the linear score given, for a product
            prod in products, by the sum of prod[i]*weights[i] over
            all column indices i with weights[i]!=None.

    For example let's assume the following database of phones
    with features name, manufacturer, size, battery capacity, price:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3300, 598],
    ...           ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    This leads to the following behavior
    >>> battery = [None, None, None, 1, None]
    >>> linearly_ranked(phones, battery)
    [['Reno Z', 'Oppo', 6.4, 4035, 397], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['iPhone11', 'Apple', 6.1, 3110, 1280]]
    >>> screen_battery_price = [None, None, 10, 1/1000, -1/100]
    >>> linearly_ranked(phones, screen_battery_price)
    [['Reno Z', 'Oppo', 6.4, 4035, 397], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['iPhone11', 'Apple', 6.1, 3110, 1280]]

    The input table is not changed by the function. That is
    after calling it, we still have:
    >>> phones
    [['iPhone11', 'Apple', 6.1, 3110, 1280], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    <Paragraph on problem, challenges, and overall approach.>
    This task has a ranking products list problem where the value in the list of weights is used to 
    multiply by the elements in the products list in order to sort and rank it.
    This means that iterating and comparing the products list is needed.
    The most challenging part in this task is sorting the products list in descending order and
    ranking order without modifying the original products list. 
    This was achieved through deep copy the products list into a new list (xori_lst).     
    In my code, the new list that already deep copied (xori_lst) is used to perform multiplication 
    to sort the products list in descending order and it also sorts the products list in ranking order
    based on the sum of multiplication. It then returns the list in the correct order.


    <Paragraph on specific programming techniques and Python
     language elements used.>
    This function is solved by implementing for-loop and if statement to iterate and compare the 
    products list. A built-in function, copy () is used to deep copy the original products list and it
    is store at another new list (xori_lst).
    Looping over the weights list, an if statement is used to append the not None value index
    into a new list (index_weights). A append () and index () built-in function are used to append the
    index of not None value into index_weights list. A len () built-in function is use to calculate the length
    of a list in products list (lenn) by looping the products list.
    Next, nested loops are used to loop the not None value and the xori_lst list to perform
    multiplication based on the value of weights and elements in list in xori_lst by refering to their
    index(j), then append the result of multiplication into the xori_lst list.
    An if statement is used to check if the length of index_weights list is equal to one, a built-in function
    sort () is used to sort the xori_lst list. In the parenthesis of sort (), the key parameter is
    specified a function to make comparison and the value of the key is lambda functions while
    lambda function is an anonymous function that defined without name. It returned the only
    one expression which is the last element of the list. The parameter ‘reverse = True’ is used
    to sort the xori_lst list in reverse (descending) order based on the last element in the xori_lst
    list which is the result of multiplication. After sorting the xori_lst list, pop () built-in function is
    used to remove the extra elements of the list in xori_lst list then return the xori_lst list. 
    Now, the else if statement will check if the length of index_weights list is more than one, slicing
    built-in function is used to slice from the length of list in products list (lenn) to the end of the
    xori_lst list, where the sum of the multiplied weights are calculated and appended into a new
    list (ranks) by looping. The ranks list is appended with the list in xori_lst list then perform
    sorting of xori_lst list based on the sum of the multiplied weights into descending order.
    After sorting the xori_lst list, the extra element of the list in xori_lst list are removed then
    return the xori_lst. Lastly, the else statement will return the original list which is products list.


    """
    
    xori_lst = products.copy()      #deepcopy the products list 
    index_weights = []              #append index of weights
    ranks = []                      #append the sum of multiplication  
    
    #append the weights index
    for i in weights:           
        if i!= None:
            index_weights.append(weights.index(i))    #append the index of weights into index_weights

    #calculate the length of nested lists
    for k in products:
        lenn = len(k)
    
    #loop over the index value in index_weights 
    for j in index_weights:
        for prod in xori_lst:                   #perform multiplication for prod and weights value by refering to the index_weights
            prod.append(prod[j] * weights[j])   #append each result of the multiplication into xori_lst

    #length of index_weights list are used categories the requirement                       
    #battery        
    if len(index_weights) == 1:           
        xori_lst.sort(key = lambda x : x[-1], reverse = True)     #sort the list in descending order
        for x in xori_lst:
            x.pop()                 #after sorting, remove the last element which is the result of the multiplication
        return xori_lst

    #linearly_ranked
    elif len(index_weights) > 1:                  
        for prod in xori_lst:
            summ = 0
            for x in prod[lenn:]:       #calculate the sum of the ranked values
                summ+=x
            ranks.append(summ)           #append all the summ into ranks list
        i=0
        for new in xori_lst:
            new.append(ranks[i])        #append the element of ranks list into the list in xori_lst
            i+=1
        xori_lst.sort(key = lambda x : x[-1], reverse = True)    #sort the list by using the last element in the list 
        
        for x in xori_lst:
            for dell in x[lenn:]:       
                x.pop()              #after sorting, remove all extra elements in the list
        return xori_lst

    #phones
    else:                       
        return products     
    

# Part 2 (due Week 11) #

def relevant(products, preferences):
    """
    Filters a product table for relevant products given user preferences.

    Input : A product table (products) and a list of preferences, where
            each preference is a pair (i, p) with i being the index of to a
            numeric column in products and p is either +1 or -1 depending
            on whether the user considers feature i to be positive or negative.
    Output: A new list of products that are relevant with respect to the
            preferences. A product is relevant if it is not dominated by another
            product, which is defined as follows:
            - prod1 dominates prod2 with respect to preference (i,p) if
              prod1[i] > prod2[i] in case p=1 (or prod1[i] < prod2[i] in case p=-1)
            - prod1 dominates prod2 if prod1 dominates prod2 with respect to at
              least one specified preference and not prod2 does not dominate prod2
              with respect to any specified preference

    For example:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S21', 'Samsung', 6.2, 3300, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3700, 497],
    ...           ['P30 Pro', 'Huawei', 6.4, 3500, 398],
    ...           ['R17 Pro', 'Oppo', 6.6, 3200, 457],
    ...           ['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> large_battery_but_cheap = [(3,1), (4,-1)]
    >>> relevant(phones, large_battery_but_cheap)
    [['Nova 5T', 'Huawei', 6.26, 3700, 497], ['P30 Pro', 'Huawei', 6.4, 3500, 398], ['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> big_screen = [(2,1)]
    >>> relevant(phones, big_screen)
    [['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_but_cheap = [(2,1),(4,-1)]
    >>> relevant(phones, big_screen_but_cheap)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_large_battery = [(2,1),(3,1)]
    >>> relevant(phones, big_screen_large_battery)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457], ['Pixel 3', 'Google', 6.3, 3800, 688]]


    >>> small_screen = [(2,-1)]
    >>> relevant(phones, small_screen)
    [['iPhone11', 'Apple', 6.1, 3110, 1280]]
    >>> large_battery_big_screen = [(3,1), (2,1)]
    >>> relevant(phones, large_battery_big_screen)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457], ['Pixel 3', 'Google', 6.3, 3800, 688]]

    >>> ikea_products = [['SUNDICK', 'wardrobe', 'white', 172, 80, 279],
    ...                  ['GRONLID', 'sofa', 'light green', 104, 247, 999],
    ...                  ['VEDBO', 'armchair', 'grey', 75, 73, 199],
    ...                  ['ALEX', 'desk', 'white', 76, 131, 1999]]
    
    >>> tall_but_cheap = [(3,1), (5,-1)]
    >>> relevant(ikea_products, tall_but_cheap)
    [['SUNDICK', 'wardrobe', 'white', 172, 80, 279], ['VEDBO', 'armchair', 'grey', 75, 73, 199]]
    >>> cheap_price = [(5,-1)]
    >>> relevant(ikea_products, cheap_price)
    [['VEDBO', 'armchair', 'grey', 75, 73, 199]]

    >>> movies = [['Australia', 6.6, 900, False, 'English', 2008, 165],
    ...           ['Lake Placid', 5.7, 1, False, 'English', 1999, 82],
    ...           ['Tommy Boy', 7.1, 20, False, 'English', 1995, 97],
    ...           ['Life is Beautiful', 8.6, 0, False, 'Italian', 1997, 116],
    ...           ['Top Secret', 7.2, 6, False, 'English', 1984, 90],
    ...           ['Back to the Future', 8.5, 1, False, 'English', 1985, 116],
    ...           ['Twister', 6.4, 2, True, 'English', 1996, 113]]

    >>> relevant(movies, [(1, 1), (2, 1)])
    [['Australia', 6.6, 900, False, 'English', 2008, 165], ['Tommy Boy', 7.1, 20, False, 'English', 1995, 97], ['Life is Beautiful', 8.6, 0, False, 'Italian', 1997, 116], ['Top Secret', 7.2, 6, False, 'English', 1984, 90], ['Back to the Future', 8.5, 1, False, 'English', 1985, 116]]
    >>> relevant(movies, [(1, 1)])
    [['Life is Beautiful', 8.6, 0, False, 'Italian', 1997, 116]]
    >>> relevant(movies, [(2, 1)])
    [['Australia', 6.6, 900, False, 'English', 2008, 165]]
    >>> relevant(movies, [(1, -1), (2, -1)])
    [['Lake Placid', 5.7, 1, False, 'English', 1999, 82], ['Life is Beautiful', 8.6, 0, False, 'Italian', 1997, 116]]

    <Paragraph on problem, challenges, and overall approach.>
    This function has a filtering list problem depending on user input products and preferences. 
    Therefore, looping and comparing the elements are needed to iterate the preferences and 
    compare with the elements in the products list. 
    The most challenging part in this task is comparing the products list according to the user 
    input preferences and returning the products list without duplication that fulfil all the 
    preferences.
    In order to achieve it, there are two sub functions in this task. 
    The function loop(preferences, products) iterates the preferences and uses the preferences 
    value to compare with the value of the products list by using index then return a compared 
    list (new_list). 
    Next, the function ans(preferences,looping,products) that used the compared list (looping) 
    from the loop function. By implementing the concept of divide and conquer, the looping list is 
    divided so as to filter it then return the correct list (return_list).
    To further explain it, I added some new product list such as ikea_products, movies, some behaviors and 
    new preferences to test with my code and it’s work.


    <Paragraph on specific programming techniques and Python language elements used.>
    This task is solved by breaking down the complex function into two sub functions which are 
    function loop(preferences, products) and function ans(preferences,looping,products). For the 
    main function relevant(products, preferences) is used to call the sub functions to perform the 
    task. Function loop(preferences, products) will return a compared list (new_list) and new_list 
    is assigned to looping in the main function. For function ans(preferences,looping,products) 
    will return a correct list (return_list) and return_list is assigned to answer in the main function. 
    Thus, the main function will return answer list. 
    The explanation for both sub functions will be illustrated under its function.

    
    <Paragraph on computational complexity.>
    The computational complexity is a general term, it is not depending on time only. It depends 
    on the space that an algorithm uses as well. The overall computational complexity for
    relevant function is O(1) which is caused by the called functions in this function at
    line “looping = loop(preferences,products)” or “answer = ans(preferences,looping,products)” or return answer. 
    The computational complexity for each line of codes in this main function are commented 
    by using in-line comments (#O()) as shown at the side of codes. 
    The computational complexity for both sub functions will be illustrated under its function. 
  


    """
    
    # ***main***

    # refer to loop function below 
    looping = loop(preferences,products)            #O(1)

    # refer to ans function below
    answer = ans(preferences,looping,products)      #O(1)

    # return answer (correct list)
    return answer                                   #O(1)

# ***Sub function***
def loop(preferences,products):
    """

    Loop products list by using user input preferences to return compared products list(new_list)

    Input : A products list and a list of preferences
    Output : A new list of products that are compared with respect to the preferences. 

    <Explanation: Paragraph on specific programming techniques and Python language elements used.>
    This sub function (loop) is solved by implementing for-loop and if statement to iterate and compare 
    the products list. Two new lists are created in this function which are new_list list and 
    new_sub_list list. New_list list is used to append the sub_new_list list while new_sub_list list 
    is used to append compared products list into six different sub lists (the number of different 
    sub lists is depending on the length of the products list). A ‘x’ is assigned to wrong to 
    represent the products list that didn’t satisfy any preferences. A for-loop is used to loop the  
    list of preferences then a if statement is used to differentiate the type of preferences by using 
    the p value(1). The p value(1) is used to represent the string operator which is ‘>’.     
    I used the combination of range () and len() built-in function in nested loop to loop the 
    products list within the given range in order to prevent the IndexError (list index out of 
    range). The new_sub_list will be initialised to an empty list in every loop to make sure the 
    products list is grouped correctly. By excluding the same products list compare with each 
    other an if statement is used to prevent it. In another if statement, the index of products list 
    (i) is used to compare the index value of products list. Group one list will use the first 
    products list to compare with the other products list. If the index value of the first products list 
    is larger than the other products list, I used the append() built-in function to append the first 
    products list into the new_sub_list list. If the index value of the first products list is smaller 
    than the other products list, a ‘x’ will be appended into the new_sub_list list. Therefore, the 
    new_sub_list list will be appended into new_list list. In this function there are part 1 and part 2, both 
    parts perform the same task. The only difference between both parts is the p value and the 
    string operator. The p value (1) represents ‘>’ while p value (-1) represents ‘<’. 

    To further illustrate how the grouping of lists works, first I used the first products list to 
    compare with other products list by excluding same list comparing with itself. Then by using 
    for-loop to update the first products list to the second products list. Second products list is 
    used to compare with the other products list by excluding same list comparing with itself. 
    Thus, the grouping of list work for the rest of the products list and ended up with a nested list(new_list).
    For example, the first new_list list for large_battery_but_cheap is [['x', 'x', 'x', 'x', 'x']]. 
    This is because the first products list (Iphone11) didn’t fulfil any preferences when 
    comparing with other products list and without comparing with itself.          


    <Paragraph on computational complexity.>
    The overall computational complexity for this sub function is O(n**3) which is caused by the
    nested three for-loop in this function at line “for z in range(len(products)):”. 
    The computational complexity for each line of codes in this sub function are commented by
    using in-line comments (#O()) as shown at the side of codes. 

    
    """
    
    new_list = []   #O(1)   # append the new_sub_list(compared list)
    wrong = 'x'     #O(1)   # represent the list that didn't satisfies any preferences

    # loop the preferences
    for x in preferences:       #O(n)
        i, p = x                #O(1)

        # ~Part 1~
        if p == 1:              #O(n)   # 1 == '>'
            for y in range(len(products)):      #O(n**2)    # loop products list
                # group the list
                new_sub_list = []               #O(n)       # grouped products list into seperate list
                for z in range(len(products)):  #O(n**3)    # loop products list
                    if products[y] != products[z]:              #O(n)   # prevent comparing same list
                        # !Only different between part 1 & 2!
                        if products[y][i] > products[z][i]:     #O(1)   # compare the value of index
                            new_sub_list.append(products[y])    #O(1)   # append products list which fulfil the preference
                        else:
                            new_sub_list.append(wrong)          #O(1)   # append 'x' if the products list didn't fulfil any preference
                new_list.append(new_sub_list)                   #O(n)   # append grouped products list
       
        # ~Part 2~
        elif p == -1:           #O(n)   # -1 == '<'
            for y in range(len(products)):      #O(n**2)    # loop the products list
                # group the list
                new_sub_list = []               #O(n)       # grouped products list into seperate list
                for z in range(len(products)):  #O(n**3)    # loop products list
                    if products[y] != products[z]:              #O(n)   # prevent comparing same list
                        # !Only different between part 1 & 2!
                        if products[y][i] < products[z][i]:     #O(1)   # compare the value of index
                            new_sub_list.append(products[y])    #O(1)   # append products list which fulfil the preference
                        else:
                            new_sub_list.append(wrong)          #O(1)   # append 'x' if the products list didn't fulfil any preference
                new_list.append(new_sub_list)                   #O(n)   # append grouped products list

    return new_list            #O(1)    # return the new_list (compared list) 


# ***Sub function***
def ans(preferences,looping,products):
    """

    Filters the compared products list(looping) and return correct list(return_list)

    Input : A products list, a looping list and a list of preferences.
    Output : A new list of products that are filtered. 

    <Explanation: Paragraph on specific programming techniques and Python language elements used.>
    In this sub function, for-loop and if statement are used to iterate and filter the compared list 
    (looping) from the previous loop function. Two new lists are created in this function which are 
    wrong_filtered_list list and return_list list (correct list). Wrong_filtered_list list is used to 
    append the filtered products list that doesn’t fulfil any preferences while return_list list is used 
    to append the filtered products list that fulfil all preferences. A ‘x’ is assigned to wrong to 
    represent the products list that didn’t satisfies any preferences. Furthermore, len() built-in 
    function is used to calculate the length of preferences list. If the preferences list is more than 
    1, looping list is divided and separated into two different lists by using slicing methods which 
    are left list (first preference) and right list (second preference). I used the combination of 
    range () and len() built-in function in nested loop to loop the products list within the given 
    range in order to prevent the IndexError (list index out of range). The second length of 
    products in for-loop (for b in range(len(products)-1)) need to be decremented by 1 because 
    we need to exclude the same list comparing with each other. If statement is used to compare 
    both left list and right list together, if both list encounter with ‘x’ the products list with index ‘a’ 
    will be appended into wrong_filtered_list list by using built-in function append(). Another 
    for-loop is used to loop the products list. An if statement and ‘not in’ operator are used to 
    filter the correct list (return_list). If products list is not in the wrong_filtered_list list, it is 
    considered as a correct list (return_list) and it will be appended into return_list. In this 
    function there are part 1 and part 2, both part perform the same task. The only difference 
    between both parts is the number of comparisons between looping list.   
    To further illustrate how the correct list has been returned, first I find out the products list that 
    doesn’t not fulfil any preferences (wrong_filtered_list) then filter the products list with 
    wrong_filtered_list list in order to get the correct products list that fulfil all preferences 
    (return_list). 


    <Paragraph on computational complexity.>
    The overall computational complexity for this sub function is O(n log n) which is caused 
    by the nested for-loop and the divided list in this function at lines “mid = len(looping)//2” and 
    "for c in products:“(any other for loop).
    The computational complexity for each line of codes in this sub function are commented by 
    using in-line comments (#O()) as shown at the side of codes. 

    
    """
    
    wrong_filtered_list = []    #O(1)   # append wrong filtered list
    return_list=[]              #O(1)   # append correct list
    wrong = 'x'                 #O(1)   # represent the list that didn't satisfies any preferences
    
    if len(preferences)>1:              #O(1)       # check length of preferences
        # divide the looping (compared list)
        mid = len(looping)//2           #O(log n)   # divide the looping list 
        # left == first preference
        left = looping[:mid]            #O(n)       # left represent the first preference
        # right == second preference
        right = looping [mid:]          #O(n)       # right represent the second preferences

        # ~Part 1~
        for a in range(len(products)):  #O(n)       # loop products list
            for b in range(len(products)-1):        #O(n**2)        # loop products list and exclude the last product list
                # !Only different between part 1 & 2!
                if left[a][b] == wrong and right[a][b] == wrong:    #O(n)   # compare both preferences together
                    wrong_filtered_list.append(products[a])         #O(n)   # append wrong products list which doesn't fulfil the preferences
            
    else:

        # ~Part 2~
        for a in range(len(products)):  #O(n)       # loop products list
            for b in range(len(products)-1):        #O(n**2)        # loop products list and exclude the last product list
                # !Only different between part 1 & 2!
                if looping[a][b] == wrong :         #O(n)           # check products list is 'x' or not
                    wrong_filtered_list.append(products[a])         #O(n)   # append wrong products list which doesn't fulfil the preferences

                
    for c in products:          #O(n)   # loop products list 
        if c not in wrong_filtered_list:            #O(n)           # remove duplicated products list
            return_list.append(c)                   #O(n)           # append correct filtered products list 


    return return_list                  #O(1)       # return return_list (correct list)  

    
def inferred_conditions(pos_examples, neg_examples):
    """
    Infers selection conditions from positive and negative product examples.

    Input:  two non-empty lists of products, pos_examples and neg_examples,
            based on the same list of _numeric_ features
    Output: Set of conditions conds such that
            len(selection(neg_examples, conds)) is minimal
            under the constraint that
            selection(pos_examples, conds)==pos_examples

    Let's first consider a simple example with one column:
    >>> pos_ex = [[10], [14]]
    >>> neg_ex = [[4], [11], [20]]
    >>> conds = inferred_conditions(pos_ex, neg_ex)
    >>> selection(pos_ex, conds)
    [[10], [14]]
    >>> selection(neg_ex, conds)
    [[11]]

    For a more complex example, let's go back to our
    phone application. Assume the user has specified
    the following positive and negative examples.
    >>> pos_ex = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> neg_ex = [['Galaxy S20', 'Samsung', 6.46, 3000, 1348],
    ...           ['V40 ThinQ', 'LG', 5.8, 3100, 598],
    ...           ['7T', 'OnePlus', 6.3, 3300, 1200]]

    Another table of new phones could be as follows.
    >>> new_phones = [['Galaxy S9', 'Samsung', 5.8, 3000, 728],
    ...               ['Galaxy Note 9', 'Samsung', 6.3, 3600, 700],
    ...               ['A9 2020', 'Oppo', 6.4, 4000, 355]]

    Then the conditions found by the function should behave
    as follows:
    >>> conds = inferred_conditions(pos_ex, neg_ex)
    >>> selection(pos_ex, conds)
    [['iPhone11', 'Apple', 6.1, 3110, 1280], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> selection(neg_ex, conds)
    [['7T', 'OnePlus', 6.3, 3300, 1200]]
    >>> selection(new_phones, conds)
    [['Galaxy Note 9', 'Samsung', 6.3, 3600, 700], ['A9 2020', 'Oppo', 6.4, 4000, 355]]


    <Paragraph on problem, challenges, and overall approach.>
    The problem in this task is to check whether there are some products list from 
    neg_examples list and new_phones list that fulfil the conditions based on the boundary value 
    of pos_examples list then return the products list which fulfil the conditions.
    The challenging part in this task is filtering the neg_examples list by using the conditions 
    based on the boundary value of pos_examples list and by using the neg_examples 
    conditions that are filtered from the conditions accurately based on the boundary value of 
    pos_examples are used to filter the new_phones list and return the products list that fulfil the 
    conditions.    
    The overall approach for this task is the boundary numeric value of pos_examples list is 
    used to set conditions within the range in order to compare with the neg_examples list and 
    new_phones list by using pairs of conditions then return the neg_examples list and 
    new_phones list which is fall in between the range (fulfil the conditions). The neg_examples 
    conditions that are filtered from pos_examples conditions are further filtered to obtain the 
    more accurate neg_examples conditions.The conditions will be used to filter the 
    new_phones list and return the new_phones list that fulfil the neg_examples conditions.


    <Paragraph on specific programming techniques and Python language elements used.>
    To solve this task, I chose for-loop and if statement to iterate the products list 
    (pos_examples, neg_examples and new_phones) to obtain and compare the conditions list 
    (boundary value). There are three new lists which are pos_numeric_index, conds and res. 
    Pos_numeric_index list is used to append the index of numeric value from the 
    pos_examples list. Conds list is used to append the conditions list based on the index of 
    numeric value of pos_examples list(j/i), string operator (‘<=’ or ‘>=’) (c) and boundary numeric 
    value of pos_examples list (v). Res list is used to append the most accurate conditions list. 

    Each list in pos_examples list has the same number of elements. Thus, a for-loop is used to 
    iterate the first pos_examples list (pos_examples[0]). An isinstance() and a str built-in 
    function is used to identify the elements in the first pos_examples list is string or not. If it is 
    string a pass statement (null statement) is used to result nothing, else the index of elements 
    in pos_examples will be appended into pos_numeric_index list by using append() built-in 
    function. Next, a nested loop is used to loop the pos_numeric_index and the pos_examples 
    list. The min() and max() built-in function is used to set the boundary value based on 
    pos_examples list and act like the limitation of conditions(v). A float() built-in function is used 
    to cast the boundary value into float value in order to encounter with both integer and 
    decimal value. The index from pos_numeric_index list(j) are used to obtain the maximum 
    value of index ‘j’ (res_max) and the string operator (‘<=’) are concatenated by using the ‘+’ 
    operator into conds. The same index from pos_numeric_index list(j) are used to obtain the 
    minimum value of index ‘j’ (res_min) and the string operator (‘>=’) are concatenated by using 
    the ‘+’ operator into conds. Thus, the conditions form in pairs which is known as boundary 
    value or range.

    Furthermore, I used the combination of range () and len() built-in function in 
    a for-loop to loop the conditions list (conds) with 2 steps (pairs). In the following if statement 
    function selection (products, conditions) from previous task is called to perform selecting 
    products list based on concatenated conditions list (conds) and return the products list which 
    fulfil the conditions. If the returned products list (neg_examples) from the selection function is 
    less than equal to 1, the conditions will be concatenated into res list by using the ‘+’ operator. 
    To make sure the most accurate conditions which fulfil what user requested based on the 
    pos_examples boundary value.

    Another for-loop with combination of range() and len() 
    built-in function is used to filter and get more accurate conditions list. Iterating the conditions 
    that fulfil the neg_examples list again by breaking down the pairs of conditions into single 
    conditions. Nested if statement is used to check accordingly to the single conditions. If the 
    conditions used that return the products list from selection function with length less than 
    equal to 1. The partner (identical first index value of pairs of conds) of the conditions that 
    grouped in pairs will be removed by using remove() built-in function if the returned products 
    list from selection function with length not equal to 1. For example, if (3, '>=', 3110.0) have a 
    return products list with length less than equal to 1, its partner (3, '<=', 3750.0) with returned 
    length of products list is not equal to 1 will be removed in order to get the more accurate 
    boundary. To be more flexible, I consider the position of the conditions can be either before 
    the more accurate conditions or after by incrementing and decrementing the more accurate 
    conditions index by 1 and the first elements of the index(m) in res list must be the same to 
    be removed. For example, res[m][0] must equal to res[m-1][0] or res[m][0] must be equal to 
    res[m+1]. Therefore, the most accurate conditions list is returned.


    <Paragraph on computational complexity.>
    The computational complexity is a general term, it is not depending on time only.
    It depends on the space that an algorithm uses as well. 
    The overall computational complexity for this function is O(n**2) which is caused by the 
    nested for-loop in this function at lines “res_max = max(float(z[j]) for z in pos_examples)” or 
    “res_min = min(float(z[j]) for z in pos_examples) “.
    The computational complexity for each line of codes in this sub function are commented by 
    using in-line comments (#O()) as shown at the side of codes. 


    """
    pos_numeric_index = []          #O(1)   # append pos_examples numeric index
    conds=[]                        #O(1)   # append conds
    res = []                        #O(1)   # append the most accurate conds

    # append the positive example numeric index into a list
    for h in pos_examples[0]:       #O(n)   # loop first row of pos_examples list
        if isinstance(h,str):       #O(n)   # remove string index in pos_examples
            pass                    #O(1)   # skip if it's string
        else:
            pos_numeric_index.append(pos_examples[0].index(h))  #O(n)       # append the index if it's numeric

    for j in pos_numeric_index:     #O(n)   # loop pos_numeric_index list
        # to find the boundary conditions value from pos_examples
        res_max = max(float(z[j]) for z in pos_examples)        #O(n**2)    # loop pos_examples to find the max value of index    
        res_min = min(float(z[j]) for z in pos_examples)        #O(n**2)    # loop pos_examples to find the min value of index
        conds += [(j,'<=',res_max)] #O(n)   # append the max value of index 
        conds += [(j,'>=',res_min)] #O(n)   # append the min value of index
    
    # first filter (less accurate)
    for k in range(0,len(conds),2): #O(n)   # loop the conds
        # call sub function (selection)
        if len(selection(neg_examples,[conds[k],conds[k+1]]))<=1:           #O(n)       # search products list in pairs of conds 
            res += conds[k],conds[k+1]      #O(n)       # append the conds by using '+' operator
    
    # second filter (more accurate) 
    for m in range(len(res)):       #O(n)   # loop res list
        if len(selection(neg_examples,[res[m]]))<=1:    #O(n)   # search products list by using conds in res list
            if len(selection(neg_examples,[res[m-1]]))!=1 and res[m][0]==res[m-1][0]:   #O(1)   # identical first index value of pairs of conds must be the same
                res.remove(res[m-1])#O(1)   # remove the conds that are less accurate if the length of returned product list is not equal to 1
            elif len(selection(neg_examples,[res[m+1]]))!=1 and res[m][0]==res[m+1][0]: #O(1)   # identical first index value of pairs of conds must be the same
                res.remove(res[m+1])#O(1)   # remove the conds that are less accurate if the length of returned product list is not equal to 1
    
    return res      #O(1)   # return the conds that are MORE accurate

  
 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
