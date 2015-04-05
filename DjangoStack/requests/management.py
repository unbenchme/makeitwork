from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _

#if notification is installed in APPS, deploy notices
if "notification" in settings.INSTALLED_APPS:
    from pinax.notifications.models import NoticeType

    def create_notice_types(app, created_models, verbosity, **kwargs):
        #Notice types to send to users related to requests
        NoticeType.create("request_available", _("Request Available"), _("A new request is available"))
        NoticeType.create("request_accepted", _("Request Accepted"), _("Someone has accepted your request"))
        NoticeType.create("request_assigned", _("Assigned to Request"), _("Let's get to work"))

    signals.post_syncdb.connect(create_notice_types, sender=NoticeType)
else:
    print "Skipping creation of NoticeTypes as notification app not found"
