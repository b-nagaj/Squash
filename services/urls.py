from django.urls import path
from services import views

urlpatterns = [
    path("", views.service_index, name="service_index")
]