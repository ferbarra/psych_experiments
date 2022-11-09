from django.db import models


class Experiment(models.Model):
    number_of_conditions = models.IntegerField()
