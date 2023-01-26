from django.shortcuts import render,HttpResponse,redirect
from home import models

#creating view
def home(request):
    #return HttpResponse("this is page")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        #print(name,email,password)
        ins = models.home(name=name, email=email, number=number, message=message)
        ins.save()
    return render(request,'home.html')

def admin(request):
    return render(request, 'admin.html')

def rdriver(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        cnic = request.POST['cnic']
        email = request.POST['email']
        workarea = request.POST['workarea']
        cardn = request.POST['cardn']
        cvc = request.POST['cvc']
        expm = request.POST['expm']
        expy = request.POST['expy']
        ins=models.driver(fullname=fullname, cnic=cnic, email=email, workarea=workarea, cardn=cardn, cvc=cvc, expm=expm, expy=expy)
        ins.save()
    return render(request, 'rdriver.html')

def rtruck(request):
    if request.method =='POST':
        truckc=request.POST['truckc']
        truckt=request.POST['truckt']
        truckn=request.POST['truckn']
        ins=models.truck(truckc=truckc, truckt=truckt, truckn=truckn)
        ins.save()

    return render(request, 'rtruck.html')

def driver(request):

    return render(request, 'driver.html')

def customer(request):

    return render(request, 'customer.html')

def vorders(request):
    all=models.order.objects.all()
    print(all)
    context={'orders': all}
    return render(request, 'vorders.html', context)

u=models.truck.objects.all()
i=[]
r=[]
p=[]
for item in u:
    v=item.truckc
    i.append(v)
    m=item.truckt
    r.append(m)
    h=item.truckn
    p.append(h)
#print(i)
#print(r)
#print(p)

def otruck(request):
    context ={'success':False}
    if request.method =='POST':
        truckc=request.POST['truckc']
        truckt=request.POST['truckt']
        truckn=request.POST['truckn']
        #print(i)
        #print(r)
        #print(p)
        #print(truckc,truckt,truckn)
        if truckc in i and truckt in r and truckn in p: 
            context = {'success': True}
            ins=models.order(truckc=truckc, truckt=truckt, truckn=truckn)
            ins.save()
        else:
            print("failed to find a truck")
    return render(request,'otruck.html', context)
        #name = request.POST['name']
        #email = request.POST['email']
        #password = request.POST['password']
        #login_type = request.POST['type']
        #print(name,email,password)
        #ins = models.login(name=name, email=email, password=password, type=login_type)
        #ins.save()
        
    #all = models.login.objects.all()
    #for item in all:
        #print(item.email)
        #print(item.password)
        #print(item.type)


def login(request):
    context ={'success':False}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        login_type = request.POST['type']
        #print(name,email,password)
        ins = models.login(name=name, email=email, password=password, type=login_type)
        ins.save()
        context = {'success': True}
    #all = models.login.objects.all()
    #for item in all:
        #print(item.email)
        #print(item.password)
        #print(item.type)
    return render(request,'login.html', context)

d = models.login.objects.all()
#print(d)
s=[]
w=[]
y=[]
for item in d:
    f=item.email
    s.append(f)
    g=item.password
    w.append(g)
    e=item.type
    y.append(e)
#print(s)
#print(w)
#print(y)
#ab=[]


def login1(request):
    if request.method == 'POST':
        a = request.POST['user']
        b = request.POST['pass']
        c = request.POST['typs']
        if a in s and b in w and c in y:
            if c=="admin":
                return redirect(admin)
            elif c=="customer":
                return redirect(customer)
            elif c=="driver":
                return redirect(driver)
            else:
                print('wrong cridentials')
        else:
            print("login failed")

     
    return render(request,'login1.html')

def feedback(request):
    allf=models.home.objects.all()
    context={'feedback': allf}
    return render(request, 'feedback.html', context)

def cusrating(request):
    if request.method == 'POST':
        username = request.POST['username']
        dname = request.POST['dname']
        rating = request.POST['rating']
        ins= models.rating(username=username, dname=dname, rating=rating)
        ins.save()
    return render(request, 'cusrating.html')

def vrating(request):
    allr=models.rating.objects.all()
    context={'rating': allr}
    return render(request, 'vrating.html', context)

def pop(request):
    return render(request, 'pop.html')

def ordersh(request):
    all=models.order.objects.all()
    print(all)
    context={'orders': all}
    return render(request,'ordersh.html', context)

def otruckpop(request):
    return render(request, 'otruckpop.html')