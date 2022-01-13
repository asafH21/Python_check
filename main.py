import random
from math import *
from Student import Student
from Phone import Phone

name = "Asaf"
age = 29

print("my name is " + name + "")
print(name + " is " + str(age) + " years old")
print(name + " don't like to be " + str(age) + " years old")
print(name + " is the king of the world")

print("----------------------------------")

print("asaf\nhermann")
print("----------------------------------")
print("asaf\"hermann")
print("----------------------------------")

a = "Asaf hermann is the king"
print(a)
print(a.replace("Asaf", "zvi"))
print("----------------------------------")

my_num = -55555
print(abs(my_num))
print("----------------------------------")
print(pow(2, 99))
print(max(9, 2))
print(min(9, 2))
print(round(4.55))
print(ceil(4.3))
print(floor(4.3))
print(sqrt(81))
print("----------------------------------")

# name  = input("Hello, please enter your name: ")
# age = input("now enter your age: ")
# print("Hi " + name + "! you are " + age + " years old")

print("----------------------------------")
# num1 = input("enter 1: ")
# num2 = input("enter 1: ")
# result = float(num1) + float(num2)
# print(result)

print("----------------------------------")
friends = ["Itay", "Yarden", "Idan", "Ayam"]
print(friends)
friends.append("Lidan")
print(friends)
print(friends[1:3])
friends[2] = "Sharon"
print(friends)
print("----------------------------------")
vehicles = ["car", "airplane", "helicopter", "train", "bus", "airplane", "airplane"]
numbers = [1, 43, 87, 34, 90, 3, 54, 7]
print(vehicles)
print(numbers)
vehicles.insert(3, "bicycle")
print(vehicles)
print(vehicles.index("airplane"))
print(vehicles.count("airplane"))
vehicles.sort()
print(vehicles)
print(numbers)
numbers.sort()
print(numbers)
numbersCopy = numbers.copy()
print(numbersCopy)
print("----------------------------------")

coordinates = [(4, 5), (6, 7), (9, 8)]
print(coordinates[0])
print("----------------------------------")


def hi(a, b):
    print("hi " + a + " your are " + b)


hi("asaf", "29")
hi("dba", "18")
hi("metamas", "67")


def cube(num):
    return num * num * num


result = cube(15)
print(result)
print("----------------------------------")

is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are a tall female")
else:
    print("you are a short female")
print("----------------------------------")


def max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


res = max(111, 22, 8)
print(res)
print("----------------------------------")


def calc(num1, operator, num2):
    if operator == "+":
        return float(num1) + float(num2)
    elif operator == "-":
        return float(num1) - float(num2)
    elif operator == "*":
        return float(num1) * float(num2)
    elif operator == "/":
        return float(num1) / float(num2)
    else:
        print("you entered a wrong value")
        return


# while True:
#     num1 = input("enter num 1: ")
#     operator = input("enter an operator: ")
#     num2 = input("enter num 2: ")
#
#     recieve = calc(num1, operator, num2)
#     print(recieve)
#     answer = input("contineu? yes/no")
#     if answer == "no" :
#         break
print("----------------------------------")

monthConversions = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June",
                    "7": "July", "8": "August", "9": "September", "10": "October", "11": "November",
                    "12": "December"}

print(monthConversions["9"])
print("----------------------------------")

i = 0
while i < 10:
    print(i)
    i = i + 1

# while True:
#     secret = input("please enter a word: ")
#     while secret != "asaf":
#
#
#
#         print("you won!")
#         break
#     else:
#         secret = input("please try again: ")
print("----------------------------------")

for dba in "Asaf Hermann":
    print(dba)

list = ["asaf", "matan", "ofer", "eyal"]
for names in list:
    print(names)

print("----------------------------------")
newList = ["asaf", "bar", "moshe"]
for i in range(len(newList)):
    print(newList[i])


def expo(num, exp):
    res2 = 1
    for i in range(exp):
        res2 = res2 * num
    return res2


res1 = expo(5, 3)
print(res1)
print("----------------------------------")

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
for row in range(3):
    for col in range(3):
        print(matrix[row][col])

print("----------------------------------")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


bbb = translate("asaf hermann")
print(bbb)

print("----------------------------------\n")

try:
    10/0
    number = int(input("please enter a number:  "))
    print(number)
except ValueError as error:
    print(error)
except ZeroDivisionError as error2:
    print(error2)

print("----------------------------------\n")
employee_file = open("employee.text", "r")
for employye in employee_file.readlines():
    print(employye)


employee_file.close()

print("----------------------------------\n")
# myFile = open("employee.text1", "r")
# myFile.write("\nidan - materials")
#
# employee_file = open("newFile.text", "w")
# employee_file.write("Ferrari")


asafFile = open("asaf.text", "r")
print(asafFile.read())

asafFile = open("asaf.text", "a")
asafFile.close()


carsFile = open("cars.txt", "a")
carsFile.write("\nLamborghini Murchielago")

print("-----------------------------")
def rollDice(num):
    return random.randint(1,num)

print(rollDice(7))

print("--------------------------------")



print("--------------------------------")
print("--------------------------------")

samsung = Phone(7.8, "108 MPix", "2", False)
print(samsung.screen())

print("--------------------------------")
print("--------------------------------")

student1 = Student("Asaf", "Mathematics", 4.0, False)
student2 = Student("Yossi", "Computer Science", 2.0, False)
student3 = Student("Dba", "Computer Science", 37.0, False)
print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll())
print(student1.isInCS())
print(student2.isInCS())









