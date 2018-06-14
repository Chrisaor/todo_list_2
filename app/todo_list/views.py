from django.http import HttpResponse
from django.shortcuts import render

from todo_list.models import List


def index(request):
    items = List.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'todo_list/index.html', context)

