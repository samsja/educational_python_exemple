### Let's say I want to code an application to manage a car renting agency online, I would need a car representation to manage the cars in my code

### a car is reprsented by :
## * a mark:
## * its price when it was new
## * the number of kilometer that the car has


def init_car(mark,price,kil):
    return [mark,price,kil]


## Here I define an inti function which allow me to create a car from three parameters : mark,price,kill



car1 = init_car("jaguar",100,1000)
car3  = init_car("jaguar",45,1000)



## I can create a cat manualy as well by doing this

car2 = ["peugot",20,2000]

## In both case the case the car is a list containing three information, the first in the mark, second, the price,last the kil

def car_repr(car):
    mark = car[0]
    price = car[1]
    kil = car[2]
    return f"This car is a {mark} which was bought {price} and has {kil} killometers"


print(car_repr(car1))

print(car_repr(car2))


## Now I want to define the hours price for the rent based on the mark info


def is_luxurious(car):

    mark = car[0]
    price = car[1]

    if mark == "jaguar":
        return True
    elif price >= 50:
        return True
    else:
        return False

def price_h(car):
 
    if is_luxurious(car):
        return 100
    else :
        return 50
    
print(price_h(car1))
print(price_h(car2))

## even if the car3 only cost 45 it is still luxiorous because it is a jaguar
print(price_h(car3))
