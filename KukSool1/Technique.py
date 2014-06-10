import random

class Set:
    def __init__(self, name, number, meaning, level=-1, starts_with="", techniques=[]):
        self.name = name
        self.number = number
        self.meaning = meaning
        self.starts_with = starts_with
        self.level=level
        self.techniques=techniques
    
    def get_description(self):
        return self.name 
    
    def get_technique(self, tech_num):
        if self.number >= tech_num:
            if len(self.techniques) >= tech_num:
                if self.techniques[tech_num-1].number==tech_num:
                    return self.techniques[tech_num-1]
            else:
                for technique in self.techniques:
                    if technique.number==tech_num:
                        return technique
            technique = Technique(tech_num, "", "")
            self.add_technique(technique)
            return technique
        else:
            return None
    
    def add_technique(self,t):
        if len(self.techniques)==0:
            self.techniques.append(t)
        else:
            i=0
            for technique in self.techniques:
                if t.number<technique.number:
                    self.techniques.insert(i, t)
                    break
                elif i==len(self.techniques):
                    self.techniques.append(t)
                    break
                i+=1
                    
    def get_random(self):
        return random.randrange(1,self.number)
    
    def get_full_description(self):
        descript_string=self.__str__()
        for technique in self.techniques:
            descript_string+="\n"+technique.__str__()
        return descript_string
    
    def __str__(self):
        return self.name+("" if self.meaning=="" else " ("+self.meaning+")")+": "+str(self.number)+" techniques"

class Technique:
    def __init__(self, number, description, similarTo, hints=[], hyuls=[], ):
        self.number = number
        self.description = description
        self.similarTo = similarTo
        self.hints = hints
        self.hyul = hyuls
    
    def set_description(self, description):
        self.description=description
    
    def get_description(self):
        return self.description
    
    def get_hint(self):
        #helpers=[self.hint,self.similarTo]
        #if len(self.hyul)>0:
        #    helpers.append(random.choice(self.hyul))
        #return random.choice(helpers)
        return random.choice(self.hints)
    
    def set_hint(self, hint):
        #TODO: This should be a smarter check- like searching for keywords
        if hint not in self.hints:
            self.hints.append(hint)
        else:
            print hint+" already in hints list"
    
    def __str__(self):
        desc=str(self.number)
        if self.description:
            desc+=": "+self.description
        if len(self.hints)>0:
            desc+=" ("+", ".join(self.hints)+")"
        return desc
                