from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import *
from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail
from django.db import connection
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
import time
import collections
import os
import json 
import csv
from django.utils import timezone


from datetime import datetime,timedelta

from django.contrib.auth import authenticate
#import unirest


@login_required(login_url="/ingresar")

def salir(request):

	logout(request)
	
	return HttpResponseRedirect("/ingresar")

def audio(request):

	# print request.get_full_path().split('&anexo')[0].split('?audio=')[1][7:9]

	# # Oct.%2023,%202017,%202:02%20p.m.
	# # 2:02 p.m.

	# mes = 10
	# anio=2017
	# dia = request.get_full_path().split('&anexo')[0].split('?audio=')[1][7:9]
	# hora= request.get_full_path().split('&anexo')[0].split('?audio=')[1][20:22]
	# minuto= request.get_full_path().split('&anexo')[0].split('?audio=')[1][23:25]
	# segundo= 59

	# audio = 

	
	return HttpResponseRedirect("/23")


def ingresar(request):
   
	if request.method=='POST':

	    username = request.POST['username']
	    password = request.POST['password']


	    user = authenticate(username=username, password=password)
	    if user is not None:

	        login(request, user)


	        return HttpResponseRedirect('/list')

	    else:


	    	return render(request, 'login.html', {'error':'Usuario no registrado'})



	else:

		return render(request, 'login.html', {})





@login_required(login_url="/ingresar")
def list(request):


	my_filter = {}

	user=User.objects.get(id=request.user.id)

	orderfecha='calldate'

	for r in request.GET:

		print 'shhs',r

		

		if r=='fechainicio':

			if request.GET['fechainicio']:

				finicio =  datetime.strptime(str(request.GET['fechainicio']), '%Y-%m-%d')

				my_filter['calldate__gte'] = finicio

		if r=='fechafin':

			if request.GET['fechafin']:

				fechafin =  datetime.strptime(str(request.GET['fechafin']), '%Y-%m-%d')

				my_filter['calldate__lte'] = fechafin

		if r=='anexo':

			if request.GET['anexo']:

				my_filter['src'] = request.GET['anexo']



		if r=='destino':

			if request.GET['destino']:

				my_filter['dst'] = request.GET['destino']


		if r=='orderfecha':

			if request.GET['orderfecha']:

				if request.GET['orderfecha']=='calldate':

					orderfecha='-calldate'

				else:

					orderfecha='calldate'

		if r=='ordertiempo':

			if request.GET['ordertiempo']:

				if request.GET['ordertiempo']=='asc':

					ordertiempo='-duration'

				else:

					ordertiempo='duration'






	contact_list = Cdr.objects.filter(**my_filter).order_by(orderfecha).values('calldate','src','dst','duration').order_by('-calldate')


	for p in range(len(contact_list)):

		print contact_list[p]['calldate'].year



		anio =  contact_list[p]['calldate'].year
		mes= contact_list[p]['calldate'].month
		dia=contact_list[p]['calldate'].day
		hora =contact_list[p]['calldate'].hour
		minuto =contact_list[p]['calldate'].minute
		segundo=contact_list[p]['calldate'].second

		print anio,mes,dia,hora,minuto,segundo

		if len(str(mes))==1: mes='0'+str(mes)
		if len(str(dia))==1: dia='0'+str(dia)		
		if len(str(hora))==1: hora='0'+str(hora)	
		if len(str(minuto))==1: minuto='0'+str(minuto)		
		if len(str(segundo))==1: segundo='0'+str(segundo)


		print 	contact_list[p]['calldate'],datetime.today()

		now = timezone.now()


		url_gsm='/var/www/html/grabaciones/OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.gsm'

		url_wav='/var/www/html/grabaciones/OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.wav'

		url_mp3='/var/www/html/grabaciones/OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.mp3'

		if os.path.isfile(url_gsm):

			contact_list[p]['url']='http://172.23.218.27/grabaciones/OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.gsm'

		if os.path.isfile(url_wav):

			contact_list[p]['url']='http://172.23.218.27/grabaciones/OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.wav'

		if os.path.isfile(url_mp3):

			contact_list[p]['url']='http://172.23.218.27/grabaciones/OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.mp3'


		if  contact_list[p]['calldate']<now:

			url_gsm='/var/www/html/grabaciones/'+str(dia)+str(mes)+str(anio)+'/'+'OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.gsm'

			url_wav='/var/www/html/grabaciones/'+str(dia)+str(mes)+str(anio)+'/'+'OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.wav'

			url_mp3='/var/www/html/grabaciones/'+str(dia)+str(mes)+str(anio)+'/'+'OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.mp3'


			if os.path.isfile(url_gsm):

				contact_list[p]['url']='http://172.23.218.27/grabaciones/'+str(dia)+str(mes)+str(anio)+'/'+'OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.gsm'

			if os.path.isfile(url_wav):

				contact_list[p]['url']='http://172.23.218.27/grabaciones/'+str(dia)+str(mes)+str(anio)+'/'+'OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.wav'

			if os.path.isfile(url_mp3):

				contact_list[p]['url']='http://172.23.218.27/grabaciones/'+str(dia)+str(mes)+str(anio)+'/'+'OUT_'+str(dia)+str(mes)+str(anio)+'_'+str(hora)+str(minuto)+str(segundo)+'_'+str(contact_list[p]['src'])+'_'+str(contact_list[p]['dst'])+'.mp3'


	paginator = Paginator(contact_list, 25) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    contacts = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)

	return render(request, 'cdr.html', {'contacts': contacts,'user':user,'orderfecha':orderfecha})


