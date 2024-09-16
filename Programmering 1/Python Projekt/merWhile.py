
age= int(input("How old are you? "))
print("You're age is ", age)
if(age >= 18 and age <= 65):
    print("You are an adult")
elif(age < 18):
    print("You are too young")
else:
    print("You are too old")