#-*- coding: utf-8 -*-
from django.test import TestCase
from subscription.models import Subscription
from subscription.forms import SubscriptionForm
from django.core import mail
from django.core.urlresolvers import reverse
import unittest

##############
### MODELS ###
##############

class SubscriptionModelTestCase(unittest.TestCase):    
    def setUp(self):
        self.subscription, self.create = Subscription.objects.get_or_create(
                    nome = 'Iorgama Porcely dos Santos Silva',
                    cpf = '00000000000',
                    email = 'abc@gmail.com',
                    fone = '082-99990000',
                )
        
    def testUnicode(self):
        self.assertEqual(self.subscription.__unicode__(), self.subscription.nome)
    
    def test_quantidade_de_inscricoes_realizadas(self):
        self.assertEquals(self.subscription.id, 1)

###############
###  FORMS  ###
###############

class SubscriptionFormTestCase(TestCase):
    def setUp(self):
        self.form = SubscriptionForm({
            'nome': 'Iorgama Porcely dos Santos Silva',
            'cpf': '00000000000',
            'email': 'abc@gmail.com',
            'fone': '082-99990000',
        })
    def test_se_form_tem_os_campos_necessarios(self):
        self.assertTrue(self.form.fields.get('nome'))
        self.assertIn('nome', self.form.fields)
        self.assertTrue(self.form.fields.get('cpf'))
        self.assertIn('cpf', self.form.fields)
        self.assertTrue(self.form.fields.get('email'))
        self.assertIn('email', self.form.fields)
        self.assertTrue(self.form.fields.get('fone'))
        self.assertIn('fone', self.form.fields)
        
    def test_se_form_nao_tem_campos_desnecessarios(self):
        self.assertFalse(self.form.fields.get('paid'))
        self.assertNotIn('paid', self.form.fields)
        self.assertFalse(self.form.fields.get('criado_em'))
        self.assertNotIn('criado_em', self.form.fields)

    def test_excecoes_do_cpf_(self):
        self.form = SubscriptionForm({
            'nome': 'Iorgama Porcely dos Santos Silva',
            'cpf': '000003aab',
            'email': 'abc@gmail.com',
            'fone': '082-99990000',
        })
        self.assertFalse(self.form.is_valid())
        self.assertIn('cpf', self.form.errors)
        self.assertTrue(self.form.errors.get('cpf'))

        
##############
###  URLS  ###
##############

class SubscriptionUrlTestCase(TestCase):
    def test_pagina_de_inscricoes_get(self):
        response = self.client.get('/inscricao/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'subscription/subscription_form.html')
        self.assertTrue(isinstance(response.context['form'], SubscriptionForm))
