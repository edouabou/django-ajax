from django.urls import path

from . import views

app_name = 'ajson'

urlpatterns = [
    path("getdata",views.getdata,name='getdata'),
    path("form-create",views.create, name='create')
]