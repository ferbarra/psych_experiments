# Prolific-Pavlovia Workflow

Prolific redirects participants to the Pavlovia experiment. To do this it needs the URL where the Pavlovia
experiment is hosted. Instead of redirecting directly to Pavlovia, the URL given to prolific should point
to this app so that a counter balancing parameter can be added. These URLs will look like this: 
www.psych_experiments.pythonanywhere.com/experpiments/<experiment_id>

Prolific adds the participant id as a parameter to the url before redirects.
Prolific will use this url to redirect participants to this link:
www.psych_experiments.pythonanywhere.com/experpiments/<experiment_id>?participant=1234

The app does counter balancing, adds the condition id as parameter and redirects to Pavlovia
www.pavlovia.com/...?particiant_id=<participant_id>&condition=<counter_balanced_condition>

Once the participant completes the experiment, pavlovia redirects participant to prolific. Our app doesn't
need to do anything else.
