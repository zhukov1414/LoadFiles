from django.db.models.signals import post_save
from django.dispatch import receiver


from files.models import File


@receiver(post_save, sender=File)
def set_processed_true(sender, instance, **kwargs):
    if not instance.processed:
        instance.processed = True
        instance.save()
