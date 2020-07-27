from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    my_dict = {"name": "Ayyaj"}
    return render(request, 'appTwo/result.html', context=my_dict)


def users(request):
    user_list = User.objects.all()
    user_dict = {"users": user_list}
    return render(request, 'appTwo/users.html', context=user_dict)
