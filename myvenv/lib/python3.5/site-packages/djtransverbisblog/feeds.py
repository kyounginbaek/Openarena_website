from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "Transverbis blog"
    link = "/"
    description = "Transverbis updates"

    def items(self):
        return Post.objects.filter(published_date__isnull=False).order_by('-published_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog:post_detail', args=[item.pk])