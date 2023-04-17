from django.contrib import admin
from .models import Movies,Cast,MoviesCast

# Register your models here.
admin.site.register(Movies),
admin.site.register(Cast),
admin.site.register(MoviesCast),


