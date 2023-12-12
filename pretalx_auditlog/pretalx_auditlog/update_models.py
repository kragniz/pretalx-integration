# this is a special file - it will regenerate the models.py file - which in turn
# will be converted to migrations when you run ./manage.py makemigrations pretalx_auditlog
# you should not run it blindly but merge it carefully with the existing version


from collections import defaultdict
import inspect

import pretalx.submission.models as submission_models
import pretalx.common.models as common_models
import pretalx.event.models as event_models
import pretalx.mail.models as mail_models
import pretalx.person.models as person_models
import pretalx.schedule.models as schedule_models

from django.db import models

template = """
@pghistory.track(
    pghistory.Snapshot(), pghistory.BeforeDelete(), exclude={1})
class {0}Proxy({0}):
    class Meta:
        proxy=True
"""


# fields that should not be logged. Some models get updated very frequently, some
# values should not be shown, such as tokens and (hashed) passwords
exclude_fields = {
    "Event": ["updated"],
    "TeamInvite": ["token"],
    "User": ["password"],
    "Submission": ["invitation_token"],
    "Review": ["updated"],
    "Answer": ["updated"]
}

exclude_models = ["PretalxModel", "ActivityLog"] # abstract classes or not useful

print("import pghistory")


for i in [submission_models, common_models, mail_models, event_models, person_models, schedule_models]:
    items = list(inspect.getmembers(i, inspect.isclass))
    for item in items:
        if issubclass(item[1], models.Model):
            if item[0] in exclude_models:
                pass
            print(f"from {i.__name__} import {item[0]}")
            print(template.format(item[0], str(exclude_fields.get(item[0], []))))

