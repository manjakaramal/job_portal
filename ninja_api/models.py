from contextlib import closing
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class CompanyType(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=500, unique=True)
    location = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company_type = models.ForeignKey(CompanyType, on_delete=models.SET_NULL, null=True, blank=True)
    website = models.URLField(max_length=500, null=True, blank=True)
    instagram = models.URLField(max_length=500, null=True, blank=True)
    facebook = models.URLField(max_length=500, null=True, blank=True)
    google_map = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class ItPark(models.Model):
    name = models.CharField(max_length=500)
    location = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        location_name = self.location.name if self.location else "No Location"
        return f"{self.name} - {location_name}"

class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sub_category = models.ManyToManyField(SubCategory, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    itpark = models.ForeignKey(ItPark, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=500)
    location = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    min_years_experience = models.PositiveIntegerField(null=True, blank=True)
    max_years_experience = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='jobs', null=True, blank=True)
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    posted = models.DateField(auto_now_add=True, null=True)
    closing_date = models.DateField(null=True, blank=True)
    source = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
