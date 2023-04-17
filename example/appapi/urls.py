from django.urls import path
from appapi import views

urlpatterns=[
    path('movies/', views.Movies_list.as_view()),
    path('movies/<int:id>/', views.Movies_details.as_view()),
     path('cast/', views.Cast_list.as_view()),
    path('cast/<int:id>/', views.Cast_details.as_view()),
]