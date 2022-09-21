from django.http import HttpResponse
from django.template import loader
from myapp.models import User


# Create your views here.

def hello(request):
    template = loader.get_template('hello.html')
    context = {'name': 'Thien chi'}
    return HttpResponse(template.render(context))


def users(request):
    template = loader.get_template('users.html')
    users_list = User.objects.all()
    context = users_list
    return HttpResponse(template.render({"users": context}))
