from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from . import views

app_name = 'repo_scanner'
urlpatterns = [
    path("scan", views.scan, name="scan"),
    path("view_db", views.view_db, name="view_db"),
]