############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############


# WRITING PROGRAMMING INTERVIEW QUESTIONS HASNT MADE ME RICH YET... SO I MIGHT GIVE UP AND START TRADING APPLE STOCKS ALL DAY INSTEAD.

# First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

# So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

# The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
# The values are the price (in US dollars) of one share of Apple stock at that time.
# So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

# Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

# For example:

#    stock_prices = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices)
# # Returns 6 (buying for $5 and selling for $11)

# No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.

# Gotchas
# You can't just take the difference between the highest price and the lowest price, because the highest price might come before the lowest price. And you have to buy before you can sell.



############
#  My Code #
############

def get_max_profit(stock_prices):
    
    best_profit = None
    
    if len(stock_prices) <= 2:
        return stock_prices[1] - stock_prices[0]
        
    if len(stock_prices) <= 1:
        return 0
    
    current_max_profit = stock_prices[1] - stock_prices[0]
    
    current_min = stock_prices[0]
    
    stock_prices = stock_prices[1:]
    
    for price in stock_prices:
        profit = price - current_min
        current_min = min(price, current_min)
        best_profit = max(profit, best_profit)

    return best_profit



###########
#  Tests  #
###########

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

unittest.main(verbosity=2)



#################################################
#  Interview Cake Test Results from above code  #
#################################################

# test_error_with_empty_prices (__main__.Test) ... ok 
# test_error_with_one_price (__main__.Test) ... ok
# test_price_goes_down_all_day (__main__.Test) ... ok 
# test_price_goes_down_then_up (__main__.Test) ... ok
# test_price_goes_up_all_day (__main__.Test) ... ok
# test_price_goes_up_then_down (__main__.Test) ... ok
# test_price_stays_the_same_all_day (__main__.Test) ... ok

# (Note: The answer to question test_price_goes_down_all_day is negative instead of an exception as this "is 
# cleaner, makes our function less opinionated, and ensures we don't lose information" according to Interview Cake)

# ----------------------------------------------------------------------
# Ran 7 tests in 0.000s

# OK



#######################
#  Something to Note  #
#######################

# When I ran this code through http://pythontutor.com, I got an error when it
# tried to run the longer list.

# Error: TypeError: '>' not supported between instances of 'NoneType' and 'int'

#Basically it didn't like that best_profit was None. When I switched None to 0(zero)



####################
#  My Revised Code #
####################

def get_max_profit(stock_prices):
    
    best_profit = 0
    
    if len(stock_prices) < 2:
        return best_profit
        
    current_max_profit = stock_prices[1] - stock_prices[0]
    
    current_min = stock_prices[0]
    
    stock_prices = stock_prices[1:]
    
    for price in stock_prices:

        profit = price - current_min
        current_min = min(price, current_min)
        best_profit = max(profit, best_profit)

    return best_profit
        
        

stock_prices1 = []
stock_prices2 = [10]  
stock_prices3 = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices1)
get_max_profit(stock_prices2)
get_max_profit(stock_prices3)



#################################################
#  Interview Cake Test Results from above code  #
#################################################

# test_error_with_empty_prices (__main__.Test) ... FAIL
# test_error_with_one_price (__main__.Test) ... FAIL
# test_price_goes_down_all_day (__main__.Test) ... FAIL
# test_price_goes_down_then_up (__main__.Test) ... ok
# test_price_goes_up_all_day (__main__.Test) ... ok
# test_price_goes_up_then_down (__main__.Test) ... ok
# test_price_stays_the_same_all_day (__main__.Test) ... ok

# ======================================================================
# FAIL: test_error_with_empty_prices (__main__.Test)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "main.py", line 67, in test_error_with_empty_prices
#     get_max_profit([])
# AssertionError: Exception not raised

# ======================================================================
# FAIL: test_error_with_one_price (__main__.Test)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "main.py", line 71, in test_error_with_one_price
#     get_max_profit([1])
# AssertionError: Exception not raised

# ======================================================================
# FAIL: test_price_goes_down_all_day (__main__.Test)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "main.py", line 58, in test_price_goes_down_all_day
#     self.assertEqual(actual, expected)
# AssertionError: 0 != -2

# ----------------------------------------------------------------------
# Ran 7 tests in 0.001s

# FAILED (failures=3)




###############################################
#  Answer Code given by Interview Cake / O(n) #
###############################################

import unittest

def get_max_profit(stock_prices):
if len(stock_prices) < 2:
    raise ValueError('Getting a profit requires at least 2 prices')

# We'll greedily update min_price and max_profit, so we initialize
# them to the first price and the first possible profit
min_price  = stock_prices[0]
max_profit = stock_prices[1] - stock_prices[0]

# Start at the second (index 1) time
# We can't sell at the first time, since we must buy first,
# and we can't buy and sell at the same time!
# If we started at index 0, we'd try to buy *and* sell at time 0.
# This would give a profit of 0, which is a problem if our
# max_profit is supposed to be *negative*--we'd return 0.
for current_time in xrange(1, len(stock_prices)):
    current_price = stock_prices[current_time]

    # See what our profit would be if we bought at the
    # min price and sold at the current price
    potential_profit = current_price - min_price

    # Update max_profit if we can do better
    max_profit = max(max_profit, potential_profit)

    # Update min_price so it's always
    # the lowest price we've seen so far
    min_price  = min(min_price, current_price)

return max_profit



##############################
#  Brute Force Code given by Interview Cake / O(n^2) #
##############################

def get_max_profit(stock_prices):
max_profit = 0

# Go through every price (with its index as the time)
for earlier_time, earlier_price in enumerate(stock_prices):

    # And go through all the LATER prices
    for later_time in xrange(earlier_time + 1, len(stock_prices)):
        later_price = stock_prices[later_time]

        # See what our profit would be if we bought at the
        # earlier price and sold at the later price
        potential_profit = later_price - earlier_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

return max_profit
