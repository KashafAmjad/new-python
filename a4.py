class Vehicle:
    def __init__(self,max_speed, mileage,name):
       self.max_speed = max_speed
       self.mileage = mileage
       self.name=name
    

modelX = Vehicle(240, 18,"BMW")
print("Model Nmae:",modelX.name)
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:",modelX.mileage)