from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext, loader

from .models import Flat, Floor, Application
from datetime import datetime
from django.contrib import auth


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

def flat(request, flat_floor_id, flat_number):

	flat = Flat.objects.filter(flat_floor_id=flat_floor_id, flat_number=flat_number).values_list('flat_number', 'flat_type')
	template = loader.get_template('rooms/flat_detail.html')
	context = RequestContext(request, {
		'flat': flat,
		})
	return HttpResponse(template.render(context))


def apply(request, flat_floor_id, flat_number):
	if request.method == 'POST':
		flat_number = flat_number
		name = request.POST.get('name','')
		student_number = request.POST.get('student_number','')
		gender = request.POST.get('gender','')
		mobile_number = request.POST.get('mobile_number','')
		date_of_application = datetime.now()

		application = Application(flat_number=flat_number, name=name,student_number=student_number, gender=gender ,mobile_number=mobile_number, email_address=student_number+'@myuct.ac.za',date_of_application=date_of_application)
		application.save()

		flat = Flat.objects.filter(flat_floor_id=flat_floor_id, flat_number=flat_number).values_list('flat_number', 'flat_type')
		template = loader.get_template('rooms/apply_confirmation.html')
		context = RequestContext(request, {
			'flat': flat,
			})
	return HttpResponse(template.render(context))


def login(request):

	template = loader.get_template('registration/login.html')
	context = RequestContext(request,{ 
		'login': login,
		})
	return HttpResponse(template.render(context))


def supervisor(request):
	if not request.user.is_authenticated():
		return HttpResponse(loader.get_template('admin/admin_index.html').render()) 	


def logout(request):
 	auth.logout(request)
 	# Redirect to a success page.
 	return HttpResponse(loader.get_template('admin/admin_index.html').render())


def authenticate(request):
	if request.method == 'POST':
 		username = request.POST['username']
 		password = request.POST['password']
 		user = auth.authenticate(username=username, password=password)
 		template = loader.get_template('admin/admin_index.html')
 		context = RequestContext(request,{
 			'user':user,
 			})
 		if user is not None and user.is_active:
 			# Correct password, and the user is marked "active"
 			auth.login(request, user)
 			# Redirect to a success page.
 			return HttpResponse(template.render(context))

 		# if user is not None and user.is_active:
 		# 	# Correct password, and the user is marked "active"
 		# 	auth.login(request, user)
 		# 	# Redirect to a success page.
 		# 	return HttpResponseRedirect("/supervisor/")
 		# else:
 		# 	# Show an error page
 		# 	return HttpResponseRedirect("/login/")
 	if request.method == 'GET':
 		return HttpResponseRedirect("/login/")