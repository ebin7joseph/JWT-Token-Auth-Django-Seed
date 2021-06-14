from django.conf.urls import url
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserView, UserProfileView

urlpatterns = [
    path("signup", UserRegistrationView.as_view()),
    path("signin", UserLoginView.as_view()),
    path("profile", UserProfileView.as_view()),
]
