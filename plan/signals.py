from django.db.models import signals
from django.dispatch import receiver

from .models import VisitAgenda, VisitLog

@receiver(signals.post_save, sender=VisitAgenda, dispatch_uid="create_visit_log")
def create_log(sender, instance, **kwargs):
    if kwargs['created'] == True:
        log = VisitLog.objects.create(status="CREATED", visit=instance)
        log.save()
    else:
        log = VisitLog.objects.create(status=instance.status, visit=instance)
        log.save()

# @receiver(signals.post_save, sender=VisitLog, dispatch_uid="update_visit_status")
# def update_status(sender, instance, **kwargs):
#     if kwargs['created'] == True:
#         instance.visit.status = instance.status
#         instance.visit.save()
