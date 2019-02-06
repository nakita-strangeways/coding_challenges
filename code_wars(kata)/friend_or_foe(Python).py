
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, 
# you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# Note: keep the original order of the names in the output.

############
#  My Code #
############

def friend(x):
    #Code
    
    friends = []
    
    for name in x:
        if len(name) == 4:
            friends.append(name)
            
    return friends


#################
#  Basic Tests  #
#################

Test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])


###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 599ms Passed: 15 Failed: 0
# Test Results:
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

def friend(x):
    return [f for f in x if len(f) == 4]

    
