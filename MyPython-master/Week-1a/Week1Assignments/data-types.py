#   1. Pick a number from 10 to 25 and assign it to variable a.
#   Then convert a to float and assign it b.
#   Convert a to string and assign it to c.
#   Print a, b, c along with their types.
#   print ("  ")

print ("1. Pick a number from 10 to 25 and assign it to variable a.")
print ("Then convert a to float and assign it b. ")
print ("Convert a to string and assign it to c. ")
print ("Print a, b, c along with their types. ")

a = 13
b = float(a)
c = str(a)
print ("a =", a, "is a ",type(a))
print ("b =", b, "is a ",type(b))
print ("c =", c, "is a ",type(c))
print (" =========== ")



#    2. f b = “9253”, how would you convert b into int? How would you convert b into float? Print the output of each conversion.
print (" 2. f b = “9253”, how would you convert b into int? How would you convert b into float? Print the output of each conversion. ")

b = "9253"
print ("b =", b, "is a ",type(b))
b = int(b)   # converting b to int
print ("b =", b, "is a ",type(b))
b = float(b)   # converting b to float
print ("b =", b, "is a ",type(b))
print (" =========== ")


#    3. What is
#	   bool(0+ 10)?
#	   bool(“” + “a”)?
#	   bool(0.0 + 0.0)?
print (" 3. What is bool(0+ 10)? ")
print (" bool(0 + 10) "), bool(0+ 10), print (" is False ")
print (" What is bool(“” + “a”)? ")
print (" bool(“” + “a”) "), print (" n Error because string null is not valid ")
print (" 3. What is bool(0+ 10)? ")
print (" bool(0.0 + 0.0) "), bool(0.0 + 0.0), print (" is True ")
print (" =========== ")


#    4. Assign a = 7 and b = a and print the ids of a and b. 
#    Then assign b = b + 11 and print ids of a and b. 
#    What can you infer from the ids before and after b was modified?
print (" 4. Assign a = 7 and b = a and print the ids of a and b. ")
print (" Then assign b = b + 11 and print ids of a and b. ")
print (" What can you infer from the ids before and after b was modified? ")
a = 7
b = a
print("id(a) =", id(a))
print("id(b) =", id(b))

print (" b = b + 11 ")
b = b + 11
print (b)
print("id(a) =", id(a))
print("id(b) =", id(b))
print (" =========== ")


#    5. If possible convert w = “87t” to float. If not explain.
print (" 5. If possible convert w = “87t” to float. If not explain. ")
print ("w = 87t")
print ("w = float(w")
#    ValueError: could not convert string to float: '87t
print (" ValueError: could not convert string to float: '87t ")
print (" =========== ")
