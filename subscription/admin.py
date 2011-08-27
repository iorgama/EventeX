from django.contrib import admin
from subscription.models import Subscription
import datetime

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','fone','criado_em', 'inscrito_hoje')
    date_hierarchy = 'criado_em'
    search_fields = ('nome','cpf','criado_em')
    list_filter = ['criado_em']

    def inscrito_hoje(self, obj):
        return obj.created_at.date() == datetime.date.today()
    inscrito_hoje.short_description = 'Inscrito hoje?'
    inscrito_hoje.boolean = True    
 

admin.site.register(Subscription, SubscriptionAdmin)
