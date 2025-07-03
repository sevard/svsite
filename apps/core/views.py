import json
import os
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def certs(request):
    # TODO: load data from DB
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    certs_json = os.path.join(BASE_DIR, "data", "certs.json")
    with open(certs_json, 'r') as f:
        data = json.load(f)

    return render(request, 'core/certs.html', {"certificates": data})
