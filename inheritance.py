#inheritance ->the process of inheritance the prperties of the parent class

class Person:
    def person_info(self,name,age):
        print('inside person class')
        self.name= name
        print('name :',name,'age',age)


class company:
    def company_info(self,company_name,location):
        print('inside employee class')
        print('name:',company_name,'loaction:',location)


class employee(Person,company):
    def employee_info(self,salary,skill):
        super()              