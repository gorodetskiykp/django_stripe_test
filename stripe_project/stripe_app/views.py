from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# - GET /buy/{id}, c помощью которого можно получить Stripe Session
# Id для оплаты выбранного Item. При выполнении этого метода c
# бэкенда с помощью python библиотеки stripe должен выполняться
# запрос stripe.checkout.Session.create(...) и полученный session.id
# выдаваться в результате запроса
# - GET /item/{id}, c помощью которого можно получить простейшую
# HTML страницу, на которой будет информация о выбранном Item
# и кнопка Buy. По нажатию на кнопку Buy должен происходить
# запрос на /buy/{id}, получение session_id и далее с помощью JS
# библиотеки Stripe происходить редирект на Checkout форму
# stripe.redirectToCheckout(sessionId=session_id)
# - Пример реализации можно посмотреть в пунктах 1-3


def buy(request, id):
    return JsonResponse({
        "operation": "buy",
        "item_id": id,
    })


def item(request, id):
    return HttpResponse("item {0}".format(id))
