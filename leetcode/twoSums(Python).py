############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


#############
#  My Code  #
#############

class Solution:
    def twoSum(nums, target):
        #base case = an empty list
        if len(nums) <= 1:
            return False
        
        #create a dictionary to hold answers    
        answers_dict = {}
        
        #using the index to loop through
        for index in range(len(nums)):
            #if the index is in answers dict
            if nums[index] in answers_dict:
                #return the value of the dictionary from nums(index) and the index currently on
                return [answers_dict[nums[index]], index]
            #otherwise, add the target minus the number at that index, and the index it was found on    
            else:
                answers_dict[target - nums[index]] = index
                

###########################################
#  leetcode Test Results from above code  #
###########################################

29 / 29 test cases passed.
Status: Accepted
Runtime: 36 ms, faster than 99.76% of Python3 online submissions for Two Sum.

