from unicodedata import name
from xml.dom import ValidationErr
from django.shortcuts import render
from .models import Store
from .models import Animal
from django.contrib.auth.decorators import login_required
from .models import Topic, Topic_intry
from .forms import TopicForm , TopicEntryForm
@login_required

def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.Post)
        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.author = request.user
            new_topic.save()
            return redirect("blog_app:topic")
    return render(request, 'blog_app/new_topic.html', context={'form':form})

#showing a message in home page
def show_home_page(request):
    ##do something here ....
    mycontent = {'mykey': 'We love IRAN'}
    return render(request, "homepage.html", context = mycontent)
# Create your views here.

#create model store instance
my_store = Store(name = 'AlirezaShamsi', address = 'Piccadilly St, No.72', city = 'London', state = 'UK', email = 'alireza@alirezashamsi.com')

#Invoke the save() method to create/save the record
my_store.save()

#change field on instance (an update operation)
my_store.address = 'SOHO st, No.9'

#invoke the save() method to update/save the record
##record has id regerence from prior save() call, so operation is update 
my_store.save()

#using other database
##my_store.save(using='replica1')

#using update field
##my_store.name = 'Ashix'
##my_store.address = 'SOHO st, No.9'
##my_store.save(update_fields=['name', 'address'])


instance1 = Animal()
instance1.save()

#for delete
Instance.delete(id = 2)

#clean_fields() this code with erro
store_corporate = Store(name="This is a very long name for the Corporate store that eceeds the 30 character limit.", address='England - London', city= 'London', state= 'UK', email='almator5@gmail.com')
store_corporate.clean_fields()

#output:
"""
Tracebace(most recent call last):
    raise ValidationError(error)
ValidationError:{'name':[u'Ensure this value has at most 30 characters(it has 84).']}

"""


#for clean
my_store.clean()

