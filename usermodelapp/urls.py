from django.urls import path
from usermodelapp import views

urlpatterns = [
    path('login',views.user_login, name='login'),
    path('logout',views.user_logout, name='logout'),
    path('mainpage',views.mainpage,name='mainpage'),
    path('user_update',views.user_update, name='user_update'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('',views.userView, name='userView')
]