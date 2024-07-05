from ninja import Router
from .models import Category, SubCategory,Job
from .schemas import CategorySchema, SubCategorySchema, JobSchema
from typing import List

router = Router()

@router.get('/categories/', response=List[CategorySchema])
def list_categories(request):
    categories = Category.objects.all()
    return categories

@router.get('/categories/{category_id}/subcategories/', response=List[SubCategorySchema])
def list_subcategories(request, category_id: int):
    subcategories = SubCategory.objects.filter(category_id=category_id)
    return subcategories


@router.get('/jobs/', response=List[JobSchema])
def list_jobs(request):
    jobs = Job.objects.all()
    return jobs

@router.get('/jobs/{job_id}/')
def get_job(request, job_id: int):
    job = Job.objects.get(id=job_id)
    return JobSchema(job).dict()
