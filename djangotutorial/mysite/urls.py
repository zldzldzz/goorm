from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as account_views  # accounts 앱의 views를 불러옴

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 비밀번호 찾기 관련 URL 경로
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # 아이디 찾기 관련 URL 경로
    path('find_username/', account_views.find_username, name='find_username'),  # 아이디 찾기
]
