# Python Object Oriented Programming
## 4 Pillars of OOP
### methods/functions
#### Modules
##### Lib - Packages

#### use case - benefits - examples of builtin modules - packages
```python
# lucky draw
# key word called import
#import random
from random import *      # *- everything
import math

# print(random)

#print(random.random())
# print(random())

# each time it's run it generates a random number 0-1


# calculate DOB







from random import *
import math


number = 23.66

# any numbers - to round the figure up -
# number 1.50 above to round up to 2
# number 1.49 or less round down to 1
print(math.ceil(number))  # ceil will help round up
print(math.floor(number))  # floor will help round down
```
```python

DRY - Don't repeat yourself
reusable - saves time - saves money
building functions
syntax def name():
def greeting():
    # greet user
    print("Hello Dear ")

    pass
    keyword called pass
the function needs to be called
greeting()

greet user with their name
def greet_user(name):    # create a function that takes and argument(name)
    print("Hello Dear " + name)    # adding 2 string with user input()
    #pass
greet_user("Adam")

create a function that takes int as an argument
def add(value1, value2):    # take user input as int then add them together display the outcome
    #print(value1 + value2)
# return_statement
    return value1 + value2
# if you are using a return statement and caling the function - it needs to be in a print statement
print(add(2, 2))



add(2, 2)

def multiply (value1 , value2):
    print(value1 * value2)
    pass

multiply(2,2)

def divide (value1, value2):
    print(value1 / value2)
    pass

divide(2,2)

def modulus (value1, value2):
    print( value1 / value2)
    pass
modulus(2,2)
#
def divide(value1, value2):
    return value1 / value2
print(divide(2,2))
 
 def multiply(value1, value2):
     return value1 * value2
 print(multiply(2,2))
 def modulo(value1, value2):
     return value1 % value2
 print(modulo(2,2))


```

####OOP code along diagram

- step 1: create animal.py as a parent
  
- step 2: create reptile.py as a child to inherit - abstract etc.
- step 3: snake.py and inherit  from reptile
- step 4: python_oop.py

![](https://i.imgur.com/axXRy82.png)