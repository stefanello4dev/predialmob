from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ManutencaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manutencao'
    label = 'manutencao'
    verbose_name = _('manutencao')
