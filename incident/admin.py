from django.contrib import admin

from incident.models import User,IncidentDetails


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','email','first_name','last_name','phone_number','is_staff','is_active')

admin.site.register(User,UserAdmin)

class IncidentDetailsAdmin(admin.ModelAdmin):
    list_display=('id',
            'incident_number',
            'reporter_name',
            'reported_date',
            'incident_details',
            'priority',
            'incident_status',
            'created_at',
            'updated_at',
        )
admin.site.register(IncidentDetails,IncidentDetailsAdmin)