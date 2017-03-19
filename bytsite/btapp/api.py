from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Articulo, Banner
class ArticuloResource(ModelResource):
    """
    API FACET
    """
    class Meta:
        queryset = Articulo.objects.all()
        resource_name='articulo'
        allowed_methods = ['post','get','patch','delete']
        authorization = Authorization()
        always_return_data = True

class BannerResource(ModelResource):
    """
    API FACET
    """
    class Meta:
        queryset = Banner.objects.filter(activo=1).order_by('orden_banner')
        resource_name='banner'
        allowed_methods = ['post','get','patch','delete']
        authorization = Authorization()
        always_return_data = True