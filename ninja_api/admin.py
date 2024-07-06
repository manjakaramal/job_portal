from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Experience, User, Category, SubCategory, ManyCategory, Country, State, District, Keyword, CompanyType, Company, Job

# Register your models here.

@admin.register(User)
class CustomUserAdmin(ModelAdmin):
    list_display = ['id', 'username', 'is_superuser', 'is_staff', 'is_customer', 'is_active']

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = [field.name for field in SubCategory._meta.fields]

@admin.register(ManyCategory)
class ManyCategoryAdmin(ModelAdmin):
    list_display = [field.name for field in ManyCategory._meta.fields]

@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]

@admin.register(State)
class StateAdmin(ModelAdmin):
    list_display = [field.name for field in State._meta.fields]

@admin.register(District)
class DistrictAdmin(ModelAdmin):
    list_display = [field.name for field in District._meta.fields]

@admin.register(Keyword)
class KeywordAdmin(ModelAdmin):
    list_display = [field.name for field in Keyword._meta.fields]

@admin.register(CompanyType)
class CompanyTypeAdmin(ModelAdmin):
    list_display = [field.name for field in CompanyType._meta.fields]

@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = [field.name for field in Experience._meta.fields]

@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]

@admin.register(Job)
class JobAdmin(ModelAdmin):
    list_display = ['id', 'get_categories', 'sub_category', 'company', 'location', 'keyword', 'name', 'email_one', 'posted']

    def get_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all()])

    get_categories.short_description = 'Categories'