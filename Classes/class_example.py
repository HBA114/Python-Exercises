class person:
    def __init__(self,name = "",age =-1):
        self.name = name
        self.age = age
    
    def setName(self,name): # you can control name standart in here if you have
        self.name = name
    
    def setAge(self,age):   # you can control age standart in here if you have
        self.age = age

    def personInfo(self):
        print("Name : {} \nAge : {}\n".format(self.name,self.age))


class employee(person):
    def __init__(self,name = "",age = -1,salary = 0):
        super().__init__(name,age)
        self.salary = salary
    
    def employeeInfo(self):
        print("Employee Name : {} \nEmployee Age : {} \nEmployee Salary : {}\n".format(self.name,self.age,self.salary))


if __name__ == "__main__":      # main function
    person1 = person("Hasan",22)

    # You can print data like this
    print("Person Name : %s \nPerson Age : %d" %(person1.name, person1.age))

    # You can print daat with function in class write once use everywhere
    person1.personInfo()

    # You can create employee with paramaters
    employee1 = employee("Ali",21,5000)

    employee1.employeeInfo()
    employee1.personInfo()

    # You can create employee without paramaters
    employee2 = employee()
    employee2.setName("Ahmet")
    employee2.setAge(25)
    employee2.salary = 5000
    employee2.employeeInfo()