from django import template
from main.models import Participation

register = template.Library()

@register.filter()
def get_username(value):
    if value is None:
        return '승자 대기중'
    else:
        participation = Participation.objects.filter(challonge_id=value).values().get()
        if participation.get('username') != '' and participation.get('username') != '-':
            return participation.get('username')
        else:
            return participation.get('dummy_username')