#exception -> an event that occcurs to distrupt the normal flow of operation
# try:
#     age = int(input())
#     print(age)
# except: 
#     print('print provide numberic value')

# print('xavier college')

# try:
#     a = int(input("enter a value"))
#     b = int(input("enter a value"))
#     c = a/b
# except ValueError:
#     print('please provide numberic value')  
# except ZeroDivisionError:
#     print('zero will not divide any other number ')      
# else:
#     print("the value of c is",c)
def login():
    user1 = 'admin'
    pass1 = 'admin'

    try:
        username = input("enter a username=")
        password = input("enter a password=")

        if user1 != username:
            raise ZeroDivisionError
        elif pass1 != password:
            raise ValueError
    
    except ZeroDivisionError:
        print("username is invalid")
    except ValueError:
        print("password is invalid")
    else:
        print("login sucessfully")
    finally:
        print("home")

login()        
    


