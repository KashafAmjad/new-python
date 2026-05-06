class Person( object ):
        def __init__(self, name, idnumber):
         self.name=name
         self.idnumber=idnumber
        def display(self):
                print (self.name)
                print (self.idnumber)
class Employee(Person):
        def __init__(self, name, idnumber,salary,post):
          self.salary=salary
          self.post=post
          Person.__init__(self, name, idnumber)
print("Employee1 detail:")
a=Employee("ali", 678929,400000000,"CEO")
a.display()
print(a.salary)
print(a.post)
print("\n")
