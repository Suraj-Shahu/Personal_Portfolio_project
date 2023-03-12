from django.urls import path
from . import views

app_name='content'
urlpatterns = [
    path('',views.hello,name='hello'),
    path('<int:blog_id>/',views.details,name='details'),


]