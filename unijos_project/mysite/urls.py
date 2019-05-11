"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

#serve media files
from django.conf import settings
from django.conf.urls.static import static


from . import views
# from
urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('world/', views.home_view, name="home"),
    path('accounts/', include("allauth.urls")),  # Django Allauth
    path('profile/',include("profiles.urls", namespace="profiles")),
    path('feedback/', include('feedback.urls', namespace="feedback"))
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)