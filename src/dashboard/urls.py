from dashboard.blog.views import blog_list, blog_edit, blog_create, blog_delete
from dashboard.receipe.views import recipe_create, recipe_list, recipe_edit, recipe_delete
from dashboard.views import *
from django.urls import path

urlpatterns = [
    path('', main_page, name='main_page'),

    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:pk>/edit/>', blog_edit, name='blog_edit'),
    path('blog/create/', blog_create, name='blog_create'),
    path('blog/<int:pk>/delete/>', blog_delete, name='blog_delete'),

    path('recipe/', recipe_list, name='recipe_list'),
    path('recipe/create/', recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
]