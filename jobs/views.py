from django.shortcuts import render
from .models import JobsModel

def home(request):
    jobs =JobsModel.objects.all()

    context={'jobs':jobs}
    return render(request, 'jobs/home.html', context)
