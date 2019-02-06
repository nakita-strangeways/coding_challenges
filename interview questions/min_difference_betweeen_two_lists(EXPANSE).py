# Given two arrays of integers, compute the smallest non-negative difference 
# between any pair of values (using one value from each array).

 
# Examples:
# Input: A = [9, 16, 5]
#        B = [15, 1, 3]
# Output: 1 (The difference of the pair (16, 15))


# Input: A = [40, 10, 90]
#        B = [20, 55, 75]
# Output: 10 (The difference of the pair (20, 10))


#############################################################

#brute force 0(n2)

def findSmallestDifference(A, B, lenA, lenB):
    
    
    current_smallest_difference = sys.maxsize

    
    for a_num in A:
        for b_num in B: 
            if abs(a_num - b_num) < current_smallest_difference:
                current_smallest_difference = abs(a_num - b_num)

    return current_smallest_difference

# efficient: O(n Log n)

def findSmallestDifference(A, B):
    
    difference = sys.maxsize

    comb_lists = sorted(A+B)
    
    for index in range(len(comb_lists)-1):
        if comb_lists[index+1] - comb_lists[index] < difference:
            difference = comb_lists[index+1] - comb_lists[index]
    return difference

