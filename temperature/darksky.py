import requests
import json

API_KEY = "96b47f43f97fdc8f03d64785b9816c5f"
API_URL = "https://api.darksky.net/forecast"

def get_url(lat, long):
  formatted_url = "{}/{}/{},{}".format(API_URL, API_KEY, lat, long)
  return formatted_url

def make_api_call(url):
  response = requests.get(url)
  data = response.json()
  temperature = data['currently']['temperature']
  celsius = (temperature - 32) / 1.8
  celsius = round(celsius)
  return celsius
