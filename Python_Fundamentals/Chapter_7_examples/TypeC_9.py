d, m = input("Enter the days and months (in integers): ").split()
# Converting the strings to integers
d = int(d)
m = int(m)
# i = iterator
# sum = total number of days
i = 0
sum = 0
for i in range(1, m):
    sum = sum + 30  # increment each month by 30
    i = i + 1
sum = sum + d
print("The month is:", m)
print("The day is:", d)
print("The total number of days in the year is ", sum)
