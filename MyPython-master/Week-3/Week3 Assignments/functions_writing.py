# 1.Define a function raised_function that takes two values v1 and v2
#   and computes v1 raised to v2 and returns the value.
#   Make a call to the function and supply 4 and 7.

def raised_function(v1, v2):
    '''
    1. Takes two values v1 and v2 and computes v1 raised to v2 and returns the value
    '''
    print("In raised_function(): v1: {}, v2: {}".format(v1,v2))
    
    ## add your code here ##
    result = v1 ** v2
    print("In raised_function(): v1: {}, v2: {} result: {}".format(v1,v2, result))
    
    return  result            # computes v1 raised to v2 and returns the value

# test code
print(raised_function.__doc__)
ret = raised_function(4,0)

ret = raised_function(4, 7)
print("raised_function({},{}), returns: {}".format(4,7, ret))

# test code
ret == 4 ** 7    # True means function worked
print (bool(ret))



# 2.Define a function string_loop that takes a string and loops through it
#   and prints only vowels.
#   Make a call to the function and pass “compute”.

def string_loop(strIn):
    '''
    2. takes a string and loops through it and prints only vowels
    '''
    print("In string_loop(): strIn: {}".format(strIn))
    
    ## add your code here ##
    # using for loop iterate the string and 
    # look if character in string is a vowel "aeiouAEIOU"
    for i in strIn :
        if  i in ("a","e","i","o","u","A","E","I","O","U") :
            print(i, end=' ')
    print()
    

# test code

print(string_loop.__doc__)
string_loop("aeiou")
string_loop("AEIOU")
string_loop("123456")
string_loop("spam and eggs")
string_loop("")

string_loop("compute")


# 3.Define a function string_len that takes a default value s1=“apples”
#   and prints the length of the string.
#   Call the function and don’t pass any arguments.
#   Then call the function again and pass “watermelon”.

def string_len(s1="apples"):
    '''
    takes a default value s1=“apples” and prints the length of the string
    '''
    print("In string_len(): s1: {}".format(s1))
    ## add your code here ##
    
    result = len(s1)           #  find the length of s1     
    print("String: {:30s}  Length: {}".format(s1, result))
    
    return s1

# test code
x = string_len('1')
x = string_len('12')
x = string_len('')

# test code
len('apples') == string_len()

# test code
len("watermelon") == string_len("watermelon")

string_len()
string_len("watermelon")


# 4.Define a function mult_two that takes default arguments a = 10, b=11.
#   The function should check if a is a multiple of b.
#   In the function call, supply b = 7 and a = 21 in that order.

def mult_two(a=10, b=11):

    '''
    Takes default arguments a = 10, b=11. The function should check if a is a multiple of b
    returns True or False depending on being a multiple or not
    '''
    
    ## add your code here ##
    result = True
    if a % b == 0 :
        print("{} is a multiple of {}, return {}".format(a,b, result))
    else:
        result = False
        print("{} is NOT a multiple of {}, return {}".format(a,b, result))
        
    return True  # returns True or False
        
# test code
False == mult_two()       # uses default argument for a and b

True == mult_two(10,5)

True == mult_two( a = 21, b = 7)

True == mult_two(b=7, a = 21)






