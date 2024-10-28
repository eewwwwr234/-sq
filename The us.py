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

    def __init__(self, name="Human", job=None, home=None, car=None):

    def get_job(self):
        if select.car.drive():
        pass



    def get_home(self):
        pass
    def get_car(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass
    def days_indexes(self, day):
        if (self.satiety < 0):
            print(f"{self.name} is dead ...")
    def is_alive(self):
        if(self.satiety <0):
            print(f"{self.name} is dead ...")
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

