from django.shortcuts import render
from .models import Test
# Create your views here.

def base(request):
    obj = Test.objects.all()
    context = {
        'obj':obj,
            }
    return render(request,'base.html', context)
