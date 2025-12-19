from django.urls import path

from .views import api_overview, GroupsListView

app_name = "DRF"

urlpatterns = [
    path("apiview/", api_overview, name="api_overview"),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
]
