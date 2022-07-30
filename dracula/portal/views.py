from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.http import HttpResponse
import random
import json
from models import Region
from models import Node
from models import Edge


def index(request):
    r = Region.objects.all()
    e = Edge.objects.all()
    n = Node.objects.all()
    e2 = [ { i :
            {"title":e[i].title,
            "point1":e[i].point1.title,
            'point2':e[i].point2.title,
            "weigth":e[i].weigth}} for i in range(0, len(e))]
    json1 = {
        'EDGE' : e2
    }
    json1 = json.dumps(json1)
    return render(request, 'portal/index.html', {'json1':json1, 'nodes':n, 'regions':r})

def get_json_node(request):
    if request.POST:
        key = request.POST['node_id']
    n_k = Node.objects.filter(id=key)
    e = Edge.objects.filter(Q(point1=n_k[0].id) | \
                            Q(point2=n_k[0].id) \
                            )
    e2 = [ { i :
            {"title":e[i].title,
            "point1":e[i].point1.title,
            'point2':e[i].point2.title,
            "weigth":e[i].weigth}} for i in range(0, len(e))]
    json1 = {
        'EDGE' : e2
        }
    json1 = json.dumps(json1)
    return HttpResponse(json1, content_type="application/json")

def get_json_region(request):
    if request.POST:
        key = request.POST['region_id']
    r = Region.objects.filter(id=key)
    n_k = Node.objects.filter(region=r)
    e = Edge.objects.filter(Q(point1=n_k[0].id) | \
                            Q(point2=n_k[0].id) \
                            )
    e2 = [ { i :
            {"title":e[i].title,
            "point1":e[i].point1.title,
            'point2':e[i].point2.title,
            "weigth":e[i].weigth}} for i in range(0, len(e))]
    json1 = {
        'EDGE' : e2
        }
    json1 = json.dumps(json1)
    return HttpResponse(json1, content_type="application/json")
