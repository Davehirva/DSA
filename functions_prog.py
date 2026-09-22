# 1. Write a function to print "Hello, World!".
def hello():
    print("Hello, World!")

hello()

# 2.
def greet(name):
    print("Hello,", name)

greet("priyaa!!!.....")

# 3.

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

#4.Write a function to find the square of a number.

def square(num):
    return num * num

n = int(input("Enter a number: "))
print("Square =", square(n))

#5.Write a function to check whether a number is even or odd.

def check_number(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

n = int(input("Enter a number: "))
check_number(n)

#6.Write a function to find the maximum of two numbers.

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("Maximum =", maximum(x, y))

# 7.Write a function to convert Celsius to Fahrenheit.








#8.Write a function to calculate the area of a circle.

def area(radius):
 return 3.14 * radius * radius
r = float(input("Enter radius: "))
print("Area of circle =", area(r))

#9.Write a function to calculate the factorial of a number.
def factorial(n):
    result=1
    for i in range(1,n+1):
     num= int(input("Enter Factorial number"))
    print=("factorial =",factorial(num))
    
#10.Write a function to check whether a number is positive, negative, or zero.
    
def number(num):
      if num > 0:
         print("number is positive ")
      elif num < 0:
        print("number is negative")
      else :
        print("number is zero")
        
n= int(input("Enter an number"))

number(n)

# 11. Find the maximum of three numbers
def maximum(a, b, c):
    return max(a, b, c)

print(maximum(10, 25, 15))

#12.Write a function to count vowels in a string.
def count_vowels(text):





#13Write a function to reverse a string.
def reverse_string(text):
    return text[::-1]

print(reverse_string("this is my reverse string program"))

#14 Write a function to check whether a string is a palindrome.
def palindrome(text):
    return text == text[::-1]

print(palindrome("hello world"))

#15 Write a function to find the sum of all elements in a list.
def list_sum(numbers):
    return sum(numbers)

print(list_sum([20, 290, 380, 60]))

#16.




 






