from django.urls import path
from event.api_endpoints.category.views import (
    CategoriyListAPIView, CategoryAPIVIew, CategoryDetailAPIView, 
    SubcategoryAPIView, SubcategoryListAPIView,SubCategoryDetailAPIView)
from event.api_endpoints.course.views import (
    CourseListAPIView, CourseAPIView, CourseDetailAPIView,
    LessonListAPIView, LessonAPIView, LessonDetailAPIView
)

urlpatterns = [
    path('category/', CategoriyListAPIView.as_view(), name='category-list'),
    path('dt-category/<int:pk>/', CategoryDetailAPIView.as_view(), name='dt-category'),
    path('my-categories/', CategoryAPIVIew.as_view(), name='admin-category-list'),

    path('subcategory/', SubcategoryListAPIView.as_view(), name='subcategory-list'),
    path('dt-subcategory/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='dt-subcategory'),
    path('my-subcategories/', SubcategoryAPIView.as_view(), name='admin-subcategory-list'),

    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('my-course/', CourseAPIView.as_view(), name='course-list'),
    path('dt-course/<int:pk>/', CourseDetailAPIView.as_view(), name='dt-course'),

    path('lessons/all/', LessonListAPIView.as_view(), name='lesson-list-all'),
    path('lessons/', LessonAPIView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
]