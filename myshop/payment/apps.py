from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name = 'Payment'
    # Load signals when Payment app is processed
    
    def ready(self):
        # import signal handlers
        import payment.signals

