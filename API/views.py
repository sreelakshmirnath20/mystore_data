from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from API.models import Products

class ProductView(APIView):
    def get(self,request,*args,**kw):
        return Response(data='list all products')
    
    def post(self,request,*args,**kw):
        return Response(data='Item successfully added')

class ProductDetailView(APIView):
    def get(self,request,*args,**kw):
        return Response(data='Details of a product')
    
    def get(self,request,*args,**kw):
        return Response(data='Item successfully updated')
    
    def delete(self,request,*args,**kw):
        return Response(data='Item deleted')