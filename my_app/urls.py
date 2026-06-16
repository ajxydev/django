from django.contrib import admin
from django.urls import include, path

from my_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login_view'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.register,name='register'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('user_home',views.user_home,name='user_home'),
    path('view_users',views.view_users,name='view_users'),
    path('view_blogs_admin',views.view_blogs_admin,name='view_blogs_admin'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('my_blogs',views.my_blogs,name='my_blogs'),
    path('edit_blog/<int:id>/',views.edit_blog,name='edit_blog'),
    path('delete_blog/<int:id>/',views.delete_blog,name='delete_blog'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password',views.reset_password,name='reset_password')
    
   
]
