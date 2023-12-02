# Register your receivers here
from django.dispatch import receiver
from django.urls import resolve, reverse
from pretalx.orga.signals import nav_event, nav_global

from . import models  # NOQA


@receiver(nav_event, dispatch_uid="event_audit_log")
def navbar_info_event(sender, request, **kwargs):
    if not request.user.has_perm("person.is_administrator", None):
        return []
    return [
        {
            "label": "Audit-log",
            "icon": "wpforms",
            "url": reverse(
                "plugins:pretalx_auditlog:auditlog",
            ),
            "active": False,
        }
    ]


@receiver(nav_global, dispatch_uid="audit_log")
def navbar_info(sender, request, **kwargs):
    url = resolve(request.path_info)
    if not request.user.has_perm("person.is_administrator", None):
        return []
    return [
        {
            "label": "Audit-log",
            "icon": "wpforms",
            "url": reverse(
                "plugins:pretalx_auditlog:auditlog",
            ),
            "active": url.url_name == "auditlog",
        }
    ]
