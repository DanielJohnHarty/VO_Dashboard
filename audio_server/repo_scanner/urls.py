from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

app_name = 'repo_scanner'
urlpatterns = [
    path("", TemplateView.as_view(template_name="repo_scanner/scan_home.html"), name="home"),
]