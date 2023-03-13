import json
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from map.services.route_map import RouteMap
from django.http import JsonResponse

@csrf_exempt
def map(_):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

@csrf_exempt
def calculate_route(request):
  body = json.loads(request.body)
  source = body['source']
  target = body['target']

  # Construct file name
  route_map = RouteMap(os.path.join(settings.BASE_DIR, "corkCityData.txt"))
  (vertex_path, time) = route_map.find_route((source['latitude'], source['longitude']), (target['latitude'], target['longitude']))
  
  route = []

  for vertex in vertex_path:
    route.append({
      'latitude': vertex.coordinates()[0],
      'longitude': vertex.coordinates()[1],
    })

  return JsonResponse({ 'route': route })