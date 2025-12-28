from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('dash', DashboardView.as_view(), name='dash'),
    path('admin_dash', AdminDashView.as_view(), name='admin_dash'), 
    path('signup', SignupView.as_view(), name='signup'), 
]

