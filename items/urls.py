from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/', view=views.get_item, name='items'),
    path('buy/<int:id>/', view=views.buy_item, name='buy_item')
]
