from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Charity)


admin.site.site_header = 'Charities Administration'
