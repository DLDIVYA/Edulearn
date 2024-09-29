from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Thinkis)
admin.site.register(Exams)
admin.site.register(Scholarship)