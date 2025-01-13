namn = input ("What's your username? ")

print ("Welcome " + namn + "!")
lösenord = input ("Password: ")

if namn=="noname" and lösenord == "nopass":
    print("Welcome!")

else: 
    print ("Wrong username or password")