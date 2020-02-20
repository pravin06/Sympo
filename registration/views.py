from django.shortcuts import render,get_object_or_404,reverse
from django.http  import HttpResponse,HttpResponseRedirect
# Create your views here.
from registration.models import StudentsDetails
from  .models import  Student,StudentsDetails
def index(request):
    alluser  = Student.objects.all();
    alldats = StudentsDetails.objects.all()
    context = {
        'mydata':"pravin",
        'alluser':alluser,
        'single':alldats
    }

    return render(request,"index.html",context)
def details(request,request_id):
    #data = get_object_or_404(StudentsDetails,id=request_id)
   # single = StudentsDetails.objects.get(student__id=request_id)
    data = get_object_or_404(Student, pk=request_id)
    context = {
        'questions': data

    }
    return render(request, 'details.html', context)
def register(request):
    name = request.POST['name']
    mobile = request.POST['mobile']
    email = request.POST['email']
    address = request.POST['address']
    pincode = request.POST['pincode']
    s=  Student();
    s.name=name
    s.mobile=mobile
    s.email=email
    s.save();
    sd = StudentsDetails()
    sd.address=address
    sd.pincode=pincode
    sd.student =  s
    sd.save()

    return  HttpResponseRedirect(reverse('registration:index'))
def loginuser(request):
    return render(request, "login.html")
def dashboard(request):
    data = request.session['mobile']
    alldata = {
        "session": data
    }
    if 'mobile' in request.session:

        return render(request, "dashboard.html", alldata)
    else:
        return HttpResponse("<h1> please loggin first</h1>");

def login(request):
    mobile = request.POST['mobile']
    email = request.POST['email']
    try:
        single = Student.objects.get(mobile=mobile,email=email)
        request.session["name"] = single.name
        request.session["mobile"] = single.mobile
        return HttpResponseRedirect(reverse('registration:dashboard'))
    except:


        return HttpResponseRedirect(reverse('registration:loginuser'))