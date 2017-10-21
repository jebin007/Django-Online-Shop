from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    # This status indicates that the paypal was successfully completed.
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        order = get_object_or_404(Order, id=ipn_obj.invoice)

        # mark the order as Paid
        order.paid = True
        order.save()


valid_ipn_received.connect(payment_notification)
