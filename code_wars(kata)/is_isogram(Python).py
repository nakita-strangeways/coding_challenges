
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an 
# isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case



############
#  My Code #
############

def is_isogram(string):
    #your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_set = set()
    
    for char in string.lower():
    
        if char in alphabet and char in alphabet_set:
            return False
        else:
            if char in alphabet and char not in alphabet_set:
                alphabet_set.add(char)
    return True


#################
#  Basic Tests  #
#################

Test.assert_equals(is_isogram("Dermatoglyphics"), True )
Test.assert_equals(is_isogram("isogram"), True )
Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
Test.assert_equals(is_isogram("isIsogram"), False )
Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )


###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 626ms Passed: 50 Failed: 0
# Test Results:
#  Basic tests
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
#  Random tests
#  Testing for wrpyrsexyoxodwrhptqjiehwxdgnxwalsnpdp
#  Testing for zkywqowpkwpvrenr
#  Testing for hetmdiyxjsrqlobfmluyrfyntcnfgykcoljdvkc
#  Testing for jrqqtmkbvfepltlbnmybnf
#  Testing for qyekwofrozowb
#  Testing for vpczlxtzbkgghvbclwvw
#  Testing for vatjjewlppdtam
#  Testing for pvczxlqaupbojrfpdqtvxbmqtvkqb
#  Testing for xdnlnwmdzkmmhenifgn
#  Testing for clnlzcebbkvdyrkcnql
#  Testing for ixzuvsewuijnrooqa
#  Testing for lihflxnfewavooaqrqmiarxzhozumrzcc
#  Testing for ieorclcxcnywsurtuefajdzugyedc
#  Testing for plmiqzaozywoffgcdlrjehnfrqozty
#  Testing for dqcxuibejlkjbzbxzlz
#  Testing for edvfcbjixkpwvamrpbgqniparmtdhor
#  Testing for pzwiuwfnwfkvztomjlbwjkwjqrnaq
#  Testing for guxas
#  Testing for nevisbrqossycshysvpgnqzffhzxqtebtibbyqprhc
#  Testing for kihadgldobwniadufycx
#  Testing for qxpjgjgbmnjafyv
#  Testing for jjvkiagtmpkxnxfgigdbatmxlbgczzzpznikwuc
#  Testing for heuleqqtfomeckamjyteqvcmczwex
#  Testing for nquypfujdbdsbvqlofjtcyxlmmbplcpuqibsoiufge
#  Testing for kndyewuspplkedfyzcsqifsdlnepnilfuzvbxjwg
#  Testing for ocyczvmtgplajbxclucjkzyzzk
#  Testing for oedpqvrmpdufoatvukbityaourdmrq
#  Testing for fqafytzlb
#  Testing for gfysg
#  Testing for kpngqinjgvcemxp
#  Testing for svawmzzdcnbvnnrty
#  Testing for slxyehxdfomhkizdbfmrqjuzgzjyxdkmdxd
#  Testing for vlkzumqafuygsrefltmb
#  Testing for lquzkyqrajy
#  Testing for eplyqudsrcffweejljpdpkihhqojdquvznywjfll
#  Testing for dvcfrakklxmz
#  Testing for misoogceusujmlydioimykbxgbaywfzfdzvtfvzyepg
#  Testing for udqyeutzqeqzcgyorllhpaxczrslgfoaoa
#  Testing for vyolwiofvweeawvhrzulmgmoupumwjbsaqwwf
#  Testing for lsfffbaaiisqnxhiofal
# You have passed all of the tests! :)



########################
#  Alternate Solutions #
########################

def is_isogram(string):
    #turn string into lowercase, and a set, then compare the lengths. 
    return len(string) == len(set(string.lower()))

def is_isogram(string):
    string = string.lower()
    for letter in string:
        #if there is more than one of these letters - return false
        if string.count(letter) > 1: return False
    return True

def is_isogram(string):
    #your code here
    char_dict = {}
    string = string.lower()
    
    for char in string:
        if char in char_dict:
            # increment count of this character
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    
    # loop over the characters in dictionary, if any have
    # more than 1 found, this string is not an isogram, so break
    # the loop and function and return False.
    for key in char_dict:
        if char_dict[key] > 1:
            return False
            
    # If no duplicates were found in the loop directly above,
    # this must be an isogram, so return true!
    return True
