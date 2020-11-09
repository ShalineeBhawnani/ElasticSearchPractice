from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from .models import Category,Subcategory,Product
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import status
from rest_framework.status import (HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND)
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect

class CategoryView(generics.GenericAPIView):

    category = Category.objects.all()
    category = Category.objects.filter().order_by('name')
    print("new",category)
    subcategories = Subcategory.objects.all()
    def get(self, request, *args, **kwargs):
        category_list = self.category.filter()
        subcategories_list = Subcategory.objects.filter()
        context_dict = {'category_list': category_list, 'subcategories_list':subcategories_list} 
        return Response(category_list.values(),status=status.HTTP_200_OK)

class SubCategoryView(generics.GenericAPIView):

    category = Category.objects.all()
    print(" cat category",category)
    
    subcategories = Subcategory.objects.all()
    print(subcategories)
    def get(self,request,pk):
        category = Category.objects.get(id=pk)
        print(category)
        subcategories_list = Subcategory.objects.filter(category=category)
        return Response(subcategories_list.values(),status=status.HTTP_200_OK)

class ProductView(generics.GenericAPIView):

    # queryset = Product.objects.all()
    # serializer_class = ProductSerializer

    def get(self, request,id=None):
        if id:
            productList = Product.objects.all().filter(category=Subcategory.objects.get(id=id)) 
        else:
            productList = Product.objects.all().order_by('-id')[:5] 
        return Response(productList.values(), status=status.HTTP_200_OK)
  