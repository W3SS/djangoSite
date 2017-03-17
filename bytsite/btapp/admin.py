from django.contrib import admin
from btapp.models import Servicio, Articulo, Banner, Contacto, Producto, Cliente


class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo','subtitulo','texto','fecha_creacion','fecha_actualizacion')
    # list_filter = ('owner','active')
    # list_search = ('name',)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('autor','titulo','texto','imagen','fecha_creacion','fecha_actualizacion','destacado')

class BannerAdmin(admin.ModelAdmin):
    list_display = ('nombre','imagen','orden_banner','activo','fecha_creacion','fecha_actualizacion')  
    
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email','telefono','empresa','texto','fecha_creacion')    
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','texto','imagen','fecha_creacion','fecha_actualizacion')    
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente','proyecto','imagen','descripcion','fecha_creacion','fecha_actualizacion')    

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
