from django.apps import AppConfig


class MultitenantApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'multitenant_api'
