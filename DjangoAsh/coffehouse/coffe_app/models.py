from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
#for slug
from django.utils.text import slugify


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

    #add error_messages for review code
    name = models.CharField(max_length=30, error_messages={'max_lengh':'Your input value is over 30 chars!!!'})
    
    #add unique for clean_fields()
    
    #for error_messages
    userdefined_error_msg={
        'required': 'error message 1',
        'max_length': 'error message 2',
    }
    address = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=30, default=default_city)
    state = models.CharField(max_length=2, default="UK", error_messages=userdefined_error_msg)

    #clean method
    def clean(self):
        my_store=Store(name='Corporate', address='England-london', city='London', state='UK', email='almator5@gmail.com')


    ## object variable is added by default, not required explicitly
    #objects = models.Manager()
    #for edit your custome name---> views.py  ins1 = ins1 = Store.mngr.get(id=3)
    mngr = models.Manager()

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

    #add email 
    email = models.EmailField()

    #add amenity
    ameneties = models.ManyToManyField('Amenity', blank=True)

    #add for unique_together
    class Meta:
        ordering = ['state']
        #to order by name descending ,, then by state ascending , use this:
        ##ordering =['-name', 'state']
        
        unique_together = ("name", "email")
        #or (a list of tuples):
        #enforces both city/state and city/zipcode fields are unique together
        #unique_together = (('city', 'state'),('city', 'zipcode'))

        #A two-fieeld index for city and state fields, and an index for the city field named
        indexes=[
            models.Index(fields=['city', 'state']),
            models.Index(fields=['city'], name='city_index')
        ]

        #Naming Convention : for optional name
        verbose_name = "Social Security Number"
        verbose_name_plural = "Social Security Numbers"

        #inheritance Meta Options
        abstract = True
    class Drink(Item):
        mili_liters = models.IntegerField()
        #Example
        abstract = True
    class Student(CommonInfo):
        home_group = models.CharField(max_length=5)


    def __str__(self):
        return "%s (%s, %s)"%(self.name, self.city, self.state)
        #also you can use python format function
        ##return "{}({}, {})", format(self.name, self.city, self.state)

#create class for mobile validation
class Contact(models.Model):
    mobile_validation = RegexValidator(regex=r'^09\d{9}$', code = "Invalid", message = "Phone number must be entered in the format:'09999999999'. Up to 11 digits allowd.")
    mobile = models.CharField(max_length=11, blank=False, null=False, help_text="Mobile number", validators=[mobile_validation], error_messages={'required': "Enter your mobile number", 'max_length':"Enter exactly 11 digit"})


def calorie_watcher(value):
    if value>5000:
        raise ValidationError(('calories are %(value)s ? We try to serbe health food, try something less'), params={'value':value},)
    if value<0:
        raise ValidationError(('calories are %(value)s ? This can\'t be , value must be greater than 0'), params={'value':value},)


class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, validators=[MinLengthValidator(5), MaxLengthValidator(30)], verbose_name="Menu Name")
    description = models.CharField(max_length=100, help_text="Ensure you probide some descriprion for your item")
    size = models.CharField(choices=ITEM_SIZE, max_length=1)
    calories = models.IntegerField(validators=[calorie_watcher], help_text="calorie count should reflect <b>size</b> of the item")

#for method save
class Animal(models.Model):
    is_hungry = models.BooleanField(default=True)
    def feed_animal(self):
        self.is_hungry = False
    def save(self, *args, **kwargs):
        self.feed_animal()
        super(Animal, self).save(*args, **kwargs)

#for slug
class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Topic, self).save(*args,**kwargs)

#for amenity
class Amenity(models.Model):
    name = models.CharField(max_length=30)
    describtion = models.CharField(max_length=100)