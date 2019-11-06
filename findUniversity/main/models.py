from django.db import models

class Domein(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

class Speciality(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField()
    domein = models.ForeignKey('Domein', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
