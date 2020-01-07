from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from totdapp.settings import SU_PASSWORD
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admintask1").exists():
            supassword= SU_PASSWORD
            User.objects.create_superuser("admintask1", "taskofthedayofficial1@gmail.com", supassword)
