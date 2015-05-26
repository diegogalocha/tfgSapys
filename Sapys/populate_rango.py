import os

import django
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
 


from principal.models import Center, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from django.db.models.fields import AutoField


django.setup()

us=User.objects.filter(is_superuser=False)
us.delete()

te=Teacher.objects.all()
te.delete()

ce=Center.objects.all()
ce.delete()

    
def populate():
   
    
    userTest=add_user(username = "user4", 
                      password = make_password("user4",salt=None,hasher='default'), 
                      email="user4@gmail.com")  
   
#     add_center(cif = "Y75789675",
#                name = "IES Fernando de Herrera",
#                email = "fernandodeherrera@gmail.com",
#                description = "Colegio de Educacion Secundaria de la provincia de Sevilla")
    centerSave = add_center(cif = "K96761222",
               name = "IES Joaquin de Vedruna",
               email = "joaquindevedruna@gmail.com",
               description = "Colegio de Educacion Secundaria de la provincia de Sevilla")
    
    add_teacher(dni = "85525456L",
                name = "TeacherPop1",
                surname = "SurnameTeacherpop1",
                email = "pop1t@gmail.com",
                center = centerSave,
                userAccount = userTest)
            
def add_user(username, password, email):
    
    u = User.objects.get_or_create(username=username, password=password, email=email)[0]
    
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
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sapys.settings")
    
    populate()
    print "Finished"