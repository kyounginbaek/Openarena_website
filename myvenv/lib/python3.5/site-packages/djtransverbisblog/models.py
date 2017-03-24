from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible  # only if you need to support Python 2
class Comment(models.Model):
    post = models.ForeignKey('djtransverbisblog.Post',
                             related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    email_address = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


@python_2_unicode_compatible  # only if you need to support Python 2
class Page(models.Model):
    title = models.CharField(max_length=200)
    en_content = models.TextField()
    page_order = models.IntegerField()
    sidebar = models.BooleanField(default=False)

    def __str__(self):
        return self.title


@python_2_unicode_compatible  # only if you need to support Python 2
class ApprovedEmail(models.Model):
    email_address = models.EmailField()

    def __str__(self):
        return self.email_address
