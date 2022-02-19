from django.contrib import admin

# Register your models here.
from webpage.models import Contact,Password

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject','email_address','message',)
    
class PasswordGeneratorAdmin(admin.ModelAdmin):
    list_display = ('length',)
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(Password,PasswordGeneratorAdmin)