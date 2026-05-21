from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from common.models import BaseModel

User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subcategories', null=True)

    def __str__(self):
        return self.name



class Course(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authored_courses')
    likes = models.ManyToManyField(User, related_name='liked_courses', blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, null=True)
    


    def average_rating(self):
        if hasattr(self, 'reviews'):
            return self.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
        return 0

    def students_count(self):
        return self.enrollments.count()
    
    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.name



class Lesson(BaseModel):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_lesson')
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='lessons/videos/', blank=True, null=True)
    duration_display = models.CharField(max_length=10)
    is_preview = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.course.name} - {self.title}"


class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Kutilmoqda'),
        ('approved', 'Tasdiqlandi'),
        ('rejected', 'Rad etildi'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    date_enrolled = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('user', 'course')