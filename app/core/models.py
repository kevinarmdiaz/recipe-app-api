from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
class UserManager(BaseUserManager):
    """Create and saves a new user"""

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email = self.normalize_email(email), **extra_fields)
        if not email:
            raise ValueError('user must have an email address')
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password):
        """Create and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    """ Custom user models that supports using email instead username"""
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
    )

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """Ingredient to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
     user = models.ForeignKey(
             settings.AUTH_USER_MODEL,
             on_delete= models.CASCADE,
     )
     title = models.CharField(max_length=255)
     time_minutes = models.IntegerField()
     price = models.DecimalField(max_digits=5, decimal_places=2)
     link = models.CharField(max_length=255, blank=True)
     ingredients = models.ManyToManyField('Ingredient')

     def __str__(self):
        return self.title
