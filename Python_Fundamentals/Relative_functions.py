a = ''
b = ' '
c = 'great'
d = 'Great'
e = 'GREAT'
f = 'Great'
g = ' GREAT'
h = ' great'
x = 29.0
y = 13
z = 2
p = 0.5
q = 12.79
i = 13
j = 29.0
k = y - 11
l = (3 + 4.5j)
m = (3 + 4.5j )
print(x > y and y > z) # True
print(x > y or y > z) # True
print(not x > y) # False
print(not x > y or y > z) # True
print(not(x > y or y > z)) # False
print(x - y * 2 > y * 2 or y * p > y)
# print(((x - (y * 2)) > (y * 2))  or ((y * p) > y))
print(not x - y * 2 > y * 2 and y * p > y)
# print(((not x - (y * 2)) > (y * 2)) and ((y * p) > y))
print(not( x - y * 2 > y * 2 and y * p > y)) # True
print(x - y * 2 > y * 2 and not y * p > y ) # False
print(i < j > k)
print(y | z)
# print(bin(y), bin(z))
# print(int('0b1111', 2))
print(y ^ z)
# print(int(bin(y^z), 2))
print(~y)
# print(int('0b0010', 2))

