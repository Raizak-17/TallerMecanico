from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from django.db import IntegrityError
import datetime

@receiver(post_migrate)
def crear_admin_por_defecto(sender, **kwargs):
    # Obtener modelos
    Registro = apps.get_model('App_TallerMecanico', 'Registro')
    Administrador = apps.get_model('App_TallerMecanico', 'Administrador')

    try:
        # Insertar registro de administrador por defecto
        if not Registro.objects.filter(username='admin').exists():
            registro_admin = Registro.objects.create(
                username='admin',
                password='admin',  # Contraseña sin encriptar
                role='admin'
            )
            print("Registro de administrador creado exitosamente.")

            # Insertar administrador vinculado al registro
            Administrador.objects.create(
                registro=registro_admin,
                rut='12345678-9',
                nombre='Admin',
                apellido='Principal',
                fecha_nacimiento=datetime.date(1980, 1, 1),
                genero='M',
                email='admin@tallermecanico.com',
                clave_unica='admin123'
            )
            print("Administrador principal creado exitosamente.")

    except IntegrityError:
        print("El administrador ya existe. No se realizaron cambios.")
