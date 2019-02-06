############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:

# Could you solve it without converting the integer to a string?

########################################
#  My Code /  turning x into a string  #
########################################

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #if x is one number - return True
        if len(str(x)) == 1:
            return True
        
        # make a copy of x as a string
        temporary = str(x)
        
        #how many indicies are in x - minus one)
        index = len(temporary) - 1
        
        #will hold numbers as they are reversed, holding the last # from temporary 
        reverse = temporary[-1]

        #our counter for index so we know when weve completed the number
        while index > 0:
            #remove last number from temporary since its already inside reverse
            temporary = temporary[:-1]
            #add the new last number to reverse
            reverse += temporary[-1]
            #subtract 1 from the index counter
            index -= 1

        #turn x into a string and compare to reverse. 
        if reverse == str(x):
            return True
        else:
            return False
        

###########################################
#  leetcode Test Results from above code  #
###########################################

# 11509 / 11509 test cases passed.
# Status: Accepted
# Runtime: 256 ms, faster than 95.16% of Python3 online submissions for Palindrome Number.


###############################################
#  My Code / without turning x into a string  #
###############################################

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #if x is one number - return True
        if len(str(x)) == 1:
            return True
        
        temporary=x
        reverse=0

        while(temporary>0):
            #mod x by 10, getting the last digit from x
            digit=temporary%10
            #multiply reverse by 10, + digit, adds digit to reverse
            reverse=reverse*10+digit
            #floor divide x by 10 - removing the last digit from x
            temporary=temporary//10

        if(x==reverse):
            return True
        else:
            return False

###########################################
#  leetcode Test Results from above code  #
###########################################

# 11509 / 11509 test cases passed.
# Status: Accepted
# Runtime: 252 ms, faster than 96.69% of Python3 online submissions for Palindrome Number.

######################################################
#  Code by mingkunhe / found in discussion comments  #
######################################################

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        stringX = str(x)
        if stringX[::-1] == stringX:
            return True
        else:
            return False

###########################################
#  leetcode Test Results from above code  #
###########################################

11509 / 11509 test cases passed.
Status: Accepted
Runtime: 252 ms, faster than 96.69% of Python3 online submissions for Palindrome Number.




