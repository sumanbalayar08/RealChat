from django.contrib import admin
from django.urls import path,include
from Chatter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('chat/', include('Chatter.urls')),

]
