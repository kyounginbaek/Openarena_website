from django.contrib import admin
from .models import Funding, Making, Reply, Video

# Register your models here.
class FundingAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'amount']

admin.site.register(Funding, FundingAdmin)

class MakingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name']
admin.site.register(Making, MakingAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
admin.site.register(Reply, ReplyAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
admin.site.register(Video, VideoAdmin)
