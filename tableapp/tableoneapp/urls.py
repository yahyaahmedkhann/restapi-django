from django.urls import path
from .views import call_stored_procedure

urlpatterns = [
    path('get-users/', call_stored_procedure, name='get-users'),
]
