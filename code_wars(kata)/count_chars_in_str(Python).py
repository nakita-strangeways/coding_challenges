
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# The main idea is to count all the occuring characters(UTF-8) in string. If you have string 
# like this aba then the result should be { 'a': 2, 'b': 1 }

# What if the string is empty ? Then the result should be empty object literal { }



############
#  My Code #
############

def count(string):
    # The function code should be here
    
    characters_dict = {}
    if not string:
        return characters_dict
        
    for char in string:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict



#################
#  Basic Tests  #
#################


test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})

###########################################
#  CodeWars Test Results from above code  #
###########################################

# Test Results:
#  Basic Tests
#  should give empty dictionary if string is empty
#  should get as a result two A characters
#  should get as a result of two a characters and two b characters
#  should get as a result of two a characters and two b characters, showing that the result order does not matter
#  Random Tests
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
# You have passed all of the tests! :)




########################
#  Alternate Solutions #
########################

def count(string):
  
    return {i: string.count(i) for i in string}


def count(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter
