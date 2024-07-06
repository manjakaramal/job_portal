from ninja import ModelSchema
from .models import Category, Country, State, District, CompanyType, Company, Job
from typing import List, Optional

class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']


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


class JobSchema(ModelSchema):
    category: List[CategorySchema] = []
    location : Optional[DistrictSchema]
    company : Optional[CompanySchema]

    class Meta:
        model = Job
        fields = [
            'id', 'category', 'itpark', 'name', 'location', 'address', 'min_years_experience', 'max_years_experience',
            'description', 'image', 'image_url', 'posted', 'closing_date', 'source'
        ]
