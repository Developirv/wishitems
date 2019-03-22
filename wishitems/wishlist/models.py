from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=420)
    pub_date = models.DateTimeField('date published')
##{% for item in item_list %}

##{% empty %}

##{% endfor %}

