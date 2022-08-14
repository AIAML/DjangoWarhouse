from django.urls import path

from . import views

urlpatterns = [
    path("PanelAdmin/", views.AdminPanelindex, name="AdminPanelindex", ),
    path("PanelUser/", views.AdminPanelindex, name="AdminPanelindex", ),
    path("Logout/", views.Logout, name="AdminPanelindex", ),
]
