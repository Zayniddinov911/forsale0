from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addData),
    path('detail/<str:pk>/', views.getDetail)

]

