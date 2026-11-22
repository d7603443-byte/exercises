# # exercise 1

# num1 = 25
# num2 = 7

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)
# print(num1 ** num2)

# # exercise 2

# balance = 100

# add_balance = balance+250

# print(add_balance)

# balance_min = balance -100

# print(balance_min)

# duble_balance = balance * 2

# print(duble_balance)

# div_balance = balance / 4

# print(div_balance)

# balance += 250
# balance -= 100
# balance *= 2
# balance /= 4

# print(balance)

# # exercise 3
# product = input("enter product")
# price = input("enter price")
# discount = input("enter precent discount")
# print(f"dicount price: {int(price)*int(discount)}")
# print(f"the total is {int(price)-int(price)*int(discount)}")

# # exercise 4
# sum_loan = input("enter the sum_loan")
# interest = input("enter the interest")

# interest_year = int(sum_loan) * int(interest)

# total_sum_year = int(interest_year) + int(sum_loan)

# # exercise 5
# grade1 = input("enter your grade")
# grade2 = input("enter your grade")
# grade3 = input("enter your grade")

# print(f"your avarge is {(float(grade1)+float(grade2)+float(grade3))/ 3}")

# # ecercise 6
# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# print(f"Hello, my name is {first_name}{last_name} and I leve in {city}")
# print("Hello, my name is",(first_name),(last_name),"and I live in",(city),".")

# # exercise 7

# foul_name = input("enter your foul name")
# print(foul_name)
# print(len(foul_name))
# print(foul_name.upper())
# print(foul_name.lower())

# # exercise 8
# sentence = input("enter a sentence")

# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.title())


# # exercise 9
# new_sentence = input("enter a sentence")
# print(new_sentence)
# clean_sentence = new_sentence.strip()
# print(clean_sentence)
# print(len(new_sentence))
# print(len(clean_sentence))
      
# exercise 10
sentence = "I love Java programming"
print(sentence.replace("Java","Python"))
print(sentence.count("love"))
print(sentence.startswith("I"))
print(sentence.endswith("programming"))

# exercise 11
word = "Programming"

print(word[0])
print(word[-1])
print(word[2])
print(word[:3])
print(word[7:])
print(word[::-1])

# exercise 12
a = "100"
b = "25"
c = 10
d = 5.5

a = int(a)
b = float(b)
c = str(c)
d = int(d)

print(type(a), type(b), type(c), type(d))

# exercise 13
age = input("Enter your age:  ")
print("your new age is", (int(age)+10),".")

# becose that str and int not connect

# exercise 14
product = input("enter the product")
p = float(product)
total = (p + (p * 0.18))
print(total)

# exercise 15

name_user = input("please enter your name")
family_user = input("please enter your family")
age_user = input("enter your age")
month_salary = input("enter your month salary")
years_work = input("enter your years working")

print(f"name:{name_user},{family_user}, age{age}, salary month: {month_salary}, years work: ,{years_work},")
print(f"total salary for year: {int(month_salary) * 12}, after:{(float(month_salary) * 12) * 1.05}," )
print(len(name_user))

# exercise 16

sum = input ("enter sum many")

usd_rata = 3.25

print(f"sum in dolrs: {float(sum) * usd_rata}")
print(f"the sum in eiro: {float(sum) * 3.75}")
print(f"the total is: {float(sum) + (float(sum) * 0.02)} ")

# exercise 17

your_name = input("enter your name").lower()
your_family =input("enter your family").lower()
your_year_birthday= input("enter your year birthday").lower()

print(f"your amail is: '{your_name}.{your_family}.{your_year_birthday}@gmail.com'")

# exercise 18

your_sentece = input("enter your sentence")

print(your_sentece)
print(len(your_sentece))
print(your_sentece.upper())
print(your_sentece.lower())
print(your_sentece[::-1])
a = 0
for i in your_sentece:
    if i == a:
        a +1
print(a)
print(your_sentece.replace(" ", "-"))

# exercise 19

client_name = input("enter your name")
product_name = input("enter product name")
price_product = input("enter product price")
quantity = input("enter the quantity")
price_all = input("enter the all price")
precent_discount = input("enter the precent discount")
vat = input("enter the precent nat")


print(f"""

================================
          PURCHASE INVOICE
================================

Customer: {client_name}
Product: {product_name}

Unit Price: {price_product}
Quantity: {quantity}

Subtotal: {price_all}
Discount: {precent_discount}
After Discount: {float(price_all) - float(precent_discount)}

VAT: {vat}%
VAT Amount: {(float(price_all) - float(precent_discount)) + ((float(price_all) - float(precent_discount)) * (float(vat) / 100))}

TOTAL: {((float(price_all) - float(precent_discount)) + ((float(price_all) - float(precent_discount)) * (float(vat) / 100))) + (float(price_all) - float(precent_discount)) }


================================
       THANK YOU FOR SHOPPING
================================

""")