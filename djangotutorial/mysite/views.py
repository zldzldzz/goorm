from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings

# 아이디 찾기 뷰
def find_username(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # 이메일로 아이디 찾기
        try:
            user = User.objects.get(email=email)
            send_mail(
                'Your Username',
                f'Your username is: {user.username}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return HttpResponse('아이디가 이메일로 전송되었습니다.')
        except User.DoesNotExist:
            return HttpResponse('등록되지 않은 이메일 주소입니다.', status=404)
    
    return render(request, 'find_username.html')
