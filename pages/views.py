from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") #string of HTML code
    return render(request, "home.html", {})

def contact_view(request,*args,**kwargs):
    #return HttpResponse("<h1>Contact Page</h1>") #string of HTML code
    return render(request, "contact.html", {})

def about_view(request,*args,**kwargs):
    #return HttpResponse("<h1>About</h1>") #string of HTML code
    my_context = {
        "title": "Abc This is about us",
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1,232,'a',4,5,45],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)

def social_view(request,*args,**kwargs):
    #return HttpResponse("<h1>Social</h1>") #string of HTML code
    return render(request, "social.html", {})