import random

class Weapon:
    def __init__(self, name, forms, meaning, meditations=[], exercises=[]):
        self.name = name
        self.meaning = meaning
        self.forms = forms
        self.meditations = meditations
        self.exercises = exercises
    
    def desc(self):
        return "%s %s" % (self.name, self.meaning) 
    
    def get_random_activity(self):
        return random.choice(self.forms+self.meditations+self.exercises)
    
    def __str__(self):
        printstr=self.name+" "+("" if self.meaning=="" else "("+self.meaning+")")
        if len(self.forms)>0:
            printstr+="\n - Forms: "
            for form in self.forms:
                printstr+="   %s (%i)" % (form.name, form.number)
        if len(self.meditations)>0:
            printstr+="\n - Meditations: "
            for med in self.meditations:
                printstr+="   %s (%i)" % (med.name, med.number)
        if len(self.exercises)>0:
            printstr+="\n - Exercises: "
            for exc in self.exercises:
                printstr+="   %s (%i)" % (exc.name, exc.number)
        return printstr