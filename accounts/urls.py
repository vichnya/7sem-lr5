from django.urls import path
from django.contrib.auth.views import \
    LogoutView, logout_then_login, \
    PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from . import views

urlpatterns = [
    # post views
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', views.register, name='register'),
]