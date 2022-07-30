from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Region(models.Model):
    title = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ['title']


class Node(models.Model):
    title = models.CharField(max_length=100)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=100)
    color = models.CharField(max_length=7, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ['title']

class Edge(models.Model):
    title = models.CharField(max_length=15)
    weigth = models.PositiveIntegerField(default=0)
    point1 = models.ForeignKey(Node, related_name='edge_point1')
    point2 = models.ForeignKey(Node, related_name='edge_point2')
    line_color = models.CharField(max_length=7, null=True, default="#008000")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ['title']
