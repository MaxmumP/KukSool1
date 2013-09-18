import random

class Set:
    def __init__(self, name, number, meaning, level=-1, starts_with="", techniques=[]):
        self.name = name
        self.number = number
        self.meaning = meaning
        self.starts_with = starts_with
        self.level=level
        self.techniques=techniques
    
    def get_desc(self):
        return self.name 
    
    def get_technique(self, tech_num):
        if len(self.techniques)>tech_num:
            return self.techniques[tech_num-1]
        else:
            return None
        
    def get_random(self):
        return random.randrange(1,self.number)
    
    def __str__(self):
        return self.name+("" if self.meaning=="" else "("+self.meaning+")")+": "+str(self.number)+" techniques"

class Technique:
    def __init__(self, number, description, similarTo, hint, hyul):
        self.number = number
        self.description = description
        self.similarTo = similarTo
        self.hint = hint
        self.hyul = hyul
    
    def desc(self):
        return self.number 
    
    def get_hint(self):
        helpers=[self.hint,self.similarTo]
        if self.hyul:
            helpers.append(self.hyul)
        return random.choice(helpers)
    
    def __str__(self):
        return self.number+" "+self.description