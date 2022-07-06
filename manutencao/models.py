from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import CoreModel


class Sistema(CoreModel):
    descricao = models.CharField(max_length=40, verbose_name=_('descricao'))

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = _('sistema')
        verbose_name_plural = _('sistemas')


class Procedimento(CoreModel):
    sistema = models.ForeignKey(to='manutencao.Sistema', on_delete=models.CASCADE, verbose_name=_('sistema'))
    subsistema = models.CharField(max_length=40, null=True, blank=True, verbose_name=_('subsistema'))
    descricao = models.CharField(max_length=40, verbose_name=_('descricao'))
    detalhes = models.TextField(verbose_name=_('detalhes'))
    responsavel = models.ForeignKey(
        to='manutencao.Responsavel', on_delete=models.CASCADE, verbose_name=_('responsavel'),
    )
    periodicidade = models.IntegerField(verbose_name=_('periodicidade'))
    tipo_periodo = models.SmallIntegerField(
        verbose_name=_('tipo de periodo'),
        choices=[(1, 'dias'), (7, 'semanas'), (30, 'meses'), (360, 'anos')],
    )

    class Meta:
        verbose_name = _('procedimento')
        verbose_name_plural = _('procedimentos')


class Responsavel(CoreModel):
    descricao = models.CharField(max_length=40)

    class Meta:
        verbose_name = _('responsavel')
        verbose_name_plural = _('responsaveis')
