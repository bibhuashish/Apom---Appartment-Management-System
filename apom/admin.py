from django.contrib import admin
from .models.postmodel import Post
from .models.residentmodel import Resident

admin.site.register(Post)
admin.site.register(Resident)