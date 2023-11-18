from django.contrib import admin
from .models import Course, Prompt, Keyword

admin.site.register(Course)
admin.site.register(Prompt)
admin.site.register(Keyword)