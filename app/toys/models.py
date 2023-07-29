from django.conf import settings
from django.db import models
from django.db.models import CheckConstraint, Q


class Toy(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(name="check_quantity_constraint", check=Q(quantity__gte=0)),
        ]

    def __str__(self):
        return f"<{self.__class__.__name__} name={self.name}, quantity={self.quantity}>"


class Order(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    toy = models.ForeignKey(to=Toy, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"<{self.__class__.__name__} user={self.user}, toy={self.toy}>"
