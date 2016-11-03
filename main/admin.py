from django.contrib import admin
from .models import Funding, Making, Reply, Video, Participation

# Register your models here.
class FundingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'amount']
admin.site.register(Funding, FundingAdmin)

class MakingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name']
admin.site.register(Making, MakingAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'comment']
admin.site.register(Reply, ReplyAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'video_name', 'video_url']
admin.site.register(Video, VideoAdmin)

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'phone', 'etc1', 'etc2']
admin.site.register(Participation, ParticipationAdmin)
