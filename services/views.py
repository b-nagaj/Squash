from django.shortcuts import render
from services.models import Service

def service_index(request):
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request, "services/service_index.html", context)