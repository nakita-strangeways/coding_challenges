############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.



############
#  My Code #
############

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #if there arent any strings, return nothing 
        if not strs: return ''

        #using min and max (when min/max have same first letter, all other words between have same letter too)
        string1 = min(strs)
        string2 = max(strs)

        #checks if first letter in string1 matches string2 using enumerate
        for index, letter in enumerate(string1):
            if letter != string2[index]:
                return string1[:index]

        return string1

###########################################
#  leetcode Test Results from above code  #
###########################################

# 118 / 118 test cases passed.
# Status: Accepted
# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Longest Common Prefix.
