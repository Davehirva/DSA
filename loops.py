#1.Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)
#2.
    i = 10

while i >= 1:
    print(i)
    i -= 1
#3.
    num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#4.
    n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

#5.
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)

#6.
for i in range(2, 101, 2):
    print(i)

#7.
    num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)

#8.
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)

#9.
num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")
#10.
        n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
