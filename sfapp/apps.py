from django.apps import AppConfig


class SfappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sfapp'

    def ready(self):
        import sfapp.signals  # Import the signals
