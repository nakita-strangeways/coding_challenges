
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Implement the function unique_in_order which takes as argument a sequence and returns 
#  list of items without any elements with the same value next to each other and 
#  preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


############
#  My Code #
############

def unique_in_order(iterable):
    
    if len(iterable) <= 1:
        return list(iterable)
        
    unique_list = [iterable[0]]
        
    for char in iterable:
        if char != unique_list[-1]:
            unique_list.append(char)
    
    return unique_list


#################
#  Basic Tests  #
#################

test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])


###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 577ms Passed: 10 Failed: 0
# Test Results:
#  lets test it
#  should work with empty array
#  should work with one element
# Test Passed
#  should reduce duplicates (5 of 5 Assertions)
#  and treat lowercase as different from uppercase
#  and work with int arrays
#  and work with char arrays
# You have passed all of the tests! :)



########################
#  Alternate Solutions #
########################

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

def unique_in_order(it):
    return [it[0]] + [e for i, e in enumerate(it[1:]) if it[i] != e] if it else []




