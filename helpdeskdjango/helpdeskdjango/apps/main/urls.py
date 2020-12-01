from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.main,),
    path('about/', views.about,),
    path('task_show/', views.task_show,),
    path('manage/', views.manage_view,),
    path('task/<int:task_id>', views.manage_detail, name = 'manage_details_url'),
]
