from django.urls import path
import post.views

urlpatterns = [
    path('', post.views.post_list, name = 'post_list'),
]
