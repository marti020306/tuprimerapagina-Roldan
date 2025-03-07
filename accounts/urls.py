from django.urls import path
from . import views
from .views import register, edit_profile_view, change_password_view, profile_view
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import logout_view
from django.urls import path


urlpatterns = [
    path("register/", register, name="register"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', logout_view, name='logout'),
    path('register/', views.edit_profile, name='profile'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('profile/change-password/', change_password_view, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
     
]

