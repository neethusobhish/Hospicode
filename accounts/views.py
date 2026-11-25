from django.shortcuts import render
from django.contrib.auth import authenticate,login

# Create your views here.


def loginpage(request):
    if request.method == 'POST':
        usern = request.POST.get('usern')
        passw = request.POST.get('passw')
        user = authenticate(request,username=usern,password=passw)
        print(user)
        if user:
            login(request,user)#session
        else:
            print('no such user')
    return render(request,'accounts/login.html')
