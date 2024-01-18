# Abdul Rauf
# Mid Term Exam

#Q1 - Write a Python program to do arithmetical operations addition and division.
num1 = int(input("Enter first number:"))
num2= int(input("Enter Second number"))

add= num1+num2
div=num2/num1
print ("The sum of the numbers are :", add)
print ("The division of the numbers are:", div)
#Q2  - Write a Python program to find the area of a triangle

base = int(input("Enter the base of the triangle: "))
Perp = int(input("Enter the perp of the triangle:"))
area = 0.5*base*Perp
print("The area of the triangle is :", area)

# Q3 - Write a Python program to convert Celsius to Fahrenheit.
calcius = float(input("Enter the temperature in  celcius"))
Fahrenheit = (9/5)*calcius+32
print("The temperature of the fahrenhite is:", Fahrenheit )

#Q4  - Write a Python program that return all datatypes that we discussed in the class.

num1 = 21
float = 34.5
str = "Abdul Rauf"
bool= False

print("This variable is of type:",type(num1))
print("This  variable is of type:", type(float))
print("This  variable is of type:"), type(str)
print("This  variable is of type:", type(bool))