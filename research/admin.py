from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


admin.site.register(Note)
admin.site.register(Photo)
admin.site.register(Experiment)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_ru')


admin.site.register(Countries, CountryAdmin)


class MonthsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'month')


admin.site.register(Months, MonthsAdmin)


#

class ProductTypesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product')


admin.site.register(ProductTypes, ProductTypesAdmin)



class PhenologyInline(admin.TabularInline):
    extra = 0
    model = PHenology


class ProductInline(admin.TabularInline):
    extra = 0
    model = Production


class ProtectionInline(admin.TabularInline):
    extra = 0
    model = Protect


@admin.register(PHenology)
class PhenologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'eggs', 'larva', 'fungus', 'mature', 'manipulation')
    search_fields = ('id', 'eggs', 'larva', 'fungus', 'mature', 'manipulation')
    ordering = ('-id',)


@admin.register(Production)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'product_hs_code')
    search_fields = ('id', 'product', 'product_hs_code')
    ordering = ('-id',)



@admin.register(Protect)
class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'agro_protect', 'bio_protect', 'chemistry_protect')
    search_fields = ('id', 'agro_protect', 'bio_protect', 'chemistry_protect')
    ordering = ('-id',)


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_latin', 'name_uzb')
    search_fields = ('id', 'name_latin', 'name_uzb')
    ordering = ('-id',)
    # inlines = PhenologyInline, ProductInline, ProtectionInline




