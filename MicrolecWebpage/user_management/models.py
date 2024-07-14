from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import hashlib
import os

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('No se ha ingresado un email.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    names = models.CharField(max_length=255)
    lnames = models.CharField(max_length=255)
    run = models.CharField(max_length=255, unique=True)
    salt = models.CharField(max_length=32, blank=True)
    password_hash = models.CharField(max_length=64, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        if not self.salt:
            self.salt = self.generate_salt()
        super(User, self).save(*args, **kwargs)

    def generate_salt(self):
        return os.urandom(16).hex()

    def set_password(self, raw_password):
        self.salt = self.generate_salt()
        self.password_hash = hashlib.sha256((self.salt + raw_password).encode()).hexdigest()
    
    def check_password(self, raw_password):
        return self.password_hash == hashlib.sha256((self.salt + raw_password).encode()).hexdigest()

