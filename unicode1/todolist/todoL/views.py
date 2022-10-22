from django.shortcuts import render
# Create your views here.
from .models import Task,List
from .form import Createview,Taskview
def home(request):
    return render(request,'home.html',{})

def create(request):
    if request.method == 'GET':
        d = Createview(request.GET)
        if d.is_valid():
            d.save()
    return render(request,'create.html',{'data':d})

def task(request):
    if request.method == 'GET':
        t = Taskview(request.GET)
        if t.is_valid():
            t.save()
    return render(request,'task.html',{'data':t})

def retrive(request):
     c = [i for i in Task.objects.all()]
     return render(request,'retrive_task.html',{'data':c})

def retriveL(request,id):
    r = List.objects.filter(task_FK=(Task.objects.get(title=id))).values()
    # print(r)
    c = []
    e=0
    for i in r:
        c.append(e+1)
        e=e+1
    dc = {'dat':zip(c,r)}
    return render(request,'retriveL.html',dc)

def checkbox(request):
    r1=[]
    r2=[]
    for i in Task.objects.all().values():
        r1.append(i['title'])
        r2.append(i['id'])
    # print(r1)
    return render(request,'deleteT.html',{'data':zip(r1,r2)})

def checkbox1(request):
    r1=[]
    r2=[]
    for i in List.objects.all().values():
        r1.append(i['title'])
        r2.append(i['id'])
    # print(r1)
    return render(request,'deleteL.html',{'data':zip(r1,r2)})

def delete_task(request):
    c = request.GET.getlist('data')
    for i in c:
        List.objects.get(title1=i).delete()
    # Anyother method
    r1=[]
    r2=[]
    for i in List.objects.all().values():
        r1.append(i['title1'])
        r1.append(i['id'])
    return render(request,'deleteT.html',{'data':zip(r1,r2)})

def delete_list(request):
    c = request.GET.getlist('data')
    for i in c:
        Task.objects.get(id=i).delete()
    # Any other method ?
    r1=[]
    r2=[]
    for i in Task.objects.all().values():
        r1.append(i['title'])
        r2.append(i['id'])
    # if request.method == 'GET':
    #     d = Taskview(request.GET)
    #     if d.is_valid():
    #         d.delete()
    return render(request,'deleteL.html',{'data':zip(r1,r2)})

def radio1(request):
    r1=[]
    r2=[]
    for i in Task.objects.all().values():
        r1.append(i['title'])
        r2.append(i['id'])
    print(r1)
    return render(request,'updateL.html',{'data':zip(r1,r2)})

def update_list(request):
    c=request.GET.get('data')

    # m=Task.objects.get(title=c)

    if request.method == 'GET':
        d = Taskview(request.GET)
        if d.is_valid():
            n=d.cleaned_data['title']
            d.title=n
            d.save()

    return render(request,'updateLL.html',{'data':d})

