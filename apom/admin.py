from django.contrib import admin
from .models.postmodel import Post
from .models.residentmodel import Resident
from .models.pollmodel import Poll
from .models.pollrecordmodel import Pollrecord

admin.site.register(Post)
admin.site.register(Resident)
admin.site.register(Poll)
admin.site.register(Pollrecord)