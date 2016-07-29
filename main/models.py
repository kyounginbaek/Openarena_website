from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.username, self.nickname, self.email, self.when)