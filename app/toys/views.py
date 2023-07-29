import time

from django.db import transaction
from django.db.models import F

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from toys.models import Order, Toy


FREE_TOY_ID = 1

# Possible solutions
# 1. Check constraint
# 2. Select for update
# 3. Higher serialization level


class ObtainFreeToyAPI(APIView):
    def post(self, request: Request) -> Response:
        with transaction.atomic():
            free_toy = Toy.objects.get(id=FREE_TOY_ID)

            time.sleep(3)

            if free_toy.quantity <= 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            free_toy.quantity = F("quantity") - 1
            free_toy.save()

            Order.objects.create(
                user=request.user,
                toy=free_toy,
            )

            return Response(status=status.HTTP_201_CREATED)
