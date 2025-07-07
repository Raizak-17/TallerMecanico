from django.apps import AppConfig


class AppTallermecanicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App_TallerMecanico'
    
    def ready(self):
        import App_TallerMecanico.decorators  # Importa el archivo de señales
