from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from users import views

urlpatterns = [
    path('gettoken/', obtain_auth_token),
    path('register/', views.UserRegister.as_view()),
    path('verification/', views.UserEmailVerification.as_view()),
    path('login/', views.UserLogIn.as_view()),
    path('logout/', views.UserLogout.as_view()),
]
