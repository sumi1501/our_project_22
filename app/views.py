from django.shortcuts import render

# Create your views here.
from app.models import *

def dept(request):
    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)

def emp(request):
    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)
def insert_dept(request):
    dno=input('Enter the deptno')
    dna=input('Enter the dname')
    lo=input('Enter the location')

    DNO=Dept.objects.get_or_create(deptno=dno,dname=dna,loc=lo)[0]
    DNO.save()

    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)
def insert_emp(request):
    dno=input('Enter the deptno')
    eno=input('Enter the empno')
    ena=input('Enter the ename')
    jo=input('Enter the job')
    mg=input('Enter the mgr')
    em=input('Enter the email')
    hir=input('Enter the hiredate')
    sa=input('Enter the sal')
    comm=input('Enter the commision')

    NDO=Dept.objects.get(deptno=dno)
    EMO=Emp.objects.get_or_create(deptno=NDO,empno=eno,ename=ena,job=jo,MGR=mg,email=em,Hiredate=hir,sal=sa,comm=comm)[0]
    EMO.save()

    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)
