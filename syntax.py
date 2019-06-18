###########################################
#
#  Basic Syntax
#
###########################################

#define a number
num = 3
print(num)

#define a string
str1 = "abc"
print(str1)

#define a boolean
bool = True
print(bool)
print(3==3)
print(3=="3")
print(3==int("3"))
print("3" == str(3))

#define an array (list in python)
mylist = [100, "abc", 20.5]
print(mylist)

#define a dictionary/objects
mydictionary = {'key1': 'value1', 'key2':'value2'}
print(mydictionary)

#undefined (is None in python)
x = None
print(x)
print(x == "") #should be False

#if else
x = 4
if (x == None):
    print("x is None")
elif (x == 3):
    print("x is 3")
else:
    print("x is neither None nor 3")

#functions with parameters and returns
def myfunc(name):
    print(f"Hello {name}")
    print("Hello {}".format(name))
    print("Hello " + name)

myfunc("Roman")

#array - add to front, add to end, update values
arr1 = [1, 2, 3]
arr2 = [6,  7, 8]
arr1.append(5)
print(arr1)
arr1.extend(arr2)
print(arr1)
arr3 = arr1 + arr2
print(arr3)
arr1.insert(0,"a")
print(arr1)
arr1.insert(0, arr2)
print(arr1)
arr1[0] = 'b'
print(arr1)
arr1[0:2] = ['a','b']
print(arr1)

#loop - for
for x in range(0, 3):
    print("x is", x)

mylist = ['a', 'b', 'c']
for letter in mylist:
    print(letter)

myrange = range(0, 3)
for rangenum in myrange:
    print(rangenum) 

#loop - for in
mylist2 = ['a', 'b', 'c']
index = 0
for letter in mylist2:
    print(letter, 'is at index ', index, 'and next will be ', index+1)
    print('{} is at index {}'.format(letter, index))
    index += 1

#loop while
i = 1
while i < 6:
    print(i)
    i+=1
    
#loop do while
print('Python does not have do while')

#loop forEach
print('Python does not have forEach')

#object - declare object
#lookup key to retrieve value
class Mateo():
    def __init__(self, first, middle, last, secret=42):
        self.first = first
        self._middle = middle
        self.last = last
        self.__secret = secret
        self.___supersecret = secret
        self.__ = secret
        self._ = secret
    def print_name(self):
        print(self.first, ' ', self.last)
        print('inside the class', self.__secret)
        return(self.first)

my_son = Mateo("Matthew", "Tristan", "Henders")
print(my_son)
print(my_son.print_name())
print(my_son._middle)
#print(my_son.__secret)
#my_son.__secret = 43
#can only access inside 
#this gives an error:
#print(my_son.__secret)
#but actually we can still access it
print(my_son._Mateo__secret)
my_son._Mateo__secret = "you cannot trust private variables will stay private"
print(my_son._Mateo__secret)
#print(my_son.___supersecret)
print(my_son._Mateo___supersecret)
#print(my_son._Mateo_middle)
print(my_son._middle)
print('_ is ', my_son._)
print('__ is ', my_son.__)

#set up a few examples with python test framework
# see math.py and test.py for examples

#make a function called email
#received 2 parameters: first name and last name
#e.g. Larry Shumlich => larry.shumlich@evolveu.ca
#e.g. Heiko Peters => heiko.peters@evolveu.ca

#write an automated test that will check the results are what you expect
#email the test to Larry before you write the code

#############################################
#
# tax function
# use hardcoded input
# create tests first
# copy and reuse as much code as possible
#
##############################################

