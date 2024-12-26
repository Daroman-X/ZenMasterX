from django.apps import AppConfig
from django.dispatch import receiver

from django.db.models.signals import post_migrate


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.usuarios'
    
    def ready(self):
        
        # Conectar las señales para crear roles y dominios por defecto
        post_migrate.connect(crear_roles_por_defecto, sender=self)
        post_migrate.connect(crear_dominios_por_defecto, sender=self)
        post_migrate.connect(crear_tipo_documento, sender=self)
        post_migrate.connect(crear_datos_colombia, sender=self)

@receiver(post_migrate)
def crear_roles_por_defecto(sender, **kwargs):
    """
    Esta función se ejecuta después de que se hayan aplicado las migraciones.
    Se asegura de que los roles "Admin", "Cliente" y "Moderador" existan.
    """
    from .models import Rol
    # Verifica si los roles ya existen, y si no, los crea.
    if not Rol.objects.filter(nombre="Admin").exists():
        Rol.objects.create(nombre="Admin")
    if not Rol.objects.filter(nombre="Cliente").exists():
        Rol.objects.create(nombre="Cliente")
    if not Rol.objects.filter(nombre="Moderador").exists():
        Rol.objects.create(nombre="Moderador")
        
@receiver(post_migrate)
def crear_dominios_por_defecto(sender, **kwargs):
    """
    Esta función se ejecuta después de que se hayan aplicado las migraciones.
    Se asegura de que los dominios "gmail", "outlook", "yahoo" y "hotmail" existan.
    """
    from .models import DominioCorreo
    # Verifica si los dominios ya existen, y si no, los crea.
    dominios = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com"]
    for dominio in dominios:
        DominioCorreo.objects.get_or_create(nombre=dominio)

@receiver(post_migrate)
def crear_tipo_documento(sender, **kwargs):
    # Crear los tipos de documento
    from .models import TipoDocumento

    tipos_documento = [
        {"nombre": "Tarjeta de Identidad"},
        {"nombre": "Cédula de Ciudadanía"},
        {"nombre": "Pasaporte"},
        {"nombre": "NIT"},
        {"nombre": "Cédula Extranjería"}
    ]
    
    for tipo in tipos_documento:
        TipoDocumento.objects.get_or_create(**tipo)
        
@receiver(post_migrate)
def crear_datos_colombia(sender, **kwargs):
    # Crear los países, departamentos y municipios
    from .models import Pais,Departamento,Municipio
    paises = [
        {"nombre": "Colombia", "departamentos": [
  {"nombre": "Amazonas", "municipios": ["Leticia", "Puerto Nariño", "Tarapacá", "La Chorrera"]},
        {"nombre": "Antioquia", "municipios": ["Medellín", "Bello", "Itagüí", "Rionegro", "Envigado", "Apartadó", "La Ceja", "Caldas"]},
        {"nombre": "Arauca", "municipios": ["Arauca", "Tame", "Arauquita", "Fortul"]},
        {"nombre": "Atlántico", "municipios": ["Barranquilla", "Soledad", "Malambo", "Puerto Colombia"]},
        {"nombre": "Bolívar", "municipios": ["Cartagena", "Magangué", "Sincelejo", "Mompox", "Turbaco"]},
        {"nombre": "Boyacá", "municipios": ["Tunja", "Duitama", "Sogamoso", "Chiquinquirá", "Paipa"]},
        {"nombre": "Caldas", "municipios": ["Manizales", "Villamaría", "Chinchiná", "Neira"]},
        {"nombre": "Caquetá", "municipios": ["Florencia", "San Vicente del Caguán", "El Doncello"]},
        {"nombre": "Casanare", "municipios": ["Yopal", "Villanueva", "Hato Corozal"]},
        {"nombre": "Cauca", "municipios": ["Popayán", "Piendamó", "Puracé", "Santander de Quilichao", "Cajibío"]},
        {"nombre": "Cesar", "municipios": ["Valledupar", "Aguachica", "La Jagua de Ibirico"]},
        {"nombre": "Chocó", "municipios": ["Quibdó", "Río Sucio", "Istmina", "Bojayá"]},
        {"nombre": "Córdoba", "municipios": ["Montería", "Lorica", "Cereté", "San Antero"]},
        {"nombre": "Cundinamarca", "municipios": ["Bogotá", "Soacha", "Chía", "Zipaquirá", "Fusagasugá"]},
        {"nombre": "Guainía", "municipios": ["Inírida", "San José del Guaviare"]},
        {"nombre": "Guaviare", "municipios": ["San José del Guaviare", "Calamar"]},
        {"nombre": "Huila", "municipios": ["Neiva", "Pitalito", "La Plata", "Campoalegre"]},
        {"nombre": "La Guajira", "municipios": ["Riohacha", "Maicao", "Fonseca"]},
        {"nombre": "Magdalena", "municipios": ["Santa Marta", "Ciénaga", "Aracataca", "Santa Bárbara de Pinto"]},
        {"nombre": "Meta", "municipios": ["Villavicencio", "Acacías", "Restrepo", "San Juan de Arama"]},
        {"nombre": "Nariño", "municipios": ["Pasto", "Tumaco", "Ipiales", "La Unión"]},
        {"nombre": "Norte de Santander", "municipios": ["Cúcuta", "Pamplona", "Villa del Rosario"]},
        {"nombre": "Putumayo", "municipios": ["Mocoa", "Puerto Asís", "Sibundoy"]},
        {"nombre": "Quindío", "municipios": ["Armenia", "Calarcá", "Montenegro", "Salento"]},
        {"nombre": "Risaralda", "municipios": ["Pereira", "Dosquebradas", "Santa Rosa de Cabal", "La Virginia"]},
        {"nombre": "San Andrés y Providencia", "municipios": ["San Andrés", "La Providencia"]},
        {"nombre": "Santander", "municipios": ["Bucaramanga", "Cúcuta", "Barrancabermeja", "Girón"]},
        {"nombre": "Sucre", "municipios": ["Sincelejo", "Sampués", "Coveñas", "Los Palmitos"]},
        {"nombre": "Tolima", "municipios": ["Ibagué", "Espinal", "Melgar", "El Espinal"]},
        {"nombre": "Valle del Cauca", "municipios": ["Cali", "Buenaventura", "Tuluá", "Palmira", "Buga"]},
        {"nombre": "Vaupés", "municipios": ["Mitú"]},
        {"nombre": "Vichada", "municipios": ["Puerto Carreño", "Cumaribo"]},
        ]},
    ]
    
    for pais_data in paises:
        pais, created = Pais.objects.bulk_create(nombre=pais_data["nombre"])
        for departamento_data in pais_data["departamentos"]:
            departamento, created = Departamento.objects.bulk_create(nombre=departamento_data["nombre"], pais=pais)
            for municipio_name in departamento_data["municipios"]:
                Municipio.objects.bulk_create(nombre=municipio_name, departamento=departamento)
    