from .models import Coral
from django.db.models import Max
from random import randint


#https://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html
def get_random_coral():
        max_id = Coral.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = randint(1, max_id)
            category = Coral.objects.filter(pk=pk).first()
            if category:
               return category