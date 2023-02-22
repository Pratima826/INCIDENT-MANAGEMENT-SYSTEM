from django.contrib import admin

from incident.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','email','first_name','last_name','phone_number','is_staff','is_active')

admin.site.register(User,UserAdmin)