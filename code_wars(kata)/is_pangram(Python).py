
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# A pangram is a sentence that contains every single letter of the alphabet at least once. For 
# example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because
#  it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
# Ignore numbers and punctuation.


############
#  My Code #
############

def is_pangram(s):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #avoids dupls
    alpha_set = set()
    
    #looks at each character in s which has been lowercased
    for char in s.lower():
        #if its a whitespace, number, or punctuation ignore it
        if char in alphabet:
            #add it to the set 
            alpha_set.add(char)
            #check length of set, if its 26, return true
            if len(alpha_set) == 26:
                return True

    return False



#################
#  Basic Tests  #
#################

pangram = "The quick, brown fox jumps over the lazy dog!"
Test.assert_equals(is_pangram(pangram), True)


###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 632ms Passed: 7 Failed: 0
# Test Results:
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

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
