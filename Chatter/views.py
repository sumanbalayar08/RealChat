from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Message,User


# Create your views here.
@login_required(login_url='login')
def chat_home(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat_home.html', {'connected_users': users})

@login_required
def chat_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        return redirect('chat_home')

    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    messages = messages.order_by('timestamp')
    
    return render(request, 'chat.html', {
        'user': user,
        'messages': messages,
    })

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('chat_home')  # Redirect to chat_home instead of 'chat/'
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')