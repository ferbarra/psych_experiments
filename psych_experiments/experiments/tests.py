from django.test import TestCase
from psych_experiments.experiments.models import Experiment, Condition


class ExperimentTestCase(TestCase):

    def setUp(self):
        experiment = Experiment(name="Test Experiment", pavlovia_url="www.pavlovia.org")
        experiment.save()
        # create some conditions for the experiment
        experiment.condition_set.create(name='A')
        experiment.condition_set.create(name='X')
        experiment.condition_set.create(name='P')
        experiment.condition_set.create(name='H')

    def test_next_condition(self):
        experiment = Experiment.objects.filter(name="Test Experiment")[0]
        conditions = experiment.condition_set.all()
        count_by_conditions = {}
        for x in range(0, len(conditions) * 2):
            counter_balanced_condition = experiment.get_counter_balanced_condition()
            if count_by_conditions.get(counter_balanced_condition.name, None) is None:
                count_by_conditions[counter_balanced_condition.name] = 0
            count_by_conditions[counter_balanced_condition.name] += 1

        # Verify that all the conditions have been returned the same number of times
        self.assertEqual(2, count_by_conditions['A'])
        self.assertEqual(2, count_by_conditions['X'])
        self.assertEqual(2, count_by_conditions['P'])
        self.assertEqual(2, count_by_conditions['H'])
