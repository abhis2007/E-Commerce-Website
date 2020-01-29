from django.contrib import admin
# Register your models here.

from .models import product
admin.site.register(product)

from .models import contactdb
admin.site.register(contactdb)

from .models import orderfromwebsite
admin.site.register(orderfromwebsite)

from .models import after_payment
admin.site.register(after_payment)
