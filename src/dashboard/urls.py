from dashboard.blog.views import blog_list, blog_edit, blog_create, blog_delete
from dashboard.views import *
from django.urls import path

urlpatterns = [
    path('', main_page, name='main_page'),

    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:pk>/edit/>', blog_edit, name='blog_edit'),
    path('blog/create/', blog_create, name='blog_create'),
    path('blog/<int:pk>/delete/>', blog_delete, name='blog_delete'),
]