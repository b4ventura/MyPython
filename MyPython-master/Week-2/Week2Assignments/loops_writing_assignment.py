#    Loops Writing Assignment

#    1. Assume x = -11. Use if-elif-else clause to check if
#       x is less than -20, x is -20, or x > -20.

x=-11
y=-20
if x < y:
    print (str(x) + " is less than " + str(y))
elif x==y:
    print (str(x) + " is equal to " + str(y))
else:
    print (str(x) + " is greater than " + str(y))

#    2. If brange = range(2, 16)
#       Loop through brange and find all the numbers that are divisible by 3
#           and print them.
#       Loop through brange and find only the first multiple of 3 and print it.

brange = range(2, 16)
for i in brange:
    if i % 3 == 0:
        print (i)

#       Loop through brange and find only the first multiple of 3 and print it.

brange = range(2, 16)
for i in brange:
    if i % 3 == 0:
        print (i)
        break

        
#    3. For x = 97, write a while-loop and increment x and print x.
#       Then exit the loop when x =101.

x=97
while x < 101 :
    print (x)
    x=x+1


#    4. Write a for-loop that loops through range(5) and doesn’t do anything.

for r in range(5):
    pass
