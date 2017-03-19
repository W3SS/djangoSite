from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api
from btapp.api import ArticuloResource, BannerResource


articulo_resource = ArticuloResource()
banner_resource = BannerResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('btapp.urls')),
    url(r'^api/', include(articulo_resource.urls)),
    url(r'^api/', include(banner_resource.urls)),
]


if settings.DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))