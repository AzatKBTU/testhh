from django.db import models
from datetime import datetime


date = datetime.now()
year = date.year
month = date.month
day = date.day

class Person(models.Model):
    uin = models.CharField(max_length=12)

    @property
    def age(self):
        if(int(self.uin[6:7]) == 5 or int(self.uin[6:7]) == 6 ):
            if(month>int(self.uin[2:4]) or (month==int(self.uin[2:4]) and day>=int(self.uin[4:6]))):
                return year - 2000 - int(self.uin[:2])
            else:
                return year - 2000 - int(self.uin[:2])-1
        if(int(self.uin[6:7]) == 3 or int(self.uin[6:7]) == 4 ):
            if(month>int(self.uin[2:4]) or (month==int(self.uin[2:4]) and day>=int(self.uin[4:6]))):
                return year - 1900 - int(self.uin[:2])
            else:
                return year - 1900 - int(self.uin[:2])-1
        else:
            if(month>int(self.uin[2:4]) or (month==int(self.uin[2:4]) and day>=int(self.uin[4:6]))):
                return year - 1800 - int(self.uin[:2])
            else:
                return year - 1800 - int(self.uin[:2])-1

