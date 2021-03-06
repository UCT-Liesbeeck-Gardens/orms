from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext, loader

from .models import Flat, Floor, Application, Approval, Decline
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

 	#redirect on accessing the url directly
 	if request.method == 'GET':
 		return HttpResponseRedirect("/login/")

def applications(request):
	if request.user.is_authenticated():
		residence_applications = Application.objects.values_list('flat_number','student_number','gender')
		template = loader.get_template('admin/applications.html')
		context = RequestContext(request,{ 
			'residence_applications': residence_applications,
			})
		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect("/login/")

def application_details(request, flat_number, student_number):
	if request.user.is_authenticated():
		application_details = Application.objects.filter(flat_number=flat_number, student_number=student_number).values_list('flat_number', 'name', 'student_number', 'mobile_number','gender','date_of_application')
		template = loader.get_template('admin/application_details.html')
		context = RequestContext(request, {
			'application_details': application_details,
			})
		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect("/login/")

def approve_application(request, flat_number, student_number):
	if request.user.is_authenticated():
		approve_application = Application.objects.filter(flat_number=flat_number, student_number=student_number).values_list('flat_number', 'name','student_number', 'mobile_number', 'email_address','gender')
		anobject = Approval(flat_number=approve_application[0][0], name=approve_application[0][1], student_number=approve_application[0][2], mobile_number=approve_application[0][3], email_address=approve_application[0][4],gender=approve_application[0][5], date_of_approval=datetime.now())
		anobject.save()
		Application.objects.filter(flat_number=flat_number, student_number=student_number).delete()
		template = loader.get_template('admin/approve_application.html')
		context = RequestContext(request,{
			'anobject':anobject,
			})
		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect("/login/")

def decline_application(request, flat_number, student_number):
	if request.user.is_authenticated():
		decline_application = Application.objects.filter(flat_number=flat_number, student_number=student_number).values_list('flat_number', 'name','student_number', 'mobile_number', 'email_address','gender')
		anobject = Decline(flat_number=decline_application[0][0], name=decline_application[0][1], student_number=decline_application[0][2], mobile_number=decline_application[0][3], email_address=decline_application[0][4],gender=decline_application[0][5], date_of_decline=datetime.now())
		anobject.save()
		Application.objects.filter(flat_number=flat_number, student_number=student_number).delete()
		template = loader.get_template('admin/decline_application.html')
		context = RequestContext(request,{
			'anobject':anobject,
			})
		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect("/login/")