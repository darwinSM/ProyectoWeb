from django.urls import path
from AppBlog import views

urlpatterns = [
    path('blog/' , views.blog , name='Blog'),
    path('blog/categoria/<int:categoria_id>/' , views.categoria , name='categoria')
]
