#!/usr/bin/python3
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
class Barista(Employee):
    def __init__(self, first_name, last_name, experience_level):
        super().__init__(first_name, last_name)
        self.experience_level = experience_level
        

    def __init__(self, first_name, last_name, cooking):
        super().__init__(first_name, last_name)
        self.cooking = cooking

barista1 = Barista("Nathan", "Wood", "expert")
barista2 = Barista("Braden", "Chance", "newbie")


print(f"Hello, my name is {barista1.first_name} {barista1.last_name} and I am a {barista1.experience_level} at steaming milk.")
print(f"Hello, my name is {barista2.first_name} {barista2.last_name} and I am a {barista2.experience_level} at steaming milk.")

