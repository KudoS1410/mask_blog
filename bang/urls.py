"""bang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static


# the urls are checked in order
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog_dev/', include('blog.urls')),
    path('register/', users_views.register, name = 'register'),
    path('profile/', users_views.profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('password_reset/',
            auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),
            name = 'password-reset'
        ),
    path('password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),
            name = 'password-reset-done'
        ),
    path('password_reset/confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),
            name = 'password_reset_confirm'
        )
    # path('', include('blog.urls'))
    # the blog applications url.py file that is this just links to all the urls of the blog at once
    # but what is passed to the url handler of blog urls yes, the part after the blog which here is empty string
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
