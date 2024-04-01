import re

from django.contrib import messages
from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from Users.forms import Userregister_Form
from Users.models import Userregister_Model, UserAdd_Model


def user_login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            enter = Userregister_Model.objects.get(name=name,password=password)
            request.session['name']=enter.id
            return redirect('user_mydetails')
        except:
            pass
    return render(request, 'users/user_login.html')


def user_register(request):
    if request.method == "POST":
        forms = Userregister_Form(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'You have been successfully registered')
            return redirect('user_login')
    else:
        forms = Userregister_Form()
    return render(request, 'users/user_register.html',{'form':forms})

def user_mydetails(request):
    name = request.session['name']
    ted = Userregister_Model.objects.get(id=name)
    return render(request, 'users/user_mydetails.html',{'object':ted})

def user_updatedetails(request):
    name = request.session['name']
    obj = Userregister_Model.objects.get(id=name)
    if request.method == "POST":
        UserName = request.POST.get('name', '')
        Email = request.POST.get('email', '')
        Password = request.POST.get('password', '')
        Phone_Number = request.POST.get('phoneno', '')
        Address = request.POST.get('address', '')
        Location = request.POST.get('location', '')

        obj = get_object_or_404(Userregister_Model, id=name)
        obj.name = UserName
        obj.email = Email
        obj.password = Password
        obj.phoneno = Phone_Number
        obj.address = Address
        obj.location = Location
        obj.save(update_fields=["name", "email", "password", "phoneno", "address","location"])
        return redirect('user_mydetails')


    return render(request, 'users/user_updatedetails.html',{'form':obj})


def user_search(request):
    objw = ''
    if request.method == "POST":
        usid = request.POST.get('search')
        objw = UserAdd_Model.objects.filter(Q(cname=usid) | Q(dept=usid))
    return render(request,'users/user_search.html', {'objes': objw})

def user_adddata(request):
    name = request.session["name"]
    obj = Userregister_Model.objects.get(id=name)
    attack1 = []
    attack2, attack3, attack4, attack5, attack6, attack7, attack8, attack9 = [], [], [], [], [], [], [], []

    splt = ''
    Cname = ''
    Dept = ''
    Description = ''
    Record = ''
    Method = ''
    txt =''
    ans = ''

    if request.method == "POST":
        Cname = request.POST.get("cname")
        Dept = request.POST.get("dept")
        Description = request.POST.get("description")
        txt = request.POST.get("name")
        Method = request.POST.get("method")
        Record = request.POST.get("record")





        splt = (re.findall(r"[\w']+", str(txt)))

    for f in splt:
        if f in ('IPid', 'FDDI', 'x25', 'rangingdistance'):
            attack1.append(f)
        elif f in ('tcpchecksum', 'mtcp', 'controlflags', 'tcpoffset', 'tcpport'):
            attack2.append(f)
        elif f in ('ICMPID', 'udptraffic', 'udpunicorn', 'datagramid', 'NTP', 'RIP', 'TFTP'):
            attack3.append(f)
        elif f in ('GETID', 'POSTID', 'openBSD', 'appid', 'sessionid', 'transid', 'physicalid'):
            attack4.append(f)
        elif f in ('SYN', 'ACK', 'synpacket', 'sycookies'):
            attack5.append(f)
        elif f in ('serverattack', 'serverid', 'blockbankwidth'):
            attack6.append(f)
        elif f in ('monlist', 'getmonlist', 'NTPserver'):
            attack7.append(f)
        elif f in ('portid', 'FTPID', 'tryion', 'fragflag'):
            attack8.append(f)
        elif f in ('malwareid', 'gethttpid', 'httpid'):
            attack9.append(f)

    if len(attack1) > len(attack2) and len(attack1) > len(attack3) and len(attack1) > len(attack4) and len(
            attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
        attack1) > len(attack8) and len(attack1) > len(attack9):
        ans = "Macro viruses"
    elif len(attack2) > len(attack1) and len(attack2) > len(attack3) and len(attack2) > len(attack4) and len(
            attack2) > len(attack5) and len(attack2) > len(attack6) and len(attack2) > len(attack7) and len(
        attack2) > len(attack8) and len(attack2) > len(attack9):
        ans = "File infectors"
    elif len(attack3) > len(attack2) and len(attack3) > len(attack1) and len(attack3) > len(attack4) and len(
            attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
        attack1) > len(attack8) and len(attack1) > len(attack9):
        ans = "System or boot-record infectors"
    elif len(attack4) > len(attack2) and len(attack4) > len(attack3) and len(attack4) > len(attack1) and len(
            attack4) > len(attack5) and len(attack4) > len(attack6) and len(attack4) > len(attack7) and len(
        attack4) > len(attack8) and len(attack4) > len(attack9):
        ans = "Polymorphic viruses"
    elif len(attack5) > len(attack2) and len(attack5) > len(attack3) and len(attack5) > len(attack4) and len(
            attack5) > len(attack1) and len(attack5) > len(attack6) and len(attack5) > len(attack7) and len(
        attack5) > len(attack8) and len(attack5) > len(attack9):
        ans = "Ransomware"
    elif len(attack6) > len(attack2) and len(attack6) > len(attack3) and len(attack6) > len(attack4) and len(
            attack6) > len(attack5) and len(attack6) > len(attack1) and len(attack6) > len(attack7) and len(
        attack6) > len(attack8) and len(attack6) > len(attack9):
        ans = "Logic bombs"
    elif len(attack7) > len(attack2) and len(attack7) > len(attack3) and len(attack7) > len(attack4) and len(
            attack7) > len(attack5) and len(attack7) > len(attack6) and len(attack7) > len(attack1) and len(
        attack7) > len(attack8) and len(attack7) > len(attack9):
        ans = "Worms"
    elif len(attack8) > len(attack2) and len(attack8) > len(attack3) and len(attack8) > len(attack4) and len(
            attack8) > len(attack5) and len(attack8) > len(attack6) and len(attack8) > len(attack7) and len(
        attack8) > len(attack1) and len(attack8) > len(attack9):
        ans = "Droppers"
    elif len(attack9) > len(attack2) and len(attack9) > len(attack3) and len(attack9) > len(attack4) and len(
            attack9) > len(attack5) and len(attack9) > len(attack6) and len(attack9) > len(attack7) and len(
        attack9) > len(attack8) and len(attack9) > len(attack1):
        ans = "Spyware "

    else:
        ans = "lowlevel"
    UserAdd_Model.objects.create(uregid=obj,cname=Cname,dept=Dept,description=Description,website=txt,method=Method,record=Record,attackresult=ans)


    return render(request,'users/user_adddata.html')

def higlevel(request):
    obj = UserAdd_Model.objects.filter(Q(attackresult='Macro viruses') | Q(attackresult='File infectors') | Q(
        attackresult='System or boot-record infectors') | Q(attackresult='Polymorphic viruses') | Q(
        attackresult='Ransomware') | Q(attackresult='Logic bombs') | Q(attackresult='Worms') | Q(
        attackresult='Droppers') | Q(attackresult='Spyware'))
    return render(request,'users/higlevel.html',{'object':obj})

def lowlevel(request):
    obj = UserAdd_Model.objects.filter(attackresult='lowlevel')
    return render(request,'users/lowlevel.html',{'object':obj})

def data_analysis(request):
    chart = UserAdd_Model.objects.values('attackresult','method').annotate(dcount=Count('attackresult'))
    return render(request,'users/data_analysis.html',{'objects':chart})

def chart_page(request,chart_type):
    chart = UserAdd_Model.objects.values('attackresult').annotate(dcount=Count('dept'))
    return render(request,'users/chart_page.html',{'chart_type':chart_type,'objects':chart})


def user_page(request):
    obj = UserAdd_Model.objects.all()
    return render(request,'users/user_page.html',{'object':obj})