thislist = ["phython","java","c++"]
print(thislist)




laptops = ['dell','hp','sony','lenovo','mac']

laptops.append('microsoft')
print(laptops)
laptops.insert(2,'microsoft')
print(laptops)
laptops.remove("dell")
print(laptops)

removed_elements = laptops.pop(3)
print(removed_elements)
print(laptops)


a = [1,2,3,4,5]
laptops.extend(a)
print(laptops)
b = [6,7,8,9,10]
laptops.extend(b)
print(laptops)
laptops.append('microsoft')
print(laptops)
count = laptops.count('sony')
print(count)

copy_list = laptops.copy()
print("this is an original list : ", laptops)
print("this is a copy list : ",copy_list)
copy_list.clear()
print(copy_list)

number =(1,2,6)
print(number)
count = number.count(6)
print(count)


user_id= {444,444,222,333}
print(user_id)