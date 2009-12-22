from django.contrib import admin
from myapp.models import User_Account

class UserAccountAdmin(admin.ModelAdmin):
    inlines = (FileInline,)
    list_display = ('first_name', 'last_name')

admin.site.register(User_Account, UserAccountAdmin)
