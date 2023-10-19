from django.shortcuts import render

# Create your views here.
def viewindex(request):
    return render(request,"index.html")

def viewMain(request):
    return render(request,"main.html")