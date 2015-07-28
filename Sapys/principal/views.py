from principal.models import Center, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from principal.forms import AdministratorForm, AppointmentForm, CenterForm, ClassForm, NotificationForm, ScoreForm, StudentForm, SubjectForm, SupervisorForm, TeacherForm, UserAccountForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import LoginForm
import json
from datetime import datetime
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import hashlib

def appointmentList(request):
    appointments = Appointment.objects.all()
    teachers = Teacher.objects.all()
    users = User.objects.all()
    return render_to_response('appointmentList.html', {'appointments':appointments, 'teachers':teachers, 'users':users,}, context_instance = RequestContext(request))

def new_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentList')
    else:
        form = StudentForm()
    return render_to_response('student_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notificationList')
    else:
        form = NotificationForm()
    return render_to_response('notification_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_score(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scoreList')
    else:
        form = ScoreForm()
    return render_to_response('score_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classList')
    else:
        form = ClassForm()
    return render_to_response('class_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_appointment(request):
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointmentList')
    else:
        form = AppointmentForm()
    return render_to_response('appointment_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjectList')
    else:
        form = SubjectForm()
    return render_to_response('subject_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_supervisor(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supervisorList')
    else:
        form = SupervisorForm()
    return render_to_response('supervisor_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherList')
    else:
        form = TeacherForm()
    return render_to_response('teacher_new.html', {'forms':form}, context_instance = RequestContext(request))

def new_userAccount(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userAccountList')
    else:
        form = UserAccountForm()
    return render_to_response('userAccount_new.html', {'forms':form}, context_instance = RequestContext(request))


def new_center(request):
    if request.method == 'POST':
        form = CenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centerList')
    else:
        form = CenterForm()
    return render_to_response('center_new.html', {'forms':form}, context_instance = RequestContext(request))

#Para editar
def edit_appointment(request, appointment_id):
    appointment=get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointmentList')
    else:
        form = AppointmentForm(instance=appointment)
    return render_to_response('appointment_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_student(request, student_id):
    student=get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentList')
    else:
        form = StudentForm(instance=student)
    return render_to_response('student_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_notification(request, notification_id):
    notification=get_object_or_404(Notification, pk=notification_id)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('notificationList')
    else:
        form = NotificationForm(instance=notification)
    return render_to_response('notification_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_score(request, score_id):
    score=get_object_or_404(Score, pk=score_id)
    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('scoreList')
    else:
        form = ScoreForm(instance=score)
    return render_to_response('score_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_class(request, class_id):
    class_=get_object_or_404(Appointment, pk=class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_)
        if form.is_valid():
            form.save()
            return redirect('classList')
    else:
        form = ClassForm(instance=class_)
    return render_to_response('class_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_subject(request, subject_id):
    subject=get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjectList')
    else:
        form = SubjectForm(instance=subject)
    return render_to_response('subject_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_supervisor(request, supervisor_id):
    supervisor=get_object_or_404(Supervisor, pk=supervisor_id)
    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            return redirect('supervisorList')
    else:
        form = SupervisorForm(instance=supervisor)
    return render_to_response('supervisor_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_teacher(request, teacher_id):
    teacher=get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacherList')
    else:
        form = TeacherForm(instance=teacher)
    return render_to_response('teacher_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_userAccount(request, userAccount_id):
    userAccount=get_object_or_404(User, pk=userAccount_id)
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=userAccount)
        if form.is_valid():
            form.save()
            return redirect('userAccountList')
    else:
        form = UserAccountForm(instance=userAccount)
    return render_to_response('userAccount_edit.html', {'forms':form}, context_instance = RequestContext(request))

def edit_center(request, center_id):
    center=get_object_or_404(Center, pk=center_id)
    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            return redirect('centerList')
    else:
        form = CenterForm(instance=center)
    return render_to_response('center_edit.html', {'forms':form}, context_instance = RequestContext(request))

#para listar
def userAccountList(request):
    userAccounts = User.objects.all()
    return render_to_response('userAccountList.html',{'userAccounts':userAccounts}, context_instance = RequestContext(request))

def studentList(request):
    students = Student.objects.all()
    return render_to_response('studentList.html',{'students':students}, context_instance = RequestContext(request))

def notificationList(request):
    notifications = Notification.objects.all()
    return render_to_response('indexTeacher.html',{'notifications':notifications}, context_instance = RequestContext(request))

def scoreList(request):
    scores = Score.objects.all()
    return render_to_response('scoreList.html',{'scores':scores}, context_instance = RequestContext(request))
def classList(request):
    classes = Class.objects.all()
    return render_to_response('classList.html',{'classes':classes}, context_instance = RequestContext(request))

def subjectList(request):
    subjects = Subject.objects.all()
    return render_to_response('subjectList.html',{'subjects':subjects}, context_instance = RequestContext(request))

def supervisorList(request):
    supervisors = Supervisor.objects.all()
    return render_to_response('supervisorList.html',{'supervisors':supervisors}, context_instance = RequestContext(request))

def teacherList(request):
    teachers = Teacher.objects.all()
    return render_to_response('teacherList.html',{'teachers':teachers}, context_instance = RequestContext(request))

# def get_queryset(self):
#         self.supervisor = get_object_or_404(Supervisor, name__iexact=self.args[0])
#         return Appointment.objects.filter(supervisor=self.supervisor)
  
def centerList(request):
    centers = Center.objects.all()
    return render_to_response('centerList.html',{'centers':centers}, context_instance = RequestContext(request))

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
                    return redirect('homepage')
                else:
                    message = "Your user is inactive"
            else:
                message = "Username and/or wrong password"
         
    else:
        form = LoginForm()
         
    return render_to_response('login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))
     

           

def homepage(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('homepage')

