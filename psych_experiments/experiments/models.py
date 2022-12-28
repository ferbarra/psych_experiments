from django.core.validators import MinValueValidator
from django.db import models


class Experiment(models.Model):
    """
    Represents an experiment hosted in Pavlovia.com. Each experiment has a set of conditions. Participants accessing
    the experiment must be assigned a condition in such a way that
    """
    name = models.CharField(max_length=200)

    # 0 based index used for counter balancing experiment conditions
    last_condition_index = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    pavlovia_url = models.URLField()

    def get_counter_balanced_condition(self):
        conditions = self.condition_set.all()
        condition = conditions[self.last_condition_index]

        # update the index round-robin like
        if self.last_condition_index == len(conditions) - 1:
            self.last_condition_index = 0
        else:
            self.last_condition_index += 1

        return condition

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=200)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)

    class Meta:
        # The ordering is going to be used to counterbalance the conditions. The criteria for ordering doesn't matter,
        # the only important thing is to always get a list of conditions in the same order.
        ordering = ['name']

    def __str__(self):
        return self.name
