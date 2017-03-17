from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api
from btapp.api import ArticuloResource


articulo_resource = ArticuloResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('btapp.urls')),
    url(r'^api/', include(articulo_resource.urls)),

]


if settings.DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))