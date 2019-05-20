# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from darksky import get_url, make_api_call

# Create your views here.
@csrf_exempt
def home(request):
    return render(request, "temperature/home.htm")

@csrf_exempt
def post_temperature(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        post_url = get_url(latitude, longitude)
        celsius = make_api_call(post_url)
        return render(request, 'temperature/home.htm', {
            "lat": latitude,
            "long": longitude,
            "celsius": celsius
        })
