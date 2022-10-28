from django.shortcuts import render,redirect
# Create your views here.
from .models import Task,List
from .form import Createview,Taskview
def home(request):
    return render(request,'home.html',{})

def create(request):
    # d=Createview()
    # if request.method == 'POST':
    # d = Createview(request.POST)
    d = Createview(request.POST or None)
    if d.is_valid():
            d.save()
            d = Createview()
    return render(request,'create.html',{'data':d})

def task(request):
    if request.method == 'GET':
        t = Taskview(request.GET)
        if t.is_valid():
            t.save()
            t=Taskview()
            return redirect('create')
    return render(request,'task.html',{'data':t})

def retrive(request):
     c = [i for i in Task.objects.all().values()]
     print(c)
     # print(c)
     return render(request,'retrive_task.html',{'data':c})

def retriveL(request,id):
    r = List.objects.filter(task_FK=(Task.objects.get(id=id))).values()
    # print(r)
    u = [i for i in List.objects.all().values()]
    c = []
    e=0
    for i in r:
        c.append(e+1)
        e=e+1
    dc = {'dat':zip(c,r,u),'id':id}
    # print(id)
    return render(request,'retriveL.html',dc)

def checkbox(request):
    r1=[]
    r2=[]
    for i in List.objects.all().values():
        r1.append(i['title1'])
        r2.append(i['id'])
    # print(r1)
    return render(request,'deleteT.html',{'data':zip(r1,r2)})

def delete_task(request):
    c = request.GET.getlist('data')
    for i in c:
        List.objects.get(id=i).delete()

    r1=[]
    r2=[]
    for i in List.objects.all().values():
        r1.append(i['title1'])
        r2.append(i['id'])
    return render(request,'deleteT.html',{'data':zip(r1,r2)})

def checkbox1(request):
    r1=[]
    r2=[]
    for i in Task.objects.all().values():
        r1.append(i['title'])
        r2.append(i['id'])
    # print(r1)
    return render(request,'deleteL.html',{'data':zip(r1,r2)})

def delete_list(request):
    c = request.GET.getlist('data')
    for i in c:
        # print(i)
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

def update_list(request,id1):

        u = Task.objects.get(id=id1)
        t = Taskview(request.POST or None,instance=u)
        if t.is_valid():
            t.save()
            return redirect('retrive')
        return render(request,'update1.html',{'data':t})


def update_task(request, id2,id3):
    u = List.objects.get(id=id2)
    print(u)
    v = Task.objects.get(id=id3)
    # print(v)
    t = Createview(request.POST or None, instance=u)
    if t.is_valid():
        t.save()
        return redirect('retriveL',v.id)
    return render(request, 'update2.html', {'data': t})
# def radio1(request):
#     r1=[]
#     r2=[]
#     for i in Task.objects.all().values():
#         r1.append(i['title'])
#         r2.append(i['id'])
#     print(r1)
#     return render(request,'updateL.html',{'data':zip(r1,r2)})

# def update_list(request,id1):
#
#     u = Task.objects.get(id=id1)
#
#     if request.method == 'GET':
#         t = Taskview(request.GET,instance=u)
#         print(t)
#         print(t.errors)
#         print('hi')
#         if t.is_valid():
#              u.save()
#              print('hi!')
#              return redirect('radio1')
#         else:
#             d = Taskview(instance=u)
#             return render(request, 'updateLL.html', {'data': d})

