import os,shutil
#file handling -> open file,close file,read file,write and maintain file



# my_file = open('test.txt')
# print(my_file)
# print(my_file.read())# to read the file.
# print(my_file.writable())# to check eheather tp write in file or not
# my_file.close()
# print(my_file.read())


# my_another_file = open('test.txt', 'r+')
# print(my_another_file.readable())
# print(my_another_file.writable())
# print(my_another_file.read())
# my_another_file.write('ram\n')


# my_another_file = open('test.txt', 'w+')
# print(my_another_file.read())
# print(my_another_file.readable())
# print(my_another_file.writable())
# my_another_file.write('ram')
# print(my_another_file.seek(0))
# print(my_another_file.read())


my_next_file = open('next.txt','a+')
print(my_next_file.writable())
print(my_next_file.readable())
my_next_file.read()
my_next_file.write('hello world')
print(my_next_file.write('hello \n world'))
print(my_next_file.seek(0))
print(my_next_file.read())
list1 =['ram','sam','hari']
print(my_next_file.writelines(list1))
print(my_next_file.seek(0))
print(my_next_file.readline())
print(my_next_file.readlines())


# shutil.copy('next.txt','next1.txt')
# os.remove('next1.txt')

shutil.move('test.txt','next1.txt')