from audioop import add
from django.db import models


#Evoid to submit null data or blank
def default_city():
    return "London"
# Create your models here.
class Store(models.Model):
    #id field is added by default, not required explicitly
    ##id = models.AutoField(primary_key=True) #Django < 3.2
    ##id = models.BigAutoField(primary_key=True) #Django > 3.2
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30, default=default_city)
    state = models.CharField(max_length=2, default="UK")
    ## object variable is added by default, not required explicitly
    #objects = models.Manager()
    def __str__(self):
        return "%s (%s, %s)"%(self.name, self.city, self.state)
        #also you can use python format function
        ##return "{}({}, {})", format(self.name, self.city, self.state)