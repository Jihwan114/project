from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model, login
from .utils import get_plot
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'accounts/main.html')

def map(request):
    return render(request, 'accounts/kakaomap.html')

@method_decorator(csrf_exempt, name='dispatch')
def registerPage(request): 

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password') 
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        login_fail_count=0
    
        if request.POST.get('password') == request.POST.get('confirm_password'):
            user = get_user_model().objects.create_user(
                user_id=user_id, 
                password=password, 
                confirm_password=confirm_password, 
                address=address,
                login_fail_count=login_fail_count
                )
            messages.info(request, '등록이 완료되었습니다.')

            return redirect('login')
                
        messages.info(request, '비밀번호가 일치하지 않습니다.')

    return render(request, 'accounts/index.html')
    

@csrf_exempt
def loginPage(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        password = request.POST['password']
        print(1)
        user = MyUserAuth().authenticate(user_id = user_id, password = password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('main')

        else:
            messages.info(request, 'ID와 비밀번호가 일치하지 않습니다.')
            return render(request, 'accounts/login.html')

    else:
        return render(request, 'accounts/login.html')



def main_view(request):
    qs = Puppy.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x,y)
    return render(requset, 'accounts/chart.html', {'chart':chart})
