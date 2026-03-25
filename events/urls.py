from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("eventos/nuevo/", views.event_create, name="event_create"),
    path("eventos/<slug:slug>/", views.event_detail, name="event_detail"),
    path("inscripciones/<int:registration_id>/asistencia/", views.attendance_toggle, name="attendance_toggle"),
    path("certificados/verificar/", views.certificate_verify, name="certificate_verify"),
]
