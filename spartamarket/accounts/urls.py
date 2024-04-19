from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path('test/', views.test, name="test"),
    path('profile/<str:username>/', views.profile, name="profile"),
    path('<int:user_id>/follow/', views.follow, name="follow"),
]
