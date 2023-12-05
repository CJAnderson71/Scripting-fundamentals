#define name
name = input("Enter your name: ")

#define password
password = "Pas$Word"

#define boolean variable
first = True

#while loop
while first:
    
    #ask the password
    pwd = input("Enter your password: ")
    
    #check if input password is correct or not
    if pwd != password:
        print("Incorrect password, try again...")
    else:
        print("Welcome back,",name)
        break
