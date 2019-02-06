############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# I figured out how to get rich: online poker.

# I suspect the online poker game I'm playing shuffles cards by doing a single riffle. 
# A "riffle" is the standard way people shuffle cards by hand. You know, the thing that looks like this:


# Here's a rigorous definition of the riffle algorithm:

# - cut the deck into halves half1 and half2
# - grab a random number of cards from the top of half1 (could be 0, must be less than or equal to the number 
#     of cards left in half1) and throw them into the shuffled_deck
# - grab a random number of cards from the top of half2 (could be 0, must be less than or equal to the number 
#     of cards left in half2) and throw them into the shuffled_deck
# - repeat steps 2-3 until half1 and half2 are empty.

# To prove this, let's write a function to tell us if a full deck of cards shuffled_deck is a single riffle of 
# two other halves half1 and half2.

# We'll represent a stack of cards as a list of integers in the range 1..521..52 (since there are 5252 distinct 
# cards in a deck).
# Why do I care? A single riffle is not a completely random shuffle. If I'm right, I can make more informed bets 
# and get rich and finally prove to my ex that I am not a "loser with an unhealthy cake obsession" (even though 
# it's too late now because she let me go and she's never getting me back).

############
#  My Code #
############



###########
#  Tests  #
###########




#################################################
#  Interview Cake Test Results from above code  #
#################################################



##################################################################################
#  Answer Code given by Interview Cake / O(n) time and O(n)O(n) additional space #
##################################################################################



#################################################
#  Interview Cake Test Results from above code  #
#################################################



