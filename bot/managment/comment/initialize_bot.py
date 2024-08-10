from django.core.management.base import BaseCommand
import sys

class Command(BaseCommand):
    help = 'Initialize Telegram Bot'

    def handle(self, *args, **kwargs):
        if sys.version_info < (3, 8):
            self.stdout.write(self.style.ERROR('Python 3.8 or higher is required.'))
        else:
            self.stdout.write(self.style.SUCCESS('Environment is properly set up.'))
