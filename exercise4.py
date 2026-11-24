import random
# exercise1
count = 0
while count != 11:
    print(count)
    count +=1

# exercise2

count = 10
while count != 0:
    print(count)
    count -= 1
print("START!")

# exercise3
count = 1
while count != 51:
    count+=1
    if count % 2 == 0:
        print(count)
    
# exercise4
number = int(input("enter number"))
for i in range(5):
    print(number)
    number *= 2


# exercise5
count = 1
sum = 0
while count != 100:
    sum += count
    count += 1
print(sum)

# exercise6

conect_password = "Python123"
while password != conect_password:
    password = input("enter password")
print("Welcome!")
    
# # exercise7
secert_number = 27
while guess!= secert_number:
    guess = input("enter your guess")

print("seccessful")

# # exercise8
list_num = []
while number != "0":
    number = input("enter number")
    list_num.append(number)
print(list_num)

# exercise9
count = 0
sum_grades = 0
grade =0
while grade != "10":
    grade = input("enter your grade")
    count += 1
    sum_grades += int(grade)
avrage_grades = float(sum_grades)/ int(count)
print (count,sum_grades, avrage_grades)

# exercise10
number = 0
sum_numbers = 0
count = 0
while int(number) >= 0:
    number = input("enter number")
    sum_numbers += int(number)
    count +=1
print(sum_numbers, count)

# exercise11

number = input("enter number")
count = 0
while count <= 10:
    print (int(number) * int(count), end=" ")
    count += 1

# exercise12
number = input("enter number")
print(len(str(number)))
count = 0
a = number
while int(count) < len(number):
    count +=1
    a = int(a)//10
print(count)

# exercise13
number = int(input("enter numbere"))
count = 0
c = -1
while int(count) < len(str(number)):
    print(str(number)[int(c)],end=" ")
    count+=1
    c-=1

number = input("enter number")
count = 0
num = number
while int(count) < len(str(number)):
    print(int(num) % 10,end= " ")
    num = int(num)//10
    count +=1
    


# # exercise14
number = input("ente nummber")
count = 2
if int(number) <= 1:
        print("not")
else:      
    while count < int(number):
        result = int(number) % count
        count +=1
        if result == 0:
            print("not")
            break
        continue
    else:
        print("yes")

    
# # exercise15
balance = 5000
choise = ""
while choise != 4:
    choise = input("enter what you want: 1.check 2.deposit 3.withdraw 4.exit")
    if choise == "1":
        print(balance)
    elif choise == "2":
        sum = input("sum")
        if sum < 0:
            break
        balance += int(sum)
    elif choise == "3":
         sum = input("sum")
         if sum < balance:
             break
         balance -= int(sum)
    else:
         break
print(balance)
          
# exercise16
count = 1
while True:
    print(count,end=" ")
    if count == 15:
        break
    else:
        count+=1

# exercise17
count = 1
while count <31:
    if count % 3 == 0:
        pass
    else:
        print(count,end=" ")
    count +=1

# # exercise18
while True:
    number = input("enter number")
    if int(number) == 100:
        print("break")
        break

# exercise19
for i in range(21):
    print(i,end=" ")

# exercise20
for i in range(101):
    if i % 5 == 0:
        print(i, end=" ")

# exercise21
sum = 0
for i in range(100):
    sum += i
print(sum)

# exercise22
number = int(input("enter number"))
for i in range(1,11):
    print (int(number) * int(i), end=" ")
    
# exercise23
number1 = input('enter number')
number2 = input('enter number')
sum = 0
for i in range(int(number1), (int(number2)+1)):
    sum += int(i)
print(sum)

# exercise24
for i in range(100):
    if int(i) % 5 == 0 and int(i) %3 == 0:
        print(i,end=" ")

# exercise25
row = input("enter rows")
columb = input("enter columbs")
for i in range(int(row)):
     print("*"*int(columb))

# exercise26
sum = 1
for i in range(1):
    for j in range(6):
        print("*"*sum)
        sum += 1
    

# exercise27
for i in range(1,11):
    for j in range(1,11):
        print(f"{j * i:4d}", end="")
    print()

# exercise28
for i in range(1,6):
    for j in range(1,6):
        print(f"{i},{j}")

# exercise29
print("""
    ===== MATH GAME =====

    1. Start Game
    2. View Instructions
    3. Exit

    Choose:
    """)
point = 0
choise = 0
while choise != "3":
    choise = input("enter choise")
    if choise == "1":
        for i in range(1,11):
            correct = 2 + int(i)
            choice = input(f"enter the result 2 +{ i}")
            if int(correct) == int(choice):
                point +=1
            else:
                point -=1
print(point)


    
