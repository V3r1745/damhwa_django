from django.urls import path
from login_api import views

urlpatterns = [path("id/", views.check_id), path("check/", views.check_account), path("create/", views.create_account)]
