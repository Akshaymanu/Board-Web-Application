from . import views
from django.urls import path


urlpatterns = [
    path('', views.login_user, name='login'),
    path('register',views.reg_user, name='user_reg'),
    path('logout',views.logout_user, name='logout'),
    path('account',views.user_account, name='account'),
    path('home', views.home_pg, name='home'),
    path('room/<str:pk>/', views.room_pg, name='room'),
    path('create-room/', views.createRoom, name="create-room"),

    
    ]