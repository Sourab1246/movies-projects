from django.shortcuts import render
from django.http import JsonResponse
from appapi.models import Movies,MoviesCast,Cast
from appapi.serializers import MoviesSerializer,MoviesCastSerializer,CastSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class Movies_list(APIView):
    def get(self,request):
        movies=Movies.objects.all()
        serializer=MoviesSerializer(movies,many=True)
        return JsonResponse(serializer.data)
    
    def post(self,request):
        serializer=MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
class Movies_details(APIView):
    def get_object(self,id):
        try:
            return Movies.objects.get(id=id)
        except  Movies.DoesNotExist:
            return JsonResponse(status=404)
    def get(self,request,id):
        movies=self.get_object(id) 
        serializer=MoviesSerializer(movies)
        return JsonResponse(serializer.data)
    def put(self,request,id):
        movies=self.get_object(id)   
        serializer=MoviesSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        movies=self.get_object(id)
        movies.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    
class Cast_list(APIView):
     def get(self,request):
        cast=Cast.objects.all()
        serializer=CastSerializer(cast,many=True)
        return JsonResponse(serializer.data)
    
class Cast_details(APIView):
    def get_object(self,id):
        try:
         return Cast.objects.get(id=id)
        except  Cast.DoesNotExist:
          return JsonResponse(status=404) 
    def get(self,request,id):
        cast=self.get_object(id)
        serializer=CastSerializer(cast)
        return JsonResponse(serializer.data)
          
    
           
    
        


