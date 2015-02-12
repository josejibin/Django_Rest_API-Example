from django.http import HttpRequest
from django.contrib.auth import login, logout
from django.conf import settings

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView

from forms import SignupForm
from rest_example.models import MyUser
from serializers import (TokenSerializer, UserDetailsSerializer,
    LoginSerializer)

class Register(APIView):
    
    permission_classes = (AllowAny,)
    user_serializer_class = UserDetailsSerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def form_valid(self, form):

        self.user = form.save(self.request)
        if isinstance(self.request, HttpRequest):
            request = self.request
        else:
            request = self.request._request
      
    def post(self, request, *args, **kwargs):
        
        self.initial = {}
        self.request.POST = self.request.DATA.copy()
        form = SignupForm(request.POST)
        if form.is_valid():
            self.form_valid(form)
            return self.get_response()
        else:
            return self.get_response_with_errors()

    def get_response(self):

        serializer = self.user_serializer_class(instance=self.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_response_with_errors(self):

        return Response(self.form.errors, status=status.HTTP_400_BAD_REQUEST)



class Login(GenericAPIView):
   
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = Token
    response_serializer = TokenSerializer

    def login(self):
        
        self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(user=self.user)

    def get_response(self):
        
        return Response(self.response_serializer(self.token).data,
            status=status.HTTP_200_OK)

    def get_error_response(self):
        
        return Response(self.serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        
        self.serializer = self.get_serializer(data=self.request.DATA)
        if not self.serializer.is_valid():
            return self.get_error_response()
        self.login()
        return self.get_response()


class UserList(generics.ListAPIView):

    queryset = MyUser.objects.all()
    serializer_class = UserDetailsSerializer


class UserDetail(generics.RetrieveAPIView):
	
    queryset = MyUser.objects.all()
    serializer_class = UserDetailsSerializer