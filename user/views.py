from django.shortcuts import render
from rest_framework.views import APIView
from .serialize import UserSerializer
from .models import User
from common.common import CommonResponse, SuccessResponse, SuccessResponseWithData, ErrorResponse
from django.contrib.auth.hashers import check_password


# Create your views here.
class Start(APIView):
    def get(self, request):
        return render(request, "main.html")



class Regist(APIView):
    def post(self, request):
        serializer = UserSerializer(request.data)
        if User.objects.filter(email=serializer.data['email']).exists():
            return ErrorResponse("이미 존재하는 이메일입니다.")
        if User.objects.filter(nickname=serializer.data['nickname']).exists():
            return ErrorResponse("이미 존재하는 닉네임입니다.")
        serializer.create(request.data)
        return SuccessResponse()



class Login(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        userEmail = User.objects.filter(email=email).first()
        if userEmail is None:
            return ErrorResponse("회원정보가 잘못되었습니다.")
        if check_password(password, userEmail.password):
            request.session['email'] = email
            return SuccessResponse()
        else:
            return ErrorResponse("회원정보가 잘못되었습니다.")