alist = ['Tom', 54, 'Julia', 78]
print(alist)
print(alist.append(help))
print(alist)
blists = [
    ['Tom', 54],
    ['Julia', 78]
]
print(blists)
blists[-1]
print(blists[-1])
blists[-2][0]
print(blists[-2][0])
blists.append(['Mak', 90])
print(blists)
a = [0]*5
print(a)
cols = 5
rows = 4
a = [[0]*cols]*rows
dlist = [[1]*cols]*rows
print(dlist)
tup1 = ('Tom', 78)
# tup1[1] = 90
l = list(tup1)
l[1] = 90
t_change = tuple(l)
print(t_change)
# 24 since a tupel is immutable we needed to convert into a list, in order to do so a variable had to be created wich in this case was l wich represented the list.  Then i created another variable with an index wich was l[1] wich represented the updated age for Tom wich was 90. Then we used the variable t_change to store the updated tuple to the list.Then the final step was to print out t_change.
tup2 = ('Julia', 89)
print(tup1 + tup2)
tup1
print(tup1)
tup3 = tup1 + tup2
print(tup3)
len(tup3)
print(len(tup3))
# dictionary
country_code = {'India': 1, 'USA': 2, 'China': 3}
print(country_code)
print(country_code['China'])
country_code['UAE'] = 4
print(country_code)
if 'Inda' in country_code:
    print(True)
else:
    print(False)
a = 1
b = 2
print(a == b)
print(a > b)
print(a < b)
print(a != b)
color = 'red'
if color == 'red':
    print("Color is red!")
    
print("Color problem is solved!!")
color = 'kjh'
if color == 'red':
    print("Color is red!")
    
else:
    print("color is not red!")
    
print("Color problem is solved!!")
color = 'green'
if color == 'red':
    print("Color is red!")
    
elif color == 'green':
    print("Color is green!")
    
else:
    print("color is not red!")
    
print("Color problem is solved!!")
age = 15
if age >= 18:
    print("Adult")
    
else:
    print("Juvenile")
a = 0
not(a)
print(not(a))
a = 3
not(a)
print(not(a))
a = True
not(a)
print(not(a))
score = 74
percentile = 83

if score > 75 or percentile > 90:
    print("Admission successful!")
else:
    print("Try again next year")
for i in range(5):
    print(i)
range(5)
print(range(5))
for i in range(1, 10, 2):
    product = 8 * i
    print(product)
    names = ('harshit', 'shubham', 'sahil')
for name in names:
    print(name.upper())
    age = [12,43,45,10]
i = 0
while i < len(age):
    if age[i] >= 18:
        print("Adult")
    else:
        print("Juvenile")
    i += 1
    # list comprehension

cubes = [n** 3 for n in range(1,10)]
print(cubes)
cubes = []
for i in range(1,10):
    cubes.append(i ** 3)
print(cubes)
abs(2-5)
print(abs(2-5))
def add_two_numbers(a, b):
    sum = a + b
    return sum
print(add_two_numbers(5,11))
def fahr_to_celsius(temp):
    """
    This function converts temperature from fahrenheit
      to celsius.
      Args:
      -----
        tempInFahr: temperature in fahrenheit

      Returns:
      --------
        tempInCel: temperature in celsius
    """
    tempInCel = (temp - 32) * 5/9
    return tempInCel
fahr_to_celsius(50)
print(fahr_to_celsius(50))