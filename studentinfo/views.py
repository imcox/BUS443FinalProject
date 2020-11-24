from django.shortcuts import render
from django.http import HttpResponse
from studentinfo.models import Studentdetails, Coursedetails, Enrollment, Home
from django.core.paginator import Paginator
from django.contrib.auth.decorators  import login_required

# Create your views here.

def home(request):
    studentinfo = Studentdetails.objects.all()
    coursedata = Coursedetails.objects.all()
    return render (request, "studentinfo/home.html", {'studentinfo':studentinfo, 'coursedetails':coursedata})


@login_required
def studentdetails(request):
    studentinfo=Studentdetails.objects.all()
    paginator = Paginator(studentinfo, 10)
    page = request.GET.get('page')
    studentdata = paginator.get_page(page)
    print (studentinfo)
    return render (request, "studentinfo/Studentdetails.html",{"data":studentdata})

@login_required
def coursedetails(request):
    studentinfo=Coursedetails.objects.all()
    paginator = Paginator(studentinfo, 10)
    page = request.GET.get('page')
    coursedata = paginator.get_page(page)
    print (studentinfo)
    return render (request, "studentinfo/Coursedetails.html",{"data":coursedata})
@login_required
def enroll(request):
    studentinfo = Studentdetails.objects.all()
    coursedata = Coursedetails.objects.all()
    enrolldata= ''
    if('studentid' in request.session):
        enrolldata= Enrollment.objects.filter(studentid = request.session['studentid'])
    if('nm' in request.GET and 'ctitle' not in request.GET):
        nm = request.GET.get('nm')
        request.session['studentid'] = nm
        return HttpResponse('Success')
    if('nm' in request.GET and 'ctitle' in request.GET):
        nm = request.GET.get('nm')
        ctitle = request.GET.get('ctitle')
        enrolldata = Enrollment.objects.filter(studentid = nm)
        for row in enrolldata:
            if row.coursetitle == ctitle:
                return HttpResponse('Error')
        newdata = Enrollment(studentid = nm, coursetitle = ctitle)
        newdata.save()
        return HttpResponse("Success")
    return render(request, 'studentinfo/enroll.html',{'studentinfo':studentinfo, 'coursedetails':coursedata,'enroll':enrolldata})
