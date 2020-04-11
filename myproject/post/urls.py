from django.contrib import admin
from django.urls import path, include
import post.views

urlpatterns = [
    path('', post.views.post_list, name = 'post_list'),
]
