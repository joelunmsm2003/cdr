from django.contrib import admin
from daterange_filter.filter import DateRangeFilter

# Register your models here.


#EJEMPLOSSSSSSSSSS......
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from daterange_filter.filter import DateRangeFilter
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

import csv


admin.site.disable_action('delete_selected')

# class CallDateListFilter(DateRangeFilter):
# 	# Human-readable title which will be displayed in the
# 	# right admin sidebar just above the filter options.
# 	title ='Citas'

# 	# Parameter for the filter that will be used in the URL query.
# 	parameter_name = 'Usuario'

# 	# def lookups(self, request, model_admin):

# 	#     return (
# 	#         ('X', 'X'),
# 	#     )

# 	def queryset(self, request, queryset):

# 		return queryset.all()




@admin.register(Cdr)
class CdrAdmin(admin.ModelAdmin):

	list_display = ('calldate','billsec','disposition','accountcode')
	search_fields =('calldate',)
	list_filter =('disposition',('calldate', DateRangeFilter),'accountcode')
	actions = ['Genera_CSV',]



	def Genera_CSV(self, request,queryset):



		my_filter={}

		print queryset.count()

		for a in request.GET:

			if a == 'disposition':

				my_filter['disposition']=request.GET['disposition']
			
			if a=='accountcode':

				my_filter['accountcode']=request.GET['accountcode']
			
			if a=='drf__calldate__gte':

				print request.GET['drf__calldate__gte']

				my_filter['calldate__gte']=request.GET['drf__calldate__gte']

			if a=='drf__calldate__lte':

				print request.GET['drf__calldate__lte']

				my_filter['calldate__lte']=request.GET['drf__calldate__lte']


		response = HttpResponse(content_type='text/csv')

		response['Content-Disposition'] = 'attachment; filename="Reporte.csv'

		writer = csv.writer(response)

		writer.writerow(['Calldate','Billsec','Disposition','Accountcode'])

		_cdr=Cdr.objects.filter(**my_filter)

		for q in _cdr:

			writer.writerow([q.calldate,q.billsec ,q.disposition,q.accountcode])

		return response





# @admin.register(BitCdr)
# class BitCdrAdmin(admin.ModelAdmin):
# 	list_display = ('calldate','clid','src','dst','dcontext','channel','dstchannel','lastapp','lastdata','duration','billsec','disposition','amaflags','accountcode','userfield','uniqueid','linkedid','sequence',
# 'peeraccount')
# 	search_fields =('calldate',)



# @admin.register(AuthUser)
# class AuthUserAdmin(admin.ModelAdmin):
# 	list_display = ('password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined')


# @admin.register(AuthUserGroups)
# class AuthUserGroupsAdmin(admin.ModelAdmin):
# 	list_display = ('user','group')


# @admin.register(AuthGroup)
# class AuthGroupAdmin(admin.ModelAdmin):
# 	list_display = ('name',)

