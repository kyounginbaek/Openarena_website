from urllib.request import urlopen

from django.core.files.base import ContentFile
# from social.utils import slugify

USER_FIELDS = ['email', 'username']

def create_user(strategy, details, user=None, *args, **kwargs):
    print(details)
    print(kwargs)
    if user:
        return {'is_new': False}
    fields = {'email': details.get('email'), 'username': details.get('username')}

    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }