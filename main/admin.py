from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Funding, Fundingdummy, Making, Video, Participation

# Register your models here.
class FundingdummyAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'amount', 'comment', 'orderno']
admin.site.register(Fundingdummy, FundingdummyAdmin)

class FundingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'amount', 'reward', 'comment', 'orderno', 'thanks']
admin.site.register(Funding, FundingAdmin)

class MakingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name', 'tournament_game', 'tournament_url', 'starttime', 'confirm']
admin.site.register(Making, MakingAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'video_name', 'video_url']
admin.site.register(Video, VideoAdmin)

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'name', 'phone', 'etc1', 'etc2', 'etc3', 'etc4', 'confirm', 'checkin', 'score', 'result', 'prize']
admin.site.register(Participation, ParticipationAdmin)
