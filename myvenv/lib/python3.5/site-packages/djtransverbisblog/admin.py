from django.contrib import admin
from .models import Post, Comment, Page, ApprovedEmail

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Page)
admin.site.register(ApprovedEmail)