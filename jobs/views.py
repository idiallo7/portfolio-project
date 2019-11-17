from django.shortcuts import render
from .models import JobsModel


def jobs_home(request):
    jobs =JobsModel.objects.all()

    context={'jobs':jobs}
    return render(request, 'jobs/home.html', context)


