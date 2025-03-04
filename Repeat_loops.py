#To print every item in the shopping list

#shopping_list = ["eggs", "milk","chantilly", "meat"]
#
# for item in shopping_list:
#     print("item bought:", item)


#----------------------><-------------
#loop using while
# age = 0
# while age < 18:
#     print ("need to be older, you are", age , "old")
#
#     if age > 18:
#         print ("you are old enough")
#
#     else: age = age + 1



#--------------------------><-------------------------
#loop using more conditions, interrupting the loop or not
number = 0
while True:
    print("number",number)
    number = number + 1

    if number % 2 == 0: #verify if the number is pair
        print(number,"its pair")
        continue

    print(number,"its odd")