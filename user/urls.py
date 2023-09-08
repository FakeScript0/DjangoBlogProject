from django.contrib import admin
from django.urls import path
from . import views
app_name="user"
#buradaki appname le blogdaki urlsye include edirik
urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path("profile/",views.profile,name="profile"),

]