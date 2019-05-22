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
    regex = re.compile(r'^([\-]?[\d]{1,2}[\.]?[\d]{1,4})$')
    errors = []
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if not latitude or not longitude:
            errors.append('Please type a latitude and longitude value.')
        elif regex.match(latitude) and regex.match(longitude):
            post_url = get_url(latitude, longitude)
            celsius = make_api_call(post_url)
            return render(request, 'temperature/home.htm', {
                "lat": latitude,
                "long": longitude,
                "celsius": celsius
            })
        else:
            errors.append('Please type a valid value. Examples: "23.454", "12", "-12.342"')
        return render(request, 'temperature/home.htm', {'errors': errors})
