from django.conf.urls import url
from . import views

appname='main'

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^signin$', views.signIn, name='signIn')
]
