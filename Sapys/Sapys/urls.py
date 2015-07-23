from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^appointments/$','principal.views.appointmentList', name="appointmentList"),
    url(r'^appointment/new/$','principal.views.new_appointment', name="new_appointment"),
    url(r'^appointment/edit/(?P<appointment_id>\d+)/$','principal.views.edit_appointment', name="edit_appointment"),
    url(r'^centers/$','principal.views.centerList', name="centerList"),
    url(r'^center/new/$','principal.views.new_center', name="new_center"),
    url(r'^center/edit/(?P<center_id>\d+)/$','principal.views.edit_center', name="edit_center"),
    url(r'^classes/$','principal.views.classList', name="classList"),
    url(r'^class/new/$','principal.views.new_class', name="new_class"),
    url(r'^class/edit/(?P<class_id>\d+)/$','principal.views.edit_class', name="edit_class"),
    url(r'^notifications/$','principal.views.notificationList', name="notificationList"),
    url(r'^notification/new/$','principal.views.new_notification', name="new_notification"),
    url(r'^notification/edit/(?P<notification_id>\d+)/$','principal.views.edit_notification', name="edit_notification"),
    url(r'^scores/$','principal.views.scoreList', name="scoreList"),
    url(r'^score/new/$','principal.views.new_score', name="new_score"),
    url(r'^score/edit/(?P<score_id>\d+)/$','principal.views.edit_score', name="edit_score"),
    url(r'^students/$','principal.views.studentList', name="studentList"),
    url(r'^student/new/$','principal.views.new_student', name="new_student"),
    url(r'^student/edit/(?P<student_id>\d+)/$','principal.views.edit_student', name="edit_student"),
    url(r'^subjects/$','principal.views.subjectList', name="subjectList"),
    url(r'^subject/new/$','principal.views.new_subject', name="new_subject"),
    url(r'^subject/edit/(?P<subject_id>\d+)/$','principal.views.edit_subject', name="edit_subject"),
    url(r'^supervisors/$','principal.views.supervisorList', name="supervisorList"),
    url(r'^supervisor/new/$','principal.views.new_supervisor', name="new_supervisor"),
    url(r'^supervisor/edit/(?P<supervisor_id>\d+)/$','principal.views.edit_supervisor', name="edit_supervisor"),
    url(r'^teachers/$','principal.views.teacherList', name="teacherList"),
    url(r'^teacher/new/$','principal.views.new_teacher', name="new_teacher"),
    url(r'^teacher/edit/(?P<teacher_id>\d+)/$','principal.views.edit_teacher', name="edit_teacher"),
    url(r'^userAccounts/$','principal.views.userAccountList', name="userAccountList"),
    url(r'^userAccount/new/$','principal.views.new_userAccount', name="new_userAccount"),
    url(r'^userAccount/edit/(?P<userAccount_id>\d+)/$','principal.views.edit_userAccount', name="edit_userAccount"),
    url(r'^login/$','principal.views.login_page', name="login"),
    url(r'^$','principal.views.homepage', name="homepage"),
    url(r'^logout/$','principal.views.logout_view', name="logout"),
    
    )
