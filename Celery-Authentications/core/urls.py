from django.contrib import admin
from django.urls import path
from .views import user_home,Register,Login,SchoolRegistration,SchoolLogin,ChangePassword,School,College,Login_With_Google

urlpatterns = [
    path('',user_home,name='user_home'),
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('school_registration/',SchoolRegistration.as_view(),name='school_registration'),
    path('school_login/',SchoolLogin.as_view(),name='school_login'),
    path('change_password/',ChangePassword.as_view(),name='change_password'),
    path('school/<int:school_id>',School,name='school'),
    path('college/',College.as_view(),name='college'),
    path('login_with_google/',Login_With_Google.as_view(),name='login_with_google'),
    
]
