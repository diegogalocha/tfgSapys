import os
from django.contrib.auth.models import User
from principal.models import Center, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student

def populate():    
    userSave = add_user(username = "user4",
             password = "pbkdf2_sha256$10000$SwSCRXULwzhp$qUlcB2ve5QIUXPyVe6+XiALvF5m6itYNsa4OX//uZg0=")
    add_center(cif = "Y75789675",
               name = "IES Fernando de Herrera",
               email = "fernandodeherrera@gmail.com",
               description = "Colegio de Educacion Secundaria de la provincia de Sevilla")
    centerSave = add_center(cif = "K96761222",
               name = "IES Joaquin de Vedruna",
               email = "joaquindevedruna@gmail.com",
               description = "Colegio de Educacion Secundaria de la provincia de Sevilla")
    add_teacher(dni = "85525456L",
                name = "TeacherPop1",
                surname = "SurnameTeacherpop1",
                email = "pop1t@gmail.com",
                center = centerSave,
                userAccount = userSave)
            
def add_user(username,password):
    u = User.objects.get_or_create(username = username,password = password)[0]
    return u
def add_center(cif, name, email, description):
    c = Center.objects.get_or_create(cif = cif, name = name, email = email, description = description)[0]
    return c
def add_teacher(dni, name, surname, email, center, userAccount):
    t = Teacher.objects.get_or_create(dni = dni, name = name, surname = surname, email = email, center = center, userAccount = userAccount)[0]
    return t
# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    populate()
    print "Finished"