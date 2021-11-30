from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from dog.models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/main.html')

def map(request):
    return render(request, 'accounts/kakaomap.html')


####회원가입 페이지####
@method_decorator(csrf_exempt, name='dispatch')
def registerPage(request): 

    #input data
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password') 
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        login_fail_count=0

        #필수 입력항목 4가지가 입력되지 않았을 경우
        if not user_id or not password or not confirm_password or not address:
            messages.info(request, '필수항목을 모두 입력하지 않았습니다. ')
            return render(request, 'accounts/index.html')
            

        input_user_id = user_id


        #아이디 중복 검증
        for_verified_user = MyUser.objects.filter(user_id=input_user_id)
        #for_verified_user가 빈 객체면 사용가능한 ID
        if len(for_verified_user) == 0:
            pass
        else:
            #아이디 중복 메세지
            messages.info(request, '이미 등록된 아이디 입니다.')
            return render(request, 'accounts/index.html')

    
        #사용자 객체 생성
        if request.POST.get('password') == request.POST.get('confirm_password'):
            try:
                user = get_user_model().objects.create_user(
                    user_id=user_id, 
                    password=password, 
                    confirm_password=confirm_password, 
                    address=address,
                    login_fail_count=login_fail_count
                    )
                #사용자 등록 알림 메세지
                messages.info(request, '사용자 등록이 완료되었습니다.')
                return redirect('login')
            except:
                return redirect('login')

        #비밀번호 불일치한 경우 알림메세지         
        messages.info(request, '비밀번호가 일치하지 않습니다.')

    return render(request, 'accounts/index.html')
    

@csrf_exempt
def loginPage(request):  
    if request.method == "POST":
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = MyUserAuth().authenticate(user_id = user_id, password = password)
        print("TEST1")
        #user 검증
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            queryset = Puppy.objects.filter(user_id_id=user_id)
            #로그인할 때 강아지 등록 할 건지 사용자 선택 사항 
            if len(queryset)!= 0:
                return redirect('home')
            else :
                return redirect('dogregister')

        else:
            print("TEST2")
            messages.info(request, 'ID와 비밀번호가 일치하지 않습니다.')
            return render(request, 'accounts/login.html')

    else:
        return render(request, 'accounts/login.html')


#logout
def logout(request): 
    auth.logout(request)
    return redirect('home')


