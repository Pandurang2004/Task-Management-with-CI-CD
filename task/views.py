from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModels 
from .forms import TaskModelForm

# Create your views here.
def add_task(request):
    form = TaskModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read_task')
    return render(request, 'add_task.html', {'form':form})

def read_task(request):
    record = TaskModels.objects.all()
    return render(request, 'read.html', {'record':record})

def update_task(request, id):
    record= get_object_or_404(TaskModels, id=id)
    form = TaskModelForm(request.POST or None , instance=record)
    if form.is_valid():
        form.save()
        return redirect('read_task')
    return render(request, 'update.html' , {'form': form})

def delete_task(request, id):
    record = get_object_or_404(TaskModels, id=id)
    if request.method == "POST":
        record.delete()
        return redirect('read_task')
    return render(request, 'delete.html' , {'record':record})
