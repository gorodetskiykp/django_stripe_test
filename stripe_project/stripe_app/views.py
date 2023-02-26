from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.urls import reverse
from .models import Item

import stripe

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


def buy(request, id):
    """При выполнении этого метода c
    бэкенда с помощью python библиотеки stripe должен выполняться
    запрос stripe.checkout.Session.create(...) и полученный session.id
    выдаваться в результате запроса"""
    item = get_object_or_404(Item, pk=id)
    print(item.name, item.price)
    product = stripe.Product(name=item.name)
    print(product)
    price = stripe.Price(
        product=product,
        currency='usd',
        unit_amount=item.price,
    )
    print(price)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': str(price.id),
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=reverse('stripe_app:success'),
            cancel_url=reverse('stripe_app:cancel'),
        )
        print(checkout_session)
        return JsonResponse(checkout_session)
    except Exception as e:
        print('ERR')
        return HttpResponse(str(e))


def item(request, id):
    return HttpResponse("item {0}".format(id))
