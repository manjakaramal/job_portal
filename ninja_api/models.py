from contextlib import closing
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=150)
    image_url = models.CharField(max_length=550, null=True, blank=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class ManyCategory(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Keyword(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class CompanyType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=150)
    location = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    company_type = models.ForeignKey(CompanyType, on_delete=models.SET_NULL, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)
    instagram = models.CharField(max_length=150, null=True, blank=True)
    facebook = models.CharField(max_length=150, null=True, blank=True)
    google_map = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class Expirience(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    many_category = models.ManyToManyField(ManyCategory, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    keyword = models.ForeignKey(Keyword, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    expirience = models.ForeignKey(Expirience, on_delete=models.SET_NULL, null=True, blank=True)
    job_type = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email_one = models.EmailField(null=True, blank=True)
    email_two = models.EmailField(null=True, blank=True)
    email_three = models.EmailField(null=True, blank=True)
    phone_one = models.CharField(max_length=20, null=True, blank=True)
    phone_two = models.CharField(max_length=20, null=True, blank=True)
    phone_three = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    source = models.CharField(max_length=150, null=True, blank=True)
    posted = models.DateField(auto_now_add=True, null=True)
    closing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
