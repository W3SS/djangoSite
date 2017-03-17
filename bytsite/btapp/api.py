from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Articulo
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