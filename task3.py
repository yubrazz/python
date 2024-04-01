a = "my country name is nepal."
b = "i study in xavier"
print(len(a))
print(a[-1])
print(a+b)
print(a.split(" "))
print(a.upper())
print(a.lower())
print(b.replace("xavier","cambridge"))


quantity = 5
item_no = 957
price = 43.33
myorder = "i want {}pieces of item {}for{}dollars"
print(myorder.format(quantity,item_no,price))