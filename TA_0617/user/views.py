import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import UserLog, UserType, User
from django.contrib.auth.hashers import make_password


# Create your views here.
# user/views.py : rest framework의 APIView를 상속받아서 회원가입을 위한 post 메소드를 구현해보세요.
# 패스워드 해쉬는 아래 메소드 참고해서 작성할 것
class JoinView(APIView):

    permission_classes = [permissions.AllowAny]
    # 회원 가입
    def post(self, request):
        # data = json.loads(request.body)
        user_type = request.data.get("user_type", None)
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        # User.objects.create(email=email, password=password)
        usertype = UserType.objects.get(user_type=user_type)

        # passcode = make_password(password)
        # print("usertype=", end=""), print(usertype)
        # User(email=email, password=make_password(password)).save()
        User(user_type=usertype, email=email, password=make_password(password)).save()

        return Response(status=status.HTTP_200_OK)


class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response(
                {"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, user)
        now = datetime.datetime.now()
        UserLog.objects.create(
            user=user, last_login_date=now.strftime("%Y-%m-%d")
        )  # 유저 로그 생성

        return Response({"success": "로그인 성공"}, status=status.HTTP_200_OK)

    def delete(self, request):
        logout(request)
        return Response({"success": "로그아웃 성공"}, status=status.HTTP_200_OK)
