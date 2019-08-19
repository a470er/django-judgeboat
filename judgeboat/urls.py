from django.urls import path

from . import views

app_name = 'judgeboat' #追記

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
]