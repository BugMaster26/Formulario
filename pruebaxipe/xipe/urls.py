from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('apertura/', views.apertura, name="apertura"),
    path('merma/', views.merma, name="merma"),
    path('cierre/', views.cierre, name="cierre"),
    ]