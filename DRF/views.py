from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


from django.contrib.auth.models import Group

from .serializers import GroupSerializer

@api_view()
def api_overview(request: Request) -> Response:
    return Response({
        "message": "Welcome to DRF API"})


class GroupsListView(GenericAPIView, ListModelMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self, request: Request) -> Response:
        return self.list(request)