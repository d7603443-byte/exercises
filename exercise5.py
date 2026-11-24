# exercise1
list = [10,20,30,40,50]
print(list,list[0],list[-1],list[2])

# a = "exercise"
# b = 1
# for i in range(30):
#     print(a+str(b))
#     b+=1

# exercise2
list_student = ["a","b","c","d"]
print(len(list_student),list_student[0],list_student[-1])
list_student[1] = 'r'
print(list_student)

# exercise3
grades = ["1","2","3","4","5"]
grades.append["100"]
grades.insert["50"]
grades[2] = "40"
print(grades)

# exercise4
numbers = ["1","2","3","4","5"]
del numbers[0]
print(numbers)
del numbers[-1]
print(numbers)
del numbers[2]
print(numbers)

# exercise5
products = ["a","b","c"]
if "n" in products:
    print("yes")
else:
    print("not")
if "a" in products:
    print("yes")

# exercise6
numbers = ["1","2","3","4","5"]
for i in numbers:
    print (i)

# exercise7
    for i in numbers:
        if i % 2== 0:
            print(i)

# exercise8
grades = ["100","80","90"]
sum = 0
for i in grades:
    sum+= i
print(sum)

# exercise9
number = ["1","2","3"]
maxi = 0
for i in numbers:
    if i > maxi:
        maxi = i
print(maxi)

# exercise10
names = ["a","b"]
name = input("enter name")
if name in names:
    print("found")
else:
    print("not found")

# exercise11
num = [1,2,3]
number = input("enter number")
if number in num:
    print(num.index(number))

# exercise12
num = [1,2]
count = 0
for i in num:
    if i >50:
        count +=1
print(count)


# exercise13
num = [1,2,3]
new_num = []
for i in num:
    if i % 2 == 0:
        new_num.append(i)
print(new_num)

# exercise14
names = ["a","b"]
a = 0
while a <= len(names):
    print(names[a],names.index[a])

# exercise15
num = [1,2,3,4,5,6,7,8,9,10]
print(num[:3],num[3:],num[2:6],num[::-1])

# exercise16
num = [1,2,3,4,5,6,7,8,9,10]
print(num[1,10,::2],num[::2],num[::-2])

# exercise17
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_num = num[:10]
new_num2 = num[10:]
new_num3 = num[5,14]

# exercise18
list = [1,2]
new_list= list[:1]
new_list2 = list[1:]

# exercise19
numbers = [1,2,3,4,5,6,7,8,9,10]
new_num = [num * 2 for num in numbers ]
new_num2 = [num ** 2 for num in numbers]
new_num3 = [num for num in numbers if num % 2 == 0]
new_num4 = [num for num in numbers if num > 5]

# exercise20
grades = [55,90,67,100,45,82,73,30]
new_list = [grade for grade in grades if grade >= 60]
new_list2 = [grade for grade in grades if grade < 60]
new_list3 = [grade +5 for grade in grades]

# exercise21
names = ["Moshe", "David", "Noa"]
new_names = [name for name in names if len(name) >4]
new_names2 = [name.upper for name in names]
new_names3 = [name for name in names if name[0] == "D"]

# exercise22
nums = [1,2,3,4]
new_num =[num for num in nums if num % 3 == 0 and num>10]

# exercise23
nums = []
for i in range(10):
    a = input("enter number")
    nums.append(a)
print(nums)
maxi = min(num)
mini= max(nums)
print(sum(nums / len(nums)))


# exercise24
names = ["Shlomsky", "David", "Noa", "Dana", "Moshe"]
name = input("enter name")
if name in names:
    names.remove(name)
    print(names)
else:
    print("not", names)


# exercise25
num = [1,2,3,4,5,6,7,8,9,10]
even_num = [n for n in num if n % 2 == 0]
add_num = [n for n in num if n % 2 !=0 ]
big_num = [n for n in num if n >20]

# exercise26
num = [1,2,3]
num_input = input("enter number")
sum = 0
for i in num:
    if num_input in num:
        sum += 1
if sum == 0:
    print("not")
else:
    print(sum)


# exercise27
num1 = [1,2,3]
num2 = [4,5,6]
new_num = []
for i in num1:
    new_num.append(i)
for i in num2:
    new_num.append(i)
print(new_num)
print(new_num[:5])
print(new_num[5:])
print(new_num[::-1])

# exercise28
list = [1,2,3]
num = input("enter num")
for i in list:
    if num == i:
        continue
    else:
        list.append(i)
print(list)

# exercise29
grades = [85, 72, 90, 55, 100, 63, 48, 77]
while True:
    print("""===== Grades Management =====

    1. Show all grades
    2. Add a grade
    3. Search for a grade
    4. Remove a grade
    5. Show passing grades
    6. Show failing grades
    7. Show highest and lowest grade
    8. Show average grade
    9. Show first 3 grades
    10. Show grades in reverse
    0. Exit
    """)

    choise = input("choice option")
    if choise == 1:
        for i in grades:
            print(i)

    if choise == 2:
        grade = input("enter grade")
        grades.append(grade)

    if choise == 3:
        grade = input("enter grade")
        for i in grades:
            if i == grade:
                print(grades.index(i))

    if choise == 4:
        grade = input("enter grade")
        for i in grades:
            if i == grade:
                grades.remove(i)
    if choise == 5:
        print([n for n in grades if n >=60])

    if choise == 6:
        print([n for n in grades if n <60])

    if choise == 7:
        big = 0
        lowr = grades[0]
        for i in grades:
            if i > big:
                big = i
            if i< lowr:
                lowr = i

    if choise == 8:
        sum = 0
        number = 0
        for i in grades:
            sum += i
            number += 1
        print(sum/number)

    if choise ==9:
        print([g for g in grades[:3]])

    if choise == 10:
        print([g for g in grades[::-1] ])

    elif choise == 11:
        break


        





