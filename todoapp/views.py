from django.shortcuts import render , redirect
from .models import ListModel,Tasks
from .forms import ListForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    a = ListModel.objects.all()
    data = {
        'item' : a
    }
    return render(request, "home.html" , data)

@login_required(login_url='admin')
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

@login_required(login_url='login')
def deletelist_or_task(request,slug):
    try:
        li = ListModel.objects.get(slug = slug)
        li.delete()
        return redirect("home")
    except:
        tsk = Tasks.objects.get(slug = slug)
        tsk.delete()
        return redirect("home")

@login_required(login_url='login')
def edit_item(request,slug):
    try:
        obj = Tasks.objects.get(slug=slug)
        if request.method == "POST":
            value = request.POST.get('editeditem')
            obj.name = value
            obj.save()

    except:
        obj = ListModel.objects.get(slug=slug)
        if request.method == "POST":
            value = request.POST.get('editeditem')
            obj.title = value
            obj.save()

    data = {
        'item' : obj
    }

    return render(request, "editform.html" , data)

@login_required(login_url='login')
def addlist(request):
    f = ListForm()
    if request.method == "POST":
        f = ListForm(request.POST)
        if f.is_valid():
            f.save()
    return render(request, "addlist.html", {'form' : f})


def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username , password = password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request, "wrong credentials!")

    return render(request, "login.html")
