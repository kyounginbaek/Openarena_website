from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    password1 = models.CharField(max_length=50)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return u'%s %s %s' % (self.username, self.nickname, self.email)