from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from Users.models import UserAdd_Model


def admin_login(request):
    if request.method =="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name=='admin' and password == 'admin':
            return redirect('user_details')
    return render(request, 'admin/admin_login.html')


def graph_analysis(request,aachart_page):
    chart = UserAdd_Model.objects.values('attackresult').annotate(dcount=Count('attackresult'))
    return render(request,'admin/achart_page.html',{'qqqchart_type':aachart_page,'objects':chart})

def admin_analysis(request):
    chart = UserAdd_Model.objects.values('attackresult','method').annotate(dcount=Count('attackresult'))
    return render(request,'admin/admin_analysis.html',{'objects':chart})

def user_details(request):
    obj = UserAdd_Model.objects.all()
    return render(request,'admin/user_details.html',{'object':obj})

