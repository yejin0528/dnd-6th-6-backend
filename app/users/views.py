import uuid
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    EmailAuthSerializer,
    CreateUserSerializer,
)
from .models import Profile, EmailAuth

USERS = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = USERS.objects.all()
    serializer_class = UserSerializer


class EmailAuthSet(viewsets.ModelViewSet):  # POST
    queryset = EmailAuth.objects.all()
    serializer_class = EmailAuthSerializer

    # post users/email
    def perform_create(self, serializer):
        signup_email = serializer.validated_data["signup_email"]
        code = self.__send_code(signup_email)
        serializer.save(code=code)
        return Response(data="인증코드가 전송되었습니다.", status=status.HTTP_200_OK)

    # 인증코드 전송
    def __send_code(self, email):
        code = str(uuid.uuid4())[:6]  # 초대코드
        email = EmailMessage(
            "Rountable 회원가입 인증코드",  # 제목
            "인증코드: " + code,  # 본문
            to=[email],  # 수신자 이메일
        )
        email.send()
        return code


class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = USERS.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        pw = request.data["password"]
        ck_pw = request.data["ck_password"]

        if pw == ck_pw:
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
