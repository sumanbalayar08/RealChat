from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Message, User, Session
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils import timezone


@login_required(login_url='login')
def chat_home(request):
    # Get all active sessions
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    # Extract user ids from active sessions
    active_user_ids = [session.get_decoded().get('_auth_user_id')
                       for session in active_sessions]
    # Get users associated with active sessions
    online_users = User.objects.filter(
        id__in=active_user_ids).exclude(username=request.user.username)
    return render(request, 'chat_home.html', {'connected_users': online_users})


@login_required
def chat_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        return redirect('chat_home')

    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(
        sender=user, receiver=request.user)
    messages = messages.order_by('timestamp')

    return render(request, 'chat.html', {
        'user': user,
        'messages': messages,
    })


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            # Redirect to chat_home instead of 'chat/'
            return redirect('chat_home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    user = request.user
    if user.is_authenticated:
        # Delete the user session
        request.session.delete()

        # Send the logout message to the group
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "online_users",  # Group name
            {
                "type": "user_logout",
                "user_id": user.id,
                "username": user.username,
            },
        )
        logout(request)
    return redirect('login')
