from django.core.validators import MinValueValidator
from django.db import models


class Experiment(models.Model):
    """
    Represents an experiment hosted in Pavlovia.com. Each experiment has a set of conditions. Participants accessing
    the experiment must be assigned a condition in such a way that
    """
    name = models.CharField()
    last_condition_index = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    pavlovia_url = models.URLField()

    def next_condition(self):
        pass

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField()
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)

    class Meta:
        # The ordering is going to be used to counterbalance the conditions. The criteria for ordering doesn't matter,
        # the only important thing is to always get a list of conditions in the same order.
        ordering = ['name']

    def __str__(self):
        return self.name
