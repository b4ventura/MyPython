# Functions Assignment

# 1.If list1 = [21, 24, 27, 32, 36, 40]. Define a function called list_3and4
#   that would take a list and output another list with elements that are
#   divisible by both 3 and 4.

def list_3and4(seq): 
    '''
     take a list and output another list with elements that are divisible by both 3 and 4
    '''
    
    print("In list_3and4(), Input: {}".format( seq))    # print seq
    
    result = []                        # initialize a new list
    
    for item in seq:                   # iterate thru seq
        ## add your code here ##
        if item / 3 == 0 and item / 4 == 0 :                 # divisible by both 3 ad 4
            result.append(item)        # append when divisible
    
    print("In list_3and4(), Result: {}".format( result))
    return result                        # return newly created list

# test code
x = list_3and4(range(1,145,12))        # range is a sequence
print(x == [])
x = list_3and4(range(0,145,12))        # range is a sequence
print(x == [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144])

list1 = [21, 24, 27, 32, 36, 40]
x = list_3and4(list1)
print(x == [24, 36])



# 2.Define a function, write_vowels that takes a word
#   and returns a list with vowels from the word.
#   Call the function and pass totality.

def write_vowels(word):
    '''
    takes a word and returns a list with vowels from the word
    '''

    print("In write_vowels(), Input: {}".format(word)) 
    vowels = []                   # create empty list to hold result
    for i in word:
        ## add your code here ##
        if i in ("a","e","i","o","u","A","E","I","O","U") :
            vowels.append(i)      # append character if a vowel
    print("In write_vowels(), Input: {}, Result: {}".format( word, vowels))
    return vowels

# test code
v = write_vowels("aeiou")
v = write_vowels("AEIOU")
v = write_vowels("san francisco")

x = []
len(x)

# test code
def test_code(v,s):
    if not v:
        print("Test Failed")
        return  False
    for i in v:
        if i not in s:
            print("Test Failed")
            return False
    print("Test Passed")
    return True

v = write_vowels("zzzzz")
False == test_code(v,"zzzzz")  # this test must fail

v = write_vowels("aeiou")
True == test_code(v,"aeiou")

v = write_vowels("AEIOU")
True == test_code(v,"AEIOU")

v = write_vowels("san francisco")
True == test_code(v, "san francisco")
