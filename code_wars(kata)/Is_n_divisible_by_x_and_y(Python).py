############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.

# Example:
# is_divisible(3,1,3)--> true because 3 is divisible by 1 and 3
# is_divisible(12,2,6)--> true because 12 is divisible by 2 and 6
# is_divisible(100,5,3)--> false because 100 is not divisible by 3
# is_divisible(12,7,5)--> false because 12 is neither divisible by 7 nor 5



############
#  My Code #
############

def is_divisible(n,x,y):
    #your code here
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False




#################
#  Basic Tests  #
#################

Test.assert_equals(is_divisible(3,3,4),False)
Test.assert_equals(is_divisible(12,3,4),True)
Test.assert_equals(is_divisible(8,3,4),False)
Test.assert_equals(is_divisible(48,3,4),True)




#################################################
#  CodeWars Test Results from above code  #
#################################################

# Time: 589ms Passed: 50 Failed: 0
# Test Results:
#  Basic tests
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
#  Random tests
#  Testing for is_divisible(80, 2, 20)
#  Testing for is_divisible(24, 1, 2)
#  Testing for is_divisible(342, 6, 3)
#  Testing for is_divisible(140, 7, 10)
#  Testing for is_divisible(1690, 10, 13)
#  Testing for is_divisible(1191, 7, 17)
#  Testing for is_divisible(2340, 9, 20)
#  Testing for is_divisible(36, 4, 1)
#  Testing for is_divisible(120, 2, 10)
#  Testing for is_divisible(1281, 5, 16)
#  Testing for is_divisible(2129, 8, 19)
#  Testing for is_divisible(2881, 9, 20)
#  Testing for is_divisible(576, 4, 16)
#  Testing for is_divisible(1153, 8, 18)
#  Testing for is_divisible(505, 9, 8)
#  Testing for is_divisible(234, 6, 13)
#  Testing for is_divisible(714, 3, 14)
#  Testing for is_divisible(108, 2, 6)
#  Testing for is_divisible(316, 5, 9)
#  Testing for is_divisible(1198, 7, 9)
#  Testing for is_divisible(120, 1, 10)
#  Testing for is_divisible(49, 4, 6)
#  Testing for is_divisible(360, 3, 15)
#  Testing for is_divisible(1920, 8, 15)
#  Testing for is_divisible(65, 2, 16)
#  Testing for is_divisible(504, 3, 14)
#  Testing for is_divisible(271, 1, 15)
#  Testing for is_divisible(288, 9, 2)
#  Testing for is_divisible(13, 1, 3)
#  Testing for is_divisible(19, 6, 1)
#  Testing for is_divisible(721, 9, 20)
#  Testing for is_divisible(1320, 8, 11)
#  Testing for is_divisible(630, 7, 15)
#  Testing for is_divisible(1100, 10, 10)
#  Testing for is_divisible(113, 2, 4)
#  Testing for is_divisible(757, 7, 9)
#  Testing for is_divisible(673, 8, 12)
#  Testing for is_divisible(1344, 8, 12)
#  Testing for is_divisible(50, 7, 7)
#  Testing for is_divisible(421, 10, 7)
# You have passed all of the tests! :)



#######################
#  Something to Note  #
#######################

# a one line code option
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

