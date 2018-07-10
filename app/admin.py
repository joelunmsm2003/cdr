from django.contrib import admin
from daterange_filter.filter import DateRangeFilter

# Register your models here.


#EJEMPLOSSSSSSSSSS......
 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from daterange_filter.filter import DateRangeFilter
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class CallDateListFilter(DateRangeFilter):
	# Human-readable title which will be displayed in the
	# right admin sidebar just above the filter options.
	title ='Citas'

	# Parameter for the filter that will be used in the URL query.
	parameter_name = 'Usuario'

	# def lookups(self, request, model_admin):

	#     return (
	#         ('X', 'X'),
	#     )

	def queryset(self, request, queryset):

		return queryset.all()


@admin.register(Cdr)
class CdrAdmin(admin.ModelAdmin):
	list_display = ('calldate','clid','src','dst','dcontext','channel','dstchannel','lastapp','lastdata','duration','billsec','disposition','amaflags','accountcode','userfield','uniqueid','userfield','import_cdr')
	list_filter = (CallDateListFilter,)
	search_fields =('calldate',)


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

