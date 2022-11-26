from django.shortcuts import render

# Create your views here.

def a1_first(request):
    return render(request,'a1_first.html',context={'name':'a1_first'})



def a2_second(request):
    return render(request, 'a2_second.html',context={'name':'a2_second'})

