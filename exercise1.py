# exercise 1

first_name = "David"
last_name = "Sapira"
age = 29
city =  "Bney Brak"
email = "D7603443@gmail.com"

print("====User Details====")
print(f"First Name: {first_name}\nLast Name: {last_name}\nAge: {age}\nCity: {city}\nEmail: {email}")

# exercise 2

birth_year = 1997

current_year = 2026

my_age = current_year - birth_year

print(f"YOU are approximately {my_age} years old.")

# exercise 3

width = 10
height = 20

area = width * height
permiter = (width + height) * 2

print(f"the area is: {area} and the peramiter is:{permiter}.")

# excersice 4

name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500


print(name,type(name))
print(age,type(age))
print(height,type(height))
print(is_student,type(is_student))
print(salary,type(salary))

# exercise 5

# your_name = input("your name  ")
# your_family = input("your family  ")
# your_city = input("your city  ")
# your_age = input("your age  ")

# print("Welcome:", your_name, your_family, "from", your_city, "you are", your_age,"age old")

# exercise 6

calculate = input("plise enter 2 numbers ")
print(f"result addition: {int(calculate[0]) + int(calculate[-1])}")
print(f"result subtraction: {int(calculate[0]) - int(calculate[-1])}")
print(f"result division: {float(calculate[0]) / float(calculate[-1])}")
print(f"result multiplication: {float(calculate) * float(calculate[-1])}")

# exercise 7

product = input("enter name product")
price = input("enter price")
quantity = input("enter quantity")

print("====== Purchase Receipt ======")
print("Product:",(product),".")
print("price:",(price),".")
print("quantity:", (quantity),".")
print("total:",{int(price) * int(quantity)})
print("==============================")

# exercise 9

name_worker = input("enter your name")
working_horus = input("enter your hours")
rate = input("enter your rate")

total_salary = working_horus * rate

print(f"the {name_worker} total salary is: {total_salary}")

# exercise 10

sum_acount = input('enter your acount')
tip_precent = input("enter precent tip you wnat to give")
diners= input("the num of diners")

print(f"sum tip: {float(sum_acount) * float(tip_precent)}")
print(f"the total sum: {(float(tip_precent) * float(sum_acount)) + float(sum_acount)}")
print(f"the total per person is: {((float(tip_precent) * float(sum_acount)) + float(sum_acount)) / float(diners)}")

# exercise 12

a = 10
b = 20

b = a
a = b

print(a,b)

# exercise 13

name_student = input("enter name  ")
family = input("enter family  ")
age = input("enter age  ")
scuol = input("enter the scoul")
course = input("enter the course")
monthes = input("enter your mounth is lernn")
price = input("enter the price")

print("================================")
print("   STUDENT REGISTRATION         ")
print("================================")

print("Student:",{name_student},{family})
print("Age:", {age}) 
print("Institution:", {scuol})
print("Course:", {course})
print("Duration:", {monthes})
print("Monthly Price:", {price})

print("Total Course Price:", {monthes}*{price})

print("Registration completed!")











