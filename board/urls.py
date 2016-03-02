from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^msg$', views.msg_submit, name='msg_submit'),
    url(r'^destroy$', views.destroy_all, name='destroy_all'),
]
