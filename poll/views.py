from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Coral, User
from .utils import get_random_coral


# Create your views here.


def index(request):
    template = loader.get_template('poll/index.html')

    currentcoral = get_random_coral()
    #Retrieve a random coral from the model

    print(currentcoral)
    context = {}
    return HttpResponse(template.render(context, request))
