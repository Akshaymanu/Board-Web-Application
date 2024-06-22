from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_pg, name='home'),
    path('login/', views.login_user, name='login'),
    path('register',views.reg_user, name='register'),
    path('logout',views.logout_user, name='logout'),
    path('account',views.user_account, name='account'),
    path('room/<str:pk>/', views.room_pg, name='room'),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),

    
    ]