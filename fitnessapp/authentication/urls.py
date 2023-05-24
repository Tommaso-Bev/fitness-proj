from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="handlelogin"),
]