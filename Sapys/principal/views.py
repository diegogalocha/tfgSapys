from principal.models import Center, UserAccount, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from principal.forms import AdministratorForm, AppointmentForm, CenterForm, ClassForm, NotificationForm, ScoreForm, StudentForm, SubjectForm, SupervisorForm, TeacherForm, UserAccountForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render_to_response('index.html')
#para crear formularios:
def new_appointment(request):
    if request.method == 'POST':
        formulario = AppointmentForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = AppointmentForm()
    return render_to_response('appointmentform.html', {'formulario':formulario}, context_instance = RequestContext(request))

#para listar

def appointmentList(request):
    appointments = Appointment.objects.all()
    return render_to_response('appointmentList.html',{'list':appointments})

