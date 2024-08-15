from . import views
from django.urls import path , include



from myapp import views


urlpatterns = [
    path('admin_api', views.ApiOverview, name='Admin'),
    path('', views.home_pg, name='home'),
    path('login/', views.login_user, name='login'),
    path('register',views.reg_user, name='register'),
    path('logout',views.logout_user, name='logout'),
    path('account/<str:pk>/',views.user_account, name='account'),
    path('room/<str:pk>/', views.room_pg, name='room'),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),

    
    ]