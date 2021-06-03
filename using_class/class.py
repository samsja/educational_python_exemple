## Now I am using Object oriented programming (Class in python)



class Car:

    def __init__(self,price,kil):
        self.price = price
        self.kil = kil


    def __repr__(self):
        return f"This car is a car which was bought {self.price} and has {self.kil} killometers"

    def is_luxurious(self):

        if self.price >= 50:
            return True
        else:
            return False

    def price_h(self):
     
        if self.is_luxurious():
            return 100
        else :
            return 50


class Jaguar(Car):
    
    def __init__(self,price,kil):
        super().__init__(price,kil)

    def is_luxurious(self):
        return True 

    def __repr__(self):
        return f"This car is a jaguar which was bought {self.price} and has {self.kil} killometers"


class Peugot(Car):
    
    def __init__(self,price,kil):
        super().__init__(price,kil)

    def __repr__(self):
        return f"This car is a Peugot which was bought {self.price} and has {self.kil} killometers"


car1 = Jaguar(100,100)
car2 = Peugot(20,2000)
car3 = Jaguar(45,100)


print(car1)
print(car2)


print(car1.price_h())
print(car2.price_h())


## even if the car3 only cost 45 it is still luxiorous because it is a jaguar

print(car3.price_h())
