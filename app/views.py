from django.shortcuts import render
from app.filtros import *
# Create your views here.
def list(request):
    f = CdrFilter(request.GET, queryset=BitCdr.objects.all())
    return render(request, 'cdr.html', {'filter': f})