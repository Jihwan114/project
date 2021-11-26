from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
import hashlib


# Create your models here.

# 사용자생성
class MyUserManager(BaseUserManager):
    def create_user(self, user_id, password, confirm_password, address, login_fail_count):
        if not user_id:
            raise ValueError('user_id is required.')

        user = self.create_user(
            user_id=user_id, 
            password=password, 
            confirm_password=confirm_password,
            address=address, 
            login_fail_count=login_fail_count
            )
        # user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_id, password):
        new_superuser = self.create_user(
            user_id=user_id,
            password=password,
            confirm_password=0,
            address=0, 
            login_fail_count=0
        )
        new_superuser.is_admin = True
        #new_superuser.is_staff = True
        print("TEST")
        new_superuser.is_active = True
        new_superuser.is_superuser = True
        new_superuser.save(using=self._db)
        return new_superuser

# 사용자클래스
class MyUser(AbstractBaseUser, PermissionsMixin):
    #Primary_key
    user_id = models.CharField(max_length=200, unique=True, primary_key=True)
    password = models.CharField(max_length=200, null=True)
    confirm_password = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    #비밀번호 실패 횟수 
    login_fail_count = models.IntegerField(default=0)
    #for admin
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []
    

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'user_id'
        verbose_name = '유저'
        verbose_name_plural = '유저'

    # def set_password(self, password):
    #     self.password = hashlib.sha256(password).hexdigest()

    @property
    def is_anonymous(self):
    #Always return False. This is a way of comparing User objects to anonymous users.
        return False
    
    @property
    def is_authenticated(self):
        # 이 함수는 기본 User model에서 사용하는 것으로, Anonymous가 아니면 로그인 된 것이므로 항상 True를 리턴
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


#Authenticate customazing
class MyUserAuth(object):
    def authenticate(self, **kwargs):
        user_id = kwargs.get('user_id')
        password = kwargs.get('password')
        try:
            user = get_user_model().objects.get(user_id = user_id)
        except:
            return None

        if user.login_fail_count >= 5:
            messages.info(request, '비밀번호 오류 횟수가 5회 초과 되었습니다.')
            return None
        
        if str(user.password) == password:
            user.login_fail_count = 0
            user.save(update_fields=['login_fail_count'])
            return user
        else:
            user.login_fail_count += 1
            user.save(update_fields =['login_fail_count'])
            return None

# #강아지 정보
# class Puppy(models.Model):
#     #이름
#     name = models.CharField(max_length=200, null=True)
#     #품종
#     kind = models.CharField(max_length=200, null=True)
#     Primary_weight = models.CharField(max_length=200, null=True)
#     gender = models.CharField(max_length=200, null=True)
#     #중성화유무
#     neutralization = models.BooleanField(default=True)
#     birth_date = models.DateTimeField (auto_now_add=True)
#     #동물ID
#     animal_id = models.CharField(max_length=200, primary_key=True)
#     user_id = models.ForeignKey(MyUser, on_delete = models.PROTECT)

#     def __str__(self):
#         return self.name

#     # def counting_age(self):
#     #     import datetime 
#         # age = (datetime.date.today() - self.birth_date) / 12

# #강아지별 몸무게
# class Puppy_Weight(models.Model):
#     #등록날짜
#     now_date = models.DateTimeField (auto_now_add=True)
#     #등록된 동물 Id
#     animal_id = models.ForeignKey(Puppy, on_delete = models.PROTECT)
#     #등록날짜기준 동물 몸무게
#     weight = models.FloatField(blank=True, default=0.0)
#     class Meta:
#         unique_together = (('now_date', 'weight'),)


#카테고리(품종, 연령별) 강아지 몸무게 
class Avg_Weight(models.Model):
    #분류된 동물 카테고리
    category_code = models.CharField(max_length=200, primary_key=True)
    #카테고리 내 최대 몸무게
    max_weight = models.FloatField(blank=True, default=0.0)
    #카테고리 내 최소 몸무게
    min_weight = models.FloatField(blank=True, default=0.0)
    #카테고리 내 평균 몸무게 
    avg_weight = models.FloatField(blank=True, default=0.0)


# 품종별, 개월수별 카테고리 분류
class Category(models.Model):
    category_code = models.ForeignKey(Avg_Weight, on_delete = models.PROTECT)
    #품종
    kind = models.CharField(max_length=200, null=True)
    #나이계산
    age = models.IntegerField(default=0)

# 건강검진일정
class Health_Check_Schedule(models.Model):
    month = models.IntegerField(default=0, primary_key=True)
    health_check_list = models.CharField(max_length=200, null=True)


# 강아지 생활Tip
class Puppy_life_Tip(models.Model):
    #기본생활
    basic_life = models.TextField()
    #놀이 및 산책 
    walk_around = models.TextField()
    #위생
    sanitary = models.TextField()
    #식생활
    food_and_etc = models.TextField()
