from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product,
    }

    return render(request, "goods/product.html", context=context)


# "goods": [
#             {
#                 "image": "deps/images/goods/set of tea table and three chairs.jpg",
#                 "name": "Чайный столик и три стула",
#                 "description": "Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.",
#                 "price": 150.00,
#             },
#             {
#                 "image": "deps/images/goods/set of tea table and two chairs.jpg",
#                 "name": "Чайный столик и два стула",
#                 "description": "Набор из стола и двух стульев в минималистическом стиле.",
#                 "price": 93.00,
#             },
#             {
#                 "image": "deps/images/goods/double bed.jpg",
#                 "name": "Двухспальная кровать",
#                 "description": "Кровать двухспальная с надголовником и вообще очень ортопедичная.",
#                 "price": 670.00,
#             },
#             {
#                 "image": "deps/images/goods/kitchen table.jpg",
#                 "name": "Кухонный стол с раковиной",
#                 "description": "Кухонный стол для обеда с встроенной раковиной и стульями.",
#                 "price": 365.00,
#             },
#             {
#                 "image": "deps/images/goods/kitchen table 2.jpg",
#                 "name": "Кухонный стол с встройкой",
#                 "description": "Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.",
#                 "price": 430.00,
#             },
#             {
#                 "image": "deps/images/goods/corner sofa.jpg",
#                 "name": "Угловой диван для гостинной",
#                 "description": "Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!",
#                 "price": 610.00,
#             },
#             {
#                 "image": "deps/images/goods/bedside table.jpg",
#                 "name": "Прикроватный столик",
#                 "description": "Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).",
#                 "price": 55.00,
#             },
#             {
#                 "image": "deps/images/goods/sofa.jpg",
#                 "name": "Диван обыкновенный",
#                 "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
#                 "price": 190.00,
#             },
#             {
#                 "image": "deps/images/goods/office chair.jpg",
#                 "name": "Стул офисный",
#                 "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
#                 "price": 30.00,
#             },
#             {
#                 "image": "deps/images/goods/plants.jpg",
#                 "name": "Растение",
#                 "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
#                 "price": 10.00,
#             },
#             {
#                 "image": "deps/images/goods/flower.jpg",
#                 "name": "Цветок стилизированный",
#                 "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
#                 "price": 15.00,
#             },
#             {
#                 "image": "deps/images/goods/strange table.jpg",
#                 "name": "Прикроватный столик",
#                 "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
#                 "price": 25.00,
#             },
#         ],
