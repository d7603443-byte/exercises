# esercise1

age = input("please enter your age")
if int(age) >= 18:
    print("Adult")
else:
    print("Minor")

# exercies2
number = input("enter number")
if int(number) > 0:
    print("Positive")
elif int(number) < 0:
    print("Negative")
else:
    print("Zero")

# exercise3
even = input("enter a number to try if is even")
print(float(even) % 2 == 0)


# exercise4
bigger = input("enter 1 numbers")
if bigger[0] == bigger[-1]:
    print("the numbers both they same")
else:
    print(max(bigger))

# exercise5
password = input("enter password")
corect_password = "python123"
if password == corect_password:
    print("Access Granted")
else:
    print("Access Denied")

# exercise6
choise = input("enter a number")
if int(choise) > 1:
    print("lowest")
elif int(choise) > 10:
    print("low")
elif int(choise) > 50:
    print("medum")
elif int(choise) < 101:
    print("big")
else:
    print("bigest")

# exercise7
grade = input("enter your grade")
if  90 <= int(grade) <= 100:
    print ("Excellent")
elif 80 <= int(grade) <= 89:
    print("Very good")
elif 70 <= int(grade) <= 79:
    print("Good")
elif 60 <= int(grade) <= 69:
    print("Passed")
elif 0 <= int(grade) <= 59:
    print("Failed")
else:
    print("Invalid Grade")

# exercise8
corect_name = "admin"
corect_password = "123456"

name = input("enter naem")
password = input("enter password")

if name == corect_name and password == corect_password:
    print("Login Successful")
elif name != corect_name and password == corect_password:
    print("Wrong Password")
else:
    print("Unknown User")

# exercise9
price_product = input("price")
age_customer = input("enter your name")

if int(age_customer) >60:
    print(f"your price is {int(price_product) *0.8} ")

elif float(age_customer) < 18:
    print(f"your price is {float(price_product) *0.9}")

else:
    print(f"your price is {price_product}")


# exercise10
number = input("enter number")
print(float(number) % 3 == 0)
print(float(number) % 5 == 0)
print(float(number) % 3 == 0 and number % 5 == 0)
if (float(number) % 3 == 0) == False and (float(number) % 5 == 0) == False:
    print("this number not divizion by 3 or 5")


# exercise11
age = input("enter your age")
addolt = input("if you whith addolt enter 1")

if int(age) >= 18 or addolt == "1":
    print("you can eccess")

else:
    print("you can't eccess")


# exercise12
avrage = input ("enter the avrage your grades")
salary = input ("enter your slalry")

if int(avrage) > 90 or (int(avrage)> 85 and int(salary) < 5000):
    print("you entitled ")
else:
    print("yuo not entitled")

# exercise13
corect_name = "admin"
corect_password = "123456"

name = input("enter naem")
password = input("enter password")
active = input("if acount is active enter 1")


if name == corect_name and password == corect_password and active =="1":
    print("Successful")
else:
    print("Wrong")

# exercise14
number = input ("enter a number")
print(int(number) >= 20 and int(number) <=80)
print(not int(number) < 20 and not int(number) > 80)
    
# exercise15
balance = 500

sum = input("sum many you wnat to pool")
if int(sum) > 0 :
    if int(sum) >= 500:
        print("Wrong")
    else:
        print("seccessful")
else:
    print("Wrong is must to be > 0")

# exercise16
def club(sum):
    return float(sum) * 0.9

card_by_age = input("enter your age")
club_card = input("if you ahve club cerd print 1")
if float(card_by_age) > 18:
    if float(club_card) == 1:
        print(club(50))
    else:
        print(50)

elif float(card_by_age) > 12:
    if float(club_card) == 1:
        print(club(35))
    else:
        print(35)

elif  float(card_by_age) < 12:
    if float(club_card) == 1:
        print(club(25))
    else:
        print(25)

  
# exercise17
age = input("enter your age")

salary = input("enter the salary")

senoiority = input("enter your senoiority")

if int(age) >= 21 and salary >= 7000 and senoiority >= 1:
    print("seccessful")
elif int(age) < 21:
    print("you need to over 21")
elif int(salary) < 7000:
    print("your salary need to over 7000")
else:
    print("your senoiority need to over 1 year")


# exercise18
# parking_lot_rates

commercial_vehicle = 30
privete_car = 20
motorcycle = 10

hours = input("hours in parking")
type = input("if your have privete enter 1 if you have commercial enter 2 if you have motorcycle enter 3")

if type == "1":
    if int(hours) > 5:
        print(f"you need to pay {(int(privete_car) * int(hours)) *0.85}")
    elif int(hours) >1:
        print(f"you need to pay {(int(privete_car) * int(hours)) *0.90}")
    else:
        print(f"you need to pay {(int(privete_car) * int(hours))}")

elif type == "2":
    if int(hours) > 5:
        print(f"you need to pay {(int(commercial_vehicle) * int(hours)) *0.85}")
    elif int(hours) >1:
        print(f"you need to pay {(int(commercial_vehicle) * int(hours)) *0.90}")
    else:
        print(f"you need to pay {(int(commercial_vehicle) * int(hours))}")
elif type == "3":
    if int(hours) > 5:
        print(f"you need to pay {(int(motorcycle) * int(hours)) *0.85}")
    elif int(hours) >1:
        print(f"you need to pay {(int(motorcycle) * int(hours)) *0.90}")
    else:
        print(f"you need to pay {(int(motorcycle) * int(hours))}")


# exercise19
number1 = input("enter a number")
number2 = input("enter n number")
options = input("enter a option(+/-/*//)")

if options == "+":
    print(number1 + number2)
elif options == "-":
    print(number1 - number2)
elif options == "*":
    print(number1*number2)
elif options == "/":
    try:
        print(number1/number2)
    except ZeroDivisionError as r:
        print(r)
else:
    print("try again")

# exercise20
year = input("enter a year")
if float(year)% 400 == 0:
    print("yes")
elif float(year) % 4  == 0 and not year % 100 == 0:
    if float(year) % 400 != 0:
        print("not")
    else:
        print("yes")
else:
    print("not")

# exercise21
base= 50
add = 1.25
add_plus = 1.5

hours = input("enter your hours")

if int(hours) < 183:
    print(float(hours)*int(base))

elif 183 <= int(hours) <= 185:
    print((183 * float(base)) +((float(hours)-183) * float(add)))

else:
    print(((183 * float(base)) + (2 * float(add))) + ((float(hours)-185) * float(add_plus)))

# exercise22
age = input("enter your age")
sum = input("enter the sum")
club_card = input("if you have club print 1")
open = input("if the product is open enter 1")
bill = input("if you have bill enter 1")

if bill == "1":
    if open != "1":
        if int(sum) > 0:
            if club_card == "1":
                print("the client is entitled")
            else:
                time = input("enter the days that over")
                if int(time) <= 30:
                    print("the client is entitled")
                else:
                    print("the client not entitled")
        else:
            print("the client not entitled")
    else:
        print("the client not entitled")
print("the client not entitled")

                    










