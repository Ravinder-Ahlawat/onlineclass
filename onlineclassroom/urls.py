## @brief urls for the website.
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import re_path

## @brief url patterns for the website.
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/', views.login_user, name='login_user'),
    re_path(r'^register_user/$', views.register_user, name='register_user'),
    re_path(r'^logout/$', views.logout_user, name='logout_user'),
    re_path(r'^course/', include(('course.urls', 'course'), namespace='course')),
    re_path(r'^instructor/', include(('instructor.urls', 'instructor'), namespace='instructor')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)