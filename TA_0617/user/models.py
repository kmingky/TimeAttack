from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=email,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # createsuperuser 시 해당 내용만 받음
    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=200)
    fullname = models.CharField("이름", max_length=50)
    address = models.CharField("주소", max_length=256, null=False)

    user_type = models.ForeignKey("UserType", on_delete=models.SET_NULL, null=True)

    join_date = models.DateTimeField("가입일", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


# user/models.py 지원자(candidate), 채용 담당자(recruiter) 등 유저 타입을 저장할 수 있는 UserType모델을 만들고 User모델과 관계
class UserType(models.Model):
    user_type = models.CharField("구분", max_length=200)

    def __str__(self):
        return self.user_type


# user/models.py : <유저가 마지막으로 로그인한 날짜(Date)와 마지막으로 지원한날짜>를 저장할수 있는 UserLog 라는 모델
class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_login_date = models.DateField("마지막 로그인 날짜")
    last_job_apply_date = models.DateField(null=True)
