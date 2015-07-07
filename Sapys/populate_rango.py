import os

import django
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from principal.models import Center, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from django.db.models.fields import AutoField

django.setup()

us=User.objects.filter(is_superuser=False)
us.delete()


def populate():
    center1 = add_center(cif = "K96761222", name = "IES Joaquin de Vedruna",email = "joaquindevedruna@gmail.com", description = "Colegio de Educacion Secundaria de la provincia de Sevilla", provincia = "SEVILLA")
    center2 = add_center(cif = "K96761223", name = "IES Maria Magdalena",email = "mmagdalenaies@gmail.com", description = "Colegio de Educacion Secundaria de la provincia de Sevilla", provincia = "SEVILLA")
    center3 = add_center(cif = "K96761224", name = "IES Jose Ponce",email = "jponceies@gmail.com", description = "Colegio de Educacion Secundaria de la provincia de Cadiz", provincia = "CADIZ")
    center4 = add_center(cif = "K96761225", name = "IES Alfredo Ruiz",email = "alfruizies@gmail.com", description = "Colegio de Educacion Secundaria de la provincia de Cadiz", provincia = "CADIZ")
    
    userAdmin = add_user(username = "admin1",password = make_password("admin1",salt=None,hasher='default'),email="admin1@gmail.com")
    userTeacher1 = add_user(username = "teacher1",password = make_password("teacher1",salt=None,hasher='default'),email="teacher1@gmail.com")
    userTeacher2 = add_user(username = "teacher2",password = make_password("teacher2",salt=None,hasher='default'),email="teacher2@gmail.com")
    userSuper1 = add_user(username = "super1",password = make_password("super1",salt=None,hasher='default'),email="super1@gmail.com")
    userSuper2 = add_user(username = "super2",password = make_password("super2",salt=None,hasher='default'),email="super2@gmail.com")
    userSuper3 = add_user(username = "super3",password = make_password("super3",salt=None,hasher='default'),email="super3@gmail.com")
    userSuper4 = add_user(username = "super4",password = make_password("super4",salt=None,hasher='default'),email="super4@gmail.com")
    
    admin1 = add_admin(dni = "00000011H",name = "Admin",surname = "SurnameAdmin",email = "admin@gmail.com",center = center1,userAccount = userAdmin)
    teacher1 = add_teacher(dni = "85525456L",name = "Teacher1",surname = "SurnameTeacher1",email = "teacher1@gmail.com",center = center1,userAccount = userTeacher1)
    teacher2 = add_teacher(dni = "25262728J",name = "Teacher2",surname = "SurnameTeacher2",email = "teacher2@gmail.com",center = center1,userAccount = userTeacher2)
    super1 = add_super(dni = "12131415L",name = "Super1",surname = "SurnameSuper1",email = "super1@gmail.com",center = center1,userAccount = userSuper1)
    super2 = add_super(dni = "23242526J",name = "Super2",surname = "SurnameSuper2",email = "super2@gmail.com",center = center1,userAccount = userSuper2)
    super3 = add_super(dni = "98979495H",name = "Super3",surname = "SurnameSuper3",email = "super3@gmail.com",center = center1,userAccount = userSuper3)
    super4 = add_super(dni = "87858682B",name = "Super4",surname = "SurnameSuper4",email = "super4@gmail.com",center = center1,userAccount = userSuper4)
    
    add_appointment(date = "2015-10-25", reason = "This is the reason of Appointment1", supervisor = super1, teacher = teacher1)
    add_appointment(date = "2015-10-26", reason = "This is the reason of Appointment2", supervisor = super2, teacher = teacher2)
    
    add_notification(date = "2015-05-25", reason = "This is the reason of Notification1", description = "This is the description of Notification1", supervisor = super3, teacher = teacher1, administrator = admin1)
    add_notification(date = "2015-05-19", reason = "This is the reason of Notification2", description = "This is the description of Notification2", supervisor = super4, teacher = teacher2, administrator = admin1)
    
    teachersToClass = [teacher1, teacher2]
    
    class1 = add_class(referenceNumber = "100001", course = "Second", letter = "A", teachers = teachersToClass, administrator = admin1)
    class2 = add_class(referenceNumber = "100003", course = "Third", letter = "B", teachers = teachersToClass, administrator = admin1)
    
    student1 = add_student(dni = "55661122F", name = "Student1", surname = "SurnameStudent1", birthday = "1999-02-25", supervisor = super1, studentClass = class1, administrator = admin1)
    student2 = add_student(dni = "66558877L", name = "Student2", surname = "SurnameStudent2", birthday = "1999-10-15", supervisor = super2, studentClass = class1, administrator = admin1)
    student3 = add_student(dni = "99880011D", name = "Student3", surname = "SurnameStudent3", birthday = "1998-11-10", supervisor = super3, studentClass = class2, administrator = admin1)
    student4 = add_student(dni = "77445522D", name = "Student4", surname = "SurnameStudent4", birthday = "1998-04-12", supervisor = super4, studentClass = class2, administrator = admin1)  
    
    subject1 = add_subject(name = "Subject1", teacher = teacher1)
    subject2 = add_subject(name = "Subject2", teacher = teacher2)
    
    score1 = add_score(mark = "6.52", student = student1, subject = subject1)
    score2 = add_score(mark = "7.12", student = student2, subject = subject1)
    score3 = add_score(mark = "4.22", student = student3, subject = subject2)
    score4 = add_score(mark = "9.52", student = student4, subject = subject2)
        
def add_user(username, password, email):
    u = User.objects.get_or_create(username=username, password=password, email=email)[0]
    return u
    
def add_center(cif, name, email, description, provincia):
    c = Center.objects.get_or_create(cif = cif, name = name, email = email, description = description, provincia = provincia)[0]
    return c

def add_teacher(dni, name, surname, email, center, userAccount):
    t = Teacher.objects.get_or_create(dni = dni, name = name, surname = surname, email = email, center = center, userAccount = userAccount)[0]
    return t
def add_admin(dni, name, surname, email, center, userAccount):
    a = Administrator.objects.get_or_create(dni = dni, name = name, surname = surname, email = email, center = center, userAccount = userAccount)[0]
    return a

def add_super(dni, name, surname, email, center, userAccount):
    s = Supervisor.objects.get_or_create(dni = dni, name = name, surname = surname, email = email, center = center, userAccount = userAccount)[0]
    return s

def add_appointment(date, reason, supervisor, teacher):
    a = Appointment.objects.get_or_create(date = date, reason = reason, supervisor = supervisor, teacher = teacher)[0]
    return a

def add_notification(date, reason, description, supervisor, teacher, administrator):
    n = Notification.objects.get_or_create(date = date, reason = reason, description = description, supervisor = supervisor, teacher = teacher, administrator = administrator)[0]
    return n

def add_class(referenceNumber, course, letter, teachers, administrator):
    c = Class.objects.get_or_create(referenceNumber = referenceNumber, course = course, letter = letter, administrator = administrator)[0]
    c.teachers.add(*Teacher.objects.filter(name__in=[teachers]))
    return c

def add_student(dni, name, surname, birthday, supervisor, studentClass, administrator):
    s = Student.objects.get_or_create(dni = dni, name = name, surname = surname, birthday = birthday, supervisor = supervisor, studentClass = studentClass, administrator = administrator)[0]
    return s

def add_subject(name, teacher):
    s = Subject.objects.get_or_create(name = name, teacher = teacher)[0]
    return s

def add_score(mark, student, subject):
    s = Score.objects.get_or_create(mark = mark, student = student, subject = subject)[0]
    return s


# Start execution here!
if __name__ == '__main__':
    
    print "Starting Rango population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sapys.settings")
    
    populate()
    print "Finished"