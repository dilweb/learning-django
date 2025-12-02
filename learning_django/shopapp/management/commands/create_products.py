from django.core.management import BaseCommand

class Command(BaseCommand):
    """
    Creates command
    """

    def handle(self, *args, **kwargs):
        self.stdout.write("Create products")
        self.stdout.write(self.style.SUCCESS("Products created"))