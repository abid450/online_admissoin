from django.contrib import admin
from .models import form_model
from .models import UserProfile
# Register your models here.

@admin.register(form_model)
class formAdmin(admin.ModelAdmin):
    list_display = ['username','email','phone','rollnumber','regnumber','Choise']


admin.site.register(UserProfile)