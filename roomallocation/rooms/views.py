from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext, loader

from .models import Flat, Floor


# Create your views here.
def index(request):

	residence_floors = Floor.objects.values_list('floor', flat=True)
	template = loader.get_template('rooms/index.html')
	context = RequestContext(request, {
		'residence_floors': residence_floors,
		})
	return HttpResponse(template.render(context))

def floor(request, flat_floor_id):

	residence_flats = Flat.objects.values_list('flat_number', flat=True).filter(flat_floor_id=flat_floor_id)
	template = loader.get_template('rooms/flats.html')
	context = RequestContext(request,{ 
		'residence_flats': residence_flats,
		})
	return HttpResponse(template.render(context))

def flat(request, flat_floor_id, flat_room_id):
	return HttpResponse("Displays the specific flat/room")