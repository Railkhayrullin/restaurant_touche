from django.contrib.sessions.models import Session

from orders.models import Order


def get_current_order(request):
    if Order.objects.filter(session__session_key=request.session.session_key, status="new"):
        return Order.objects.filter(session__session_key=request.session.session_key, status="new").first()
    else:
        order = Order()
        if not request.session.session_key:
            request.session.save()
        session = Session.objects.get(session_key=request.session.session_key)
        order.session = session
        order.save()
        return order
