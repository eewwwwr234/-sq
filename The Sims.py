import random

from select import select


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
    def getjob(self):
        if select.car.drive():
        pass
    def gethome(self):
        if (self.satiety < 0):
            print(f"{self.name} is work ...")
    def getcar(self):
        if (self.satiety < 0):
            print(f"{self.name} is drive ...")
    def eat(self):
        if (self.satiety < 0):
            print(f"{self.name} is dead ...")
    def work(self):
        if (self.satiety < 0):
            print(f"{self.name} is work ...")
    def shopping(self, manage):
        if (self.satiety < 0):
            print(f"{self.name} is money ...")
    def chill(self):
        if (self.satiety < 0):
            print(f"{self.name} is warm clothes ...")
    def cleanhome(self):
        if (self.satiety < 0):
            print(f"{self.name} is clean ...")
    def torepair(self):
        if (self.satiety < 0):
            print(f"{self.name} is work ...")
    def daysindexes(self, day):
        if (self.satiety < 0):
            print(f"{self.name} is calendar ...")
    def isalive(self):
        if (self.satiety < 0):
            print(f"{self.name} is live ...")
    def live(self, day):
        if (self.satiety < 0):
            print(f"{self.name} is dead ...")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

        def drive(self):
            if self.strength > 0 and self.fuel >= self.consumption > 0 :
                self.fuel - self.consumption


def drive(self):
    if self.strength > 0 and self.fuel >= self.consumption > 0:
        self.fuel - self.consumption


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary=job_list[self.job]['salary']
        self.gladness = job_list[self.job]['gladness']




brands_of_cars = {
    'BMW': {'fuel': 100, 'strength': 100, 'consuption': 6},
    'Volvo': {'fuel': 208, 'strength': 128, 'consuption': 20},
    'Ferrari': {'fuel': 88, 'strength': 180, 'consuption': 28},
}
print(type(brands_of_cars))