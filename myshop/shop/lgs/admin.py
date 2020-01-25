from django.contrib import admin
# Register your models here.

from .models import product
admin.site.register(product)

from .models import contactdb
admin.site.register(contactdb)

from .models import orderfromwebsite
admin.site.register(orderfromwebsite)