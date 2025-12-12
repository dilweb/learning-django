from django.urls import path

from .views import process_get_view, user_form

app_name = "requestdataapp"

urlpatterns = [
  path("process-get/", process_get_view, name="process_get"), 
  path("user-bio/", user_form, name="user_bio")
]
