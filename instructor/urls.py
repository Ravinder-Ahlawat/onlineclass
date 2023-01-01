## @brief urls for the instructor app.

from django.conf.urls import include
from django.contrib import admin
from . import views
from django.urls import re_path

## @brief url patterns for the instructor app.
urlpatterns = [
    re_path(r'^instructor_index/$', views.instructor_index, name='instructor_index'),
    re_path(r'^(?P<course_id>[0-9]+)/instructor_detail/$', views.instructor_detail, name='instructor_detail'),
    re_path(r'^(?P<course_id>[0-9]+)/add_assignment/$', views.add_assignment, name='add_assignment'),
    re_path(r'^(?P<course_id>[0-9]+)/add_resource/$', views.add_resource, name='add_resource'),
    re_path(r'^(?P<course_id>[0-9]+)/add_notification/$', views.add_notification, name='add_notification'),
    re_path(r'^(?P<course_id>[0-9]+)/view_all_assignments/$', views.view_all_assignments, name='view_all_assignments'),
    re_path(r'^(?P<assignment_id>[0-9]+)/view_all_submissions/$', views.view_all_submissions, name='view_all_submissions'),
    re_path(r'^(?P<assignment_id>[0-9]+)/view_feedback/$', views.view_feedback, name='view_feedback'),
]