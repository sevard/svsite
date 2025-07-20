import os
import json
import requests
from django.shortcuts import render
from django.shortcuts import render
from dotenv import load_dotenv


load_dotenv()


def sha_functions(request):
    return render(request, 'webtools/sha_func.html')


IPSTACK_ACCESS_KEY = os.getenv('IPSTACK_API_KEY')  
IPSTACK_LOOKUP_URL = os.getenv('IPSTACK_URL')

def get_client_ip(request):
    """ Get IP address of the client. """

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        x_real_ip = request.headers.get('X-Real-Ip')
        if x_real_ip:
            ip = x_real_ip
    else:
        # On local the ip will be 127.0.0.1
        ip = request.META.get('REMOTE_ADDR')

    return ip


def ip_lookup(request):
    ip = get_client_ip(request)

    # For local development, override IP with public one
    if ip.startswith("127.") or ip == "::1":
        ip = "8.8.8.8"

    url = f"{IPSTACK_LOOKUP_URL}/{ip}?access_key={IPSTACK_ACCESS_KEY}"
    response = requests.get(url)
    data = response.json()

    ctx = {
        "ip": ip,
        "type": data.get("type"),
        "continent_code": data.get("continent_code"),
        "continent_name": data.get("continent_name"),
        "country_code": data.get("country_code"),
        "country_name": data.get("country_name"),
        "region_code": data.get("region_code"),
        "region_name": data.get("region_name"),
        "city": data.get("city"),
        "zip": data.get("zip"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "location": {
            "country_flag": data.get("location", {}).get("country_flag"),
        },
    }

    return render(request, "webtools/iplookup.html", {"ctx": ctx})
