# Author: Yong Zi Ying
# Dynamic Programming
# Grade: 19.4/20 HD 
#%% Task 1
def best_schedule(weekly_income, competitions):
    ''' This function is used to search for the largest income + winning within the week by using brute force smartly.
    :Input: A list of weekly_income and a list of tuple of competitions
    :Output: The maximum amount of money that can be earned
    :Time Complexity: Best and worst case will be the same (the loop did not exit early) which is O (N log (N)), 
                      where N is the length of weekly_income + competitions (combine) 
    :Auxiliary Space Complexity: O (M), where M is the length of memo which is representing the length of weekly_income
    :Space Complexity: O (N + M), space complexity is input space + extra space.
                       The input space is O (N) where N is the total element of weekly_income + competitions (combine).
                       The extra space is O (M), where M is the length of weekly_income only (explained above). 
    :Explanation: An extra memo list is created and convert the weekly_income list into list of tuples
                  which is the same format as competitions then combine both weekly_income and competitions. 
                  The optimal amount of money that can earn on each week is saved into the memo. 
                  The maximum amount of money will be store at the last element of memo. 
                  More details explanation is commented at the code.
    '''
    size = len(weekly_income)
    memo = [0] * (size + 1)     # include base case
    memo[0] = 0 # base case
    base_tuple = (0, 0, 0)
    
    # change weekly_income into tuple and reposition it (start with index 1)
    for i in range(size):
        weekly_income[i] = (i+1, i+1, weekly_income[i])

    # add base tuple into weekly_income
    weekly_income.append(base_tuple)

    # combine both weekly_income + competitions (reposition it and start with index 1) 
    for j in range(len(competitions)):
        competitions[j] = (competitions[j][0] + 1, competitions[j][1] + 1, competitions[j][2])
        weekly_income.append(competitions[j])

    # sort the end_time (second element of the tuple, index 1)
    weekly_income.sort(key= lambda x:x[1])

    # The weekly_income is the combination of weekly_income and competitions 
    # The list is sorted based on the end_time
    index = 0
    for k in range(1, len(weekly_income)):
        income = weekly_income[k][2] + memo[weekly_income[k][0] - 1]
        if weekly_income[k][1] != weekly_income[k-1][1]:
            # add the winnings into memo
            index += 1
            memo[index] = income
        elif weekly_income[k][1] == weekly_income[k-1][1]:
            # found new large winnings
            if income > memo[index]:
                memo[index] = income
    return memo[-1]


# %% Task 2
def best_itinerary(profit, quarantine_time, home):
    ''' This function is used to search for the maximum profit within the days and cities by using brute force 
    smartly. Salesperson has 3 decisions to move around the city either stay, move left or move right. It 
    takes one day to move from city to city and each city has instituted a policy of having traveler’s quarantine.
    :Input: A list of lists of profit which represent different day and city (profit[day][city]), a list of 
            quarantine_time that is required to quarantine before working at the city and home is an integer 
            between 0 to n-1 inclusive, where n is the length of city.
    :Output: Maximum amount of money that can be earned by the salesperson by walking through the best path of the city.
    :Time Complexity: Best and worst case will be the same (the loop did not exit early) which is O (ND), 
                      where N is the length of cities and D is the number of days.
    :Auxiliary Space Complexity: O (ND),  where N is the length of cities and D is the number of days. 
                                 As it is a matrix so it required ND extra space to keep track of the maximum profit.
    :Space Complexity: O (ND + ND) = O (2ND) = O (ND), space complexity is input space + extra space.
                       The input space is O (ND) where N is the length of cities and D is the number of days.
                       The extra space is O (ND) as well where N is the length of cities and D is the number of days. (explained above)
    :Explanation: A ND size of memo is created and initialized the list of lists of lists of the memo which is 
                  the most inner  lists. The most inner list consists of 3 elements (move, quarantine, stay) which are 
                  the maximum profit that MOVE from other city, the previous maximum profit that move from other 
                  city is saved meanwhile it is used to update or insert the maximum profit at the day after 
                  QUARANTINE at the city, the maximum profit that STAY at the same city or stay at new city after 
                  moving around. Three decisions need to make at each city either stay, move left or move right. By 
                  comparing the first element of the most inner lists which is move and the last element of the most 
                  inner lists which is stay, the largest profit from both is saved at the last element of the most inner 
                  lists. The maximum amount of money that can be earned by the salesperson is the maximum value 
                  of the last element of the most inner lists on the last day.
                  More details explanation is commented at the code.
    '''
    day_size = len(profit)
    city_size = len(profit[0])
    memo =  [0] * (day_size+1)      # memo[-1] is base case
    max_day = len(profit)
    move_quarantine_stay = 3        # for the inner list with 3 elements
    
    # store city with a list of 3 elements (move from other city, quarantine, stay)
    for i in range(len(memo)):
        memo[i] = []
        for j in range(city_size):
             memo[i].append([])
             for _ in range(move_quarantine_stay):      # constant 
                 memo[i][j].append(0)

    # setup the first day into memo (D0)
    day = 0 
    memo[day][home][-1] = (profit[day][home])   # stay at first day
    if day+quarantine_time[home]+2 < max_day:      # BOUNDARY CHECK
        daytomove = day+quarantine_time[home]+2      # move at the first day and move back on the next day to same city
        memo[daytomove][home][2] = profit[daytomove][home] 
    # home is the first element which can either stay or move right only
    if home == 0:   # first element on first day
        for innercity in range(1, city_size):
            if day+quarantine_time[home+innercity]+1 < max_day:      # BOUNDARY CHECK
                daytomove = day+quarantine_time[home+innercity]+1     # move right on first day 
                memo[daytomove][home+innercity][2] = profit[daytomove][home+innercity]
                day += 1

    # home is the last element which can either stay or move left only
    elif home == city_size-1:   # last element on first day
        for innercity in range(1, city_size):
            if day+quarantine_time[home-innercity]+1 < max_day:      # BOUNDARY CHECK
                daytomove = day+quarantine_time[home-innercity]+1     # move left on first day
                memo[daytomove][home-innercity][2] = profit[daytomove][home-innercity]
                day += 1

    # home is the middle element which can either stay, move left or move right    
    elif home > 0 and home < city_size-1:
        for innercity in range(1, city_size-1):
            if home+innercity < city_size:  # BOUNDARY CHECK
                if day+quarantine_time[home+innercity]+1 < max_day:      # BOUNDARY CHECK
                    daytomove = day+quarantine_time[home+innercity]+1     # move right on first day 
                    memo[daytomove][home+innercity][2] = profit[daytomove][home+innercity]
                    day += 1
        day = 0
        for innercity in range(1, home+1):
            if day+quarantine_time[home-innercity]+1 < max_day:      # BOUNDARY CHECK
                daytomove = day+quarantine_time[home-innercity]+1     # move left on first day
                memo[daytomove][home-innercity][2] = profit[daytomove][home-innercity]
                day += 1
    
    # setup memo from D1
    for day in range(1, day_size):     # loop day_size times
        for city in range(city_size):      # loop city_size times
            max_right_diagonal = 0
            max_left_diagonal = 0
            if  city == 0:    # city that can move from right diagonally ONLY (first element)
                max_left_diagonal = -1 
                max_right_diagonal_stay = memo[day-1][city+1][2] 
                max_right_diagonal_move = memo[day-1][city+1][0] 
                if max_right_diagonal_move > max_right_diagonal_stay:   # choose biggest profit between stay and move
                    max_right_diagonal = max_right_diagonal_move
                elif max_right_diagonal_stay > max_right_diagonal_move:
                    max_right_diagonal = max_right_diagonal_stay

            elif city == city_size-1:  # city that can move from left diagonally ONLY (last element) 
                max_right_diagonal = -1
                max_left_diagonal_stay = memo[day-1][city-1][2]
                max_left_diagonal_move = memo[day-1][city-1][0]
                if max_left_diagonal_move > max_left_diagonal_stay:     # choose biggest profit between stay and move
                    max_left_diagonal = max_left_diagonal_move
                elif max_left_diagonal_stay > max_left_diagonal_move:
                    max_left_diagonal = max_left_diagonal_stay

            elif city > 0 and city < city_size-1: # city that can move from left and right diagonally
                # check right diagonally
                max_right_diagonal_stay = memo[day-1][city+1][2] 
                max_right_diagonal_move = memo[day-1][city+1][0] 
                if max_right_diagonal_move > max_right_diagonal_stay:   # choose biggest profit between stay and move
                    max_right_diagonal = max_right_diagonal_move
                elif max_right_diagonal_stay > max_right_diagonal_move:
                    max_right_diagonal = max_right_diagonal_stay

                # check left diagonally
                max_left_diagonal_stay = memo[day-1][city-1][2]
                max_left_diagonal_move = memo[day-1][city-1][0]
                if max_left_diagonal_move > max_left_diagonal_stay:     # choose biggest profit between stay and move
                    max_left_diagonal = max_left_diagonal_move
                elif max_left_diagonal_stay > max_left_diagonal_move:
                    max_left_diagonal = max_left_diagonal_stay
                    
                # move or stay value at left and right diagonal is not exist
                if max_left_diagonal == 0 and max_right_diagonal == 0:
                    max_right_diagonal = memo[day-1][city+1][0]
                    max_left_diagonal = memo[day-1][city-1][0]

            # save the optimal value for the possible MOVE from adjacent city
            if max_left_diagonal >= max_right_diagonal:
                memo[day][city][0] = max_left_diagonal
            elif max_right_diagonal > max_left_diagonal:
                memo[day][city][0] = max_right_diagonal

            # save the optimal value when there's a new move from other city, calculate the profit after QUARANTINE at the city
            # and insert the profit into the stay column on the next day of the last day of quarantine 
            if memo[day-1][city][0] != 0:   # if move != 0, quarantine on next day
                if day+quarantine_time[city] < max_day:      # BOUNDARY CHECK
                    memo[day][city][1] = memo[day-1][city][0]
                    daytomove = day+quarantine_time[city]
                    memo[daytomove][city][2] = memo[day][city][1] + profit[daytomove][city]     # setup the profit after quarantine
              
            # save the optimal value for stay, replace the previous profit that set after quarantine if larger profit is found
            if memo[day-1][city][2] != 0:
                prev_stay = memo[day-1][city][2] + profit[day][city]    
                current_stay = memo[day][city][2]
                if prev_stay > current_stay:   # update current stay if new bigger profit found
                    memo[day][city][2] = prev_stay 
    
    max_profit = 0
    # the max profit will be placed at the last element of the innerlist of each city
    for last_max_city in range(city_size):
        if memo[day_size-1][last_max_city][2] >= max_profit:
            max_profit = memo[day_size-1][last_max_city][2]
    
    return max_profit    