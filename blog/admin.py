from django.contrib import admin


from .models import Blogpost,Message

admin.site.register(Blogpost)
admin.site.register(Message)