from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login as logins,logout
from .models import Task,List,user

from .form import user_createform
from .form import Createview,Taskview
def home(request):
    return render(request,'home.html',{})


# creating login page
# start
def home1(request):
    return render(request,'home1.html',{})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            logins(request,user)
            if user.is_superuser:
                return redirect('home')
            else:
                print('normal')
                return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not in our database'})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        fuser = user_createform(request.POST,request.FILES)
        if fuser.is_valid():
            fuser.save()
            fuser = user_createform()
    else:
            fuser = user_createform()
    return render(request,'signup.html',{'data':fuser})
    # return HttpResponse('<h1>404</h1>')



# end
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
    # print(u)
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

def checkbox2(request):
    r1=[]
    r2=[]
    for i in List.objects.all().values():
        r1.append(i['title1'])
        r2.append(i['id'])
    # print(r1)
    return render(request,'complete.html',{'data':zip(r1,r2)})

def complete(request):
    c = request.POST.getlist('data')
    for i in c:
        p = List.objects.get(id=i)
        p.status = True
        p.save()
    r1=[]
    r2=[]
    r3=[]
    for i in List.objects.all().values():
        r1.append(i['title1'])
        r3.append(i['status'])
        r2.append(i['id'])
    return render(request,'complete.html',{'data':zip(r1,r2,r3)})

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

