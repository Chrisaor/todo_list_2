from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo_list.models import List


def index(request):
    if request.method == 'POST':
        added_item = request.POST['add_item']
        created_item = List.objects.create(item=added_item, completed=False)
        items = List.objects.all()
        context = {
            'items':items,
        }
        return render(request, 'todo_list/index.html', context)
    else:
        items = List.objects.all()
        context = {
            'items':items,
        }
        return render(request, 'todo_list/index.html', context)

def detail(request, item_id):
    item = List.objects.get(id=item_id)
    context = {
        'item':item,
    }
    return render(request, 'todo_list/detail.html', context)

def crossoff(request, item_id):
    item = List.objects.get(id=item_id)
    item.completed = True
    item.save()
    return redirect('detail', item_id)

def uncross(request, item_id):
    item = List.objects.get(id=item_id)
    item.completed = False
    item.save()
    return redirect('detail', item_id)

def crossoff_index(request, item_id):
    item = List.objects.get(id=item_id)
    item.completed = True
    item.save()
    return redirect('index')

def uncross_index(request, item_id):
    item = List.objects.get(id=item_id)
    item.completed = False
    item.save()
    return redirect('index')

def about(request):
    return render(request, 'todo_list/about.html')

def delete(request, item_id):
    item = List.objects.get(id=item_id)
    item.delete()
    return redirect('index')

def edit(request, item_id):
    if request.method == 'POST':
        item_title = request.POST['item']
        item = List.objects.get(id=item_id)
        item.item = item_title
        item.save()
        return redirect('detail', item_id)
    else:
        item = List.objects.get(id=item_id)
        context = {
            'item':item,
        }
        return render(request, 'todo_list/edit.html', context)
