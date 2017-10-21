from django.shortcuts import render
from app.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from datetime import datetime
def list(request):


	my_filter = {}

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






	contact_list = Cdr.objects.filter(**my_filter).order_by(orderfecha)
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

	return render(request, 'cdr.html', {'contacts': contacts,'orderfecha':orderfecha})


