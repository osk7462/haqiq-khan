from django.contrib import admin
from .models import PriceList, OurWork, OurWorkPhoto, SlideImage

# Register your models here.
admin.site.register(PriceList)
admin.site.register(OurWork)
admin.site.register(OurWorkPhoto)
admin.site.register(SlideImage)
