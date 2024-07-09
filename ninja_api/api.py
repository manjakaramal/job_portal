from ninja import Router
from .models import Category, SubCategory, Job
from .schemas import CategorySchema, SubCategorySchema, JobSchema
from typing import List
from ninja.pagination import paginate, PageNumberPagination

router = Router()

@router.get('/categories/', response=List[CategorySchema])
def list_categories(request):
    categories = Category.objects.all()
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
        
@router.get('/categories/{category_id}/jobs/', response=List[JobSchema])
def list_category_job(request, category_id: int, sub_category: int = None):
    category = Category.objects.get(id=category_id)
    jobs_query = Job.objects.filter(category=category)
    
    if sub_category:
        jobs_query = jobs_query.filter(sub_category=sub_category)
    
    jobs = jobs_query.all()
    return jobs
