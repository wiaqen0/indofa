from django.urls import path
from . import views

urlpatterns = [path("register", views.register, name = 'register'),
               path("account", views.account, name = 'account'),
               path("login", views.login, name = 'login'),
               path("logout", views.logout, name = 'logout'),
                path('register/account', views.returnhome, name='returnhome'),
               path("activate/<uidb64>/<token>",views.activate, name = 'activate')]