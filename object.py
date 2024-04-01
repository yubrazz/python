# # oop in phython(object oriented program).we deal with real time object and its entities


# # class Room(): # blueprint of object.
# #     l = int(input("enter a length"))
# #     w = int(input("enter a width"))


# #     def area(self):
# #         print("area of room is ", self.l*self.w)

      

# class Room(): # blueprint of object.
#     l = int(input("enter a length:"))
#     w = int(input("enter a width:"))
#     h = int(input("enter a height:"))


#     def volume(self):
#         print("volume of room is ", self.l*self.h)


# Room= Room()
# print(Room.volume())  

class Calculator:
    length = 20

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self,num1, num2):
        return num1+num2
    
    def substract(self,*args):
        for n in args[1:]:
            total *= n
        return total
    def multiply(self,num1,num2):
        return num1*num2
    
    def divide(self,num1,num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            print("error: division by zero")
      
cal = Calculator(1,2)
print(cal.num1)
addition = cal.add(2,3)
print(addition)



