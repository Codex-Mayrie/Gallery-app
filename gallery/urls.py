from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.index, name = 'index'),
  url(r'^location/(\d+)', views.display_location, name='display_location'),
  url(r'^search/', views.search_results, name='search_results')
  
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  