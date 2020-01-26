from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Coral, User, Answer
from .utils import get_random_coral
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.


def index(request):
    template = loader.get_template('poll/index.html')

    currentcoral = get_random_coral()
    #Retrieve a random coral from the model

    context = {'currentcoral': currentcoral}
    return HttpResponse(template.render(context, request))


def vote(request):

    try:
        current_coral_id = request.POST['current_coral_id']
        user_selected_health = request.POST['submitbutton']
    except(KeyError, Coral.DoesNotExist):
        return render(request, 'poll', {
            'error_message': "There was an unexpected error saving the information.",
        })
    else:
        coral = get_object_or_404(Coral, pk=current_coral_id)
        if user_selected_health == 'Yay!':
            new_answer = Answer(coral=coral, choice='HEALTHY')
            new_answer.save()
            return HttpResponseRedirect(reverse('index'))
        elif user_selected_health == "Nay!":
            new_answer = Answer(coral=coral, choice='UNHEALTHY')
            new_answer.save()
            return HttpResponseRedirect(reverse('index'))




