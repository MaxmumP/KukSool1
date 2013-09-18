import Exercise

class Meditation(Exercise.Exercise):
    def __str__(self):
        return self.name+("" if self.meaning=="" else "("+self.meaning+")")+": "+str(self.number)+" meditation"