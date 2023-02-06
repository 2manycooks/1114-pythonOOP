class CoffeeCup:
    # init takes the place of the constructor method in js.
    # always provide self as the first parameter. this is how it handles binding (similar to 'this' in js)
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    # this is intended to be a human readable string representation of an object. when printing a class instance, it will look for this method to decide what to print.
    def __str__(self):
        return f"this is a cofveve cup with a maximum capacity of {self.capacity} fluid ounces. It currently has {self.amount} fluid ounces in it."

    def fill(self):
        self.amount = self.capacity

    def drink(self, drink_amount):
        self.amount -= drink_amount
        if(self.amount <= 0):
            self.amount = 0

    def empty(self):
        self.amount = 0
        print("pour one out for the homies 🫗")

gabes_cup = CoffeeCup(12)
westons_cup = CoffeeCup(16)
westons_larger_cup = CoffeeCup(36)


#  default parameters
# we're gonna need some math
import math 
# where once there was no math, bam, now there's math.

class Point():

    # you can set default parameters values by just giving their default value in the __init__ parameter.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def distance(self, p2 = None):
        if(p2 == None):
            p2 = Point.ORIGIN
        else:
            dx = self.x - p2.x
            dy = self.y - p2.y
            return math.sqrt(dx**2 + dy**2)
            

Point.ORIGIN = Point()

# p0 = Point()
# print(p0.distance())
p1 = Point(3,4)
# print(p1.distance())
p2 = Point(6,13)
p3 = Point(1,1)
# print(p1.distance())


# Let's make a class together!

class Car():
    # we need a make, a model, a year, and a speed. ✅
    # we also need to be able to accelerate and brake. 
    # any parameter with default values NEEED to go at the end.
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        return f"woo, this sweet lil {self.make} {self.model} is hummin like a hummingbird 🧆"

    def accelerate(self, amount):
        self.speed += amount
        print("varoom 🏎")

    def brake(self, amount):
        self.speed -= amount
        print("skrrt skrrt ☸️")

gabes_volvo = Car("Volvo", "XC40", "2022")



#  <-------- CLASS INHERITANCE ------->

class Phone():
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"You have reached {self.number}"

    def call(self):
        print(f"calling you for some reason from {self.number}")

    def text(self):
        print(f"this is how people actually communicate these days. anyways, you're getting a text from {self.number}")


gabes_generic_phone = Phone("510-666-6666")
# gabes_generic_phone.call()

# just like in js, we can make child classes that inherit properties from their parent class.

class IPhone(Phone):
    def __init__(self, number, generation, color):
        super().__init__(number)
        self.generation = generation
        self.color = color
        self.fingerprint = None

    # you can override a method from the parent by simply redefining it. Otherwise, you will inherit methods from the parent as-is.
    def __str__(self):
        return f"this is my bougie iphone {self.generation}. i managed to get it in {self.color}. FINGERPRINT SETTINGS: {self.fingerprint}"

    def set_fingerprint(self, value):
        self.fingerprint = value
    
    def unlock(self, input):
        if(self.fingerprint == input):
            print("unlocked! welcome user!")
        else:
            print("fingerprint not recognized. calling the police.")

gabes_iphone = IPhone("510-666-6666", 14, "Rose Gold")
gabes_iphone.set_fingerprint("Gabe")
# print(gabes_iphone)
# gabes_iphone.unlock("Weston")

class Android(Phone):
    def __init__(self, number, keyboard = "Default"):
        super().__init__(number)
        self.keyboard = keyboard

    def __str__(self):
        return f"This Android uses the {self.keyboard} keyboard."

    def set_keyboard(self, input):
        self.keyboard = input

gabes_google_pixel_6 = Android("510-666-6666")
print(gabes_google_pixel_6)