from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients', views.get_all_patients)
]