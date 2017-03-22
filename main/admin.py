from django.contrib import admin
from .models import Fundingdummy, Funding, Making, Tournament, Video, Participation, Privacy, Agreement, Help, Comment, Chat, Gamerule

# Register your models here.
class FundingdummyAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'amount', 'reward', 'comment', 'orderno', 'thanks']
admin.site.register(Fundingdummy, FundingdummyAdmin)

class FundingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'amount', 'reward', 'comment', 'orderno', 'thanks']
admin.site.register(Funding, FundingAdmin)

class MakingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name', 'tournament_game', 'tournament_url', 'starttime', 'confirm']
admin.site.register(Making, MakingAdmin)

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name', 'tournament_game', 'tournament_url', 'tournament_format', 'participation', 'participation_fee', 'funding', 'streaming', 'confirm']
admin.site.register(Tournament, TournamentAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'video_name', 'video_url']
admin.site.register(Video, VideoAdmin)

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_id', 'tournament_name', 'username', 'email', 'name', 'phone', 'etc1', 'etc2', 'etc3', 'etc4', 'etc5', 'etc6', 'confirm', 'checkin', 'score', 'result', 'prize']
admin.site.register(Participation, ParticipationAdmin)

class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
admin.site.register(Privacy, PrivacyAdmin)

class AgreementAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
admin.site.register(Agreement, AgreementAdmin)

class HelpAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'question', 'answer']
admin.site.register(Help, HelpAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name', 'username', 'content', 'date', 'depth', 'path']
admin.site.register(Comment, CommentAdmin)

class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_name', 'user', 'message', 'created']
admin.site.register(Chat, ChatAdmin)

class GameruleAdmin(admin.ModelAdmin):
    list_display = ['id', 'tournament_game', 'tournament_type']
admin.site.register(Gamerule, GameruleAdmin)
