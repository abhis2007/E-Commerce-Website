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

from .models import orderupdate
admin.site.register(orderupdate)
#
# from .models import userProfileInfo
# admin.site.register(userProfileInfo)


from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
