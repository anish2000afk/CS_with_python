import random
import statistics

num1 = random.randrange(0, 5, 2)
num2 = random.randrange(0, 5, 2)
num3 = random.randrange(0, 5, 2)
num4 = random.randrange(0, 5, 2)
num5 = random.randrange(0, 5, 2)
num6 = random.randrange(0, 5, 2)

print("Random number b/w 0 and 5 :", num1)
print("Random number b/w 0 and 5 :", num2)
print("Random number b/w 0 and 5 :", num3)
print("Random number b/w 0 and 5 :", num4)
print("Random number b/w 0 and 5 :", num5)
x = [num1, num2, num3, num4, num5, num6]
print("The mean of the given numbers is:", statistics.mean(x))
print("The median of the given numbers is:", statistics.median(x))
print("The mode of the given numbers is:", statistics.mode(x))
