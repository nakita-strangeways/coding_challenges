
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Task
# Given a string str, reverse it omitting all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str

# A string consists of lowercase latin letters, digits and symbols.

# [output] a string


############
#  My Code #
############

def reverse_letter(string):
    #do your magic here
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string_copy = list(string[:])
    string_length = len(string_copy)
    reversed = []
    
    while string_length != 0:
        char = string_copy.pop(-1)
        string_length -= 1
        if char in alphabet:
            reversed.append(char)
            
    return "".join(reversed)


#################
#  Basic Tests  #
#################

Test.describe("Basic test")

Test.assert_equals(reverse_letter("krishan"),"nahsirk")

Test.assert_equals(reverse_letter("ultr53o?n"),"nortlu")

Test.assert_equals(reverse_letter("ab23c"),"cba")

Test.assert_equals(reverse_letter("krish21an"),"nahsirk")


###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 665ms Passed: 104 Failed: 0
# Test Results:
#  Basic test
# Test Passed
# Test Passed
# Test Passed
# Test Passed
#  Random tests
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

def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]


def reverse_letter(string):
    str = ""
    for n in string:
        if n.isalpha():
            str = n + str
    return str

def reverse_letter(string):
    new_str=""
    for i in string:
        if i.isalpha():
            new_str=i+new_str
    return new_str