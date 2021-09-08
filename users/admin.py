from django.contrib import admin
from .models import  OTP, UserProfile

# Register your models here.


class OTPAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', 'user_id', 'valid_upto']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'is_valid']


admin.site.register(OTP, OTPAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
