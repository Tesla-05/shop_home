from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories


class IndexView(TemplateView):
    template_name = "main/index.html"

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Главная"
        context["content"] = "Магазин мебели HOME"
        return context


class DeliveryView(TemplateView):
    template_name = "main/delivery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Доставка"
        context["content"] = "Доставка"
        context["text_on_page"] = {
            "time_delivery": "Время доставки",
            "time_delivery_text": """Доставка заказов осуществляется с понедельника по субботу с 10:00 до 21:00, кроме праздничных дней.
                Обращаем ваше внимание, что доставка осуществляется в этом временном интервале, а не к определенному часу.
                За день до доставки заказа вы получите СМС с контактными данными водителя, который свяжется с вами утром в день доставки и сообщит примерный интервал приезда.
                Внимание! В случае отсутствия получателя по адресу водитель ожидает не более 20 минут!""",
            "delivery_one_day": "Доставка за 1 день",
            "delivery_one_day_text": """Мы доставим ваш заказ на следующий день, если вы сделаете заказ в нашем интернет-магазине с 
            понедельника по пятницу и менеджер подтвердит его до 15:00.""",
            "speshial_delivery": "Срочная доставка",
            "speshial_delivery_text": """Заказ будет доставлен после подтверждения заказа у менеджера. Вы можете выбрать удобное для себя время доставки в интервале времени 10:00–24:00 
             (+/– 30 мин) и заказать сборку товара в день доставки (кроме корпусной мебели). Стоимость срочной доставки – 4 000 ₽ Сборка и выезд за МКАД оплачиваются отдельно.""",
        }
        return context


class ContactsView(TemplateView):
    template_name = "main/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Контакты"
        context["content"] = "Контакты"
        context["text_on_page"] = {
            "ur_adr": "Юридический адрес:",
            "ur_text": "Млечный Путь, Солнечная система, пл. Земля, Российская Федерация, г. Нерюнгри, ул. Ленина",
            "grafik": "График работы:",
            "grafik_text": "пн.-сб. с 10:00 до 21:00, с перерывом на обед",
            "email": "Электронная почта:",
            "email_text": "happy_russia.@mail.ru",
            "phone": "Связь по телефону:",
            "phone_number": "+7 (495) 123-45-67",
        }
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - О нас"
        context["content"] = "О нас"
        context[
            "text_on_page"
        ] = """     <p>Наша цель - сделать дизайнерскую мебель более доступной, чтобы каждый имел возможность создать в своем доме красивое и уютное пространство, сделать его уникальным, «своим».</p>
        <br><p>Наш ассортимент подобран с учетом последних мировых трендов в сфере дизайна интерьеров. Мы постоянно работаем над обновлением коллекций, благодаря которым возможно воплотить в жизнь самые яркие дизайнерские задумки. При этом обязательно учитываем такие важные факторы, как габариты, практичность и функциональность. </p>
        """
        return context


# def index(request):
#     context = {
#         "title": "Home - Главная",
#         "content": "Магазин мебели HOME",
#     }
#     return render(request, "main/index.html", context)


# def about(request):
#     context = {
#         "title": "Home - О нас",
#         "content": "О нас",
#         "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар",
#     }
#     return render(request, "main/about.html", context)
