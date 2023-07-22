
'''num1=2
num2=9

a=num1+num2/2

print(a)'''

                                                          # excercise strings

'''myString = "452-1111-2222"

print(myString[:3], "is your pin code")
print(myString[4:8], "is your product code")
print(myString[-4:], "is your code")


firstname = input("Enter your first name :")
middlename = input("Enter your first name :")
lastname = input("Enter your first name :")

print("your initial are", firstname[0], middlename[0],lastname[0])'''

                                                        # exercise numbers

'''import math

a = math.factorial(5)
b = math.sqrt(2)

print(a, b)

radius = int(input("Enter the radius : "))

area = 3.14*radius**2

circum = 2*3.14*radius

print("Area 0f the circle is ", area)
print("circumference 0f the circle is ", circum)'''


                                                        #excerise lists and tuples

'''months = ("jan", "feb", "march", "april", "may", "june", "july", "aug")

birth = input("Enter you birthday:")

index = int(birth[3:5])-1

bd_month = months[index]

print(bd_month)'''

                                                      #Dictionaries

'''info = {'firstname':'prasad', 'lastname':'kalelar', 'birth':2003, 'location':'mumbai'}

user = input("what info are you looking for")

info_is = info.get(user)

print(info_is)'''


                                                       #booleans
'''a = 20
user = int(input("What is your age "))


if(user>a):
    print("your are greater than me")

elif(user == a):
    print("We are of same age")

else:
    print("you are smaller than me")'''

                                                        #conditional 

'''a = float(input("enter your height in meters"))
b = int(input("enter your weight in kg"))

bmi = b/(a*a)
1.
if(bmi<=18.5):
    print("uderweight")
elif(bmi>18.5  or bmi<=24.9):
    print("normal weight")
elif(bmi>24.9 or bmi<=29.9):
    print("overweight")
elif(bmi>=30):
    print("obsity") '''


                                                                  #loops 
'''import random


people =[]

for x in range(0,8):
    a = input("Enter the names")
    people.append(a)

index = random.randint(0,7)
random_person = people[index]

print("the random perso is ", random_person)'''


                         #error handling


'''grade = str(input("enter the grade"))

Try:'''

                                                  #matplot
import matplotlib.pyplot as plt

x = [1,2,3,4]

y = [10,20,40,20]

plt.plot(x,y)

plt.show()





