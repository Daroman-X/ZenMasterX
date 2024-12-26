from django.contrib.auth.models import BaseUserManager

class UsuarioPersonalizado(BaseUserManager):
    def create_user(self, correo, password=None, rol="Cliente", **extra_fields):
        if not correo:
            raise ValueError("El usuario debe tener un correo electronico")
        if password and len(password) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        if not any(char.isdigit() for char in password):
            raise ValueError('La contraseña debe contener al menos un número')
        if not any(char.isupper() for char in password):
            raise ValueError('La contraseña debe contener al menos una letra mayúscula')
        if not any(char in '!@#$%^&*()' for char in password):
            raise ValueError('La contraseña debe contener al menos un carácter especial')

        correo = self.normalize_email(correo)
        user = self.model(correo=correo, rol=rol, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, correo, password=None, **extra_fields):
        from .models import Rol
        rol_admin, created = Rol.objects.get_or_create(nombre="Admin")
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("rol", rol_admin)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get("is_superuser") is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        
        return self.create_user(correo, password, **extra_fields)

 