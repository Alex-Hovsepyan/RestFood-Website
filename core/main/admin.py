from django.contrib import admin
from .models import Header, Home, Title, About, AboutContent, Offer, Chef, Gallery, ReservationContent, OpenDays, Reservation
from .models import ContactContent, ContactInfo, Menu, Product
# Register your models here.

admin.site.register(Header)
admin.site.register(Home)
admin.site.register(Title)
admin.site.register(About)
admin.site.register(AboutContent)
admin.site.register(Offer)
admin.site.register(Chef)
admin.site.register(Gallery)
admin.site.register(ReservationContent)
admin.site.register(OpenDays)
admin.site.register(Reservation)
admin.site.register(ContactContent)
admin.site.register(ContactInfo)
admin.site.register(Menu)
admin.site.register(Product)