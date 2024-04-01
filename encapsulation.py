class Employee:


    def __init__(self,name,project,salary):
        self.name = name
        self._project = project
        self.__salary = salary

    def show(self):
        print("name : ",self.name)


emp = Employee('madhva', 'xavier',1000)
emp.show()
print(emp.name)
print(emp._project)
print(emp._Employee__salary)            