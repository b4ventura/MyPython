#    Formatted Print and Comments Writting Assignment


#    1. Perform the following and use comments to document your work.
#        a. If w1 =1723.3789913, use format specifier to only print 4 decimal places in w1.
#        b. If a1 = 16.789, b1 = "working" and c1 = 19, in the print statement, use format specifiers
#        so that the output will have a1 as an integer, b1 as a string and c1 as a float.

print ("1a. If w1 =1723.3789913, use format specifier to only print 4 decimal places in w1.")

w1 =1723.3789913
print ('{:08.4f}'. format (w1))
print (" ====")

print ("1b")
print ('If a1 = 16.789, b1 = "working" and c1 = 19)')


a1 = 16.789
b1 = "working"
c1 = 19

print ("a1 is equal to " + '{:02.0f}'.format(a1))
print ("b1 is " + '{:s}'.format(b1))
print ("c1 is equal to " + '{:f}'.format(c1))
print (" ====")

print ("2. Use format() method and print values 81 and 729. Print the same values using labels first")
print ("and second and switch input order.")

print ('{0} and {1}' .format (81 , 729))
print ('{1} and {0}' .format (81 , 729))
print (" ====")


print ("3. Ask the user to input an integer. Perform the required operations to make the user input is")
print ("an integer and then square the number and then print them using format specifiers.")
print ("Include single and multiple line comments to explain the code.")

x = int(input("Enter a Number: "))
print (x**2)
print ("====")

print ("4. Which format specifier would you use for integers, floats and strings?")
print ("Use d or i for integers")
print ("Use f for floats")
print ("And s for strings")
print ("=eof=")
