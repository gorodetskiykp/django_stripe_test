from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'stripe_app'
urlpatterns = [
    path("buy/<int:id>", views.buy, name="buy"),
    path("item/<int:id>", views.item, name="item"),
    path("success", TemplateView.as_view(template_name="success.html"), name="success"),
    path("cancel", TemplateView.as_view(template_name="cancel.html"), name="cancel"),
]
