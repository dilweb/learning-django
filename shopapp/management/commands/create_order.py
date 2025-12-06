from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Order

class Command(BaseCommand):
    """
    Creates command
    """

    def handle(self, *args, **kwargs):
        self.stdout.write("Create order")
        user = User.objects.get(username="dil")
        order = Order.objects.get_or_create(
            delivery_address="Some Stupid Street",
            promo="Some stupid SALE",
            user=user,
        )
        self.stdout.write(self.style.SUCCESS(f"Order created{order}"))