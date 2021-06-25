# Question 2
n = int(input("Enter number"))
sum = 0

for num in range(1, n + 1, 1):
   sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)

#Question 1

a = int(input("Enter the 1st Value = "))
b = int(input("Enter the 2nd Value = "))
c = int(input("Enter the 3rd Value = "))
if (a > b) and  (a > c):
  largest= a
elif (b > a) and (b > c):
  largest=b
else:
  largest=c
#print the largest value
print("The largest value is",largest)

