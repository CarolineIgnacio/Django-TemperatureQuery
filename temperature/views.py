# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from darksky import get_url, make_api_call

# Create your views here.
@csrf_exempt
def home(request):
    return render(request, "temperature/home.htm")


@csrf_exempt
def post_temperature(request):
    regex = re.compile(r'^[-\d]{2,3}|[\d]{2}$')
    errors = []
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if not latitude or not longitude:
            errors.append('Please enter a latitude and longitude value.')
            #adicionar condicao caso nao de match com o regex
        else:
            post_url = get_url(latitude, longitude)
            celsius = make_api_call(post_url)
            return render(request, 'temperature/home.htm', {
                "lat": latitude,
                "long": longitude,
                "celsius": celsius
            })
        return render(request, 'temperature/home.htm', {'errors': errors})
