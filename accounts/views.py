from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'index2.html')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')

    else:
        return render(request, 'login.html')




def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                #print('Username taken')
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                #print('email taken')
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                print('user created') 
                #return redirect('/')
                return redirect('login')     

        else:
            #print('password not matching')
            messages.info(request, 'password not matching')
            return redirect('register')  

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index1.html')