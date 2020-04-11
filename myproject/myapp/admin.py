from django.contrib import admin
from myapp.models import Lion
from post.models import Post

# Register your models here.

admin.site.register(Lion)
admin.site.register(Post)