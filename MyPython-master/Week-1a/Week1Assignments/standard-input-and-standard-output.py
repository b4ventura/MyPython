
#    1. Evaluate the following in the print function:
#        a. If t1 = 72 and t2 = 7, evaluate t1/t2.
#        b. If h1 = 17.8899 and h2 = 2, evaluate h1 - h2.
#        c. If s1 = "bright" and s2 = "light", concatenate s1 and s2, so that there is a space between the words.
#        d. If a1 = 45 and b1 is 5, evaluate a1 raised to b1.
#    2. If h1 = "hello", perform appropriate operation on h1 and generate the output hellohello
#    3. Get a positive number from the user and convert it into float. Then divide it by 5 in the print function.
#    4. Use two print functions to print "Daily" and "Practice"
#        a. In two separate lines
#        b. In the same line     

print ("\n")

print ("1a. If t1 = 72 and t2 = 7, evaluate t1/t2.")
t1 = 72
t2 = 7
print ("t1/t2 = " + str(t1/t2))
print ("\n")
print ("1b. If h1 = 17.8899 and h2 = 2, evaluate h1 - h2.")
h1 = 17.8899
h2 = 2
print ("h1 - h2 = " + str(h1-h2))
print ("\n")
print ('1c. If s1 = "bright" and s2 = "light", concatenate s1 and s2, so that there is a space between the words.')
s1 = "bright"
s2 = "light"
print (s1 + " " + s2)
print ("\n")

print ("1d. If a1 = 45 and b1 is 5, evaluate a1 raised to b1.")
a1 = 45
b1 = 5
print ("a1 raised to b1 is " + str(a1**b1))
print ("\n")

print ('2. If h1 = "hello", perform appropriate operation on h1 and generate the output hellohello')
h1 = "hello"
print (h1+h1)
print ("\n")

print ("3. Get a positive number from the user and convert it into float. Then divide it by 5 in the print function.")
x = int(input("Enter a number: "))
y = float(x)
print (str(x) + " is " + str(y) + " Float")
print (str(y) + " divided by 5 is " + str(y/5))
print ("\n")
