# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from subscription import validators

class Subscription(models.Model):
    nome = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 11, unique = True,validators=[validators.CpfValidator])
    email = models.EmailField("E-mail", unique = True,blank = True)
    fone = models.CharField("Telefone", max_length = 20, blank = True)
    criado_em = models.DateTimeField(auto_now_add = True)
    pago = models.BooleanField()
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        ordering = ["criado_em"]
        verbose_name = u"Inscrição"
        verbose_name_plural = u"Inscrições"
