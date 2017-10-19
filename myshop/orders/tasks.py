# This is the place where Celery will look for asynchronous tasks

from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    '''
    Task to send an e-mail notification when an order is successfully created
    '''
    order = Order.objects.get(id=order_id)
    subject = 'Order no. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfuly placed an order. You order id is {}.'.format(order.first_name, order.id)

    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent
