from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    print ('**HOME**' * 50)
    return render(request, 'main/home.html')

def signIn(request):
    print ('**SIGNIN**' * 50)
    return redirect(url('logReg:login'))
