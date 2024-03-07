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
r = 0
s = 0.0
print(a or c) # great
print(a and c) # leaves a blank line
print(f == g or f == d) # True
print(f or g) # Great (returns the value)
print(f or d) # Great
print(d or f) # Great
print(c == h and e == g) # False
print(a and g) # Blank line
print(c or g) # first operand
print(g or c) # first operand
print(g and a) # first operand
print(a and g) # Blank line 
print(c or g) # great
print(g or c) #  ' GREAT'
print(g and a) #  Blank line
print(a or g) # ' GREAT'
print(g or a) # ' GREAT'
