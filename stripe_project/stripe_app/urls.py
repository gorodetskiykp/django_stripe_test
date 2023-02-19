from django.urls import path
from . import views

app_name = 'stripe_app'
urlpatterns = [
    path("buy/<int:id>", views.buy, name="buy"),
    path("item/<int:id>", views.item, name="item"),
]
