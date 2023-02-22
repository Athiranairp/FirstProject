from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.
def demo(request):
    # name='India'
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'res': obj1})

# #def addition(request):
#     n1=int(request.GET['num1'])
#     n2=int(request.GET['num2'])
#     res=n1+n2
#     return render(request,"result.html",{'result':res})
