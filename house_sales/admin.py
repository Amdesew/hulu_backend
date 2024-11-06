from django.contrib import admin
from house_sales.models import SellHouses, SellVilla, SellGroundPlus, SellBuildings, SellAppartment, SellCondominum, SellStudio

admin.site.register(SellHouses)
admin.site.register(SellVilla)
admin.site.register(SellGroundPlus)
admin.site.register(SellBuildings)
admin.site.register(SellAppartment)
admin.site.register(SellCondominum)
admin.site.register(SellStudio)
