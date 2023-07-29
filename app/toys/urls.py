from django.urls import path

from toys.views import ObtainFreeToyAPI


urlpatterns = [
    path("obtain/free", ObtainFreeToyAPI.as_view()),
]
