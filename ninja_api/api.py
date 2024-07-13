from ninja import Router, Query
from .models import Category, SubCategory, Job, District
from .schemas import CategorySchema, SubCategorySchema, JobSchema, DistrictSchema
from typing import List, Optional
from ninja.pagination import paginate, PageNumberPagination
from django.db.models import Q

router = Router()

# @router.get('/categories/', response=List[CategorySchema])
# def list_categories(request):
#     categories = Category.objects.all()
#     return categories

@router.get('/categories/', response=List[CategorySchema])
def list_categories(request):
    categories = Category.objects.filter(job__isnull=False).distinct()
    return categories

@router.get('/jobs/', response=List[JobSchema])
@paginate(PageNumberPagination)
def list_jobs(request):
    jobs = Job.objects.all()
    return jobs

@router.get('/jobs/{job_id}/', response=JobSchema)
def get_job(request, job_id: int):
    job = Job.objects.get(id=job_id)
    return job

@router.get('/categories/{category_id}/subcategories/', response=List[SubCategorySchema])
def list_category_subcategories(request, category_id: int):
    subcategories = SubCategory.objects.filter(category_id=category_id)
    return subcategories

# /api/categories/${categoryId}/jobs?sub_category=${subcategoryId}        
@router.get('/categories/{category_id}/jobs/', response=List[JobSchema])
@paginate(PageNumberPagination)
def list_category_job(request, category_id: int, sub_category: int = None):
    category = Category.objects.get(id=category_id)
    jobs_query = Job.objects.filter(category=category)
    
    if sub_category:
        jobs_query = jobs_query.filter(sub_category=sub_category)
    
    jobs = jobs_query.all()
    return jobs

# @router.get("/jobs/search", response=List[JobSchema])
# def search_jobs(request, name: Optional[str] = Query(None), category: Optional[int] = Query(None), subcategory: Optional[int] = Query(None)):
#     jobs = Job.objects.all()

#     if name:
#         jobs = jobs.filter(name__icontains=name)
    
#     if category:
#         jobs = jobs.filter(category_id=category)
    
#     if subcategory:
#         jobs = jobs.filter(sub_category__id=subcategory)
    
#     return jobs

# /api/jobs/search - returns all jobs.
# /api/jobs/search?name=developer - returns jobs with "developer" in their name.
# /api/jobs/search?category=1 - returns jobs in category with ID 1.
# /api/jobs/search?subcategory=2 - returns jobs in subcategory with ID 2.
# /api/jobs/search?name=developer&category=1&subcategory=2 - returns jobs matching all provided filters.

# /api/jobs/search?query=developer
@router.get("/jobs/search", response=List[JobSchema])
@paginate(PageNumberPagination)
def search_jobs(request, query: Optional[str] = Query(None)):
    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(sub_category__name__icontains=query)
        ).distinct()

    return jobs

@router.get("/subcategories/", response=List[SubCategorySchema])
def list_sub_categories(request):
    sub_categories = SubCategory.objects.filter(job__isnull=False).distinct()
    return sub_categories

@router.get("/districts/", response=List[DistrictSchema])
def list_districts(request):
    districts = District.objects.filter(job__isnull=False).distinct()
    return districts