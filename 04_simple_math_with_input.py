# request user input
integer1 = input("Please input integer1: ")
integer2 = input("Please input integer2: ")
integer3 = input("Please input integer3: ")

# user input are strings. Need to cast to integers to add them
sum_of_all = int(integer1) + int(integer2) + int(integer3)

print("The Sum of All integers is", sum_of_all)