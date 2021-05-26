from django.shortcuts import render
from . models import blog
# Create your views here.
def blogs(request):
    obj=blog.objects.all()
    return render(request,'blog.html',{'results':obj})