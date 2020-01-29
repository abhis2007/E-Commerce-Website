"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.index,name="shophome"),
    path("about",views.about,name="AboutUs"),
    path("cart",views.cart,name="Cart"),
    path("contact",views.contact,name="ContactUs"),
    path("tracker",views.tracker,name="TrackingStatus"),
    path("search",views.search,name="Search"),
    path("product/<int:myid>",views.productview,name="Product View"),
    path("checkout/<int:checkoutId>",views.checkoutPage,name="checkout Page"),
    path("billing",views.billingpage,name="checkout Page"),
    path("billingsearcher",views.billingsearcher,name="checkout Page"),
    path("contact",views.contact,name="contact"),
    path("paytmsentposturl",views.paytmsentposturl,name="paytmsentposturl"),
    path("checkout/handlepaymentmode",views.handlepaymentmode,name="handlepaymentmode")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
