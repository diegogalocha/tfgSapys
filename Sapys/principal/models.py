from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Center(models.Model):
    cif = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=50, blank=False, verbose_name="Introduce el nombre del Centro")
    email = models.EmailField(help_text='Inserta tu e-mail')
    description = models.TextField(blank=False)
    
    def __unicode__(self):
        return self.name
    
class UserAccount(models.Model):
    username = models.CharField(max_length=32, unique=True) #el min_length lo haremos a nivel de formulario
    password = models.CharField(max_length=32, verbose_name='Contrasena')
    
    def __unicode__(self):
        return self.username
    
class Actor(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=20, blank=False, verbose_name="Introduzca su nombre")
    surname = models.CharField(max_length=40, blank=False)
    email = models.EmailField(help_text='Inserta tu email')
    
    center = models.ForeignKey(Center)
    userAccount = models.ForeignKey(UserAccount, blank=True) #Blank=True por pruebas
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.name
    
class Administrator(Actor):
    
    def __unicode__(self):
        return self.name

class Teacher(Actor):

    def __unicode__(self):
        return self.name
    
class Supervisor(Actor):

    def __unicode__(self):
        return self.name
    
class Appointment(models.Model):
    date = models.DateField(help_text='dd/mm/aaaa', verbose_name='Fecha de la Cita')
    reason = models.TextField(blank=False)
    
    supervisor = models.ForeignKey(Supervisor)
    teacher = models.ForeignKey(Teacher)
    
    def __unicode__(self):
        return self.teacher.name + self.supervisor.name
    
class Notification(models.Model):
    date = models.DateField(help_text='dd/mm/aaaa', verbose_name='Fecha de la Notificacion')
    reason = models.TextField(blank=False)
    description = models.TextField(blank=False)
    
    supervisor = models.ForeignKey(Supervisor)
    teacher = models.ForeignKey(Teacher)
    administrator = models.ForeignKey(Administrator, blank=True) #Esto hay que modificarlo porque no tiene porque crearla un administrador
    
    def __unicode__(self):
        return self.teacher.name + self.supervisor.name
    
class Class(models.Model):
    referenceNumber = models.CharField(max_length=15, unique=True)
    course = models.CharField(max_length=10)
    letter = models.CharField(max_length=1)
    
    administrator = models.ForeignKey(Administrator)
    teachers = models.ManyToManyField('Teacher', blank = False)
    
    def __unicode__(self):
        return self.course+'x'+self.letter
    
class Student(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=40, blank=False)
    birthday = models.DateField(help_text='dd/mm/aaaa')
    
    supervisor = models.ForeignKey(Supervisor)
    studentClass = models.ForeignKey(Class)
    administrator = models.ForeignKey(Administrator)
    
    def __unicode__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=20, blank=False)
    
    teacher = models.ForeignKey(Teacher)
    
    def __unicode__(self):
        return self.name
    
class Score(models.Model):
    mark = models.DecimalField(max_digits=4,decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    
    def __unicode__(self):
        return self.student.name
    

