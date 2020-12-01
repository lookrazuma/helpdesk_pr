
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('grappelli/', include('grappelli.urls')), 
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', include('register.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
]

