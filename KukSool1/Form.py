import random

class Form:
    def __init__(self, name, number, meaning, level=-1, difficulty=0, clues=[]):
        self.name = name
        self.number = number
        self.meaning = meaning
        self.level = level
        self.difficulty = difficulty
        self.clues = clues
    
    def desc(self):
        return self.name 
    
    def get_random(self):
        return random.random(0,self.number)
    
    def get_clue(self, number):
        if len(self.clues)>=number:
            return self.clues[number]
        else:
            return ""
    
    def __str__(self):
        return self.name+" "+("" if self.meaning=="" else "("+self.meaning+")")+("" if self.number==1 else ": "+str(self.number)+" parts")+" (dif: "+str(self.difficulty)+")"