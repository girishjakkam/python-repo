class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %s MPG."%(self.color,self.model,self.mpg)
        
class ElectricCar(Car):
    def __init__(self,model, color, mpg,battery_type):
        self.battery_type=battery_type
        super(ElectricCar,self).__init__(model,color,mpg)
        
    
my_car = Car("DeLorean", "silver", 88)
print my_car.display_car()
my_car=ElectricCar("Gary","red",98,"molten salt")
print my_car.display_car()

