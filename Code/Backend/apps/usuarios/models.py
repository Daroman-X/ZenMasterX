from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import re
from .manage import UsuarioPersonalizado

class BaseModel(models.Model):
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)
    estado=models.BooleanField(default=True)
    class Meta:
        abstract = True  
         
class Pais(BaseModel):
    nombre=models.CharField(max_length=200, unique=True)
    class Meta:
        db_table="usuarios.pais"
        verbose_name="Pais"
        verbose_name_plural="Paises"
        ordering=["nombre"]
    def __str__(self):
        return self.nombre  
     
class Departamento(BaseModel):
    nombre=models.CharField(max_length=200, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='departamentos')  # added related_name
    def __str__(self):
        return self.nombre  
    class Meta:
        db_table="usuarios.departamento"
        verbose_name="Departamento"
        verbose_name_plural="Departamentos"
        ordering=["nombre"]
        indexes=[
            models.Index(fields=['pais','nombre']),
        ]
     
class Municipio(BaseModel):
    nombre=models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='municipios')  # added related_name
    def __str__(self):
        return self.nombre   
    class Meta:
        db_table="usuarios.municipio"
        verbose_name="Municipio"
        verbose_name_plural="Municipios"
        ordering=["nombre"]
        indexes=[
            models.Index(fields=['departamento','nombre']),
        ]       

class TipoDocumento(BaseModel):
    nombre=models.CharField(max_length=200, unique=True)
    descripcion=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.nombre 
    class Meta:
        db_table="usuarios.tipodocumento"
        verbose_name="Tipo de Documento"
        verbose_name_plural="Tipo de Documentos"
        ordering=["nombre"]
        
     
class Rol(BaseModel):
    nombre=models.CharField(max_length=50, unique=True)
    descripcion=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table="usuarios.rol"
        verbose_name="Rol"
        verbose_name_plural="Roles"
        ordering=["nombre"]
        
class DominioCorreo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table="usuarios.dominiocorreo"
        verbose_name="Dominio de Correo"
        verbose_name_plural="Dominio de Correos"
        ordering=["nombre"]
    def __str__(self):
        return self.nombre

class Usuario(AbstractBaseUser,BaseModel):
    tipo_documento=models.ForeignKey(TipoDocumento, verbose_name=("Tipo de Documento"), on_delete=models.CASCADE, null=True,blank=True)
    numero_documento=models.CharField(max_length=200,unique=True, null=True,blank=True)
    nombre_apellido=models.CharField(verbose_name="Nombre Completo", max_length=100)
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento", auto_now=False, auto_now_add=False, null=True,blank=True)
    numero_contacto=models.CharField(verbose_name="Numero de Contacto",max_length=255,unique=True, null=True,blank=True)
    correo=models.EmailField(verbose_name="Correo Electronico", max_length=254, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    dominio_correo = models.ForeignKey(DominioCorreo, on_delete=models.CASCADE, null=True, blank=True)

    # Acceso
    is_active = models.BooleanField("Habilitado", default=True)  # Define el campo is_active como BooleanField
    is_staff = models.BooleanField("Acceso al admin", default=False)  # Define el campo is_staff como BooleanField
    is_superuser = models.BooleanField("Superusuario", default=False)  # Para indicar si el usuario es superusuario

    rol=models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    objects=UsuarioPersonalizado()
    USERNAME_FIELD='correo'
    REQUIRED_FIELDS=[]
    
    class Meta:
        db_table="usuarios.usuario"
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
        ordering=["numero_documento"]
        indexes=[
            models.Index(fields=['numero_documento','correo'])
        ]
    def __str__(self):
        return f"{self.nombre_apellido} ({self.correo})"
    
    def clean(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            raise ValidationError("El correo electrónico no tiene un formato válido.")

        if self.dominio_correo:
            email_domain = self.correo.split('@')[-1]
            if email_domain != self.dominio_correo.nombre:
                raise ValidationError(f"El correo electrónico debe ser de dominio {self.dominio_correo.nombre}.")
        if not self.numero_documento.isdigit():
            raise ValidationError("El número de documento debe contener solo números.")
        if not re.match(r'^[\d\s\+\-]+$', self.numero_contacto):
            raise ValidationError("El número de contacto debe contener solo números, espacios, o los símbolos + y -. Verifique que no haya caracteres no permitidos.")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.nombre_apellido}")
        base_slug = self.slug
        i = 1
        while Usuario.objects.filter(slug=self.slug).exists():
            self.slug = f"{base_slug}-{i}"
            i += 1
        super(Usuario, self).save(*args, **kwargs)

    # Métodos necesarios para trabajar con permisos
    def has_perm(self, perm, obj=None):
        """
        Método que debe ser implementado para gestionar permisos.
        Devuelve True si el usuario tiene el permiso.
        """
        return self.is_superuser

    def has_module_perms(self, app_label):
        """
        Método que debe ser implementado para gestionar permisos de módulo.
        Devuelve True si el usuario tiene permisos sobre el módulo.
        """
        return self.is_superuser