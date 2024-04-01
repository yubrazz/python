#function is a block of code. we used function to reuse the code . teo types of function are 
#1 build in function
#2 user defined function


#def function_name():
 #function body


#function_name() 


# #def helloworld():
#  #   print("helloworld")

# #helloworld()    

# #positionl aruguments takes vlaues according to proper positional order
# def hello(name,course_name):   #parameter
#     print("hello",name,"welcome to web development training")
#     print(course_name)

# hello('ram','phython with django')    #aruguments


# def hello(name,course_name):   #parameter
#     print("hello",name,"welcome to web development training")
#     print(course_name)
# #keyword agruments = takes value from key word
# hello( name='ram',course_name='phython with django')

# #default agruments
# def hello(name,course_name):   #parameter
#     print("hello",name,"welcome to web development training")
#     print(course_name)

# hello(name='ram',course_name ='phython with data science')



def sum(*args):
    total = args[0]+args[1]+args[2]
    return total #return gives result of function and stops the execution of function

result = sum(2,3,5)
print(result)
1
#arbirtrary arguments = *
def sum (*args):
    total = 0
    for n in args:
        total+=n

        return total #return give the result
    print(result)

# #arbitiary keywords arguments - **kwargs which contaion data in key:value pairs
# def hello(**kwargs): 
#     print("hello",kwargs['name'],"welcome to web development training")
#     print(kwargs['course_name'])

# hello(name='ram',course_name='phython with data science',another_course='phython with data science')

l = float(input("enter length :"))
w = float(input('enter width :'))

def area():
    global area_of_object  
    area_of_object = l*w
    return area_of_object
result = area()
print(result)

# def volume():#local variable - that is defined inside the function and cannot acessible from outside the function.lts scope is only around the declared
#     h = float(input("enter height :"))
#     arera_of_object = l*w
#     return arera_of_object,volume
# reult = volume()
# print(result)



#lambda fucntiion -nameless function .it is used for instant use or one time use. lamda is the keyword
# x = lambda a, b : a+b
# sum = x(2,3)
# print(sum)

# x = lambda a, b : a*b
# area = x(2,3)
# print(area)


# recursive function - function calling itself again and again
def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    a = factorial(4)
    print(a)


#filterb
#map()
    #module-



