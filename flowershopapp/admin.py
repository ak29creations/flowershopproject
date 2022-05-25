from django.contrib import admin

from .models import District, Place,Flower


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
admin.site.register(District, DistrictAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['district_name', 'name']

    def district_name(self, instance):
        return instance.district.name
admin.site.register(Place, PlaceAdmin)

class FlowerAdmin(admin.ModelAdmin):
    list_display = ['district_name','place_name', 'name','price']
    list_editable = ['price']
    def district_name(self, instance):
        return instance.place.district.name
    def place_name(self, instance):
        return instance.place.name
admin.site.register(Flower, FlowerAdmin)
