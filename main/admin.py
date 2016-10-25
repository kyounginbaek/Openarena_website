from django.contrib import admin
from .models import Funding, Making

# Register your models here.
class FundingAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'amount']

admin.site.register(Funding, FundingAdmin)

class MakingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name']
admin.site.register(Making, MakingAdmin)
