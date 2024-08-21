from django.apps import AppConfig


class LeassonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Lesson_app'

    def ready(self) -> None:
        import Lesson_app.signals
