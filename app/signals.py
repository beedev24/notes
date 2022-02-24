from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=School)
def create_institution(sender, instance, created, **kwargs):
    if created:
        Institution.objects.create(school=instance)

@receiver(post_save, sender=Subject)
def create_topic(sender, instance, created, **kwargs):
    if created:
        Topic.objects.create(subject=instance)

@receiver(post_save, sender=Note)
def create_memo(sender, instance, created, **kwargs):
    if created:
        Memo.objects.create(note=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=School)
def save_institution(sender, instance, **kwargs):
    instance.institution.save()

@receiver(post_save, sender=Subject)
def save_topic(sender, instance, **kwargs):
    instance.topic.save()

@receiver(post_save, sender=Note)
def save_memo(sender, instance, **kwargs):
    instance.memo.save()