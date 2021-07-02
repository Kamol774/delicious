from django.urls import path
from .views import recipe_create, recipe_list, recipe_edit, recipe_delete
urlpatterns = [
    path('recipe/list', recipe_list, name='recipe_list'),
    path('recipe/create', recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete', recipe_delete, name='recipe_delete'),
]