from djtransverbisblog.models import Page, Comment
from django.conf import settings


def base_variables(request):
    return {'tvblog_pages': Page.objects.filter(sidebar=False).order_by('page_order'),
            'tvblog_sidebar': Page.objects.filter(sidebar=True).first(),
            'tvblog_newcomms': len(Comment.objects.filter(approved_comment=False)),
            'website_name': settings.WEBSITE_NAME,
            'website_slogan': settings.WEBSITE_SLOGAN}
