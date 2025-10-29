from django.apps import AppConfig
from admin import site



class ShortenerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Shortener"
    verbose_name = "URL Shortener Application"
    def ready(self):
        
        return super().ready()
    


    


