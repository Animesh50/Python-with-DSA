x = int(input("Enter your age:  "))

if(x>=18):
    print("You are above the age. ")
    print("Yes you can go.")

elif(x<0):
        print("this is not a valid age: ")

elif(x==0):
     print("this is also not valid: ")
else:
    print("you are below the age. ")
    print("you are not allow in this area.")