from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User, auth
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser,FileUploadParser
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from .serializers import UserSerializer
from django.db.models import Q
from rest_framework import status
# Create your views here.

User = get_user_model()
class Login(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):

        data = request.data
        username = data.get('username')
        print(username)
        password = data.get('password')
      
        user = authenticate(username=username,password=password)
        print(user)
        
        qs = User.objects.filter(
            Q(username__exact=username)
        ).distinct()
      
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                login(request, user)
                current_user=request.user
                print(current_user)
                user_dict = {k: getattr(user, k) for k in ['id', 'username']}
                print(user_dict) 
                # token ={
                #        'data':[user_dict['id'],user_dict['username']],
                #     }
    
                return Response({'details':  f'user succesfully loggedin {username}','token':user_dict['username']})
            return Response({'details': 'password wrong'})
        return Response({'details': 'something went wrong while logout'})

class Registration(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):

        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        qs_name = User.objects.filter(
            Q(username__iexact=username)
        )
        qs_email = User.objects.filter(
            Q(email__iexact=email)
        )
    
        if qs_name.exists():
            return Response("already user id present with this username ")
        elif qs_email.exists():
            return Response("already user id present with this  email")
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.is_active = False
            print(user)
            user.save()
        
            return Response("User Registerd Successfully")
           