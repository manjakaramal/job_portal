from ninja import ModelSchema
from .models import Category, Expirience, SubCategory, ManyCategory, Country, State, District, Keyword, CompanyType, Company, Expirience, Job
from typing import List, Optional

class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']

class SubCategorySchema(ModelSchema):
    category: Optional[CategorySchema]

    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name']

class ManyCategorySchema(ModelSchema):
    sub_category : Optional[SubCategorySchema]
    
    class Meta:
        model = ManyCategory
        fields = ['id', 'sub_category', 'name']

class CountrySchema(ModelSchema):
    class Meta:
        model = Country
        fields = ['id', 'name']

class StateSchema(ModelSchema):
    country : CountrySchema

    class Meta:
        model = State
        fields = ['id', 'country', 'name']

class DistrictSchema(ModelSchema):
    state : StateSchema

    class Meta:
        model = District
        fields = ['id', 'state', 'name']

class KeywordSchema(ModelSchema):
    class Meta:
        model = Keyword
        fields = ['id', 'name']

class CompanyTypeSchema(ModelSchema):
    class Meta:
        model = CompanyType
        fields = ['id', 'name']

class CompanySchema(ModelSchema):
    location : Optional[DistrictSchema]
    company_type : Optional[CompanyTypeSchema]

    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'company_type', 'website', 'instagram', 'facebook', 'google_map']

class ExpirienceSchema(ModelSchema):
    class Meta:
        model = Expirience
        fields = ['id', 'name']

class JobSchema(ModelSchema):
    category: CategorySchema
    sub_category : Optional[SubCategorySchema]
    many_category : List[ManyCategorySchema] = []
    location : Optional[DistrictSchema]
    keyword : Optional[KeywordSchema]
    company : Optional[CompanySchema]
    expirience: Optional[ExpirienceSchema]

    class Meta:
        model = Job
        fields = [
            'id', 'category', 'sub_category', 'many_category', 'location',
            'keyword','expirience', 'company','job_type', 'description', 'email_one',
            'email_two', 'email_three', 'whatsapp', 'phone_one', 'phone_two', 'phone_three', 'source'
        ]
