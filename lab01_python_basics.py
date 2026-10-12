"""
Lab 01: Python Basics
File: lab01_python_basics.py

Codes in this file (in order):
  1. input_conversion  - input() with int()/float()
  2. operators         - / // % **
  3. string_methods    - upper, lower, title, strip, replace, len
  4. string_slicing    - s[i:j:k]
  5. if_elif_else      - conditionals, nested if, ternary, and/or/not
  6. loops             - for, range, while, break, continue, pass
  7. functions         - greet(), add(), is_even(), factorial(), fib()
  8. modules           - math, random
"""

# input() always returns str: convert it
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))

# operators
print(10 / 3)    # 3.333...
print(10 // 3)   # 3
print(10 % 3)    # 1
print(2 ** 3)    # 8

# strings
s = "  hello world  "
print(s.upper(), s.lower(), s.title())
print(s.strip())
print(s.replace("hello", "hi"))
print(len(s))
print("ab" + "cd", "ab" * 3)

# slicing: s[start:end:step], end excluded
t = "abcdefgh"
print(t[2:5])    # cde
print(t[:3])     # abc
print(t[-1])     # h
print(t[::2])    # aceg
print(t[::-1])   # reversed

# if / elif / else
marks = 72
if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")

# ternary
a, b = 5, 3
print("A") if a > b else print("B")

# for / range / while
for i in range(5):          # 0..4
    print(i)
for i in range(1, 10, 2):   # 1,3,5,7,9
    print(i)

n = 0
while n < 3:
    print(n)
    n += 1                  # must update the variable

# break / continue / pass
for i in range(1, 6):
    if i == 3:
        continue            # skip 3
    if i == 5:
        break               # stop before printing 5
    print(i)                # prints 1 2 4

def todo():
    pass                    # empty block

# functions
def add(x, y=0):
    return x + y

# even/odd, factorial, fibonacci
def is_even(n):
    return n % 2 == 0

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fib(n):
    a, b = 0, 1
    out = []
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out


# ============================================================
# EXTRA CODE FROM THE MANUAL
# ============================================================
# variables and types
name = "Ali"; age = 20; gpa = 3.75; is_student = True
print(type(gpa))                         # <class 'float'>

# input conversion
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

# modules
import math
import random
print(math.pi, math.sqrt(16))            # 3.14159..., 4.0
print(random.randint(1, 10))

# string slicing on "Sammy Shark!"
ss = "Sammy Shark!"
print(ss[0], ss[-1], ss[0:5], ss[6:11], ss[:5], ss[6:], ss[0:10:2])
# S ! Sammy Shark Sammy Shark! SmySa

# functions
def greet(name):
    print("Hello, " + name.title() + "!")

def add(a, b):
    return a + b

# loops over a list and a string
for fruit in ["apple", "banana", "cherry"]:
    print("I like " + fruit)
for letter in "Python":
    print(letter)
for i in range(1, 6):
    print(i, "x 3 =", i * 3)

# while
i = 1
while i <= 5:
    print("Number:", i)
    i = i + 1

# break / continue
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana":
        break
    print(fruit)                          # only apple

# if / elif / else and nested if
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

x = 15
if x > 10:
    print("Above 10")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("10 or less")

# logical operators
a, b, c = 200, 33, 500
if a > b and c > a:
    print("Both conditions are True")
if a > b or c < a:
    print("At least one condition is True")
if not (a > c):
    print("a is NOT greater than c")
