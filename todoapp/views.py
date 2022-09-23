from django.shortcuts import render , redirect
from .models import ListModel,Tasks
from .forms import ListForm

# Create your views here.

def homepage(request):
    a = ListModel.objects.all()
    data = {
        'item' : a
    }
    return render(request, "home.html" , data)

def ConfigureView(request, slug):
    a = ListModel.objects.get(slug=slug)
    if request.method == "POST":
        task = request.POST['task'].strip()
        if task != "" :
            t = Tasks(name = task , catagory = a)
            t.save()


    data = {
        'i' : a
    }
    return render(request, "configure.html" , data)

def deletelist_or_task(request,slug):
    try:
        li = ListModel.objects.get(slug = slug)
        li.delete()
        return redirect("home")
    except:
        tsk = Tasks.objects.get(slug = slug)
        tsk.delete()
        return redirect("home")

def edit_item(request,slug):
    try:
        obj = Tasks.objects.get(slug=slug)
        if request.method == "POST":
            value = request.POST.get('editeditem')
            obj.name = value
            obj.save()
            return redirect("home")

    except:
        obj = ListModel.objects.get(slug=slug)
        if request.method == "POST":
            value = request.POST.get('editeditem')
            obj.title = value
            obj.save()
            return redirect("home")

    data = {
        'item' : obj
    }

    return render(request, "editform.html" , data)


def addlist(request):
    f = ListForm()
    if request.method == "POST":
        f = ListForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("home")
    return render(request, "addlist.html", {'form' : f})
