
# Lecture 1: Introduction to Programming

## Agenda for the Class:
1. Python in-built datatypes
2. Basic mathematical operators and Precedence order
3. Python Interpreter vs Python for Scripting

Firstly we'll focus on the **datatypes**.
1. **Numeric**
2. **Strings**
3. **Lists**

General format for **Assigning** a variable a value:
Variable_name = Variable_Value

1. We **Do not** mention datatype while assigning a variable a value in Python. (i.e. Dynamically Typed)
2. **=** is used to assign a variable a value. ( L Value and R value)
3. A variable name must follow certain naming conventions. Example: '23', 'len' can be variable names.
4. There is no such thing as "variable declaration" or "variable initialization" in Python. It's only variable assignment

## Numeric data


```python
a=1
b=3.14
# Assigning value 1 to variable a and 3.14 to variable b
```

Mathematical Operations on Variables:
1. Add ('+')
2. Multiple ('*')
3. Subtract ('-')
4. Divide ('/')
5. Modulo ('%')
6. Exponentiation (\*\*)

### **Order of Precedence**

Exponent > (Multiple, Divide, Modulo) > (Add, Subtract)


```python
a = 20
b = 10
c = 15
d = 5
e = 0
```


```python
e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ",  e)
```

    Value of (a + b) * c / d is  90.0



```python
e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)
```

    Value of ((a + b) * c) / d is  90.0



```python
e = (a + b) * (c / d);    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ",  e)
```

    Value of (a + b) * (c / d) is  90.0



```python
e = a + (b * c) / d;      #  20 + (150/5)
print ("Value of a + (b * c) / d is ",  e)
```

    Value of a + (b * c) / d is  50.0


## Strings
1. **Immutable** datatype
2. String enclosed within **" String"** or **'String'**


```python
course_name = "Introduction to Programming"
question = "Having a good time ? ;)"
print(course_name)
print(question)
```

    Introduction to Programming
    Having a good time ? ;)


### Operations on Strings
1. Since strings are immutable, we can't change the value stored in a string
2. We can concatenate ('join') multiple strings.
3. Slice/substring operations


```python
string_1 = "Hello World!"
n = len(string_1)  # "len" gives us the number of characters in the string
print(string_1 + " has", n , "characters")
```

    Hello World! has 12 characters


1. **Indexing** : Every charcater of the string can be accessed by it's position in the string.
2. Indexing starts from zero.
3. Syntax
    string_name[index_number]
    
Example:    


```python
print(string_1[0])
print(string_1[1])
```

    H
    e



```python
print(string_1[-2])
```

    d


Negative Indexing:
string[-1] gives us the last character
string[-2] gives us the second last character
and so on...


#### Slicing operations
Syntax:

string_name[start_index,end_index]


```python
print(string_1[0:2])
print(string_1[5 : len(string_1)])
```

    He
     World!



```python
print(string_1[0:4]+string_1[4:len(string_1)])
```

    Hello World!


## Lists
1. Initializing syntax: \n
    list_name = [value_1,value_2,...,value_n]
2. Behaviour Similar to strings
3. Mutable
4. Can contain multiple data types.


```python
primes = [2,3,5,8,11]
print(primes)
print(primes[0])
print(len(primes))

```

    [2, 3, 5, 8, 11]
    2
    5



```python
classroom = ['L','T', 1]
print(classroom)
print((classroom[2]+ 4))
```

    ['L', 'T', 1]
    5


## What to do next?
1. Play around in the python interpreter to explore various functionalities
2. Understand the rules to name variables.


## Download the Jupyter Notebook from [here](https://github.com/bpgc-cte/python2017/blob/master/notebooks/Lecture_1%20-%20Intro%20to%20Programming.ipynb)