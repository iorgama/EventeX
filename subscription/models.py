# -*- coding:utf-8 -*-
from django.db import models

class Subscription(models.Model):
    nome = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 11, unique = True)
    email = models.EmailField("E-mail", unique = True)
    fone = models.CharField("Telefone", max_length = 20, blank = True)
    criado_em = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        ordering = ["criado_em"]
        verbose_name = u"Inscrição"
        verbose_name_plural = u"Inscrições"
