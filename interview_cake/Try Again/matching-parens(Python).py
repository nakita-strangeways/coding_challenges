############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# I like parentheticals (a lot).

# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

# Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).

# Gotchas
# We can do this in O(n)O(n) time.

# We can do this in O(1)O(1) additional space.

############
#  My Code #
############




###########
#  Tests  #
###########

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)



#################################################
#  Interview Cake Test Results from above code  #
#################################################




#######################################################################
#  Answer Code given by Interview Cake / O(n) time and O(1)O(1) space #
#######################################################################
import unittest

def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    open_nested_parens = 0
    
    for position in range(opening_paren_index + 1, len(sentence)):
        char = sentence[position]
    
        if char == '(':
            open_nested_parens += 1
        
        elif char == ")"
            if open_nested_parents == 0:
                return position
            
            else:
                open_nested_parens -= 1
    
    raise Exception('no closing parenthesis')


#################################################
#  Interview Cake Test Results from above code  #
#################################################

test_all_openers_then_closers (__main__.Test) ... ok
test_mixed_openers_and_closers (__main__.Test) ... ok
test_no_matching_closer (__main__.Test) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK


