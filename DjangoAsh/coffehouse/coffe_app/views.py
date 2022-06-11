from django.shortcuts import render
def show_home_page(request):
    ##do something here ....
    mycontent = {'mykey': 'We love IRAN'}
    return render(request, "homepage.html", context = mycontent)
# Create your views here.
