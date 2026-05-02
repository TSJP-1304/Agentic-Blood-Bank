from django.contrib import admin
from .models import BloodStock, Donor

@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
    list_display = ('group', 'units', 'threshold')

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'last_donation_date', 'is_eligible')