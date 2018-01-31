from django.db import models
import bcrypt


# Create your models here.

class UserManager(models.Manager):
    def regUser(self, postData):
        status = {'valid': True, 'errors': [], 'user': None}
        if not postData['first_name'] or len(postData['first_name']) < 2:
            status['valid'] = False
            status['errors'].append('Invalid')
        if not postData['last_name'] or len(postData['last_name']) < 2:
            status['valid'] = False
            status['errors'].append('Invalid')
        if not postData['username'] or len(postData['username']) < 2:
            status['valid'] = False
            status['errors'].append('Invalid')
        if not postData['email'] or re.match('r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"'):
            status['valid'] = False
            status['errors'].append('Invalid Email')
        if not postData['password'] or len(postData['password']) < 8:
            


class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()
