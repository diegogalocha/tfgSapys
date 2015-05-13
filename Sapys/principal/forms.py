#encoding:utf-8

from django.forms import ModelForm
from django import forms
from principal.models import Center, UserAccount, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
    
class CenterForm(ModelForm):
    class Meta:
        model = Center
        
class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        
class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        
class SupervisorForm(ModelForm):
    class Meta:
        model = Supervisor
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        
class ClassForm(ModelForm):
    class Meta:
        model = Class
        
class ScoreForm(ModelForm):
    class Meta:
        model = Score
        
class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        
