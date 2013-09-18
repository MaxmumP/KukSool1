import random

class Exercise:
    def __init__(self, name, number, meaning=""):
        self.name = name
        self.number = number
        self.meaning = meaning
    
    def desc(self):
        return self.name 
    
    def get_random(self):
        return random.random(0,self.number)
    
    def __str__(self):
        return self.name+("" if self.meaning=="" else "("+self.meaning+")")+": "+str(self.number)+" exercises"