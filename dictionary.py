student ={
    'name':'ram',
    'age':20,
'address':'boudha'
}
print(student)


capital ={
    "nepal":"kathmandu",
    "india":"new delhi",
    "china":"beijing",
}
print (capital) 
print(len(capital))
print(type(capital))
print(capital.keys())#gives list of keys in the dictionary
print(capital.values())
print(capital['nepal'])
capital['japan'] = "tokyo"#adds the values in the dictionary
print(capital)
capital['bhutan'] = "thimpu"
print(capital)
pop_element = capital.pop('bhutan')
print(pop_element)
print(capital)
#remining list part
a = (1,2,3,4)
b = (1,2,3,4)
c = ['a','b','c','e','f']
print(c.index('a'))#gives the index number of given data
c.sort()#ascending order
print(c)
c.sort(reverse=True)
print(c)

marks = {
    "maths":100,
    "science":99,
    "english":98
}
print(marks)
capital.update(marks)
print(capital)
copy_capital = capital.copy()
print("this is a copy capital : ",copy_capital)
clearcapital = capital.clear()
print(clearcapital)
