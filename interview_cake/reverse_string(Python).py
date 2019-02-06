############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# WRITE A FUNCTION THAT TAKES A LIST OF CHARACTERS AND REVERSES THE LETTERS IN PLACE.

# Why a list of characters instead of a string?

# The goal of this question is to practice manipulating strings in place. Since we're modifying the input, we need a mutable ↴ type like a list, instead of Python's immutable strings.

# Breakdown
# In general, an in-place ↴ algorithm will require swapping elements.


############
#  My Code #
############

def reverse(list_of_chars):

    list_of_chars = list_of_chars[::-1]

    return list_of_chars


###########
#  Tests  #
###########

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)



#################################################
#  Interview Cake Test Results from above code  #
#################################################

test_empty_string (__main__.Test) ... ok
test_longer_string (__main__.Test) ... FAIL
test_single_character_string (__main__.Test) ... ok

======================================================================
FAIL: test_longer_string (__main__.Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "main.py", line 41, in test_longer_string
    self.assertEqual(list_of_chars, expected)
AssertionError: Lists differ: ['A', 'B', 'C', 'D', 'E'] != ['E', 'D', 'C', 'B', 'A']

First differing element 0:
'A'
'E'

- ['A', 'B', 'C', 'D', 'E']
+ ['E', 'D', 'C', 'B', 'A']

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)


#######################################################################
#  Answer Code given by Interview Cake / O(n) time and O(1)O(1) space #
#######################################################################
import unittest

def reverse(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1


#################################################
#  Interview Cake Test Results from above code  #
#################################################


test_empty_string (__main__.Test) ... ok
test_longer_string (__main__.Test) ... ok
test_single_character_string (__main__.Test) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK


