import stripe
import os
from django.shortcuts import render
from .models import Item
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

stripe.api_key = os.environ.get('STRIPE_API_KEY')

def get_item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item
    }
    return render(request, 'items/items.html', context)


def buy_item(request, id):
    item = Item.objects.get(id=item_id)
    serializer = ItemSerializer(item)
    item_data = serializer.data

    stripe.api_key = settings.STRIPE_API_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
          'name': item_data['name'],
          'description': item_data['description'],
          'amount': item_data['price'],
          'currency': 'usd',
          'quantity': 1,
        }],
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )

    return redirect(session.url)
