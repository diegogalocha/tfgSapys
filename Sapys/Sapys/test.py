'''
Created on Jul 23, 2015

@author: Boss
'''
from principal.models import Center, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from django.contrib.auth.models import User


if __name__ == '__main__':
    teachers = Teacher.objects.all()
    users = User.objects.all()
    for teacher in teachers:
        for user in users:
            if(teacher.userAccount.username == user.username):
                print (user)
    supervisors = Supervisor.objects.all()
    
    for super in supervisors:
        for user in users:
            if(super.userAccount.username == user.username):
                print(super)