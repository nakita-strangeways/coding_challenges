############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so
#  "a" is considered a different type of stone from "A".



############
#  My Code #
############

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        jewels_counter = 0
        
        #for each char in S
        for stone in S:
            #if the stone is in the list J
            if stone in J:
                #add 1 to the jewels counter
                jewels_counter += 1
        
        return jewels_counter


###########################################
#  leetcode Test Results from above code  #
###########################################


# 254 / 254 test cases passed.
# Status: Accepted

# Runtime: 120 ms, faster than 0.80% of Python3 online submissions for Jewels and Stones.