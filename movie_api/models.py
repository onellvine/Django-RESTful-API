from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


DEFAULT_SYSUSERID, DEFAULT_MOVIEID = 1, 1

class SysUserManager(BaseUserManager):
    def create_user(self, phone, username, password, **other_fields):
        user = self.model(phone=phone, username=username, password=password, **other_fields)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, phone, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        super_user = self.create_user(phone, username, password, **other_fields) 

        return super_user



class SysUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=64, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=256)

    is_staff = models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)  # remember to change to False before production...for validation of user sign up

    objects = SysUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = "SysUsers"

    def __str__(self):
        return self.username


class Movie(models.Model):
    categories = (
        ('MOV', 'movie'),
        ('SER', 'series'),
    )
    title = models.CharField(max_length=128)
    cast = models.JSONField()
    category = models.CharField(max_length=3, choices=categories, default='MOV')
    comments = models.IntegerField(default=0)
    cover_photo = models.ImageField(upload_to ='uploads/')
    genre = models.JSONField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    released =models.IntegerField()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_id = models.ForeignKey(SysUser, default=DEFAULT_SYSUSERID, verbose_name="SysUser", on_delete=models.PROTECT)
    movie_id = models.ForeignKey(Movie, default=DEFAULT_MOVIEID, verbose_name="Movie", on_delete=models.PROTECT)
    comment = models.TextField()

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment[:100]

