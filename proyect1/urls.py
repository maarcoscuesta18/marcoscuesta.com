"""proyect1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.views.generic.base import TemplateView 
from webpage.sitemaps import StaticSitemap # new
from . import views

sitemaps = {
    'static': StaticSitemap,
}

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('passgen',views.passwordgenerator, name='passgen'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
