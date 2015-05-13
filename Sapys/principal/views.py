from principal.models import Center, UserAccount, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from principal.forms import AdministratorForm, AppointmentForm, CenterForm, ClassForm, NotificationForm, ScoreForm, StudentForm, SubjectForm, SupervisorForm, TeacherForm, UserAccountForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import LoginForm


def index(request):
    return render_to_response('index.html')
#para crear formularios: HAY QUE CAMBIAR LOS REDIRECTS
def new_student(request):
    if request.method == 'POST':
        formulario = StudentForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = StudentForm()
    return render_to_response('studentform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_notification(request):
    if request.method == 'POST':
        formulario = NotificationForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = NotificationForm()
    return render_to_response('notificationform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_score(request):
    if request.method == 'POST':
        formulario = ScoreForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = ScoreForm()
    return render_to_response('scoreform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_class(request):
    if request.method == 'POST':
        formulario = ClassForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = ClassForm()
    return render_to_response('classform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_appointment(request):
    if request.method == 'POST':
        formulario = AppointmentForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = AppointmentForm()
    return render_to_response('appointmentform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_subject(request):
    if request.method == 'POST':
        formulario = SubjectForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = SubjectForm()
    return render_to_response('subjectform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_supervisor(request):
    if request.method == 'POST':
        formulario = SupervisorForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = SupervisorForm()
    return render_to_response('supervisorform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_teacher(request):
    if request.method == 'POST':
        formulario = TeacherForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = TeacherForm()
    return render_to_response('teacherform.html', {'formulario':formulario}, context_instance = RequestContext(request))

def new_userAccount(request):
    if request.method == 'POST':
        formulario = UserAccountForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserAccountForm()
    return render_to_response('useraccountform.html', {'formulario':formulario}, context_instance = RequestContext(request))


def new_center(request):
    if request.method == 'POST':
        formulario = CenterForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = CenterForm()
    return render_to_response('centerform.html', {'formulario':formulario}, context_instance = RequestContext(request))


#para listar
def userAccountList(request):
    userAccounts = UserAccount.objects.all()
    return render_to_response('userAccountList.html',{'list':userAccounts})

def studentList(request):
    students = Student.objects.all()
    return render_to_response('studentList.html',{'list':students})

def notificationList(request):
    notifications = Notification.objects.all()
    return render_to_response('notificationList.html',{'list':notifications})

def scoreList(request):
    scores = Score.objects.all()
    return render_to_response('scoreList.html',{'list':scores})
def classList(request):
    classes = Class.objects.all()
    return render_to_response('classList.html',{'list':classes})

def subjectList(request):
    subjects = Subject.objects.all()
    return render_to_response('subjectList.html',{'list':subjects})

def supervisorList(request):
    supervisors = Supervisor.objects.all()
    return render_to_response('supervisorList.html',{'list':supervisors})

def teacherList(request):
    teachers = Teacher.objects.all()
    return render_to_response('teacherList.html',{'list':teachers})

def appointmentList(request):
    appointments = Appointment.objects.all()
    return render_to_response('appointmentList.html',{'list':appointments})

def centerList(request):
    centers = Center.objects.all()
    return render_to_response('centerList.html',{'list':centers})

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correcto"
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()
    return render_to_response('login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))

def homepage(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('homepage')

