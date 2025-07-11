from django.apps import AppConfig, apps

from .conf import app_settings


class DjangoAutoAdminConfig(AppConfig):
    name = "django_auto_admin"
    verbose_name = "Django Auto Admin"

    def ready(self):
        if "polymorphic" in apps.app_configs:
            from .registrar import PolymorphicAdminModelRegistrar as Registrar
        else:
            from .registrar import AdminModelRegistrar as Registrar

        app_label = app_settings.APP_LABEL
        if app_label:
            self.registrar = Registrar(app_label=app_label) 