from principal.models import Center, UserAccount, Administrator, Teacher, Supervisor, Subject, Class, Score, Notification, Appointment, Student
from django.contrib import admin

admin.site.register(Center)
admin.site.register(UserAccount)
admin.site.register(Administrator)
admin.site.register(Teacher)
admin.site.register(Supervisor)
admin.site.register(Subject)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('course', 'letter')
admin.site.register(Class, ClassAdmin)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('mark', 'student', 'subject')
admin.site.register(Score, ScoreAdmin)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('date', 'reason')
admin.site.register(Notification, NotificationAdmin)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'reason')
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Student)


