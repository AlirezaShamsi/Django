from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import RegexValidator


#our choices option is a List of values as a Tuple of Tuples: (key, Value)
ITEM_SIZE = (
    ('U', 'Unkown'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

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

    #Add date
    my_date = models.DateField(default=date.today)
    my_datetime = models.DateTimeField(default=timezone.now)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

    #Add size of city
    size = models.CharField(choices=ITEM_SIZE, max_length=1, default='U')
    #or
    #size = models.CharField(choices=ITEM_SIZE, max_length=1)

    ## object variable is added by default, not required explicitly
    #objects = models.Manager()


    def __str__(self):
        return "%s (%s, %s)"%(self.name, self.city, self.state)
        #also you can use python format function
        ##return "{}({}, {})", format(self.name, self.city, self.state)

#create class for mobile validation
class Contact(models.Model):
    mobile_validation = RegexValidator(regex=r'^09\d{9}$', code = "Invalid", message = "Phone number must be entered in the format:'09999999999'. Up to 11 digits allowd.")
    mobile = models.CharField(max_length=11, blank=False, null=False, help_text="Mobile number", validators=[mobile_validation], error_messages={'required': "Enter your mobile number", 'max_length':"Enter exactly 11 digit"})

