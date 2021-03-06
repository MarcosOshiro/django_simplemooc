from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'^registrar/$', views.register, name='register'),
    url(r'^resetar-senha/$', views.password_reset, name='password_reset'),
    url(r'^editar/$', views.edit, name='edit'),
    url(r'^editar-senha/$', views.edit_password, name='edit_password'),
    url(r'^confirmar-senha/(?P<key>\w+)/$', views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout')
]
