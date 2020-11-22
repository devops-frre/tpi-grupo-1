from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from todolist.views import index
from django.contrib.auth.models import User, Group

urlpatterns = [
    path('', index, name='todolist'),
]

admin.site.site_header = "DevOps TPI"
admin.site.index_title = "DevOps Administration | Grupo Nº 1"
admin.site.site_title = "Grupo 1"

admin.site.unregister(Group)
admin.site.unregister(User)