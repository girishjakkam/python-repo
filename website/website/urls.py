from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^skills/', include('persons.urls')),
    url(r'^accounts/login/$',views.login),
    url(r'^accounts/auth/$',views.auth_view),
    url(r'^accounts/logout/$',views.logout),
    url(r'^accounts/loggedin/$',views.loggedin),
    url(r'^accounts/invalid/$',views.invalid_login),
    url(r'^accounts/register/$',views.register),
    url(r'^accounts/register_success/$',views.register_success)

]

