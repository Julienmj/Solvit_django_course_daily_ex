# Name: Mugisha Julien

# Exercise 1: Basic Arithmetic
a = 20
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# Exercise 2: Calculate Student Marks
math = 80
english = 75
science = 90
total = math + english + science
average = total / 3
print("Total marks:", total)
print("Average marks:", average)


# Exercise 3: Rectangle
length = 12
width = 8
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)


# Exercise 4: Even or Odd
number = 27
if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


# Exercise 5: Update Variables
score = 50
score += 20
print("After adding 20:", score)
score -= 10
print("After subtracting 10:", score)
score *= 2
print("After multiplying by 2:", score)
score /= 4
print("After dividing by 4:", score)


# Exercise 6: Comparison Operators
a = 15
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# Exercise 7: Logical Operators
age = 22
has_id = True
print("and:", age >= 18 and has_id)
print("or:", age >= 18 or has_id)
print("not:", not has_id)


# Exercise 8: User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)


# Exercise 9: Mini Calculator
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print("Addition =", n1 + n2)
print("Subtraction =", n1 - n2)
print("Multiplication =", n1 * n2)
print("Division =", n1 / n2)
print("Remainder =", n1 % n2)
print("Power =", n1 ** n2)


# Exercise 10: Student Result
math_marks = float(input("Enter Math: "))
english_marks = float(input("Enter English: "))
science_marks = float(input("Enter Science: "))

total_marks = math_marks + english_marks + science_marks
average_marks = total_marks / 3
passed = average_marks >= 50

print("Total:", total_marks)
print("Average:", average_marks)
print("Passed:", passed)
