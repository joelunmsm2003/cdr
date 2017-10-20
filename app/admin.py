from django.contrib import admin

# Register your models here.


#EJEMPLOSSSSSSSSSS......
 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

@admin.register(BitCdr)
class BitCdrAdmin(admin.ModelAdmin):
	list_display = ('calldate','clid','src','dst','dcontext','channel','dstchannel','lastapp','lastdata','duration','billsec','disposition','amaflags','accountcode','userfield','uniqueid','linkedid','sequence',
'peeraccount')



@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
	list_display = ('password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined')


@admin.register(AuthUserGroups)
class AuthUserGroupsAdmin(admin.ModelAdmin):
	list_display = ('user','group')


@admin.register(AuthGroup)
class AuthGroupAdmin(admin.ModelAdmin):
	list_display = ('name',)

