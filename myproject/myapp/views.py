from django.http import HttpResponse


# Create your views here.

def hello(request):
    html = "<p>Hello world, my name is Carl and Thien chi is my boss</p>"
    return HttpResponse(html)
