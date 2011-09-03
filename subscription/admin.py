#-*- coding:utf-8-*-
from django.contrib import admin
from django.conf.urls.defaults import *
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from subscription.models import Subscription
import datetime
from django.http import HttpResponse

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','fone','criado_em', 'inscrito_hoje', 'pago')
    date_hierarchy = 'criado_em'
    search_fields = ('nome','cpf','criado_em')
    list_filter = ['pago']

    actions = ['marcado_como_pago']
    actions = ['inscrito_hoje']
    
    def marcado_como_pago(self, request, queryset):
        count = queryset.update(pago = True)
        
        msg = ungettext(
        	u'%(count)d inscrição foi marcada como paga.',
        	u'%(count)d inscrições foram marcadas como pagas.',		
        ) % {'count': count}
        self.manage_user(request, msg)
    marcado_como_pago.short_description = _(u"Marcar como pagas")
	#

    def inscrito_hoje(self, obj):
        return obj.created_at.date() == datetime.date.today()
    inscrito_hoje.short_description = 'Inscrito hoje?'
    inscrito_hoje.boolean = True   

    def export_subscriptions(self, request):
    	subscriptions = self.model.objects.all()
    	rows = [','.join([s.nome, s.email]) for s in subscriptions]
    
    	response = HttpResponse('\r\n'.join(rows))
    	response.mimetype = "text/csv"
    	response['Content-Disposition'] = 'attachment; filename=inscricoes.csv'
    	return response 
 
    def get_urls(self):
        original_urls = super(SubscriptionAdmin, self).get_urls()
        extra_urls = patterns('',
                url(r'exportar-inscricoes/$',
                    self.admin_site.admin_view(self.export_subscriptions),
                    name = 'export_subscriptions'
                )
        )
        return extra_urls + original_urls
 
admin.site.register(Subscription, SubscriptionAdmin)
