import abc
print("Hello World!")
input("'data science'")
# 3 The input data science was missing inverted commas there for resulting in a syntax error. 
a = 5
if a == 5:
    # 4 indented spaces to this block of code
    print("'a equals 5'")
    myString = "Hello World!"
    print(type("Hello World!"))
    # 9 needed to have a capital H in hello and capital W in world as well as a exclamation point and needed to be inside double qoutation instead of single .
n = 10
print(type(n))
n_float = 7.5
print(type(n_float))
single_string = ('It\'s a single qoute string')
print(single_string)
# 16 added an apostrophe on the Its by pressin /' to make it It's and we also added parentheses before and after the single qoutes.
double_string = ("It\'s a double qoute string")
print(double_string)
# 19 added parenthese before and after the double qoutes. 
n1 = 5
n2 = 7.5
print(n1+n2)
nstr1 = "abc"
print(f'{nstr1}{n1}')
# 26 had to insert f string and close nstr1 and n1 with curly brackets to merge the string and int. 
nstr2 = "def"
print(f'{nstr2}{n2}')
nstr2 = "def"
print (nstr1 + nstr2)
n1, n2 = 10, 11
print(n1)
print(n2)
result = 3 + 4.0 / 2 * 5  # DMAS
print(result)
# module operator %
remainder = 17%10
print(remainder)
# x ^ n
x = 5
n = 4
print(x ** n)
nstr = "abc"
ans = nstr * 10
print(len(ans))
name = "Harshit"
print("%s is a data scientist!" %name)
print(name.upper())
print(name.lower())
nstr = "it is a nice day today."
print(nstr.capitalize())
name.index('s')
print(name.index('s'))
name[2:5]
print(name[2:5])
alist = [3,4,5]
print(alist)
alist = ['harshit', 2, 5.5]
print(alist)
alist.append(10)
alist.append(15)
print(alist)
alist.pop()
print(alist)
alist[3]
print(alist[3])
alist[1:]
print(alist[1:])
alist.append([1,2,3])
print(alist)
alist*2
print(alist*2)
alist + alist
print(alist + alist)