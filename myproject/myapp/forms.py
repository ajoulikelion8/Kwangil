# Forms.py

from django import forms
from post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post                      # 저장하기를 원하는 데이터 모델 지정
        fields = ['title','content']