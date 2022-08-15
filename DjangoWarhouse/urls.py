from django.contrib import admin
from django.urls import path, include
from Login.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", include("Login.urls")),
    path("Panel/", include("Panel.urls"))
]

handler404 = "Panel.views.page_not_found_view"