from django.contrib import admin
from .models import Pais, Departamento, Municipio, TipoDocumento, Rol, DominioCorreo, Usuario

# Registrar el modelo Pais en el admin
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creado', 'actualizado', 'estado')
    search_fields = ('nombre',)
    list_filter = ('estado',)
    ordering = ('nombre',)

# Registrar el modelo Departamento en el admin
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'creado', 'actualizado', 'estado')
    search_fields = ('nombre', 'pais__nombre')
    list_filter = ('estado', 'pais')
    ordering = ('nombre',)

# Registrar el modelo Municipio en el admin
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'creado', 'actualizado', 'estado')
    search_fields = ('nombre', 'departamento__nombre', 'departamento__pais__nombre')
    list_filter = ('estado', 'departamento')
    ordering = ('nombre',)

# Registrar el modelo TipoDocumento en el admin
@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'creado', 'actualizado', 'estado')
    search_fields = ('nombre',)
    list_filter = ('estado',)
    ordering = ('nombre',)

# Registrar el modelo Rol en el admin
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'creado', 'actualizado', 'estado')
    search_fields = ('nombre',)
    list_filter = ('estado',)
    ordering = ('nombre',)

# Registrar el modelo DominioCorreo en el admin
@admin.register(DominioCorreo)
class DominioCorreoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Solo mostrar 'nombre'
    search_fields = ('nombre',)
    ordering = ('nombre',)

# Registrar el modelo Usuario en el admin
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('correo', 'nombre_apellido', 'rol', 'fecha_nacimiento', 'numero_contacto', 'is_active', 'is_staff', 'is_superuser', 'creado', 'actualizado')
    search_fields = ('correo', 'nombre_apellido', 'numero_documento')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'rol')
    ordering = ('correo',)

    # Eliminar filter_horizontal porque no es un campo ManyToMany
    # filter_horizontal = ('rol',)
    raw_id_fields = ('tipo_documento', 'dominio_correo')
    date_hierarchy = 'creado'
    list_editable = ('is_active', 'is_staff', 'is_superuser')
