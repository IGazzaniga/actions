from django.contrib import admin

from .models import Branch, Dealer, Item, Product, Sell, SellDetail, Service

# Register your models here.


class BranchAdmin(admin.ModelAdmin):
    model = Branch


class DealerAdmin(admin.ModelAdmin):
    model = Dealer


class ItemAdmin(admin.ModelAdmin):
    model = Item


class ProductAdmin(admin.ModelAdmin):
    model = Product


class ServiceAdmin(admin.ModelAdmin):
    model = Service


class SellAdmin(admin.ModelAdmin):
    model = Sell


class SellDetailAdmin(admin.ModelAdmin):
    model = SellDetail


admin.site.register(Branch, BranchAdmin)
admin.site.register(Dealer, DealerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Sell, SellAdmin)
admin.site.register(SellDetail, SellDetailAdmin)
