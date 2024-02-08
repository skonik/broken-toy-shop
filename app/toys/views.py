import threading
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
            print(threading.current_thread())

            updated_rows = Toy.objects.filter(
                id=FREE_TOY_ID,
                quantity__gt=0,
            ).update(quantity=F("quantity") - 1)

            time.sleep(10)

            toy = Toy.objects.get(id=FREE_TOY_ID)

            if updated_rows != 0:
                Order.objects.create(
                    user=None,
                    toy=toy,
                )
                return Response(status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_400_BAD_REQUEST)
