
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############


# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

# Task
# Write a function that returns both the minimum and maximum number of the given list/array.

# Examples
# min_max([1,2,3,4,5])   == [1,5]
# min_max([2334454,5])   == [5, 2334454]
# min_max([1])           == [1, 1]
# Remarks
# All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.



############
#  My Code #
############
def min_max(lst):

    sorted_list = sorted(lst)
    min_max_list = []
    
    min_max_list.append(sorted_list[0])
    min_max_list.append(sorted_list[-1])
    
    return min_max_list


#################
#  Basic Tests  #
#################

from random import randint, shuffle

def test(lst, res):
  Test.assert_equals(min_max(lst), res, "tested on " + str(lst));

Test.describe("min_max")
Test.it("should work for some examples")
test([1,2,3,4,5], [1,5])
test([2334454,5], [5, 2334454])

for i in xrange(0,20):
    r = randint(0,100)
    test([r], [r,r])



###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 618ms Passed: 122 Failed: 0
# Test Results:
#  min_max
#  should work for some examples (22 of 22 Assertions)
#  should work for random lists (100 of 100 Assertions)
# You have passed all of the tests! :)



########################
#  Alternate Solutions #
########################

def min_max(lst):
  return [min(lst), max(lst)]

def min_max(lst):
    return [sorted(lst)[0],sorted(lst)[-1]]

#Solution with out using SORT or MIN/MAX - runtime o(n)?
def min_max(lst):
    
    min_max_list = []
    
    min_num = lst[0]
    max_num = lst[0]
    
    for num in lst:
        if num <= min_num:
            min_num = num
        if num > min_num:
            if num >= max_num:
                max_num = num
    
    min_max_list.append(min_num)
    min_max_list.append(max_num)
    
    return min_max_list

