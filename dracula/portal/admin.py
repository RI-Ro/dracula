from django.contrib import admin

# Register your models here.
from models import Region, Node, Edge

admin.site.register(Region)
admin.site.register(Node)
admin.site.register(Edge)
