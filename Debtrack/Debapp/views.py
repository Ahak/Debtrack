from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request, 'index.html')
    
    def post(self, request):
        username = request.POST['username']
        password =request.POST['password']
        user = authenticate(username=username, password= password)

        if user:
            login(request, user)
            if user.is_staff:
                messages.success(request, 'login success')
                return redirect('admin_dash')
            else  :
                messages.success(request, 'login success')
                return redirect('dash')
            
        else:
            messages.error(request, 'invalid username or password')  
            return render(request, 'index.html')
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class DashboardView(View, LoginRequiredMixin):
    login_url = 'login'

    def get(self, request):
        if request.user.is_staff:
            return redirect('admin')
        return render(request, 'dashboard.html')
    
class AdminDashView(View, LoginRequiredMixin):
    login_url = 'login'
    def get(self ,request):
        if not request.user.is_staff:
            return redirect('dash')
        return render(request, 'admin.html')
    
    
class SignupView(View):
    def get(self, request):
        return render(request, 'Signup.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'Signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'Signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return render(request, 'Signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, phone=phone)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')
        
class DebtorsView(View, LoginRequiredMixin):
    login_url = 'login'

    def get(self, request):
        return render(request, 'debts.html')
