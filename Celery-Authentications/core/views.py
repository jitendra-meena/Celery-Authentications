from django.shortcuts import render,redirect
from django.http import HttpResponse
from .tasks import test_celery
from django.views.generic import TemplateView
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views import View
from django.contrib import messages
from .models import SchoolManagement
from django.contrib.auth.models import User




def user_home(request):
    test_celery.delay()
    return HttpResponse("Done")




class Register(APIView):
    def post(self,request):
        serializer =  RegisterSerializer(data =request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)                
        


class SchoolRegistration(View):
    def get(self, request):
        return render(request,'school_registions.html')

    def post(self,request):
        username =  request.POST.get('username')
        password =  request.POST.get('password')
        cnf_password =  request.POST.get('cnf_password')
        school_name =  request.POST.get('school_name')
        school_code =  request.POST.get('school_code')
        address =  request.POST.get('address')
        school_type =  request.POST.get('school_type')    
        if (username!='' and username == None) or (password!='' and password == None) or (school_name!='' and school_name == None):
            messages.warning(request, f'{full_name} Please enter full detail', 'warning')
            return render(request,'school_registions.html')
        if password == cnf_password:
            if not  User.objects.filter(username =username,is_active =True).exists():
                try:
                    user = User.objects.create_user(username = username,password =password)
                    school_obj = SchoolManagement.object.create(user = user, school_name = school_name,school_code = school_code,address = address)
                    school_obj.save()
                except Exception as e:
                    print(e)                
            else:
                messages.warning(request, 'Email already taken', 'danger')
                return redirect('/school_registrations')
        else:
            messages.warning(request, 'Unmatched password !', 'danger')
            return redirect('/school_registrations')
        messages.success(request, 'Registrations Successfull', 'success')    
        return render(request,'school_registions.html',{'msg':'test'})   

class SchoolLogin(View):
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.object.filter(username =username, is_active =True).exists():
            user = authenticate(username =username, password =password)
            if user is not None:
                login(request,user)
                return redirect('/dashboard')
            return redirect('/school_login')    
        else:
            messages.warning(request, 'Unmatched password !', 'danger')
            return redirect('/school_login')


class ChangePassword(View):
    def post(self,request):
        old_pass = request.POST.get('old_pass')
        new_pass = request.POST.get('new_pass')
        cfm_pass = request.POST.get('cfm_pass')
        user_id = request.user
        user_obj = SchoolManagement.objects.get(user = user_id) 
        if user_obj.user.check_password(old_pass):
            if new_pass == cfm_pass:
                user_obj.user.set_password(new_pass)
                user_obj.user.save()
                update_session_auth_hash(request, user_obj.user)
                messages.success(request, 'Your password was successfully updated!')
            return redirect('/edit_userprofile')
        else:
            massage = messages.error(request, 'Wrong Password !')
            return redirect('/edit_userprofile',{'msg':'Wrong Password !'})


