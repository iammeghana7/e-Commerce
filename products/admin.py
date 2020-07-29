from django.contrib import admin
from products.models import Watch,Laptop,Phone,Product
from accounts.models import Account

# Register your models here.
@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    pass
@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    pass
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductForm(admin.ModelAdmin):
    pass