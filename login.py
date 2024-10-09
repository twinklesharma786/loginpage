# login page 
username=input("enter the username")
password=int(input("enter the password"))
confirmpassword=int(input("enter the confirm password"))
max_attempt=3
if(password==confirmpassword):
    print("login succefull")
else:
    print("try again")
        
    attempts=0
    max_attempts=3
    while(attempts<max_attempt):
        password=int(input("enter the password"))
        confirmpassword=int(input("enter the confirm password"))
        if(password==confirmpassword):
            print("login succefull")
            break
        else:
            print("try again")
            attempts+=1
            if attempts==max_attempts:
                print("too much attempts ")