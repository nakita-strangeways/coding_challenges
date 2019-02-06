
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 
# percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the 
# town need to see its population greater or equal to p = 1200 inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.
# More generally given parameters:

# p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

# the function nb_year should return n number of entire years needed to get a population greater or equal to p.

# aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)

# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10
# Note: Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter 
# percent is 2 you have to convert it to 0.02.



############
#  My Code #
############

def nb_year(p0, percent, aug, p):
    
    growth_percent = float(percent) / 100
    year_counter = 0
        
    while p0 < p:
        
        p0 = p0 + p0 * growth_percent + aug
        year_counter += 1
        
    return year_counter


#################
#  Basic Tests  #
#################

Test.describe("nb_year")
Test.it("Basic tests")
Test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
Test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
Test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)


###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 631ms Passed: 106 Failed: 0
# Test Results:
#  nb_year
#  Basic tests (106 of 106 Assertions)
# You have passed all of the tests! :)



########################
#  Alternate Solutions #
########################

def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year
