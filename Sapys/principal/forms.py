#encoding:utf-8

from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from principal.models import Center, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from django.contrib.admin import widgets

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ()
           
class CenterForm(ModelForm):
    class Meta:
        model = Center
        exclude = ()
class UserAccountForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
    
class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        exclude = ()
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ()
class SupervisorForm(ModelForm):
    class Meta:
        model = Supervisor
        exclude = ()
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        exclude = ()
class ClassForm(ModelForm):
    class Meta:
        model = Class
        exclude = ()
class ScoreForm(ModelForm):
    class Meta:
        model = Score
        exclude = ()
class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        exclude = ()
class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ()
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())