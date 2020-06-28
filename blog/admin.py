from django.contrib import admin


from .models import Blogpost,Phone,New

admin.site.register(Blogpost)

admin.site.register(Phone)
admin.site.register(New)