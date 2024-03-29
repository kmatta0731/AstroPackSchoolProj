from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# from myapp.resources import ClothingResource
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# from import_export.formats import base_formats

class ClothingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class occasionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class EssentialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ComfortAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ElectronicAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ToiletrieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class HealthAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class AccessorieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ShoeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class GenderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ActivitiesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class OccasionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class TempAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class EquipmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(Essential, EssentialAdmin)
admin.site.register(Comfort, ComfortAdmin)
admin.site.register(Electronic, ElectronicAdmin)
admin.site.register(Toiletrie, ToiletrieAdmin)
admin.site.register(Health, HealthAdmin)
admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Accessorie, AccessorieAdmin)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Trip)
admin.site.register(TempRange, TempAdmin)
admin.site.register(Occasion, OccasionAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Generated_list)
admin.site.register(Activities, ActivitiesAdmin)