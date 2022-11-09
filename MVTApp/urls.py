from django.urls import path

from MVTApp.views import mostrar_Familiares
urlpatterns = [
path('', mostrar_Familiares)
]