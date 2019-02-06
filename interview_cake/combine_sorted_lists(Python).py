############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# In order to win the prize for most cookies sold, my friend Alice and I are going to merge 
# our Girl Scout Cookies orders and enter as one unit.

# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in lists. Write a function to merge
# our lists of orders into one sorted list.

# For example:

# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

# # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print merge_lists(my_list, alices_list)

############
#  My Code #
############

def merge_lists(my_list, alices_list):
    
    combined_list = []
    
    my_list_copy = my_list[:]
    alices_list_copy = alices_list[:]
    

    while (my_list_copy and alices_list_copy):
        if my_list_copy[0] <= alices_list_copy[0]:
            num = my_list_copy.pop(0)
            combined_list.append(num) 
        else:
            num = alices_list_copy.pop(0)
            combined_list.append(num) 
    
    combined_list.extend(my_list_copy if my_list_copy else alices_list_copy)
            
    return combined_list


###########
#  Tests  #
###########

# class Test(unittest.TestCase):

#     def test_both_lists_are_empty(self):
#         actual = merge_lists([], [])
#         expected = []
#         self.assertEqual(actual, expected)

#     def test_first_list_is_empty(self):
#         actual = merge_lists([], [1, 2, 3])
#         expected = [1, 2, 3]
#         self.assertEqual(actual, expected)

#     def test_second_list_is_empty(self):
#         actual = merge_lists([5, 6, 7], [])
#         expected = [5, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_both_lists_have_some_numbers(self):
#         actual = merge_lists([2, 4, 6], [1, 3, 7])
#         expected = [1, 2, 3, 4, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_lists_are_different_lengths(self):
#         actual = merge_lists([2, 4, 6, 8], [1, 7])
#         expected = [1, 2, 4, 6, 7, 8]
#         self.assertEqual(actual, expected)


# unittest.main(verbosity=2)



#################################################
#  Interview Cake Test Results from above code  #
#################################################

# test_both_lists_are_empty (__main__.Test) ... ok
# test_both_lists_have_some_numbers (__main__.Test) ... ok
# test_first_list_is_empty (__main__.Test) ... ok
# test_lists_are_different_lengths (__main__.Test) ... ok
# test_second_list_is_empty (__main__.Test) ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK


##################################################################################
#  Answer Code given by Interview Cake / O(n) time and O(n)O(n) additional space #
##################################################################################

def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list


#################################################
#  Interview Cake Test Results from above code  #
#################################################

# test_both_lists_are_empty (__main__.Test) ... ok
# test_both_lists_have_some_numbers (__main__.Test) ... ok
# test_first_list_is_empty (__main__.Test) ... ok
# test_lists_are_different_lengths (__main__.Test) ... ok
# test_second_list_is_empty (__main__.Test) ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK

