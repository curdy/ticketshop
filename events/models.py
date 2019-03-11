from django.db import models

# Create your models here.
class Event(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    host        = models.CharField(max_length=100)
    #image       = models.ImageField()
    event_date  = models.CharField(max_length=100)
    event_time  = models.CharField(max_length=100)
    vanue       = models.CharField(max_length=100)

    def get_name(self):
        return self.name 

    def get_description(self):
        return self.description

    def get_host(self):
        return self.host

    def get_image(self):
        return self.image

    def get_event_date(self):
        return self.event_date

    def get_event_time(self):
        return self.event_time

    def __str__(self):
        return self.name
