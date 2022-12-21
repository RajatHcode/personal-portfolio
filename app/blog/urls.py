from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.blog_index, name="blog_index"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blogs/<category>/", views.blog_category, name="blog_category"),
    path("blogs/delete/<int:pk>/", views.blog_delete, name="blog_delete"),
]
