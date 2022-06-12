from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from computerApp.models import Machine

# Create your views here.

def index(request):
	machines = Machine.objects.order_by('-id')
	context = {'machines': machines,}

	return render(request, 'index.html', context=context)

def login(request):
	machines = Machine.objects.order_by('-id')
	context = {'machines': machines,}

	return render(request, 'login.html', context=context)

def machine_list_view(request) :
	machines = Machine.objects.all()
	context = {'machines':machines}
	return render (request,
		'computerapp/machine_list.html',
		context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	context={'machine': machine}
	return render(request, 'computerapp / machine_detail.html',context)