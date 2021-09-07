from django.conf import settings
from django.contrib.auth.models import User
from restaurant_touche import settings as site_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_messages_to_managers(order):
    if User.objects.filter(groups__name='managers'):
        managers = User.objects.filter(groups__name='managers')
        emails = [manager.email for manager in managers]

        html = render_to_string('email/new_order_email.html', {'order': order})
        if not settings.DEBUG:
            send_mail(f'Новый заказ на сайте {site_settings.SITE_URL}', html, settings.DEFAULT_FROM_EMAIL,
                      emails, html_message=html)
        else:
            print(html)
    else:
        print('Менеджеры не найдены!')
