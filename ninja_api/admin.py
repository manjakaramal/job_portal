from django.contrib import admin
from .models import (
    User, Category, SubCategory, Country, State, District,
    CompanyType, Company, ItPark, Job
)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_url')
    search_fields = ('name',)
    
@admin.register(SubCategory)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'image_url')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(State)
class StateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name',)
    list_filter = ('country',)

@admin.register(District)
class DistrictModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')
    search_fields = ('name',)
    list_filter = ('state',)

@admin.register(CompanyType)
class CompanyTypeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'company_type', 'email')
    search_fields = ('name', 'email')
    list_filter = ('company_type', 'location')

@admin.register(ItPark)
class ItParkModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name',)
    list_filter = ('location',)

@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'category', 'location', 'posted', 'closing_date')
    search_fields = ('name', 'company__name', 'description')
    list_filter = ('category', 'company', 'location', 'posted', 'closing_date')
