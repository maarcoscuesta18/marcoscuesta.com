from django.contrib.sitemaps import Sitemap
from .models import Contact
from django.shortcuts import reverse

class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return ['index']
    
    def location(self,item):
        return reverse(item)