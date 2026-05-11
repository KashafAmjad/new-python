class myClass:
    __privateVar=27;
    def__privMeth = (self):
    print("I'm inside class myClass")
    def hello(self):
        print("Private Variable value:",myClass.__privateVar)
  

obj=myClass()
obj.hello()
obj.__privMeth