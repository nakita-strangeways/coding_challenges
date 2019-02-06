############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# YOURE WORKING ON A SECRET TEAM SOLVING CODED TRANSMISSIONS

# Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.

# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place. 


############
#  My Code #
############




###########
#  Tests  #
###########

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)



#################################################
#  Interview Cake Test Results from above code  #
#################################################




#######################################################################
#  Answer Code given by Interview Cake / O(n) time and O(1)O(1) space #
#######################################################################

import unittest

def reverse_words(message):

    # Decode the message by reversing the words
    reverse_characters(message,0,len(message)-1)
    
    current_word_start_index = 0
    
    for i in range(len(message) + 1):
        
        if (i == len(message)) or (message[i] == " "):
            reverse_characters(message,current_word_start_index, i - 1)
            
            current_word_start_index = i + 1
            
def reverse_characters(message, left_index, right_index):
    while left_index < right_index:
        message [left_index], message[right_index] = message[right_index], message[left_index]
        left_index += 1
        right_index -= 1


#################################################
#  Interview Cake Test Results from above code  #
#################################################

test_empty_string (__main__.Test) ... ok
test_multiple_words_different_lengths (__main__.Test) ... ok
test_multiple_words_same_length (__main__.Test) ... ok
test_one_word (__main__.Test) ... ok
test_three_words (__main__.Test) ... ok
test_two_words (__main__.Test) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK


