from orders.models import Order


def unread_orders(request):
    orders = Order.objects.filter(read=False)
    return {'unread_orders': len(orders)}



