'''
homework 3
Create a script for calculating the area of a cycle and print it:
○ Input value: radius
○ Output: print the value of the area of the cycle
'''

radius = input("Please input the radius")
while not radius.replace('.', '', 1).isdigit():
    print("Provided value is not a valid number")
    radius = input("Please input the radius")
else:
    area = 3.14 * float(radius) ** 2
    print(f"The area of given cycle is {area}")
